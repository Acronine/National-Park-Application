from pathlib import Path
import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(
    page_title="Parks Near You",
    page_icon="⛰️",
        menu_items={
        'About': """This is an app developed by 5 Peers at Coding Temple. Here are our
        Github accounts: \n\rHarrison : https://github.com/Acronine, \n\rJoshua : https://github.com/TechNTalk,
        \n\rLogan : https://github.com/Sir-Roe, \n\rVaidic: https://github.com/tvaidic"""}
)
#establish a filepath to the orcale_cards.csv file
filepath=os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from tomongo import ToMongo
import myfuncs as mf
c=ToMongo()

#grab my collection
cursor=c.park_info.find({ "longitude" : {"$ne" :None},"latitude" : {"$ne" :None}})

#list into a dataframe
df =  pd.DataFrame(list(cursor))

#generate Possible values of states
states=mf.pos_values(df,'states')

st.header("Parks by State")
#set options to pos values func
state=st.selectbox("Select a State:",options=states)

#generate map based off the locator return value
st.map(df[['latitude','longitude']].iloc[mf.locator(df,'states',state)],color="#39FF14")

#create a clean string that plays nice in data_editor
df['States_in_Park'] = mf.stringConvert(df,'states')

#create a clean list to see the info generated
result = st.data_editor(df[['full_name','States_in_Park']].iloc[mf.locator(df,'states',state)],hide_index=True,width=800)


