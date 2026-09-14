class Addr():
    def __init__(self, name, phone, email, address, group, birth):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.group = group
        self.birth = birth

    def __str__(self):
        return f"이름:{self.name} 전화번호:{self.phone} 이메일:{self.email} 주소:{self.address} 그룹:{self.group} 생일: {self.birth}"
    
class CompanyAddr(Addr):
    def __init__(self, name, phone, email, address, group, birth, co_name, part, rank):
        super().__init__(name, phone, email, address, group, birth)
        self.group = '회사'
        self.co_name = co_name
        self.part = part
        self.rank = rank

    def __str__(self):
        return f"이름:{self.name} 전화번호:{self.phone} 이메일:{self.email} 주소:{self.address} 그룹:{self.group} 생일: {self.birth} 회사명: {self.co_name} 부서명:{self.part} 직급:{self.rank}"

class CustomerAddr(Addr):
    def __init__(self, name, phone, email, address, group, birth, cu_name, item, rank):
        super().__init__(name, phone, email, address, group, birth)
        self.group = '거래처'
        self.cu_name = cu_name
        self.item = item
        self.rank = rank

    def __str__(self):
        return f"이름:{self.name} 전화번호:{self.phone} 이메일:{self.email} 주소:{self.address} 그룹:{self.group} 생일: {self.birth} 거래처명:{self.cu_name} 품목:{self.item} 직급:{self.rank}"