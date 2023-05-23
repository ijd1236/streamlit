import streamlit as st

def main():
    st.title('웹 대시보드')

    name = '홍길동'

    print('제 이름은 {}입니다.'.format(name)) # 터미널에 찍힘 st만 웹브라우저에 찍힘
    st.text('제 이름은 {}입니다.'.format(name))
    st.header('이 영역은 헤더 영역') 
    st.subheader('이 영역은 서브헤더 영역')
    st.success('성공했을때 나타내고 싶은 문장')
    st.warning('공고하고 싶을때 문장')
    st.info('알림을 주고 싶을때')
    st.error('문제가 발생했을음 알려주고 싶을때')
    st.help(range)



if __name__ == '__main__':
    main()


# Local URL: http://localhost:8501 뒤의 8501는 port 이다