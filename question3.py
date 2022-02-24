'''Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki humara password strong hai.

Pehle user se ek password ka string input lijiye.

Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:

Kam se kam uski length 6 honi chaiye
Jada se jada length 16 se jyada na ho
Kam se kam ek dollar ka sign ($) hona chaiye
Kam se kam password mein 2 ya 8 hona chaiye
Password mein capital A ya capital Z hona chaiye
Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo'''

password = input("enter a password :")
if len(password) >= 6 and len(password)<=16:
    if "$" and( "A" or "Z" ) in password :
        if 2 or 8 in password:
            print("strong password")
        else:
            print("weak password")
    else:
        print("weak password")
else:
    print("weak password")

    