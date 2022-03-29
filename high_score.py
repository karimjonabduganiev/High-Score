student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

total_score = 0
for score in student_scores:
    if score > total_score:
        total_score = score

print(f"The highest score is: {total_score}")