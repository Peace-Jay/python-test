def grades(user_score):
    user_grade = ""
    if 99 <= user_score <= 100:
        user_grade = "A+"
    elif 96 <= user_score <= 98:
        user_grade = "A"
    elif 94 <= user_score <= 95:
        user_grade = "A-"
    elif 91 <= user_score <= 93:
        user_grade = "B+"
    elif 88 <= user_score <= 90:
        user_grade = "B"
    elif 85 <= user_score <= 87:
        user_grade = "B-"
    elif 82 <= user_score <= 84:
        user_grade = "C+"
    elif 79 <= user_score <= 81:
        user_grade = "C"
    elif 76 <= user_score <= 78:
        user_grade = "C-"
    elif 74 <= user_score <= 75:
        user_grade = "D+"
    elif 72 <= user_score <= 73:
        user_grade = "D"
    elif 70 <= user_score <= 71:
        user_grade = "D-"
    elif 0 <= user_score <= 70:
        user_grade = "F"
    return user_grade
class School:
    def __init__(self, name, student_list=None, student_score=None):
        self.name = name
        self.students = student_list
        self.score = student_score
    def Show_name(self):
        names = self.students["students_names"]
        for i in names:
            print(i, "is a student")
    def Show_score(self):
        names = self.students["students_names"]
        scores = self.students["students_scores"]
        for i in range(len(scores)):
            #print(scores[i])
            #print(grades(scores[i]))
            print(names[i], "scored", scores[i], "had a grade of", grades(scores[i]))


students = {
    "students_names": ["basit", "joy", "peace", "emma", "favour", "precious", "faith", "dolapo", "toyosi", "victoria"],
    "students_scores": [70,  55, 90, 95, 100, 50, 99, 85, 90, 80]
}
my_school = School("emma", student_list=students, student_score=students)
my_school.Show_score()



