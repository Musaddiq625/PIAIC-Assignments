import  decimal
print("** MARKSHEET **")
s_name= input("Enter Student Name: ")
s1_eng= int(input("Enter English Marks: "))
s2_math= int(input("Enter Mathematics Marks: "))
s3_phy= int(input("Enter Physics Marks: "))
s4_islam= int(input("Enter Islamiat Marks: "))
s5_urdu= int(input("Enter Urdu Marks: "))
s6_chem= int(input("Enter Chemistry Marks: "))

s_totalMarks= s1_eng+ s2_math+ s3_phy+ s4_islam+ s5_urdu+ s6_chem
s_per= s_totalMarks/6
if (s_per>= 90 and s_per<=100):
    grade= 'A'
    congo= "Excellent!"
elif (s_per>= 80 and s_per<=90):
    grade= 'B'
    congo= "Congratulations!"
elif (s_per>= 70 and s_per<=80):
    grade= 'C'
    congo= "Well Done!"
elif (s_per>= 60 and s_per<=70):
    grade= 'D'
    congo= "You Can Do Better!"
elif (s_per>= 50 and s_per<=60):
    grade= 'E'
    congo= "Not a Good Result! :("
elif (s_per>= 0 and s_per< 50 ):
    grade= 'F'
    congo= "Focus On Your Studies"
else:
    grade='N/A'
    congo= ""

print("╔════════════════════════════════════════════════════════════╗")
print("╠════════════════════════ MARKSHEET ═════════════════════════╣")
print("║════════════════════════════════════════════════════════════║")
print("║    Student Name:       {:>20} {:>16}".format(s_name, '║'))
print("╟------------------------------------------------------------╢")
print("║    English Marks:      {:>20} {:>16}".format(s1_eng, '║'))
print("║    Mathematics Marks:  {:>20} {:>16}".format(s2_math, '║'))
print("║    Physics Marks:      {:>20} {:>16}".format(s3_phy, '║'))
print("║    Islamiat Marks:     {:>20} {:>16}".format(s4_islam, '║'))
print("║    Urdu Marks:         {:>20} {:>16}".format(s5_urdu, '║'))
print("║    Chemistry Marks:    {:>20} {:>16}".format(s6_chem, '║'))
print("╟------------------------------------------------------------╢")
print("║    Total Marks:        {:>20}/600 {:>12}".format(s_totalMarks, '║'))
print("║    Percentage:         {:>20.2f}% {:>15}".format((round(decimal.Decimal(s_per), 2)), '║'))
print("║    Grade:              {:>20} {:>16}".format(grade, '║'))
print("╚════════════════════════════════════════════════════════════╝")
print(congo)
