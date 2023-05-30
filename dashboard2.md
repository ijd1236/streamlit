# 간단한 대시보드 만들기

## 간단한 문자 표현
```
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
```
### 실행결과

![image](https://github.com/ijd1236/streamlit/assets/130967884/6b1db52b-5fad-4e3d-9c2a-22d399045fae)

## 대시보드에 데이터 출력

```python
import streamlit as st
import pandas as pd # 데이터를 출력할 것이기 때문에 pandas 라이브러리를 import 해줘야 합니다.

def main():
    st.title('웹 대시보드')
    
    df = pd.read_csv('data/iris.csv') # 'iris.csv' 데이터를 불러옵니다
    print(df) # 터미널에 출력한 데이터를 보이게 합니다.
    st.dataframe(df) # 대시보드에 데이터를 보이게 합니다
    species = df['species'].unique() # 데이터 'species' 컬럼에 있는 고유값들을 species 변수에 저장합니다
    st.text('아이리스 꽃은' + species + '으로 되어있다') # 'species' 변수에 저장된 species열의 고유값들과 문자를 조합하여 텍스트로 출력합니다
    st.write(df.head()) # 데이터의 head(5행)를 출력합니다.


if __name__ == '__main__':
    main()

```

### 실행결과

![image](https://github.com/ijd1236/streamlit/assets/130967884/ce196360-32f6-485a-877c-eda0847c3b72)

## 선택 따른 데이터 출력

```python
import streamlit as st
import pandas as pd

def main():
    st.title('웹 대시보드')
    df = pd.read_csv('data/iris.csv')
    # 버튼
    if st.button('데이터보기'): #데이터 보기 버튼을 생성하고 if 문을 사용하여 버튼을 누를 시 데이터가 보이게 설정한다
        st.dataframe(df)
 ```
 ![image](https://github.com/ijd1236/streamlit/assets/130967884/f91b259d-84c6-40ce-aeff-52bed47292a6)

### button 활용

 ```python
    name = 'Mike'
    # if 문을 사용하여
    # 대문자 버튼을 누르면, 대문자로 표시하고
    # 소문자 버튼을 누르면, 소문자로 나오게 하자
    if st.button('소문자') :
        st.text(name.lower()) # lower 함수를 사용하여 name 변수에 저장된 문자를 소문자로 출력
    if st.button('대문자') :
        st.text(name.upper()) # upper 함수를 사용하여 name 변수에 저자오딘 문자를 대문자로 출력
```
        
- 해당 버튼을 누를 시 name 변수에 저장된 문자 Mike를 변환하여 소문자, 대문자가 출력된다     
  ![image](https://github.com/ijd1236/streamlit/assets/130967884/690f2dc2-74b1-42d3-90db-05fd084978ca)
 
 ### radio 활용
 
```python
    #petal_length 컬럼을 정렬하고 싶다.
    #오름차순정렬, 내림차순 정렬 두가지 옵션 선택하도록
    status =st.radio('정렬을 선택하세요',['오름차순', '내림차순'])
    
    # if문을 사용하여 오름차순, 내림차순을 각각 클릭시 해당 데이터 프레임을 보이게 합니다
    
    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length', ascending=True))  #petal_length열 기준으로 오름차순 정렬
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length', ascending=False)) #petal_length열 기준으로 내림차순 정렬
        
```
- 버튼을 누를 시 해당 데이터 프레임을 출력합니다.

![image](https://github.com/ijd1236/streamlit/assets/130967884/c24f0b2a-a47e-43fc-a323-fd07279db1b6)

### checkbox 활용

```

    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df.head(3))
    else:
        st.write('데이터가 없습니다')
 ```

- 체크박스를 누를시 head(3) 3행의 데이터 프레임을 출력하게 합니다.
![image](https://github.com/ijd1236/streamlit/assets/130967884/2a4f35ef-cc3d-4083-9a57-ed918286a181)


  
### selectbox 활용
```python
    # 여러개의 항목중 1개를 선택하고 싶을때 사용합니다
    # if 문을 사용하여 각 박스를 선택시 출력할 내용을 입력합니다.
    language= ['Python', 'Java', 'C', 'Go', 'PHP']
    selected_lang = st.selectbox('선호하는 언어를 선택!', language)
    if selected_lang == 'Python':
        st.text('파이썬이 최고지')
    elif selected_lang == 'Java':
        st.text('클래스가 좀 어렵지')
    elif selected_lang == 'C':
        st.text('드록바')
    elif selected_lang == 'GO':
        st.text('렘파드')
    elif selected_lang == 'PHP':
        st.text('몰라')
```
![image](https://github.com/ijd1236/streamlit/assets/130967884/be8e9003-ce0f-409d-af89-d8209ddd5bde)

### multiselect 활용

```python
    # 데이터 프레임의 컬럼이름을 보여주고, 유저가 컬럼을 선택하면
    # 해당컬럼만 가져와서 데이터프레임을 보여주고 싶다.
    column_list =st.multiselect('컬럼을 선택하세요', df.columns) # 데이터 프레임의 열들을 박스 항목에 넣습니다 
    # 선택한 컬럼으로 데이터 프레임 보여주기
    st.dataframe(df[column_list]) # 셀렉박스에서 선택한 열의 데이터를 출력하게 합니다.
```
![image](https://github.com/ijd1236/streamlit/assets/130967884/77dccfc5-880f-4eab-9a90-2a565131e227)


### slider 활용

```python
    age =st.slider('나이',10, 110, step = 1,value = 50) # (타이틀, min, max)
    st.text('나이는'+str(age)+'입니다.')
```
- 이런식으로 slider를 지정할때마다 해당 숫자와 텍스트가 입력됩니다.

![image](https://github.com/ijd1236/streamlit/assets/130967884/811101a5-f3b5-49c6-8f3e-d87e8262802d)
    
 ### expander 활용
 
    with st.expander('hello'):   # expander를 누르면 텍스트가 나오게 한다
        st.text('안녕하세요') 
```
- 아래로 접었다 펴지는 expander를 만듭니다.

![image](https://github.com/ijd1236/streamlit/assets/130967884/078fe0e4-1527-4a56-85f9-94e9b115de17)




