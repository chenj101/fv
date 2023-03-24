import streamlit as st
import  pandas  as pd
#import numpy as np
#import openpyxl
def navigation_bar(s):
    #st.set_page_config(page_title="运维管理后台",layout="wide") #设置屏幕展开方式，宽屏模式布局更好
    st.sidebar.write(f'文档管理导航栏{s}')
    
    add_selectbox = st.sidebar.radio(
        "文档管理",
        ("上传文档", "下载文档", "文档查询")
    )
    
    if add_selectbox == '上传文档':
        st.title("上传文档")
        uploaded_file = st.file_uploader("Choose a CSV file", type="xlsx")
        if uploaded_file is not None:
           data = pd.read_excel(uploaded_file)
           st.write(data)
        #fileupload()
    elif add_selectbox == '下载文档':
        st.title("下载文档")
       
        #filedownload()  
    elif add_selectbox == '文档查询':
        st.title("文档查询")
        #querybooks()  
                                         
    return add_selectbox
    
def main(s):
    navigation_bar(s)

if __name__ == '__main__':
    main('123')
