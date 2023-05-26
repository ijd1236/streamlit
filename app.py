
# 환경 설정 : conda create -n app_dash python=3.9 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn

# Streamlit은 Python을 사용하여 데이터 분석 및 웹 애플리케이션 개발을 위한 오픈 소스 라이브러리입니다


# conda deactivate - 가상환경 나가기


# conda env list - 가상환경 리스트 확인하기


# conda activate app_dash- 가상환경 들어가기


# streamlit run app.py : streamlit run app.py 명령은 Streamlit 애플리케이션을 실행하는 명령입니다.

# 이 명령은 app.py 파일을 실행하여 Streamlit 애플리케이션을 시작합니다. app.py 파일은 Streamlit 애플리케이션의 소스 코드가 있는 파일의 이름을 나타냅니다.


import streamlit as st

def main():  #화면에 나타낼것
    st.title('내 앱 대시보드') 


if __name__ == '__main__':
    main()



