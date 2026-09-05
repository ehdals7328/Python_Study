vision_detections = [
    {"object": "apple", "x": 120, "y": 80, "depth": 450, "confidence": 0.95},
    {"object": "cup", "x": 300, "y": 200, "depth": 5, "confidence": 0.3},       # 노이즈/낮은 신뢰도 (제외)
    {"object": "apple", "x": 124, "y": 82, "depth": 454, "confidence": 0.92},   # 연속 프레임 재인식
    {"object": "cup", "x": 310, "y": 205, "depth": 600, "confidence": 0.88},
]

def process_vla_vision_data(detections):
    """
    VLA 비전 인식 데이터에서 노이즈를 제거하고 객체별 평균 위치(X, Y, Depth)를 도출하는 함수
    """
    obj_totals = {}  # 객체별 (x합, y합, depth합) 누적
    obj_counts = {}  # 객체별 유효 인식 횟수 누적

    for item in detections:
        obj_name = item["object"]
        x, y, depth = item["x"], item["y"], item["depth"]
        conf = item["confidence"]

        # 1. 노이즈 및 유효성 필터링 (신뢰도 0.5 이상 & 정상 거리 100mm~1500mm)
        if conf >= 0.5 and (100 <= depth <= 1500):
            if obj_name not in obj_totals:
                obj_totals[obj_name] = [0.0, 0.0, 0.0]
                obj_counts[obj_name] = 0

            # X, Y, Depth 좌표 누적
            obj_totals[obj_name][0] += x
            obj_totals[obj_name][1] += y
            obj_totals[obj_name][2] += depth
            obj_counts[obj_name] += 1

    # 2. 동적 평균 좌표 계산 (로봇 제어부에 전달할 Target Location)
    target_locations = {}
    for obj_name in obj_totals:
        avg_x = obj_totals[obj_name][0] / obj_counts[obj_name]
        avg_y = obj_totals[obj_name][1] / obj_counts[obj_name]
        avg_depth = obj_totals[obj_name][2] / obj_counts[obj_name]

        target_locations[obj_name] = {
            "x": round(avg_x, 2),
            "y": round(avg_y, 2),
            "depth": round(avg_depth, 2)
        }

    return target_locations

# 실행 및 결과 확인
vla_target_data = process_vla_vision_data(vision_detections)
print("[VLA 로봇 목표 좌표 처리 결과]:")
print(vla_target_data)