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
        self.score_sum = self.korean +self.english + self.math + self.science
        return self.score_sum

    # 학생 평균 계산 함수
    def stu_avg(self):
        self.score_avg = self.stu_total()/4
        return self.score_avg
    
    # 학생 총점, 평균 성적표
    def stu_string(self):
        return f"[{self.name}] 총점:{self.stu_total()} 평균:{self.stu_avg()}"

# ======================================================================

students =[Students('김민재',1,2,3,1), Students('손재호',2,2,3,4), Students('박세람',3,2,3,4),Students('노동균',3,2,3,4),Students('서동안',4,2,3,4),]
print()
print("이름","총점", "평균",sep="\t")
for s in students:
    print(s.stu_string())
print()
for s in students:
    print(s.stu_string())