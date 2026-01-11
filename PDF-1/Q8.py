class Course:
    total_students = 0
    def __init__(self,student_name,age):
        self.student_name = student_name
        self.age = age
    def enroll(self):
        Course.total_students +=1
    @classmethod
    def show_total(cls):
        print("Total Students enrolled: ",cls.total_students)
    @staticmethod
    def is_eligible(age):
        if age >= 18:
            return True
        return False

stu1 = Course("Yaswanth",23)
stu2 = Course("Pavani",25)
stu3 = Course("Prasanna",21)
stu4 = Course("Rohith",16)

Course.is_eligible(19)
if Course.is_eligible(stu1.age):
    stu1.enroll()
if Course.is_eligible(stu4.age):
    stu4.enroll()
if Course.is_eligible(stu2.age):
    stu4.enroll()
if Course.is_eligible(stu3.age):
    stu4.enroll()
print(f"Is Yaswanth Eligible? : Yes {stu1.age}", Course.is_eligible(stu1.age))  # True
print("Rohith eligible?", Course.is_eligible(stu4.age))
print("Prasanna eligible?", Course.is_eligible(stu3.age))
print("Pavani eligible?", Course.is_eligible(stu2.age))
Course.show_total()
