# class Student: pass

# student = Student()

# students =[Student(),Student(),Student()]

# class 클래스이름:
#     def __init__: (self, 추가적인 매개변수): pass
#         self.name => name는 식별자.

class Students:
    """학생 성적관리 클래스"""
    # 학생 등록 메서드
    def __init__(self, name:str="홍길동", korean:int=0, english:int=0, math:int=0, science:int=0):
        self.name = name
        self.korean = korean
        self.english =english
        self.math = math
        self.science = science
        print(f"[{self.name}] 학생 성적 리스트 등록!")
    
    # 학생 총점 계산 함수
    def stu_total(self):
        return self.korean +self.english + self.math + self.science

    # 학생 평균 계산 함수
    def stu_avg(self):
        return self.stu_total()/4
    # 학생 총점, 평균 성적표
    def stu_string(self):
        print(f"[{self.name}] 총점:{self.stu_total()} 평균:{self.stu_avg()}")

# ======================================================================

students =[Students('김민재',1,2,3,4), Students('손재호',1,2,3,4)]
print()
for s in students:
    s.stu_string()