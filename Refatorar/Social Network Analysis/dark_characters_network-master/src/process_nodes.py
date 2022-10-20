'''
Description: Script used to processed the nodes and edges for the network visualization
'''

import os
import re
import sys

import pandas as pd

FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGEX_GREATPARENTS = '(/|)great-.*(/|)'
REGEX_MULTI_RELATIONSHIP = '(;|,).*'
REGEX_ADOPTIVE = 'adoptive'
REGEX_FIRST_LEVEL_RELATIVES = '(mother|father|sister|brother|wife|husband|son|daughter)'
REGEX_LAW_RELATIVES = '(law)'
REGEX_SECOND_LEVEL_RELATIVES = '(cousin|nephew|aunt|uncle)'
REGEX_GRANDRELATIVES = '(grand)'

def create_relationship(data, from_char, to_char, relation):
    '''
    Function used to create custom relationship between characters
    '''
    relation_dict = {'character': from_char,
                     'relationship': relation,
                     'relative': to_char,
                     'url': data.loc[data['relative'] == to_char, 'url'].iloc[0]
                    }
    data = data.append(pd.DataFrame([relation_dict]))
    return data

data = pd.read_csv(FILE_PATH + '/data/raw/characters_relationship.csv')

# Removing unuseful relationships with regex
data['relationship'] = data['relationship'].str.replace(REGEX_GREATPARENTS, '', case=False)
data['relationship'] = data['relationship'].str.replace(REGEX_MULTI_RELATIONSHIP, '', case=False)
data['relationship'] = data['relationship'].str.replace(REGEX_ADOPTIVE, '', case=False)

# Capitalizing relationships
data['relationship'] = data['relationship'].str.capitalize()
data['relationship'] = data['relationship'].str.strip()

# Dropping empty relationships
data = data.loc[data['relationship'] != '']

# Enriching relationships
data = create_relationship(data, 'Martha Nielsen', 'Jonas Kahnwald', 'Killed')
data = create_relationship(data, 'Jonas Kahnwald', 'Martha Nielsen', 'Killed')
data = create_relationship(data, 'Hannah Kahnwald', 'Jonas Kahnwald' , 'Killed')
data = create_relationship(data, 'Claudia Tiedemann', 'Hanno Tauber', 'Killed')
data = create_relationship(data, 'Hanno Tauber', 'Hanno Tauber', 'Killed')
data = create_relationship(data, 'Hanno Tauber', 'Agnes Nielsen', 'Killed')
data = create_relationship(data, 'Regina Tiedemann','Tronte Nielsen', 'Killed')
data = create_relationship(data, 'Egon Tiedemann', 'Claudia Tiedemann', 'Killed')
data = create_relationship(data, 'Claudia Tiedemann', 'Claudia Tiedemann', 'Killed')
data = create_relationship(data, 'Mads Nielsen', 'Helge Doppler', 'Killed')
data = create_relationship(data, 'Mikkel Nielsen', 'Michael Kahnwald', 'Same person')

# Saving dataset
#data.to_csv(FILE_PATH + '/data/processed/characters_cleaned_relationship.csv', index=False)

# Preparing data for network viz

## Creating/Dropping columns
data['color'] = '#ecf0f1'
data['shape']= 'circularImage'
data = data.drop('url', axis=1)

# Selecting color for each relationship
data.loc[data['relationship'].str.contains(REGEX_FIRST_LEVEL_RELATIVES, case = False), 'color'] = '#f1c40f'
data.loc[data['relationship'].str.contains(REGEX_SECOND_LEVEL_RELATIVES, case = False), 'color'] = '#2ecc71'
data.loc[data['relationship'].str.contains(REGEX_LAW_RELATIVES, case = False), 'color'] = '#3498db'
data.loc[data['relationship'].str.contains(REGEX_GRANDRELATIVES, case = False), 'color'] = '#e67e22'
data.loc[data['relationship'] == 'Same person', 'color'] = '#9b59b6'
data.loc[data['relationship'] == 'Killed', 'color'] = '#e74c3c'

data.columns = ['from', 'label', 'to', 'color', 'shape']

print(data.to_dict(orient='records'))