# import libraries
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title='Consoleflare Analytics Prortal'
)


st.title(':rainbow[Data Analytics Portal]')
st.header(':grey[Explore Data with ease.]',divider='rainbow')


file = st.file_uploader('Drop csv or Excel file',type=['csv','xlxs'])


if(file!= None):
    if(file.name.endswith('csv')):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    st.dataframe(data)
    st.info('File is Succesfully Uploaded')






