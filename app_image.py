import streamlit as st
import os 
import pandas as pd
from datetime import datetime
from app_utils import save_uploaded_file

def run_app_image():
    st.subheader('이미지 파일 업로드')
    img_file= st.file_uploader('이미지를 업로드 하세요', type = ['png', 'jpg', 'jpeg'])
    if img_file is not None : 
        print(type(img_file))
        print(img_file.name)
        print(img_file.size) #바이트 단위
        print(img_file.type)
        #유저가 올린 파일을.
        #서버에서 유니크하게 처리하기 위해서
        #파일명을 현재시간 조합으로 해서 만든다.
        current_time = datetime.now()
        print(current_time)
        print(current_time.isoformat().replace(':', '_') + '.jpg') #isoformat(): 데이터 포맷을 문자열로 만드는
        filename = current_time.isoformat().replace(':', '_') + '.jpg'
        img_file.name = filename
        save_uploaded_file('image', img_file)
        st.image('image/'+ filename)
