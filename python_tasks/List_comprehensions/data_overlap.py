'''Data Overlap
💪 This exercise is HARD 💪 

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

You are going to create a list called result which contains the numbers that are common in both files. 
e.g. if file1.txt contained: 

1 
2 
3
and file2.txt contained: 
2
3
4
result = [2, 3]
IMPORTANT:  The output should be a list of integers and not strings!'''


with open("file1.txt","r") as file1:
    file1_numbers=[int(num.strip()) for num in file1]

with open("file2.txt","r") as file2:
    file2_numbers=[int(num.strip()) for num in file2]

result=[num for num in file1_numbers if num in file2_numbers]


print(result)