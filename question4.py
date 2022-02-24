'''input ka use kar ke 3 alag variables mein 3 integers ka input lein.
Input lene ke baad inn 3 mein se sabse bade number ko print karo'''

num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
if num1>(num2 and num3) :
    print(num1)
elif num2>(num1 and num3):
    print(num2)
else:
    print(num3)