from collections import Counter
sensor_logs = [
    {"sensor": "lidar", "status": "ok"},
    {"sensor": "camera", "status": "error"},
    {"sensor": "lidar", "status": "ok"},
    {"sensor": "imu", "status": "ok"},
    {"sensor": "camera", "status": "ok"},
    {"sensor": "lidar", "status": "error"},
]

result = [logs['sensor'] for logs in sensor_logs]

print(Counter(result))