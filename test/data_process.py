# 이 함수는 로봇이 센서로 측정한 데이터의 노이즈를 제거하고 평균을 도출하는 함수임
sensor_records = [
    {"sensor_id": "front", "distance": 150},
    {"sensor_id": "back", "distance": 5},     # 노이즈 (10 미만: 제외)
    {"sensor_id": "front", "distance": 120},
    {"sensor_id": "left", "distance": 300},   # 노이즈 (200 초과: 제외)
    {"sensor_id": "left", "distance": 80},
    {"sensor_id": "back", "distance": 50}
]

def process_sensor_data(sensor_records):
    total_distance = {}
    avg_distance = {}
    count = {}
    for line in sensor_records:
        side = line['sensor_id']
        dis = line['distance']
        if dis >= 10 and dis <= 200:
            total_distance[side] = total_distance.get(side, 0) + float(dis)
            count[side] = count.get(side, 0) + 1

    for side in total_distance:
        avg_distance[side] = total_distance[side] / count[side]
    return avg_distance

a = process_sensor_data(sensor_records)
print(a)
