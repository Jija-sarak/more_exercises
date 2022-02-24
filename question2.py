'''Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul 
ka ek mahine ka kharcha nikalenge

input ka use kar ke do values ka input lo:

Number of students

Ek student ka kharcha

Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya usse kam hai
toh print karein "Hum budget ke andar hain" nahi toh print karo ki hum budget ke bahar hain.'''

students_count = int(input("enter number of students:"))
cost_of_a_student = int(input("enter a amount:"))
if students_count > 1:
    cost_of_all_student = students_count*cost_of_a_student
    if cost_of_all_student <= 50000:
        print("we are in the budget",cost_of_all_student)
    else:
        print("we are out of budget", cost_of_all_student)