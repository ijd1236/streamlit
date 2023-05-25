# streamlit으로 앱 대시보드 만들기
- Streamlit은 Python을 사용하여 데이터 분석 및 웹 애플리케이션 개발을 위한 오픈 소스 라이브러리입니다.
## 기본적인 환경 설정
- conda create -n app_dash python=3.9 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn
- 가상환경을 만들고 대시보드에 필요한 각종 라이브러리를 설치합니다.
- conda deactivate - 가상환경 나가기
- conda env list - 가상환경 리스트 확인하기
- conda activate app_dash- 가상환경 들어가기
- streamlit run app.py : streamlit run app.py 명령은 Streamlit 애플리케이션을 실행하는 명령입니다.

## 앱 대시보드 설정을 위한 기본적인 코드
- 기본적인 환경설정 후 conda activate app_dash로 가상환경에 들어갑니다.
![image](https://github.com/ijd1236/streamlit/assets/130967884/e62bff4c-d109-4549-9045-8b241a9b680e)

- 사용하고 있는 파이썬 버젼 체크
![image](https://github.com/ijd1236/streamlit/assets/130967884/eb3925e5-3891-4797-8929-41ab45d62936)

- 터미널 변경 이후 코드를 입력합니다.

```python 
def main():  
    st.title('내 앱 대시보드')  #화면에 나타낼것

if __name__ == '__main__':
    main()
```

- 터미널에 steamlit run app(파일명).py 입력


![image](https://github.com/ijd1236/streamlit/assets/130967884/dbf741f0-2885-4e4c-b0ae-733d849c29d4)

- 내 앱 대쉬보드가 만들어졌습니다.

