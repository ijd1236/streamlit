import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():  #화면에 나타낼것
    st.title('내 앱 대시보드') 

    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)
    # sepal_length(꽃받침 길이), sepal_width(너비)의 관계를 차트로
    fig=plt.figure()
    plt.scatter(data = df, x = 'sepal_length', y='sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal lenth')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.regplot(data = df, x = 'sepal_length', y='sepal_width')
    st.pyplot(fig2)
    correlation = df[['sepal_length', 'sepal_width']].corr() #상관관계
    st.dataframe(correlation)

    # sepal_length 로 히스트그램 그리자.
    # bin의 갯수는 20개로
    fig3 = plt.figure(figsize= ( 10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(data=df, x = 'sepal_length', rwidth=0.8, bins = 10)
    plt.subplot(1, 2, 2)
    plt.hist(data=df, x = 'sepal_length', rwidth=0.8, bins = 20)
    st.pyplot(fig3)

    # species 컬럼에는 종에 대한 정보가 들어있는데, 
    # 각 종별로 몇개씩의 데이터가 있는지
    # 차트로 나타내시오.
    st.dataframe(df['species'].value_counts())
    fig4 =plt.figure()
    sns.countplot(data=df, x= 'species') #숫자세서 막대형식으로 보여준다.
    st.pyplot(fig4)
    ## 데이터프레임의 차트 그리는 코드도 실행 가능!
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='barh') #plot 안에 kind로 표시 종류 지정 가능
    st.pyplot(fig5)
    # 데이터 프레임 자체 plot 함수는 스트림릿에서 안됨
    # fig6 = plt.figure()
    # df.plot()
    # st.pyplot(fig6)
    fig7 = plt.figure(figsize= (10, 4))
    df['sepal_length'].hist()
    st.pyplot(fig7)








if __name__ == '__main__':
    main()