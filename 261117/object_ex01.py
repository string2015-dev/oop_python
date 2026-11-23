# 학생 리스트(Students)를 선언해 주세요
# 5 명의 학생 정보를 아래 속성으로 저장하세요
# 학생은 이름(name), 국어(korean), 영어(english), 수학(math) 속성을 갖는다.

class Students:
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
# ================================================================================================

students = [
    {"name":"김민재", "korean": 10, "english":50, "math":10, "science": 50},
    {"name":"서동안", "korean": 20, "english":40, "math":20, "science": 50},
    {"name":"김희진", "korean": 30, "english":30, "math":30, "science": 50},
    {"name":"류현수", "korean": 40, "english":20, "math":40, "science": 50},
    {"name":"손재호", "korean": 50, "english":10, "math":50, "science": 50}
    ]



stu_list =[]
for k in students:
    stu_obj = Students(name=k['name'], korean=k['korean'], english=k['english'], math=k['math'], science=k['science'])
    stu_list.append(stu_obj)

# 학생명단(성적표) 출력
print()
for i in stu_list:
    print(i.name, i.korean, i.english, i.math, i.science)

# 점수의 총합과 평균을 구하시오.
print()
for i in stu_list:
    total_ = i.korean +i.english + i.math + i.science
    avg_ = int(total_/4)
    print(f"[{i.name}] 총점:{total_} 평균:{avg_}")