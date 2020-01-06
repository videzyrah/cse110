student_name = input("Enter student's name:")
course_name = input("Enter course name:")
      
quizzes_weight = float(input("Enter quizzes weight:")) 
projects_weight = float(input("Enter projects weight:")) 
activities_weight = float(input("Enter activities weight:")) 
attendance_weight = float(input("Enter attendance weight:")) 
exams_weight = float(input("Enter exams weight:")) 

quizzes_average = float(input("Enter quizzes average:")) 
projects_average = float(input("Enter projects average:")) 
activities_average = float(input("Enter activities average:")) 
attendance_average = float(input("Enter attendance average:")) 
exams_average = float(input("Enter exams average:"))

course_grade = (quizzes_weight * quizzes_average +
               projects_weight * projects_average +
               activities_weight * activities_average +
               attendance_weight * attendance_average +
               exams_weight * exams_average) * 100
               
print("Hi", str(student_name) +",", "\nYou have a " + str(course_grade) + "% in your", course_name, "course.")
