import numpy as np
from math import exp

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(s):
    return s * (1 - s)


def forward(x, w, b):
    z = w * x + b
    o = sigmoid(z)
    return z, o 

def backward(x, t, o):
    dw = (o - t) * sigmoid_derivative(o) * x
    db = (o - t) * sigmoid_derivative(o) * 1
    return dw, db


lr = 0.1
x = 0.5
t = 1.0
w = 0.8
b = 0.2

for epoch in range(1000):
   z, o = forward(x, w, b)

   loss = 0.5 * (t - o)**2
   dw, db = backward(x, t, o)

   w = w - dw
   b = b - db

print(f"최종 예측값: {o:.4f}, 목표값: {t}")