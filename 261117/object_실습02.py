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
    
# 사원정보 + Salary 객체를 속성으로 가진다 (has-a관게)
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept =dept
        self.salary = salary

    def to_string(self):
            """출력 문자열"""
            return f"{self.name}\t{self.dept}\t{self.salary.get_total()}\t{self.salary.get_tax()}\t{self.salary.get_net()}"
        

# =========================================================================================================================
employees =[Employee('김민수','개발팀',Salary(300,50,20)),
            Employee('이지은','인사팀',Salary(320,40,30)),
            Employee('박준호','영업팀',Salary(280,60,10)),
            Employee('최서연','개발팀',Salary(350,30,25)),
            Employee('한도윤','마케팅팀',Salary(300,70,15),)]

print()
print(f"이름\t부서\t총액\t세금\t실수령액")
for emp in employees:
     print(emp.to_string())