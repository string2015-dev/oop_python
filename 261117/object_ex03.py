# 딕셔너리를 리턴하는 함수를 선언
def create_student(name:str,korean:int, math:int, english:int, science:int):
    return {
        "name": name,
        "korean": korean,
        "math":math,
        "english": english,
        "science": science,
    }

students = [
    create_student('김민재', 1, 5, 1, 5),
    create_student('손재호', 2, 4, 2, 4),
    create_student('서동안', 3, 3, 3, 3),
    create_student('김희진', 4, 2, 4, 2),
    create_student('류현수', 5, 1, 5, 1),
]

# 학생을 처리하는 함수
# 학생 한명의 총점을 리턴하는 함수 : student_get_sum(student)
def student_get_sum(student):
    score_sum = student['korean'] + student['math'] + student['english'] + student['science']
    return  score_sum
# 학생 한명의 평균을 리턴하는 함수 : student_get_average(student)
def student_get_average(student):
    score_avg = student_get_sum(student) /4
    return score_avg
# 학생 한명의 점수를 출력하는 함수 : student_to_string(student)
def student_to_string(student):
    return "({})\t{}\t{}".format(student['name'], student_get_sum(student),student_get_average(student))

# 학생명단(성적표) 출력하세요
print("이름","총점","평균", sep="\t")
for student in students:
    print(student_to_string(student))