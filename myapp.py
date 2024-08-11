# import libraries
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title='Consoleflare Analytics Prortal'
)


st.title(':rainbow[Data Analytics Portal]')
st.header(':grey[Explore Data with ease.]',divider='rainbow')


file = st.file_uploader('Drop csv or Excel file',type=['csv'])


if(file!= None):
    if(file.name.endswith('csv')):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    st.dataframe(data)
    st.info('File is Succesfully Uploaded')
    
    st.subheader(':rainbow[Basic information of Datasets]',divider='rainbow')
    tab1,tab2,tab3,tab4 = st.tabs(['Summery','Top & Bottom Rows','Datatypes','Columns'])
    
    with tab1:
        st.write(f'There  are  {data.shape[0]}  Rows  and {data.shape[1]}  Columns  in  the  Dataset')
        st.subheader(':grey[Statistical Summery of Dataset]')
        st.dataframe(data.describe())

    with tab2:
        st.subheader(':grey[Top 5 Rows]')
        toprows = st.slider('Number of Rows you want',1,data.shape[0],key='topslider')
        st.dataframe(data.head(toprows))
        st.subheader(':grey[Bottom Rows]')
        bottomrows = st.slider('Number of Rows you want',1,data.shape[0],key='bottomslider')
        st.dataframe(data.head(bottomrows))

    with tab3:
        st.subheader(':grey[Datatype in the Dataset]')
        st.write(list(data.dtypes))

    with tab4:
        st.subheader(':grey[Columns in the Dataset]')
        st.write(list(data.columns))


