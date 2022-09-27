#I honastly dont know what this is for
from sys import exit

score = 0
lives = 3
asn1 = input("Do you want to play a game ")
if asn1 == "no":
  print ("Too Bad you have to play")
elif asn1 == "yes":
  print ("Let's get started")
#This is the start of the questions 
  ans2 =int(input("Question 1: What is the best race to make money fast? \n1. Resort Circuit 2. J.Storm 3. Columbia \n"))
  
  if ans2 == 1:
    print ("Correct")
    score = score + 1
    print(score)
    print(lives)
  else:
    print ("Incorrect")
    print(score)
    lives = lives - 1
    print(lives)
    if lives == 0:
      exit(0)
  asn3 = int(input("Question 2:What company releised Need For Speed Heat \n1. E.A 2. bethesda 3. Valve \n"))
  if asn3 == 1:
    print("Correct")
    score = score + 1
    print(score)
    print(lives)
  else: 
    print ("Incorrect")
    print(score)
    lives = lives - 1
    print(lives)
    if lives == 0:
      exit(0)
  ans4 = (int(input("Question 3:What is the best super car \n 1. koenigsegg regera 2. lamborghini aventador 3. porsche 911 \n")))
  if ans4 == 1:
    print ("Correct")
    score = score + 1
    print(score)
    print(lives)
  else:
    print("Incorrect")
    print(score)
    lives = lives - 1
    print(lives)
    if lives == 0:
      print("How have you got every question wrong I suggest you start again ")
      exit(0)

  ans5 = (int(input("Question 4:When was Need For Speed Heat released /n 1. 2015  2. 2010  3. 2019 \n")))
  if ans5 == 3:
    print ("correct")
    score = score + 1
    print(score)
    print(lives)
  else:
    print("incorrect")
    print(score)
    lives = lives - 1
    print(lives)
    if lives == 0:
    
      print("are you from the 1890's")
      exit(0)
  ans6 = (int(input("Question 5: Do E.A mention charecters from other Need for speed games \n 1. yes 2. no \n"))) 
  if ans6 == 1:
    print("Correct")
    score = score + 1
    print(score)
    print(lives)
  else:
    print("Incorrect")
    print(score)
    lives = lives - 1
    print(lives)
    if lives == 0:
    #When you tr your best but you dont succssed 
      print("you got so close")
      exit(0)
  #yes origin is very morbid and made the game so that you can 
  ans7 = (int(input( "Question 6: Can you hit padestrians whlie they are walking down the street \n 1. yes 2. no \n"))) 
  if ans7 == 1:
    print("Correct")
    score = score + 1
    print(score)
    print(lives)
  else:
    print("Incorrect")
    lives = lives - 1
    if lives == 0:
      print("Get Run over by James on a Vespa ")
      exit(0)

#This is the end of the quiz it will show you your final score and lives 
  print ("Congrats you have completed my Need For Speed heat quiz with the score of")
  print (score)
  print(lives)

