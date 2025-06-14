score = 554

if score > 100:
    print("Please verify your grade again")
    exit()

if score>=90 and score<=100:
    print("Grade A")
elif score<90 and score>=80:
    print("Grade B")
elif score<80 and score>=70:
    print("Grade C")
elif score<70 and score>=60:
    print("Grade D")
else:
    print("Fail")