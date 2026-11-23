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
    
    def get_years(self):
        """이전 회사 하나에 해당하는 근무한 경력"""
        return (self.end_year - self.start_year)
    
    def to_string(self):
        return f"{self.company}\t{self.position}\t{self.start_year}~{self.end_year}\t{self.get_years()}년"

# 사원정보 + Salary 객체를 속성으로 가진다 (has-a관게)
# ====================================================================
class Employee:
    def __init__(self, name, salary, histories =None):
        self.name = name
        self.dept =""
        self.salary = salary
        self.histories = histories if histories is not None else []
        
    def add_history(self,history):
        """이전 회사의 경력을 추가합니다.
        회사 직무 근무시작년도 근무끝년도"""
        self.histories.append(history)

    def get_career(self):
        """총 경력을 불러옵니다."""
        return sum(h.get_years() for h in self.histories)
    
    def to_string(self):
            """출력 문자열 이름|경력|총액|세금|실수령액"""
            return f"{self.name}\t{self.get_career()}년\t{self.salary.get_total()}\t{self.salary.get_tax()}\t{self.salary.get_net()}"
        

# =========================================================================================================================
class Department:
    """부서에 대한 class"""
    def __init__(self, name,employees =None):
        self.name =name
        self.employees = employees if employees is not None else []

    def add_employee(self,employee):
        """부서에 사원 추가, 사원의 부서를 부서이름으로 지정"""
        employee.dept =self.name
        self.employees.append(employee)

    def get_payroll(self):
        """부서 구성원 전체의 급여 총액을 구합니다"""
        return sum(e.salary.get_total() for e in self.employees)
            
    def get_avg_career(self):
        """부서원 전체 평균 경력을 구합니다.""" 
        if not self.employees:
            return 0
        return sum(h.get_career() for h in self.employees)/len(self.employees)
    
    def print_members(self):
        """부서 구성원을 출력합니다."""
        print(f"[{self.name}] {len(self.employees)}명 | 급여 총액 {self.get_payroll()} | 평균 경력 {self.get_avg_career()}년")
        print("  이름\t경력\t총액\t세금\t실수령액")
        for en in self.employees:
            print("  " + en.to_string())
# =========================================================================================================================
class Company:
    """회사에 대한 class"""
    def __init__(self, name, departments =None):
        self.name = name
        self.departments = departments if departments is not None else []

    def add_department(self,department):
        """회사에 부서 추가"""
        self.departments.append(department)

    def get_employee_count(self):
        """회사 직원 수"""
        return sum(len(e.employees) for e in self.departments)
            
    def get_payroll(self):
        """회사 전체 급여 총액"""
        return sum(s.get_payroll() for s in self.departments)
    
    def print_report(self):
        """부서 순회 -> 사원 순회(이중 반복)"""
        print(f"===== {self.name} 사원 현황 =====")
        for d in self.departments:
            d.print_members()
        print(f"전체 사원 {self.get_employee_count()}명 | 전체 급여 총액 {self.get_payroll()}")
# ==========================================================================================================================

# 1. 사원 생성 (부서 없이) → 근무이력 추가
kim  = Employee('김민수', Salary(300, 50, 20))
choi = Employee('최서연', Salary(350, 30, 25))
lee  = Employee('이지은', Salary(320, 40, 30))
park = Employee('박준호', Salary(280, 60, 10))   # 신입
han  = Employee('한도윤', Salary(300, 70, 15))

kim.add_history(WorkHistory('네오소프트', '사원', 2015, 2018))
kim.add_history(WorkHistory('한빛시스템', '대리', 2018, 2022))
choi.add_history(WorkHistory('데이터랩', '연구원', 2012, 2016))
choi.add_history(WorkHistory('클라우드원', '선임', 2016, 2020))
choi.add_history(WorkHistory('넥스트AI', '책임', 2020, 2023))
lee.add_history(WorkHistory('그린HR', '사원', 2017, 2021))
han.add_history(WorkHistory('브랜드웍스', '사원', 2019, 2022))

# 2. 부서 생성 → add_employee()로 배치 (dept 자동 지정)
dev_dept = Department('개발팀')
hr_dept = Department('인사팀')
sales_dept = Department('영업팀')
mkt_dept = Department('마케팅팀')

dev_dept.add_employee(kim)
dev_dept.add_employee(choi)
hr_dept.add_employee(lee)
sales_dept.add_employee(park)
mkt_dept.add_employee(han)

# 3. 회사 생성 → add_department()로 부서 등록 → 리포트 출력
company = Company('블루웨이브')
for dept in [dev_dept, hr_dept, sales_dept, mkt_dept]:
    company.add_department(dept)

company.print_report()