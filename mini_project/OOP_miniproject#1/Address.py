class Addr():
    address_list = []
    def __init__(self, name, phone, email, adress, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.adress = adress
        self.group = group

    def __str__(self):
        return f"이름:{self.name} 전화번호:{self.phone} 이메일:{self.email} 주소:{self.adress} 그룹(친구/가족):{self.group}"

    def add_adress(self, obj):
        self.address_list.append(obj)

#adress2 = Addr('김철수', '010-1111-2222', 'cjftn1111@gmail.com', '서울', '가족')
#adress3 = Addr('최영희', '010-3333-4444', 'dudgml3333@gmail.com', '부산', '가족')
#Addr.address_list.append(adress2)
#Addr.address_list.append(adress3)