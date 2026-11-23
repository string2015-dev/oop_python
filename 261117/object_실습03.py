# Has-a 관게는 포함 속성을 먼저 정의 해야한다.
class Salary:
    """급여 계산만 담당하는 class다."""
    def __init__(self, base_pay, bonus, overtime):
        self.base_pay =base_pay
        self.bonus =bonus
        self.overtime = overtime

    def get_total(self,):
        """기본급 + 보너스 + 야근수당을 합한 총액입니다."""
        return (self.base_pay + self.bonus + self.overtime)
        
    def get_tax(self):
        """세금을 게산합니다.
        총액 * 0.1"""
        return (self.get_total() * 0.1)
    
    def get_net(self):
        """총액 - 세금"""
        return (self.get_total() - self.get_tax())

# Has-many 관계
class WorkHistory:
    """회사, 직책, 입사년도, 퇴사년도"""
    def __init__(self, company, position, start_year, end_year):
        self.company = company
        self.position = position
        self.start_year =start_year
        self.end_year = end_year
    
    def get_year(self):
        """이전 회사 하나에 해당하는 근무한 경력"""
        return (self.end_year - self.start_year)
    
    def to_string(self):
        return f"[{self.company}]에서 {self.get_year()}년 근무했습니다"

# 사원정보 + Salary 객체를 속성으로 가진다 (has-a관게)
# ====================================================================
class Employee:
    def __init__(self, name, dept, salary, histories =None):
        self.name = name
        self.dept =dept
        self.salary = salary
        self.histories = histories if histories is not None else []
        
    def add_history(self,history):
        """이전 회사의 경력을 추가합니다.
        회사 직무 근무시작년도 근무끝년도"""
        self.histories.append(history)

    def get_career(self):
        """총 경력을 불러옵니다."""
        return sum(h.get_year() for h in self.histories)
    
    def to_string(self):
            """출력 문자열"""
            return f"{self.name}\t{self.dept}\t{self.get_career()}년\t{self.salary.get_total()}\t{self.salary.get_tax()}\t{self.salary.get_net()}"
        

# =========================================================================================================================

employees =[Employee('김민수','개발팀',Salary(300,50,20),[WorkHistory('회사','과장',2018,2025)]),
            Employee('이지은','인사팀',Salary(300,50,40),[WorkHistory('회사','직급',2021,2025)]),
            Employee('박준호','영업팀',Salary(280,60,10)),
            Employee('최서연','개발팀',Salary(300,65,40),),
            Employee('한도윤','마케팅팀',Salary(300,60,25),[WorkHistory('회사','과장',2022,2025)]),]

for h in employees:
    if h.name =='최서연':
        h.add_history(WorkHistory('데이터랩','사원',2000,2004))
        h.add_history(WorkHistory('클라우드원','사원',2004,2008))
        h.add_history(WorkHistory('넥스트AI','대리',2008,2011))

print()
print(f"이름\t부서\t경력\t총액\t세금\t실수령액")
for emp in employees:
    print(emp.to_string())
print()
print(*(employees[3].histories[i].to_string() for i in range(len(employees[3].histories))),sep='\n')
print()
for emp in employees:
    print(f"[{emp.name}] 총 경력 {emp.get_career()}")
    if len(emp.histories) == 0:
        print(" 이력 없음(신입)")
    for h in emp.histories:
        print(" "+h.to_string())