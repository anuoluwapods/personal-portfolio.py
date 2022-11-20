import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Image/image.png'))

st.header('Anuoluwapo Balogun | Data Analyst')

st.info('Email: ifeoluwapobalogun1@gmail.com \n\nPhone: +2349090251869')

import time

my_bar = st.progress(70)
perc = '70%'
st.write(my_bar{} . format(perc))



st.info('A Certified Data analyst and a self taught Data scientist and engineer specialized in sales and consultancy')
st.info('Database: PostgreSQL | Microsoft SQL Server | MongoDB')
st.info('Visualization: PowerBI | Tableau')
st.info('Programming: Python | R')
st.info('Statistics: Excel | SAS | SPSS')
st.info('Distributed SQL: FaunaDB | CockroachDB')
st.info('Cloud Platforms: Snowflake | AWS | GCP | Azure')
st.info('Skills: ML Algorithmn | A/B Testing | Data Wrangling |'
         ' Analytics | Data Preprocessing | Data Visualization'
         ' Exploratory Data Analysis | Fraud Analysis |'
         ' Hypothesis Testing | Sales Analysis | Consulting')

icon_size = 20

st_button('twitter', 'https://twitter.com/AnuoluwapoDs','Twitter', icon_size)
st_button('github', 'https://github.com/anuoluwapods', 'GitHub', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/anuoluwapo-abiodun-balogun-64b977186/', 'LinkedIn', icon_size)
st_button('instagram', 'https://www.instagram.com/anuoluwapods/', 'Instagram', icon_size)
st_button('facebook', 'https://www.facebook.com/ifeoluwapo.balogun', 'Facebook', icon_size)
st_button('medium', 'https://anuoluwapods.medium.com', 'Data Analysis', icon_size)
st_button('jovian', 'https://jovian.ai/designegycreatives/notebooks', 'Data Science', icon_size)
st_button('hashnode', 'https://hashnode.com/@AnuoluwapoDS', 'Web Application', icon_size)
st_button('dev.to', 'https://dev.to/anuoluwapods', 'Data Engineering', icon_size)
