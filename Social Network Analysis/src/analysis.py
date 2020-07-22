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

def main():
    print("Conecatando...", end="")
    conn = open_db()
    print("Ok.")

    query = import_query(os.path.join( SRC_DIR, "query.sql" ))
    df = pd.read_sql_query( query, conn )

    G = nx.from_pandas_edgelist(df,
                                source='user_a',
                                target='user_b' )

    st.bokeh_chart(hv.render(G, backend='bokeh'))

if __name__ == "__main__":
    main()