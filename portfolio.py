import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('image/image.png'))

st.header('Anuoluwapo | Data Analyst')

st.info('A Certified Data analyst and a self taught Data ccientist and engineer specialized in Sales and Consultancy')
st.info('Skills and Softwares: Python| R | Streamlit | Rapid Miner |Excel | PowerBI | Tableau | Plotly |  Matplotlib | Seaborn |'
        'Postgre SQL | Microsoft SQL Server | Flask | Django | Canva')

icon_size = 20

st_button('medium', 'https://anuoluwapods.medium.com', 'Data Analysis Portfolio', icon_size)
st_button('github', 'https://github.com/anuoluwapods', 'GitHub Page', icon_size)
st_button('hashnode', 'https://hashnode.com/@AnuoluwapoDS', 'Web Application Portfolio', icon_size)
st_button('dev.to', 'https://dev.to/anuoluwapods', 'Data Engineering Portfolio', icon_size)
st_button('jovian', 'https://jovian.ai/designegycreatives/notebooks', 'Data Science Portfolio', icon_size)
st_button('instagram', 'https://www.instagram.com/anuoluwapods/', 'Instagram Page', icon_size)
st_button('twitter', 'https://twitter.com/AnuoluwapoDs', 'Twitter Page', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/anuoluwapo-abiodun-balogun-64b977186/', 'LinkedIn Page', icon_size)
st_button('facebook', 'https://www.facebook.com/ifeoluwapo.balogun', 'Facebook Page', icon_size)
