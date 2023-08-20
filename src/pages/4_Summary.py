import streamlit as st

st.set_page_config(
    page_title="Summary Page",
    page_icon="⛰️",
    menu_items={
        'About': """This is an app developed by 5 Peers at Coding Temple.
        Here are our Github accounts: \n\rHarrison :
        https://github.com/Acronine, \n\rJoshua : https://github.com/TechNTalk,
        \n\rLogan : https://github.com/Sir-Roe,
        \n\rVaidic: https://github.com/tvaidic"""}
)

st.header("National Park's Application Summary")
st.text("""
        The purpose of this application is to create an application using the
        National Park's Api. The first steps to do this was pulling the data,
        cleaning the data, pushing the data to MongoDB. After, we create a
        virtual environment that will house all of our python installs and
        the application. Following, we query the data and run it through
        Streamlit. We create an easily accessible application that allows
        the user to look up any National Park and its corresponding info.
        
        In addition to the park info, the next page allows the user to enter
        any state and see all National Parks on a map that are either in the
        State or run through it. Afterwards, the activities page lets the user
        inquire any activity and the related parks that house them. They can
        also filter using a state if the state has that activity to begin with.
        """)

st.text("""
        We would like to thank the National Park Service for giving us
        permission to use their api. If you would like to reach out to
        them, their github is:   https://github.com/nationalparkservice
        """)

st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')