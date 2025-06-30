def avg_score(score):

    total = sum(score)
    length = len(score)
    
    average_score = total / length
    return average_score


def compute_grade(avg):
    if avg >= 80.0:
        grade = 'A'

    elif avg > 60.0:
        grade = 'B'
    
    elif avg >=50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

num_elements= int(input("enter how many grades per student: "))
grades_list =[]

for i in range(num_elements):
    value = int(input(f"Enter element {i+1}: "))
    grades_list.append(value)

avg_score = avg_score(grades_list)
grade = compute_grade(avg_score)
print(f"Average Score: {avg_score}")
print(f"Grade: {grade}") 