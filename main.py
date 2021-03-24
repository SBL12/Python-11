Str1 = "I like swimming and playing tennis"
str2 = 'swimming'

check = str2 in Str1
if check:
  print(str2 + " is part of" + Str1)
else:
  print(str2 + "is not part of" + Str1)

  #def check(Str1, str2):
    




Main_string = "I like to play Badminton"
Comparing_string = "Badminton"

def check(Main_string,Comparing_string):
  check = Comparing_string in Main_string 
  if check:
    print("Comparing_string is part of Main_string.")
  else:
    print("Comparing_string is not part of Main_string.")
check (Main_string, Comparing_string)

check ("I live in Portland, Oregon", "Portland1")