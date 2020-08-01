
class userEntity:
    #생성자정의 : member variable - name, age, email, major 초기화
    def __init__(self, id_, password_, name, contact, gender, area):
        self.id_ = id_
        self.password_ = password_
        self.name=name
        self.contact=contact
        self.gender=gender
        self.area = area
        

    #email정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, contact):
        if(self.contact == contact):
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} : {3} : {4} : {5}  ".format(self.id_, self.password_, self.name, self.gender, self.contact, self.area)


    #toJson   : Entity -> json 변환 
    #fromJson : jons -> Entity 변환

