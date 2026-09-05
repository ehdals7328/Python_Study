# 로봇의 좌/우 모터 속도를 제어하는 절차지향 코드를 OOP로 리팩토링

class RobotSystem:
    def __init__(self):
        self.left_speed = 0
        self.right_speed = 0

    def set_speed(self, left, right):
        self.left_speed = left
        self.right_speed = right
        print(f"속도 설정 완료: 좌={self.left_speed}, 우={self.right_speed}")

    def stop(self):
        self.left_speed = 0
        self.right_speed = 0
        print("로봇이 정지 했습니다.")

    def set_status(self):
        status = (self.left_speed, self.right_speed)
        return status
        
