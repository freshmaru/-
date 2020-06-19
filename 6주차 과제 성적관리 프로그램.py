# 학생 성적 입력
class Student:

    def __init__(self, Number, Name, Major, Korean, English, Math):
        self.Number = Number
        self.Name = Name
        self.Major = Major
        self.Korean = Korean
        self.English = English
        self.Math = Math

    # 학생 검색하기
    def search(self):
        search_number = int(input("학번을 입력하세요 : "))
        if search_number == self.Number:
            print("이름 : ", self.Name)
            print("학번 : ", self.Number)
            print("국어 : ", self.Korean)
            print("영어 : ", self.English)
            print("수학 : ", self.Math)
        else:
            print('해당 이름이 없습니다')
        return self

    # 학생 정보 삭제하기
    def __del__(self):
        print('정보가 삭제되었습니다')

    # 학점 순으로 정렬하기
    def sort(self):
        print("이름 : ", self.Name)
        print("학번 : ", self.Number)
        print("국어 : ", self.Korean)
        print("영어 : ", self.English)
        print("수학 : ", self.Math)


student = {}

conf = True

while conf:

    print("1. 데이터 추가 ")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("0. 종료")
    menu = int(input("번호를 입력하시오 : "))
    if menu == 1:  # 성적 입력
        number = int(input("학번을 입력하세요 : "))
        name = input("이름을 입력하세요 : ")
        major = input("학과를 입력하세요 : ")
        korean = int(input("국어 접수를 입력하세요 : "))
        english = int(input("영어 점수를 입력하세요 : "))
        math = int(input("수학 점수를 입력하세요 : "))

        student = Student(number, name, major, korean, english, math)

    elif menu == 2:  # 학생 점수 검색하기
        student = Student.search(student)

    elif menu == 3:  # 학생 정보 삭제하기
        del(student)

    elif menu == 4:  # 학점 순으로 정렬하기
        Student.sort(student)

    elif menu == 0:
        print("종료")
        conf = False
