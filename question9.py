# A number is said to be the Harshad number if it is divisible by the sum of its digit. For example,
# if number is 156, then sum of its digit will be 1 + 5 + 6 = 12. 
# Since 156 is divisible by 12. So, 156 is a Harshad number.
'''1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 
36, 40, 42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81, 84, 90,
100, 102, 108, 110, 111, 112, 114, 117, 120, 126, 132, 133,
135, 140, 144, 150, 152, 153, 156, 162, 171, 180, 190, 192,
195, 198, 200, ...'''
j = int(input("enter a number :"))
num = j
sum = 0
while j > 0:
    sum = sum +(j%10)
    j//=10
if num%sum==0:
    print(num,"It is a Harshad Number")
else:
    print(num,"It is not a Harshad Number")