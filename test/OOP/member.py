class Member():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"회원명: {self.name} 나이: {self.age}"

    