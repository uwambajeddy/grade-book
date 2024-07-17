class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.gpa = 0.0

    def calculate_GPA(self):
        total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
        total_credits = sum(course['credits'] for course in self.courses_registered)
        if total_credits > 0:
            self.gpa = total_points / total_credits
        else:
            self.gpa = 0.0

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})
        self.calculate_GPA()

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
    
    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda student: student.gpa, reverse=True)

    def search_by_grade(self, course_name, min_grade, max_grade):
        result = []
        for student in self.student_list:
            for course in student.courses_registered:
                if course['course'].name == course_name and min_grade <= course['grade'] <= max_grade:
                    result.append(student)
                    break
        return result

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            transcript = f"Transcript for {student.names} (Email: {student.email}):\n"
            for course in student.courses_registered:
                transcript += f"{course['course'].name} - Grade: {course['grade']} - Credits: {course['credits']}\n"
            transcript += f"GPA: {student.gpa}"
            return transcript
        return "Student not found"

def main():
    gradebook = GradeBook()

    while True:
        print("\n\n=============Choose an action =============\n\n 1. add student \n 2. add course\n 3. register student for course\n 4. calculate ranking\n 5. search by grade\n 6. generate transcript\n 7. exit\n")
        action = input("Action: ")

        if action == "1":
            print("\n\n============= Add student =============")
            email = input("Student Email: ")
            names = input("Student Names: ")
            gradebook.add_student(email, names)
        elif action == "2":
            print("\n\n============= Add course =============")
            name = input("Course Name: ")
            trimester = input("Course Trimester: ")
            credits = int(input("Course Credits: "))
            gradebook.add_course(name, trimester, credits)
        elif action == "3":
            print("\n\n============= Register student for course=============")
            student_email = input("Student Email: ")
            course_name = input("Course Name: ")
            grade = float(input("Grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
        elif action == "4":
            print("\n\n============= Calculate ranking =============")
            ranking = gradebook.calculate_ranking()
            for i, student in enumerate(ranking, start=1):
                print(f"{i}. {student.names} - GPA: {student.gpa}")
        elif action == "5":
            print("\n\n============= Search by grade =============")
            course_name = input("Course Name: ")
            min_grade = float(input("Min Grade: "))
            max_grade = float(input("Max Grade: \n"))
            result = gradebook.search_by_grade(course_name, min_grade, max_grade)
            for student in result:
                print(f"{student.names} - GPA: {student.gpa}")
        elif action == "6":
            print("\n\n============= Generate transcript =============")
            student_email = input("Student Email: ")
            transcript = gradebook.generate_transcript(student_email)
            print(transcript)
        elif action == "7":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
