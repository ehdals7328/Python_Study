from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1단계 - 데이터 불러오고 나누기
X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# 2단계 - 모델을 만들고 학습시키기
model = LinearRegression()
model.fit(X_train, y_train) # 훈련용 데이터를 통해 학습, input과 target을 같이 -> 지도학습

# 3단계 - 시험용 데이터로 예측하기
pred = model.predict(X_test) # 미리 나눠둔, 20%의 테스트용 데이터, 과적합 방지

# 4단계 - 채점하기
print("-" * 32)
print("직접 학습시킨 MyModel")
print(f"평균오차 = {mean_absolute_error(y_test, pred):6.2f}") # 정답과 예측데이터를 비교해서 오차(손실)을 검사
print(f"설명력 = {r2_score(y_test, pred):7.4f}") # 0~1로 성능 표현

# 5단계 - 기준 모델과 비교하기
base = DummyRegressor(strategy="mean") # DummyRegressor는 전체 환자 평균 점수로 추론을함, mean의 의미임.

# 5-1 기준 모델을 학습시키기
base.fit(X_train, y_train)

# 5-2 기준 모델을 예측하기
dum_pred = base.predict(X_test)

# 5-3 기준 모델을 채점하기 - 단순히 평균값으로 계산하는 것 보다 직접 학습시킨 모델이 오차가 낮고 설명력이 높음을 증명
print("-" * 32)
print("기준 모델 DummyBase")
print(f"평균오차 = {mean_absolute_error(y_test, dum_pred):6.2f}")
print(f"설명력 = {r2_score(y_test, dum_pred):7.4f}")

# 데이터를 확인 해보기
for i in range(10):
    print(f"{i+1}번 환자의 실제 진행도 :{y_test[i]:6.2f}, 예상 당뇨 진행도 :{pred[i]:6.2f}, 오차 :{pred[i]-y_test[i]:6.2f}") # 오차가 양수면 모델이 과대예측, 음수면 과소예측