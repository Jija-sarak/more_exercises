# s='Welcome to My Site https://nayaksworld.com '              
# print(s.find('come'))              
# print(s.find('o'))
# print(s.find('o', 10, 20))
# print(s.find('o', 5, 10))
# words = "navrukul is great"
# A = []
# c = ""
# counter = 0
# while counter < len(words):
#     if words[counter] == " ":
#         A.append(c)
#         c = "" 
#     else:
#         c = c+ words[counter]
#     counter+=1
# A.append(c)
# print(A)


def break_into_words(sentence):
    A = []
    c = ""
    counter = 0
    while counter < len(sentence):
        if sentence[counter] == " ":
            A.append(c)
            c = "" 
        else:
            c = c+ sentence[counter]
        counter+=1
    A.append(c)
    print(A)
break_into_words( "NavGurukul is an alternative to higher education reducing the barriers of current formal education system")