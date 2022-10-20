import os
import sqlalchemy
import pandas as pd
import networkx as nx
import holoviews as hv
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from bokeh.plotting import figure

SRC_DIR = os.path.join( os.path.abspath('.'), 'src' )
SRC_DIR = os.path.dirname( os.path.abspath(__file__) )
BASE_DIR = os.path.dirname( SRC_DIR )
DATA_DIR = os.path.join( BASE_DIR, 'data')

def open_db():
    return sqlalchemy.create_engine("sqlite:///" + os.path.join(DATA_DIR, 'album.db'))

def import_query(path:str, **kwargs):
    with open(path, "r", **kwargs ) as file_open:
        query = file_open.read()
    return query

def exec_query_file(path:str):
    conn = open_db()
    query = import_query( path )
    return pd.read_sql_query( query, conn )

def get_netdata():
    return exec_query_file(os.path.join( SRC_DIR, "netquery.sql" ))
    
def get_people():
    return exec_query_file(os.path.join(SRC_DIR, "peoplequery.sql"))

def make_network(data):
    G = nx.from_pandas_edgelist(data,
                                source='user_a',
                                target='user_b' )

    return hv.Graph.from_networkx(G,
                                  nx.layout.fruchterman_reingold_layout,
                                  k=1)

def get_user_network(data, user):
    data_filter = data[ (data['user_a'] == user) | (data['user_b'] == user) ]
    users = list( set( data_filter['user_a'].unique().tolist() + data_filter['user_b'].unique().tolist() ) - set([user]) )
    data_net = data[ (data['user_a'].isin(users)) & (data['user_b'].isin(users)) ]
    return make_network(data_net)
    
def main():

    st.title('Figurinhas!!')
    st.write("Vamos analisar a nossa rede sociais de participantes das figurinhas...")

    people = get_people()
    data = get_netdata()

    option = st.selectbox( 'Gostaria de ver a rede de qual jogador?',
                           ['None'] + people['user'].tolist()  )

    if option != "None"  :
        'Você selecionou: ', option, "\n\nConfira as informações básicas deste usuário:\n"
        st.table( people[people['user']==option].rename(columns={"user":"Jogador",
                                                                    "qtde_relacionamentos":"Relacionamentos",
                                                                    "qtde_figurinhas":"Figurinhas Trocadas"}) )
        simple_graph = get_user_network(data,option)
    else:
        st.dataframe( people.rename(columns={"user":"Jogador",
                                         "qtde_relacionamentos":"Relacionamentos",
                                         "qtde_figurinhas":"Figurinhas Trocadas"}) )
        
        simple_graph = make_network(data)

    st.bokeh_chart(hv.render(simple_graph, backend='bokeh'), use_container_width=True)

if __name__ == "__main__":
    main()