# Python_program
build up my python skills
from game_data import data
from art import logo,vs
import random

score=0
flag=True
flag1=True

while flag1:
  a=random.choice(data)
  b=random.choice(data)
  if a['follower_count']==b['follower_count']:
    b=random.choice(data)
  print(logo)  
  
  print(f"Compare A: {a['name']},{a['description']},from {a['country']}")
  print(vs)
  print(f"Against B: {b['name']},{b['description']},from {b['country']}")
  while flag:
    input_followers=input("Who has more followers? Type 'A' or 'B':").lower()
      
    def find_win(a,b):
      if a['follower_count']>b['follower_count']:
      
        return("a")
      else:
        return("b")
      
    
    result=find_win(a,b)
    
    if input_followers==result:
      
      score+=1
      print(f"Youre right! current score: {score}.")
      
      a=b
      print(f"Compare A: {a['name']},{a['description']},from {a['country']}")
      print(vs)
      b=random.choice(data)
      print(f"Against B: {b['name']},{b['description']},from {b['country']}")
      
    else:
      
      print(f"You lose current score: {score}.")  
      answer=input("Do you want to continue? 'y' or 'n'.")
      flag=False
  if answer=='y'and flag1==True:
      flag=True
      score=0
  else:
      print(f"You'r total score is {score}.")
      flag=False
      flag1=False
