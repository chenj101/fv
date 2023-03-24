import streamlit as st
import streamlit_authenticator as stauth
import st0
st.set_page_config(page_title="运维管理后台")#,layout="wide") #设置屏幕展开方式，宽屏模式布局更好
# 如下代码数据，可以来自数据库
names = ['肖永威', '管理员']
usernames = ['xiaoyw', 'admin']
passwords = ['S0451', '123']

hashed_passwords = stauth.Hasher(passwords).generate()

credentials={'usernames':{}}
for i in range(len(names)):
   credentials['usernames'][usernames[i]]={'name':names[i],'password':hashed_passwords[i]}
print(credentials)   
authenticator = stauth.Authenticate(credentials,
    'some_cookie_name', 'some_signature_key',cookie_expiry_days=30)

name,authentication_status,username = authenticator.login('用户登录', 'main')

if authentication_status:
    with st.container():
        cols1,cols2 = st.columns(2)
        cols1.write(f'欢迎 {name}')
        with cols2.container():
            authenticator.logout('退出', 'main')

    st0.main('123')
elif authentication_status == False:
    st.error('用户名/密码不正确')
elif authentication_status == None:
    st.warning('请输入您的用户名和密码')

