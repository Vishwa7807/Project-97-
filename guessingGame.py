    import random

print("number guessing game")
number=random.randint(1,9)
chances=0

print("guess a number between 1 and 9")

while chances < 5:
  guess=int(input("enter your guess: "))
  if guess==number:
    print("congratulations you win")
    break

  elif guess < number:
    print("guess was too low")
  
  else:
    print("your guess is too high")

  chances+=1
if not chances < 5:
      print("you lose")
