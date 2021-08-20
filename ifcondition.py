marks=int(input("enter the Marks Obtained by the student : "))
if marks>=90 and marks<=100:
    if marks>=95:
        print("excellent")
if marks>=80 and marks<90:
    print("Good")
if marks<80 and marks>=70:
    print("Avarage")
if marks<70 and marks>50:
    print("pass")
else:
    print("try again")
