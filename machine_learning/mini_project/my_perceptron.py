import numpy as np

X = np.array([[70,100,70,80],[90,60,80,80],[90,90,90,100],[85,70,95,75],
              [100,55,85,90],[60,95,65,70],[85,85,75,85],[70,90,70,75],
              [95,65,85,75],[80,75,70,70,],[90,85,90,95],[85,70,75,70]], float)
y = np.array([1,0,1,0, 0,1,1,1, 0,0,1,0]) # 1=합격, 0=불합격

# 1단게 - 초기설정
w = np.array([0.1, 0.2, 0.3, 0.1]) # weight
b = -20.0 # bias
eta = 0.0005 # 0.005일때보다 선형적으로 증가하는 모습

for epoch in range(12): # 학생 12명 epoch 0일때는 초기 가중치 값임
    pred_all = (X @ w + b >=0).astype(int)
    acc = (pred_all == y).sum()
    print(f"에포크 : {epoch}, 정확도 : {acc}")

    for i in range(len(X)):
        net = X[i] @ w + b
        pred = 1 if net >= 0 else 0
        err = y[i] - pred
        w = w + eta * err * X[i]
        b = b + eta * err

        