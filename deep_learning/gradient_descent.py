import numpy as np

def gradient(w):
    return 2 * (w - 3) # 에러함수의 미분

def gradient_descent(w_init, learning_rate, tolerance, max_iter):
    w = w_init
    history = [w]

    for t in range(max_iter):
        grad = gradient(w)
        w_next = w - (learning_rate * grad)
        history.append(w_next)

        if abs(w_next - w) < tolerance:
            return w_next, t + 1, history

        w = w_next
    return w, max_iter, history

f_w, epochs, history = gradient_descent(0, 0.1, 0.000001, 100)
print(f"반복 종료 ! 시행 횟수 : {epochs}, 최종 가중치 : {f_w}")