from random import randint


def get_numbers():
  score = set()

  while len(score) < 6:
    score.add(randint(1, 49))

  return(score)

today_numbers = get_numbers()
our_numbers = set([14, 26, 30, 41, 47, 3])

number_of = 0

while True:
 number_of += 1
 print(number_of)  
 today_numbers = get_numbers()
 good_numbers = today_numbers & our_numbers
 if len(good_numbers) == 4:
   print("You became millioner congratulation its your 300$")
   break

print(f"I spent on this {number_of * 6} - it was expensive")
