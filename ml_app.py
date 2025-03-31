# ml_app.py

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="주택 가격 예측기", page_icon="🏠")

st.title("🏠 주택 가격 예측기")

# 입력 받기
area = st.slider("면적 (㎡)", 20, 100, 55)
bedrooms = st.slider("방 개수", 1, 5, 2)

# 학습 데이터
df = pd.DataFrame({
    'area': [30, 40, 50, 60],
    'bedrooms': [1, 2, 2, 3],
    'price': [200, 300, 400, 500]
})

X = df[['area', 'bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# 예측
new_data = pd.DataFrame({'area': [area], 'bedrooms': [bedrooms]})
prediction = model.predict(new_data)[0]

st.markdown(f"### 💰 예측된 집값: **{prediction:.1f} 단위**")
