import numpy as np
import matplotlib.pyplot as plt

# 시그모이드 함수 및 그 도함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 학습 데이터
X = np.array([
    [0.0], [0.1], [0.2], [0.3],
    [0.4], [0.5], [0.6], [0.7],
    [0.8], [0.9], [1.0]
]) # (11,1)

y = np.array([
    [0.00], [0.36], [0.64], [0.84],
    [0.96], [1.00], [0.96], [0.84],
    [0.64], [0.36], [0.00]
]) # (11,1)

# 신경망 구조
input_size = 1
hidden_size = 16
output_size = 1

# 가중치 초기화
np.random.seed(42)
weights_input_hidden = np.random.uniform(-1, 1, (input_size, hidden_size)) # input -> hidden 의 w
weights_hidden_output = np.random.uniform(-1, 1, (hidden_size, output_size)) # hidden layer -> output 의 w

# bias
bias_hidden = np.random.uniform(-1, 1, (1, hidden_size))
bias_output = np.random.uniform(-1, 1, (1, output_size))

# 학습률 및 반복 횟수
eta = 0.25
epochs = 1000000

# 학습 과정
for i in range(epochs):

    # forward
    hidden_input = X @ weights_input_hidden + bias_hidden # w 들은 초기 상태가 random , hidden_input == net 값 (행렬 곱) (11, 1) @ (1, 4) -> (11, 4)
    hidden_output = sigmoid(hidden_input) # net 값을 activation function에 집어넣은 Output, 다음 layer에서 input이 되는 값

    final_input = (hidden_output @ weights_hidden_output) + bias_output # hidden layer -> Output
    final_output = sigmoid(final_input) # input 부터, (11, 1) @ (1, 4) -> (11, 4) hidden layer (11, 4) @ (4, 1) -> (11, 1)

    # 오차 계산
    err = y - final_output # tnk - onk , L2_score (MSE) 의 미분꼴로 봐도 됨

    # 역전파
    d_output = err * sigmoid_derivative(final_output) # 출력층의 gradient, 단층이 아님 ! hidden layer와 output 사이의 chain rule
    error_hidden = d_output @ weights_hidden_output.T # hidden layer까지의 err함수 미분 꼴, 차원을 맞추기 위해 전치 
    d_hidden = error_hidden * sigmoid_derivative(hidden_output) # 은닉층 의 gradient (은닉층 노드의 오차)

    # 가중치,bias 업데이트
    weights_hidden_output += (hidden_output.T @ d_output) * eta # hidden_output은 3번째 layer의 input이며,  d_output은 E'(w) * derivate_sigmoid(o) 꼴이므로 일반화식 과 동일함. (델타 w 를 구하는)

    bias_output += np.sum(d_output, axis=0, keepdims=True) * eta # 11개의 데이터를 전부 합쳐야함 (11, 1) -> (1, 1) 편향은 업데이트 공식이 E'(w) * derivate_sigmoid(o) 까지라 d_output 자체가 기울기가됨

    weights_input_hidden += (X.T @ d_hidden) * eta # 여기서 input값은 X ,

    bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * eta # (11, 16) -> (1, 16)  

    # 학습 상태 출력 (100,000번 마다)
    if i % 100000 == 0:
        loss = np.mean(np.square(err)) # 에러함수, MSE 평균제곱오차
        print(f"반복:{i}, 오차: {loss:.6f}")

# 결과 시각화
plt.plot(X, y, 'ro', label='Actual Data')
plt.plot(X, final_output, 'b-', label='Predicted')
plt.xlabel('Input (x)')
plt.ylabel('Output (f(x))')
plt.legend() # 범례
plt.title('Neural Network Approximation of f(x) = 4x(1 - x)')
plt.show()
