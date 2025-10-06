class Student:
    def __init__(self, name = "", student_id = "", major = ""):
        self.name = name
        self.student_id = student_id
        self.major = major
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Major: {self.major}"
    
class UndergraduateStudent(Student):
    # Overriding of methods
    def __init__(self, name, student_id, major, year = ""):
        super().__init__(name, student_id, major)
        self.year = year

    def __str__(self):
        return super().__str__() + f", Year: {self.year}"


if __name__ == "__main__":
    student = Student("Jack", "U1010", "Computer Science")
    print(student)

    undergrad = UndergraduateStudent("Alice", "R4564", "Physics", "Freshman")
    print(undergrad)