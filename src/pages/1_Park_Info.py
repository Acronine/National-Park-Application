import streamlit as st
import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Park Info",
    page_icon="⛰️",
    menu_items={
        'About': """This is an app developed by 5 Peers at Coding Temple.
        Here are our Github accounts: \n\rHarrison :
        https://github.com/Acronine, \n\rJoshua : https://github.com/TechNTalk,
        \n\rLogan : https://github.com/Sir-Roe,
        \n\rVaidic: https://github.com/tvaidic"""}
)

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

import myfuncs as mf
from tomongo import ToMongo
c = ToMongo()
cursor = c.park_info.find()
df = pd.DataFrame(list(cursor))

st.title('Find A Park')
pk_list = df.full_name.tolist()

select = st.selectbox('Search any National Park', options=pk_list)

if select:
    st.subheader(select)

    for i in range(len(df['full_name'])):
        if select == df['full_name'][i]:
            link = (df['images'][i])
            index = i
    ran_num = np.random.randint(0,len(df['images'][index]))
    st.image(link[ran_num]['url'], caption=link[ran_num]['caption'])

    st.subheader('About The Park:')

    st.write(df['description'][index])
    st.subheader('Things to do:')

    act_string = ''
    for act in df['activities'][index]:
        act_string += act + ', '
    st.markdown(act_string)
    st.subheader('Entrance fees types and hours:')
    st.dataframe(mf.hour_sort(df['standard_hours'][index]), width=500)

    if type(df['entrance'][index]) == list:
        st.dataframe(
            pd.DataFrame(
                {"Fee": df['entrance'][index], "Costs": df['cost'][index]}
                ),
            hide_index=True, width=500)
    else:
        st.dataframe(
            {"Fee": df['entrance'][index], "Costs": df['cost'][index]}
            )

    st.subheader('Press the link for more info')
    st.write(df['url'][index])