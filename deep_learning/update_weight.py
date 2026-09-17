import numpy as np

def update_weight(w_t, learning_rate, gradient):
    w_next = w_t - (learning_rate * gradient)
    return w_next

# --- 테스트 코드 ---
current_w = 0.5
eta = 0.01
grad = 2.0

new_w = update_weight(current_w, eta, 2.0)
print(f"업데이트 된 가중치: {new_w:.2f}")