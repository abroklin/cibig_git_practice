## ask the user to enter 3 grades which are stored in 3 variables
grade1 = input("Enter first grade ")
grade2 = input("Enter second grade ")
grade3 = input("Enter third grade ")

## calculate the sum of the 3 variables
grade_total = float(grade1) + float(grade2) + float(grade3)
print(grade_total)

## average of 3 variables
ave_grade = grade_total / 3
print(ave_grade)
print(f"The average is {ave_grade}")

## use the if and else conditionals
## "failed" if the average is less than 10
## "passable" if the average is greater than or equal to 10
## "fairly good" if the average is greater than or equal to 12
## "good" if the average is greater than or equal to 14
## "very good" if the average is greater than or equal to 16

## if ave_grade >= 16: This method also works as Method 2
   ##  grade = "very good"
## elif ave_grade >= 14:
   ## grade = "good"
## elif ave_grade >= 12:
    ## grade = "fairly good"
## elif ave_grade >= 10:
    ## grade = "passable"
## else:
     ## grade = "failed"
## print(grade)

## Method 2
if ave_grade < 10:
   grade = "failed"
elif ave_grade >= 10:
     grade = "passable"
elif ave_grade >= 12:
     grade = "fairly good"
elif ave_grade >= 14:
     grade = "good"
elif ave_grade >= 16:
    grade = "very good"
else:"excellent"
print(grade)

####################################################


animal_list = ['cow', 'mouse', 'yeast', 'bacteria']



## Executing with the while condition





















