student_scores=[12,21,23,32,43,453,432,177]
#print(max(student_scores))

max=0
for score in student_scores:
    if score>max:
        max=score
print(max)