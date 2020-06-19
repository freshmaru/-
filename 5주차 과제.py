student = {}


# 성적 입력
def enter_student(student):
    number = int(input("학번을 입력하세요 : "))
    name = input("이름을 입력하세요 : ")
    major = input("학과를 입력하세요 : ")
    korean = int(input("국어 접수를 입력하세요 : "))
    english = int(input("영어 점수를 입력하세요 : "))
    math = int(input("수학 점수를 입력하세요 : "))

    avg = (korean + english + math) / 3

    student[number] = [name, number, korean, english, math, avg]

    return student


# 학생 검색하기
def search_student(student):
    search_number = int(input("학번을 입력하세요 : "))
    if search_number != student:
        for i, k in student.items():
            print("  이름 학번 국어 영어 수학 평균")
            print(i, ":", k)
    else:
        print('해당 이름이 없습니다')


# 학생 정보 삭제하기
def delete_student(student):
    del_std = int(input("삭제하고 싶은 학생의 학번을 입력하세요 : "))
    if del_std != student:
        student.pop(del_std)
    return student


# 학점 순으로 정렬하기
def sort_student(student):
    studentList = sorted(student.items())
    print(studentList)
    return student


conf = True

while conf:

    print("1. 데이터 추가 ")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("0. 종료")
    menu = int(input("번호를 입력하시오 : "))
    if menu == 1:       #성적 입력
        student = enter_student(student)

    elif menu == 2:     #학생 점수 검색하기
        search_student(student)

    elif menu == 3:     #학생 정보 삭제하기
        student = delete_student(student)

    elif menu == 4:     # 학점 순으로 정렬하기
        student = sort_student(student)

    elif menu == 0:
        print("종료")
        conf = False
