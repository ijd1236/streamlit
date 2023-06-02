import tensorflow as tf

# 데이터셋 생성
x_train = [1, 2, 3, 4, 5]
y_train = [2, 4, 6, 8, 10]

# 가중치와 편향 변수 생성
W = tf.Variable(0.0)
b = tf.Variable(0.0)

# 선형 모델 정의
def linear_model(x):
    return W * x + b

# 손실 함수 정의 (평균 제곱 오차)
def loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# 옵티마이저 설정
optimizer = tf.optimizers.SGD(learning_rate=0.01)

# 학습 과정 정의
def train_step(x, y):
    with tf.GradientTape() as tape:
        # 모델 예측값 계산
        y_pred = linear_model(x)
        # 손실 계산
        current_loss = loss(y, y_pred)
    # 가중치와 편향에 대한 경사값 계산
    gradients = tape.gradient(current_loss, [W, b])
    # 경사하강법을 이용하여 가중치와 편향 업데이트
    optimizer.apply_gradients(zip(gradients, [W, b]))

# 학습
epochs = 1000
for epoch in range(epochs):
    train_step(x_train, y_train)

# 학습된 모델 평가
x_test = [6, 7, 8, 9, 10]
y_test = [12, 14, 16, 18, 20]
y_pred = linear_model(x_test)
test_loss = loss(y_test, y_pred)
print(f"Test Loss: {test_loss.numpy()}")

# 학습된 모델 예측
x_new = [11, 12, 13, 14, 15]
y_new = linear_model(x_new)
print(f"Predictions: {y_new.numpy()}")