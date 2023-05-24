import streamlit as st
import os 
import pandas as pd
from datetime import datetime

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




    elif choice == menu[1] :
        st.subheader('CSV 파일 업로드')
        csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'])
        if csv_file is not None:
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':', '_')+ '.csv'
            csv_file.name = filename
            save_uploaded_file('csv', csv_file)
            df =pd.read_csv('csv/'+ filename)
            st.dataframe(df)

    else :
        st.subheader('이 대시보드 설명')






if __name__ == '__main__':
    main()