# import libraries
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title='AnalytiX',
    page_icon = 'logo.png'
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
        st.dataframe(data.tail(bottomrows))

    with tab3:
        st.subheader(':grey[Datatype in the Dataset]')
        st.write(list(data.dtypes))

    with tab4:
        st.subheader(':grey[Columns in the Dataset]')
        st.write(list(data.columns))

    st.subheader(':rainbow[Column Vlues to count]',divider='rainbow')
    with st.expander('Value count'):

        col1,col2=st.columns(2)
        with col1:
           column = st.selectbox('Chose Column name',options=(data.columns))
        with col2:
           toprows=st.number_input('Top Rows',min_value=1,step=1)


        count = st.button('COUNT')
        if(count == True):
            result = data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)
            st.subheader('Visualization',divider='grey')
            fig = px.bar(data_frame=result,x=column,y='count',text='count',color=column)
            st.plotly_chart(fig)

    
    st.subheader(':rainbow[Group By]',divider='rainbow')
    with st.expander('Group By Column'):
        col1,col2,col3= st.columns(3)

        with col1:
            group_by = st.multiselect('Column to Group By',options=list(data.columns))

        with col2:
            operation_col = st.selectbox('Column for Operation',options=list(data.columns))

        with col3:
            operation = st.selectbox('Operation',options=['sum','mean','min','max'])
        
        if(group_by):
            result = data.groupby(group_by).agg(newcol=(operation_col,operation)).round().sort_values(by='newcol',ascending=False).reset_index()
            st.dataframe(result)
            st.subheader(':grey[Visualization]',divider='grey')
            graph = st.selectbox('Choose your chart',options=['line','bar','scatter','line','pie','sunburst'])
            if(graph=='line'):
                x_axis = st.selectbox('Choose X-axis',options=list(result.columns))
                y_axis = st.selectbox('Choose Y-axis',options=list(result.columns))
                color = st.selectbox('Color Information',options=[None]+list(result.columns))
                fig = px.line(data_frame=result,x=x_axis,y=y_axis,color=color)
                st.plotly_chart(fig)
            elif(graph=='bar'):
                x_axis = st.selectbox('Choose X-axis',options=list(result.columns))
                y_axis = st.selectbox('Choose Y-axis',options=list(result.columns))
                color = st.selectbox('Color Information',options=[None]+list(result.columns))
                facet = st.selectbox('Column Information',options=[None]+list(result.columns))
                fig = px.bar(data_frame=result,x=x_axis,y=y_axis,color=color,facet_col=facet,barmode='group')
                st.plotly_chart(fig)
            elif(graph=='scatter'):
                x_axis = st.selectbox('Choose X-axis',options=list(result.columns))
                y_axis = st.selectbox('Choose Y-axis',options=list(result.columns))
                color = st.selectbox('Color Information',options=[None]+list(result.columns))
                size = st.selectbox('Size',options=[None]+list(result.columns))
                fig = px.bar(data_frame=result,x=x_axis,y=y_axis,color=color,)
                st.plotly_chart(fig)
            elif(graph=='pie'):
                value = st.selectbox('Choose Numeric value',options=list(result.columns))
                names = st.selectbox('Choose Lable',options=list(result.columns))
                fig = px.pie(data_frame=result,values=value,names=names)
                st.plotly_chart(fig)
            elif(graph=='sunburst'):
                path = st.multiselect('Choose your path',options=list(result.columns))
                fig = px.sunburst(data_frame=result,path=path,values='newcol')
                st.plotly_chart(fig)


