s = input("Your Marks in Science: ")
m = input("Your Marks in Maths: ")
e = input("Your Marks in English: ")
l = input("Your Marks in 2L: ")
sst = input("Your Marks in Social: ")

all = [s, m, e, l, sst]

total_marks = int(s) + int(m) + int(e) + int(l) + int(sst)
print("Your Total Marks is", total_marks)

percent = total_marks / 200 * 100

if percent > 80:    
    print("You Got 'A' Grade")
elif percent > 60:
    print("You Got 'B' Grade")
elif percent >= 50:
    print("You Got 'D' Grade")
elif percent < 50:
    print("Your Total Marks is", total_marks)

print("---------------------")
print("Your percentage is", percent)

if percent > 80:
    print("---------------------")
    print("You Got 'A' Grade")
    print("---------------------")
elif percent > 60:
    print("---------------------")
    print("You Got 'B' Grade")
    print("---------------------")
elif percent >= 50:
    print("---------------------")
    print("You Got 'D' Grade")
    print("---------------------")
elif percent < 50:
    print("---------------------")
    print("You Failed")
    print("---------------------")