from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score # 분류 평가 지표

X, y = load_diabetes(return_X_y=True)

y_binary = (y >= 150).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
pred_prob = model.predict_proba(X_test)[:,-1]

print("학습시킨 LogisticRegression")
print(f"정확도: {accuracy_score(y_test, pred):.4f}")
print("-" * 50)


for i in range(10):
    if pred[i] == 1:
        status = "위험(1)"
    else:
        status = "정상(0)"
    if y_test[i] == 1:
        real_status = "위험(1)"
    else:
        real_status = "정상(0)"
    print(f"{i+1:2d}번 환자 실제상태 : {real_status} , 예측상태 : {status}, 당뇨확률 {pred_prob[i] * 100:.1f}%")