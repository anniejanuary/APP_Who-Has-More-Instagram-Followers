from art import logo
from art import vs
from replit import clear
import random
from game_data import data

# Creates "list_of_dicts" with indices of dicts from game_data.py to remove used Insta profiles from the pool
number_of_dicts = len(data)
def numbered_dictionaries_list (n1, n2):
    return list(range(n1, n2+1))
list_of_dicts = numbered_dictionaries_list(0,49)

score = 0

def random_pick(data):
  '''- Picks a random Instagram profile from game_data.py and removes it from future selection
     - Returns 4 outputs accessible as tupple indices, eg. A = random_pick(data) | A_followers = A[3]'''
  random_dict_index = random.choice(list_of_dicts)
  list_of_dicts.remove(random_dict_index)
  name = data[random_dict_index]['name']
  description = data[random_dict_index]['description']
  country = data[random_dict_index]['country']
  follower_count = int(data[random_dict_index]['follower_count'])
  return name, description, country, follower_count # function 


def display_A_and_B (A, B):
  '''Takes follower numbers from random_pick() functions and asks to compare A vs B'''
  A_followers = A[3]
  B_followers = B[3]

  global score
  
  print(f"A: {A[0]}, a {A[1]} from {A[2]}")
  print(vs)
  print(f"B: {B[0]}, a {B[1]} from {B[2]}")

  compare(A_followers, B_followers, A, B)  


def pick_new_B_and_compare_again (A, B):
  '''Picks a new random B profile, clears the screen, prints logo, adds +1 and displays score'''
  global score
  B = random_pick(data)
  clear()
  print(logo)
  score += 1
  print(f"You're correct! Current score: {score}")
  display_A_and_B (A, B)


def compare (A_followers, B_followers, A, B):
  '''Compares number of followers based on user's choice'''
  global game_on

  if len(list_of_dicts) == 0:
    print("You've correctly compared all 50 Instagram profiles in my database. You beast, have a damn good day!")
    game_on = False
  
  while game_on and len(list_of_dicts) != 0:
    global score
    user_choice = input("Who has more Instagram followers? Type 'A' or 'B': ").upper() # converting eg. 'a' to 'A'
    if (user_choice == 'A' and A_followers < B_followers) or (user_choice == 'B' and A_followers > B_followers):
      print(f"Sorry, that's incorrect. Final score: {score}")

      # play again?
      if input("Would you like to play again? 'y' or 'n': ") == 'y':
        score = 0
        new_game()
      else:
        # end of game
        game_on = False
        
      
    elif (user_choice == 'A' and A_followers > B_followers):
      
      # loop with same A and new randomized B
      pick_new_B_and_compare_again (A, B)
      
    elif (user_choice == 'B' and A_followers < B_followers):  
          
      # B becomes A
      # clearing A tuple
      temp_tuple_to_list = list(A)
      temp_tuple_to_list.clear()
      # appending B tupple elements to A list
      temp_tuple_to_list.append(B[0])
      temp_tuple_to_list.append(B[1])
      temp_tuple_to_list.append(B[2])
      temp_tuple_to_list.append(B[3])
      # turning A list back into a tupple
      A = tuple(temp_tuple_to_list)
  
      # loop with A (old B) and a new randomized B
      pick_new_B_and_compare_again (A, B)

    else: 
      print("Enter 'A' or 'B', try again")
      compare (A_followers, B_followers, A, B)
    

def new_game():
  '''Starts a new game'''
  clear()
  global score
  A = random_pick(data)
  B = random_pick(data)
  print(logo)
  display_A_and_B (A, B)
  A_followers = A[3]
  B_followers = B[3]
  compare(A_followers, B_followers, A, B)

game_on = True

while game_on:
  new_game()



  
