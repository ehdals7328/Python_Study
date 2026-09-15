from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, confusion_matrix) # 분류 평가 지표

X, y = load_diabetes(return_X_y=True)
y_binary = (y >= 140).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("학습시킨 LogisticRegression")
print(f"정확도: {accuracy_score(y_test, pred):.4f}")
print(f"정밀도: {precision_score(y_test, pred):.4f}")
print(f"재현율: {recall_score(y_test, pred):.4f}")
print(confusion_matrix(y_test, pred))
print("-" * 50)

dum = DummyClassifier(strategy="most_frequent")
dum.fit(X_train, y_train)

pred_dum = dum.predict(X_test)

print("학습시킨 Dummy")
print(f"정확도: {accuracy_score(y_test, pred_dum):.4f}")
print(f"정밀도: {precision_score(y_test, pred_dum):.4f}")
print(f"재현율: {recall_score(y_test, pred_dum):.4f}")
print(confusion_matrix(y_test, pred_dum)) # 아니오를 예라 답하고 예를 예라 답함. 예만 답하고있음
print("-" * 50)