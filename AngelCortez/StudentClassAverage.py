#This is a calculator that will find a students class average.

test1 = float(input("Please enter test score: "))
test2 = float(input("Please enter test score: "))
test3 = float(input("Please enter test score: "))
test4 = float(input("Please enter test score: "))
test5 = float(input("Please enter test score: "))

total = test1 + test2 + test3 + test4 +test5
average = (total / 500) * 100

print("Class average = %.2f" %average)

if(average >= 90):
    print("Grade is a A")
elif(average >=80):
    print("Grade is a B")
elif(average >=70):
    print("Grade is a C")
elif(average >=60):
    print("Grade is a D")
else:
    print("Grade is a F")

