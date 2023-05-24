import streamlit as st
import os 
import pandas as pd
from datetime import datetime
from app_image import run_app_image #파일명에 저장된 함수를 불러온다.
from app_csv import run_app_csv
from app_about import run_app_about

# 디렉토리 이름과, 파일이름을 주면,
# 해당 디렉토리에 파일을 저장해주는 함수
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리가 있는지 확인
    #    없으면 디렉토리를 먼저 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f : #파일 경로 합치고 저장
        f.write(file.getbuffer())
    return st.success('파일 저장 완료')


def main():  #화면에 나타낼것
    st.title('내 앱 대시보드') 

    menu = ['이미지 업로드', 'csv업로드', 'About']
    choice=st.sidebar.selectbox("메뉴", menu)
    
    if choice == menu[0] :
        run_app_image()



    elif choice == menu[1] :
        run_app_csv()

    else :
        run_app_about()
        






if __name__ == '__main__':
    main()