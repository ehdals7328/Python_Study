import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# 1단계 - 데이터 불러오기
data = load_iris()
X = data.data # 꽃 150송이 x 네 가지 길이

# 2단계 - 모델 만들기
km = KMeans(n_clusters=3, random_state=42, n_init=10)

# 3단계 - 무리 만들기
km.fit(X)

# 4단계 - 결과 살펴보기
labels = km.labels_
print(f"무리별 인원 = {np.bincount(labels)}")
print(f"무리 안 흩어진 정도 = {km.inertia_:.2f}")
print("무리 중심점:")
print(np.round(km.cluster_centers_,2))

# 5단계 - 실제 품종과 비교해 보기
for c in range(3):
    m = labels == c # 반복문 c의 번호와 레이블 번호 0 1 2 와 맞는지 확인
    print("무리", c, "인원", m.sum(), np.bincount(data.target[m], minlength=3))
    # m.sum 으로 0,1 로 나뉘어진 값중 1을 전부 더하면 무리에 속한 인원이 나옴
print(data['target_names'])
