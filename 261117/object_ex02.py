# 딕셔너리를 리턴하는 함수를 선언
def create_student(name:str,korean:int, math:int, english:int, science:int):
    return {
        "name": name,
        "korean": korean,
        "math":math,
        "english": english,
        "science": science,
    }
