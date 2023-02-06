import streamlit_authenticator as stauth
import yaml,csv,json
import streamlit as st
import requests
import streamlit as st
from io import StringIO
import pandas as pd
import time
import numpy as np
import pandas as pd




streamlit_style = """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

                html, body, [class*="css"]  {
                font-family: 'Roboto', sans-serif;
                }
            </style>
            """
st.markdown(streamlit_style, unsafe_allow_html=True)

# print(st)

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
            
            # add env vars - backend url
            r = requests.post('http://127.0.0.1:8000/runall', json=jsonopt)
            # st.write(r.status_code)
            
    elif username == 'satyar':
        st.write(f'Welcome *{name}*')
        st.title('Application 2')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

