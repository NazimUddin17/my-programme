
from random import randint

for x in range(1,7):
   guessNumber = int(input('enter your guess from 1 to 6: '))
   randomNumber = randint(1,6)

   if guessNumber == randomNumber:
      print('you have won')
   else:
       print('you have lost')
       print('random number was: ',randomNumber)


