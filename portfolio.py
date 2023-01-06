import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Image/image.png'))

st.header('Anuoluwapo Balogun | Data Analyst')

st.info('A Certified Data analyst')
st.write('Email: anuoluwapobalogunds@gmail.com | Phone: +2349090251869')

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
