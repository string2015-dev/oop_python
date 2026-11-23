class Employee:
    """사원 급여 명세서 정의 클래스"""
    def __init__(self,name:str, base_pay:int, bonus:int, overtime:int):
        """사원의 이름 기본급, 보너스, 야근"""
        self.name =name
        self.base_pay =base_pay
        self.bonus = bonus
        self.overtime =overtime
        print(f"[{self.name}] 등록 완료")


    def get_total(self,):
        """기본급 + 보너스 + 야근수당을 합한 총액입니다."""
        return self.base_pay + self.bonus + self.overtime
    
    def get_tax(self):
        """세금을 게산합니다.
        총액 * 0.1"""
        return (self.get_total() * 0.1)
    
    def get_net(self):
        """총액 - 세금"""
        return (self.get_total() - self.get_tax())
    
    def to_string(self):
        """출력 문자열"""
        return f"{self.name}\t{self.get_total()}\t{self.get_tax()}\t{self.get_net()}"
# =============================================================================

employees =[Employee('김민수',300,50,20),
            Employee('이지은',320,40,30),
            Employee('박준호',280,60,10),
            Employee('최서연',250,30,25),
            Employee('한도윤',300,70,15),]    
print("|이름\t|총액\t|세금\t|실수령액|")    
for emp in employees:
    print(emp.to_string())