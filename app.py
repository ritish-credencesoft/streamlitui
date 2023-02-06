import streamlit_authenticator as stauth
import yaml,csv,json
import streamlit as st
import requests
import streamlit as st
# import pandas as pd
from io import StringIO
import time
# import matplotlib.pyplot as plt
import numpy as np


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

with open('./style/style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)   

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)
st.header('Onboarding Automation System')
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username= authenticator.login('Login', 'main')

labels = 'Odisha', 'Mumbai', 'Pune', 'Shirdi'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
fig1.set_facecolor('#00172B')
patches, texts, autotexts  = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
texts[0].set_color('white')
texts[1].set_color('white')
texts[2].set_color('white')
texts[3].set_color('white')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)







if authentication_status:
    authenticator.logout('Logout', 'main')
    if username == 'ritishm':
        st.write(f'Welcome *{name}*')
        st.title('Hotel Automation')
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(df)
            jsonopt = df.to_json(orient='records')
            df = pd.DataFrame(
                np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                columns=['lat', 'lon'])

        if st.button('Run'):
            my_bar = st.progress(0)

            for percent_complete in range(100):
                time.sleep(0.1)

                my_bar.progress(percent_complete + 1)
            
            r = requests.post('http://52.66.64.204/runall', json=jsonopt)
            # st.write(r.status_code)
            
    elif username == 'satyar':
        st.write(f'Welcome *{name}*')
        st.title('Application 2')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')