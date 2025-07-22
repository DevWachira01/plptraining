#grading system that takes input from users

# ask the user to input score
score = int(input("Enter the Students score(0-100)"))

if score >=90:
    grade= 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >=60:
    grade = 'C'

else :
    grade = "Fail"

#print the result

print("the student grade is : "+grade)