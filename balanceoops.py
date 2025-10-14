# # # static method
# class student:
#     @staticmethod
#     def prints(stu):
#         print(f'The student name is {stu}')

# s= student()
# s.prints("XYZ")



# class student:
#     def prints(self,stu):
#         self.stu = stu
#         print(f'The student name is {self.stu}')
# s= student()
# s.prints("XYZ")





# class method
class student:
    course = "Python"
    name = "Abc"
    @classmethod
    def change_courseName(cls,newCourse):
        cls.course = newCourse
        print(f'Student Name :{cls.name} Course Name : {cls.course}')

        

# student.change_courseName("Java")
# student.show()

s1 = student()
s1.change_courseName("Java")

