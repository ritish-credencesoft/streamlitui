import streamlit_authenticator as stauth
import yaml
import streamlit as st
import requests

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)
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
        # r = requests.get('http://127.0.0.1:8000/runall')
    elif username == 'satyar':
        st.write(f'Welcome *{name}*')
        st.title('Application 2')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')