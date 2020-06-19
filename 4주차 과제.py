student = {}
conf = True
while conf:
    print("1. 데이터 추가 ")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("0. 종료")
    menu = int(input("번호를 입력하시오 : "))
    if menu == 1:
        number = int(input("학번을 입력하세요 :"))
        name = input("이름을 입력하세요 : ")
        major = input("학과를 입력하세요 : ")
        korean = input("국어 점수를 입력하세요 : ")
        english = input("영어 점수를 입력하세요 : ")
        math = input("수학 점수를 입력하세요 : ")
        student[number] = [name, number, korean, english, math]

    elif menu == 2:
        search = int(input("학번을 입력하세요 : "))
        if search != student:
            for i, k in student.items():
                print("    이름 학번 국어 영어 수학")
                print(i, ":", k)
        else:
            print('해당 이름이 없습니다')
    elif menu == 3:
        del_std = int(input("삭제하고 싶은 학생의 학번을 입력하세요 : "))
        if del_std != student:
            student.pop(del_std)

    elif menu == 4:     # 학점 순으로 정렬하기
        studentList = sorted(student.items())
        print(studentList)

    elif menu == 0:
        print("종료")
        conf = False



