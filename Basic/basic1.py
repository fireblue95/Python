import random
def num():
  num1 = int(input("Input num1:\n"))
  num2 = int(input("Input num2:\n"))
  if(num1 > num2):
    print("num1 must be smaller than num2")
  else:
    end = random.randint(num1, num2)
    while(True):
      print("Guess the number:", num1, "~" , num2)
      guess = int(input())
      if(guess == end):
        print("Bingo!")
        break
      else:
        print("Sorry! try again")
        if(guess > num1 and guess < end):
          num1 = guess
        elif(guess < num2 and guess > end):
          num2 = guess
if __name__ == "__main__":
  num()