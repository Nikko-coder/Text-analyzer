'''
author = Nikola Ticha
'''
texts = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

register = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
print("-" * 30)
print("Welcome to the app. Please log in: ")
username = input("USERNAME: ")
password = input("PASSWORD: ")
while register.get(username) != password:
    print("Password or username is wrong")
    username = input("USERNAME: ")
    password = input("PASSWORD: ")

print("-" * 30)
print("We have three texts to be analyzed.")
choice = int(input("Please enter a number: btw. 1 and 3: "))
if choice != [1, 2, 3]:
    print("Entered number out of range. ")
    choice = int(input("Please enter a number btw. 1 and 3: "))
print("-" * 30)

i = choice - 1

print(texts[i])
# delka textu
print("-" * 30)
texts_2 = texts[i].split()
delka = len(texts_2)
print(f"There are {delka} words in the selected text.")

titlc = 0
smol = 0
allup = 0
numbr = 0
# zacina velkym pismenem - titlecase
for word in texts[i].split():
    if word[0].isupper():
       titlc += 1
print(f"There are {titlc} titlecase words.")
count = 0
# zacina malym pismenem
for word in texts[i].split():
    if word.islower():
       smol += 1
print(f"There are {smol} lowercase words.")
count = 0
# pouze velka pismenem
for word in texts[i].split():
    if word.isupper():
       allup += 1
print(f"There are {allup} uppercase words.")
count = 0
# pouze cisla
for word in texts[i].split():
    if word.isnumeric():
       numbr += 1
print(f"There are {numbr} numeric strings. ")
print("-" * 30)
# Frequency
d = {}

for word in texts[i].split():
    word = word.strip(",.-")
    d.setdefault(len(word), 0)
    d[len(word)] += 1

for key, value in sorted(d.items()):
    k = "*" * int(value)
    print(f"{key} {k} {value}")

print("-" * 30)
# suma cisel
sum_digit = 0
for word in texts[i].split():
    if word.isdigit():
       sum_digit += float(word)
print(f"If we would sum up all numbers in this text, we would get {sum_digit:,.1f}.")
