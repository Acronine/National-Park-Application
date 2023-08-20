import streamlit as st

st.set_page_config(
    page_title="National Parks App",
    page_icon="⛰️",
    menu_items={
        'About': """This is an app developed by 5 Peers at Coding Temple. Here are our
        Github accounts: \n\rHarrison : https://github.com/Acronine, \n\rJoshua : https://github.com/TechNTalk,
        \n\rLogan : https://github.com/Sir-Roe, \n\rVaidic: https://github.com/tvaidic"""}
)

st.title("National Park Service")

st.image('https://www.nps.gov/articles/images/NPS-Transparent-Logo.png',width=200)

st.text("Our Teams application uses the following to create a National Parks App:")
st.text(""">Streamlit 
>Python
>MongoDB
>Pandas
>National Parks API """)

st.header("Here are the different pages of our application:")

st.subheader('Park Info')

st.text('Queries to pull up a single park and its information.')

st.markdown("""The information fields displayed are:
        park name, an image, park hours, park description, park url, 
        activities & topics, entrance fees if any""")

st.subheader("Activities Search")
st.text("Queries and returns all parks based on selected activities.")

st.subheader("Parks by State")
st.markdown("Creates an interactive map based on a selected state to display all parks within it.")

st.subheader("Summary")
st.markdown("""This page provides a comprehensive explanation 
        of the app's internal mechanisms and delves into the underlying 
        reasons for each design choice.""")