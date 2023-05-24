import streamlit as st
from PIL import Image #이미지 처리하는 라이브러리

def main():  
    st.title('내 앱 대시보드') 
    # 사진과 영상을 보여주는 방법
    img =Image.open('data/image_03.jpg')
    print(img)
    st.image(img) #대시보드에 이미지를 표현
    st.image(img, use_column_width=True) # use_column_width=True 화면 꽉차게
    # 이미지 URL 로 불러와서 보여주기
    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')
    video_file=open('data/video1.mp4', 'rb') # 'rb' 동영상 읽어올때 사용
    st.video(video_file)
    



if __name__ == '__main__':
    main()

