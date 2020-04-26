#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
    DocString:
    
    A) Introduction:
    This game is an original content inspired by a fantasy puzzle game.
    The setting is somewhat creepy however there is no horror content involved
    
    It consists of 3 stages and the player can win by completing the 3 stages..
    
    (Or maybe..) <-- Easter egg hint
    
    Stage 1: Riddle Game = Guess the right word (inspired by Gollum (LOTR))
    Stage 2: Random Luck Game = Roll dices AND OR flip a coin
    Stage 3: Final Boss Battle = Normal RPG battle game
    

    B) Known Bugs and/or Errors:
    None.
    
    C) Possible improvements:
    1. Add more replayable mini-games
    2. Visual improvements
    3. Fighting game mechanics & balance improvements
    4. Open-world system instead of a just 1-way storyline
    
    
    References:
    http://tolkien.cro.net/talesong/riddles.html
    
Created on Thu Oct 13 12:01:37 2019

@author: ReynerAkira 
"""




from sys import exit
import random
import time
from termcolor import cprint



#basic introduction stage
def start(): 
  global hero_name
  global inventory
  
  cprint("hello", color = 'white', on_color = 'on_red')
  time.sleep(1)
  print("welcome")
  time.sleep(1)
  print("to")
  time.sleep(1)
  print("your")
  time.sleep(1)
  cprint("nightmare!", color = 'white', on_color = 'on_blue')
  time.sleep(1)
  input("<Press enter to continue>\n")
  print("""
  
  ------DO NOT READ THIS IF YOU WANT TO LOSE------
  
  You are now inside a fantasy realm; a labyrinth based on your deepest fear
  You need to navigate through the labyrinth to exit this realm
  This labyrinth requires you to collect 3 pieces of artifact 
  Before going to the final gate to exit this realm
  A Voice will be guiding you the whole time so just follow the flow~
  
  """)
  input("<Press enter to continue>\n")
  
  print("""
--Do you remember your name?--
  
Me: Yes uh, of course I do, it is...
  """)
  
  hero_name = input("<Enter your name>\n").upper()
  
  print(f"""
It is {hero_name}!, Why would I forget that?
  
--The Labyrinth makes you feel weird, it is understandable--
  """)
  time.sleep(2)
  
  inventory = []
  
  stage_1()

#puzzle game intro
def stage_1(): 

  
  print("""
  
For the first game, you are required to guess a number
Are you ready?
1. Yes
2. No
  """)
  
  choice = input("<Input the number of the option to continue>\n").lower()
  
  if "yes" in choice or "1" in choice:
    print("\n--Excellent, let us proceed!--")
    input("<Press enter to continue>\n")
    stage_1a()
  
  else:
      while "1" not in choice or "yes" not in choice:
        print("""
--What are you scared of? are you ready?--
1. Yes 
2. No
        """)
        choice = input("<Input the number of the option to continue>\n").lower()
        
        if "yes" in choice or "1" in choice:
          print("--Excellent, let us proceed!--")
          input("<Press enter to continue>\n")
          stage_1a()

#puzzle game function
def stage_1a():
  
  answer_list = ["mountain","wind", "fish", "teeth", "egg"]
          
  print(f"""
  
--Are you ready, {hero_name}?--
  
--Now you need to guess an object from a clue given--

--Should you be correct, you are going to receive--

  """)
  time.sleep(2)
  cprint("The Mind", color = 'white', on_color = 'on_red')
  input("<Press enter to continue> \n")
  
  print(f"""\n

--You have 3 tries--

--Should you fail to guess, you will be trapped in eternity in this world!--
  
--Here is your question:--
  """)
  
  input("<Press enter to continue>\n")
  
  chances = 3
  
  while chances > 0:
    question = random.choice(answer_list)
    if question == "mountain":
      print("""
What has roots as nobody sees, Is taller than trees, 
Up, up it goes, And yet never grows?
      """)
    
      answer = input("<Guess the riddle with a singular word>\n").lower()
    
      if "mountain" in answer:
        print("'Mountain' is the answer indeed!")
        stage_1b()
        break
      
      else:
        chances = chances -1
        print("Wrong!!, try again!")
        print("<Hint: You can google the riddle>")
        print(f"You have {chances} chances remaining")
    
    elif question == "wind":
      print("""
Voiceless it cries, Wingless flutters,
Toothless bites, Mouthless mutters.
      """)
    
      answer = input("<Guess the riddle with a singular word>\n").lower()
    
      if "wind" in answer:
        print("'Wind' is the answer indeed!")
        stage_1b()
        break
      
      else:
        chances = chances -1
        print("Wrong!!, try again!")
        print("<Hint: You can google the riddle>")
        print(f"You have {chances} chances remaining")
        
    elif question == "fish":
      print("""
Alive without breath, As cold as death;
Never thirsty, ever drinking, All in mail never clinking.
      """)
    
      answer = input("<Guess the riddle with a singular word>\n").lower()
    
      if "fish" in answer:
        print("'Fish' is the answer indeed!")
        stage_1b()
        break
      
      else:
        chances = chances -1
        print("Wrong!!, try again!")
        print("<Hint: You can google the riddle>")
        print(f"You have {chances} chances remaining")
        
    elif question == "teeth":
      print("""
Thirty white horses on a red hill, First they champ,
Then they stamp, Then they stand still.
      """)
    
      answer = input("<Guess the riddle with a singular word>\n").lower()
    
      if "teeth" in answer:
        print("'Teeth' is the answer indeed!")
        stage_1b()
        break
      
      else:
        chances = chances -1
        print("Wrong!!, try again!")
        print("<Hint: You can google the riddle>")
        print(f"You have {chances} chances remaining")

    elif question == "egg":
      print("""
A box without hinges, key, or lid, Yet golden treasure inside is hid.
      """)
    
      answer = input("<Guess the riddle with a singular word>\n").lower()
    
      if "egg" in answer:
        print("'Egg' is the answer indeed!")
        stage_1b()
        break
      
      else:
        chances = chances -1
        print("Wrong!!, try again!")
        print("<Hint: You can google the riddle>")
        print(f"You have {chances} chances remaining")
        
  fail()
   
#transition, gives prize to player for winning first round
def stage_1b(): 
  input("<Press enter to continue>\n")
  
  print("""
--Congratulations!--

Intelligence is certainly a forte of yours

  """)
  cprint("The Mind", color = 'white', on_color = 'on_red')
  
  time.sleep(1)
  
  print("""

Shall be in yours!
Keep it safe in your inventory until it is needed
  """)
  
  inventory.append("The Mind")
  
  input("<Press enter to continue> \n")
  
  print(f"""
------------------------------------------------
{hero_name}\'s inventory now consists of: {inventory}
------------------------------------------------
""")
  
  time.sleep(1)
  
  print(f"""
*The world seems fuzzy and {hero_name} blacked out for a second*
  """)
  input("<Press enter to continue>\n")
  
  stage_2()

# dice and coin game, mostly automatic  
def stage_2(): 
  print(f"""
------------------------------------------------
{hero_name} is now in front of a maze entrance.
To {hero_name}'s right, lies an obelisk with letters engraved
  """)
  input("<Press enter to continue> \n")
  print(f"""
  
   There are 3 paths to move on to the next stage:
   1. Long Road
   2. Normal Road
   3. Instant Road

   The criteria is as follows:
  
   Long Road = Accumulated number from rolling 3 dices    : 1-9
   Normal Road = Accumulated number from rolling 3 dices  : 10-14
   Instant Road = Accumulated number from rolling 3 dices : 15-18
  
   Now roll 3 dices!

**{hero_name} rolls 3 dices; one-by-one **

  """)
  
  input("<Press enter to continue>\n")
  
  dice_1 = random.randint(1,7) 
  print(f"You rolled a {dice_1} on your first dice")
  time.sleep(1)
  dice_2 = random.randint(1,7) 
  print(f"You rolled a {dice_2} on your second dice")
  time.sleep(1)
  dice_3 = random.randint(1,7) 
  print(f"You rolled a {dice_3} on your third dice")
  
  input("<Press enter to continue> \n")

  
  total = dice_1 + dice_2 + dice_3
  
  print(f"""
--Congratulations, you accumulated number from rolling 3 dices is {total}-- \n """)
  
  if total <= 9:
    print("""
--Now you have to be lucky to proceed to the actual game--
--If you fail, it's game over~ --
--Well then...--
    """)
    time.sleep(1)
    print("""
--Flip a coin--
--To win you need 'Head'--
""")
    input("<Press enter to continue> \n")
    
    coin = [0,1] # 0 is heads, 1 is tails
    
    flip = random.choice(coin)
    
    print(f"{hero_name} flips a coin")
    time.sleep(2)
    
    if flip == 0:
      print("--Congratulations you got heads!, let's go to the real game--")
      stage_2a()
    
    else:
      print("""
--You flipped tails!--
--You are not lucky enough--
--HAHAHAHA--
      """)
      fail() #goes to fail function
  
  elif total >= 15:
    print("--You are so lucky! Lucky enough to win immediately--")
    inventory.append("The Luck")
    print(f"""
------------------------------------------------
{hero_name}'s inventory is now: {inventory}
------------------------------------------------
    """)
    input("<Press enter to continue>\n")
    win() #automatic win if player's roll value >= 15
  else:
    print("--You are lucky enough to move to the real game--")
    stage_2a()
  
def stage_2a(): #gives prize and transitions to next stage
  input("<Press enter to continue\n")
  print("""

This is a simple game, you just need to enter a number that ranges from 0 to 9
  
That number has to be bigger than the number that is randomly generated 
Should you win once , you will obtain 
  """)
  time.sleep(2)
  cprint("The Luck", color = 'white', on_color = 'on_red')
  print("""
  
Oh.. wait...

  """)
  input("<Press enter to continue>\n")
  print("""

Actually, you already proof you are lucky enough!

The artifact is yours!

Keep it safe until it is needed

  """)
  
  inventory.append("The Luck")
  time.sleep(2)
  
  print(f"""
{hero_name}\'s inventory now consists of: {inventory}
  
Now move along, into the maze to enter the final stage of the game!
  
--{hero_name} enters the maze--
  """)
  input("<Press enter to continue> \n")
  stage_3()
  
def stage_3(): # standard RPG style fighting game
  hero_health = 20
  boss_health = 50
  boss_mana = 0
  
  
  boss_moves = ["roll", "roll", "channel", "spell"]
  
  print(f"""
------------------------------------------------

After going around in the maze for a while,
{hero_name} sees a shadow, just standing there guarding the exit

  """)
  time.sleep(1)
  
  boss_name = input("<Input the name of an object you hate> \n").upper()
  
  print(f"""
**The Shadow morphs into {boss_name}, the thing {hero_name} hates the most**
  """)
  input("<Press enter to continue> \n")
  print(f"""
**The last thing that {hero_name} needs to do is defeat that shadow** 
""")
  
  time.sleep(1)
  print(f"""
  
--------Rules of The Fight--------

{hero_name} can damage the boss by attacking directly with the artifacts given.
The Mind allows {hero_name} to damage {boss_name} with mind attacks
The Luck allows {hero_name} to dodge damages done by {boss_name}
  
  """)
  time.sleep(4)
  print(f"""
  
{boss_name} will attack by rolling a 6-sided dice, dealing pure damage
{boss_name} can also do "Channel" to gather his mana...
Then uses "Spell" to deal 1/2 of {hero_name}'s current health

  """)
  input("<Press enter to continue> \n")
  print(f"""
Ready yourself, {hero_name}
  """)
  input("<Press enter to continue> \n")
  
  while boss_health > 0:
    if hero_health > 0:
      
      print("""
------------------------------------------------
What should {hero_name} do?
1. Fight
2. Dodge
      """)
      action = input("<Input the option's number to continue> \n").lower()
      print("------------------------------------------------")
      
      if "1" in action or "fight" in action:
        damage = random.randint(10,14) #damage between 10-14
        boss_health = boss_health - damage
        print(f"""
{hero_name} dealt {damage} to {boss_name}
{boss_name} has {boss_health} HP remaining
        """)
        
        boss_action = random.choice(boss_moves)
        
        if "roll" in boss_action:
          boss_damage = random.randint(1,6) # 6 sided dice
          hero_health = hero_health - boss_damage
          print(f"""
{boss_name} rolls a {boss_damage} with the dice
          """)
          print(f"""
{hero_name} took {boss_damage} damage
{hero_name} has {hero_health} HP remaining
          """)
          
        elif "channel" in boss_action:
          print(f"""
{boss_name} gathers some mana
          """)
          boss_mana = boss_mana + 1
          
        elif "spell" in boss_action:
          
          print(f"""
{boss_name} casts a spell
          """)
          
          if boss_mana > 0:
            hero_health = hero_health / 2
            print(f"""
{hero_name}'s remaining HP is now {hero_health}
            """)
            boss_mana = boss_mana - 1
          else:
            print("the spell failed due to lack of mana")
        
      elif "2" in action or "dodge" in action:
        boss_action = random.choice(boss_moves)
        print(f"""
{hero_name} is going to dodge the next attack!
        """)
        if "roll" in boss_action:
          boss_damage = random.randint(1,6) # 6 sided dice
          print(f"""
{boss_name} rolls a {boss_damage} with the dice
          """)
          print(f"""
{hero_name} dodges the attack
{hero_name} has {hero_health} HP remaining
          """)
          
        elif "channel" in boss_action:
          print(f"""
{boss_name} gathers some mana
          """)
          boss_mana = boss_mana + 1
          
        elif "spell" in boss_action:
          
          print(f"""
{boss_name} casts a spell
          """)
          
          if boss_mana > 0:
            print(f"""
{hero_name} dodges the spell
            """)
            print(f"""
{hero_name}'s remaining HP is now {hero_health}
            """)
            boss_mana = boss_mana - 1
          else:
            print("the spell failed due to lack of mana")
      
      else:
          input("<Invalid command, press enter to continue> \n")
          
    else:
      print(f"You got killed by {boss_name}")
      fail()

  else:
    print("You beat the boss!")
    win()
    
#end game sequence    
def win():
  print(f"""
---Congratulations, {hero_name}---

                  __    __ _        
/\_/\___  _   _  / / /\ \ (_)_ __   
\_ _/ _ \| | | | \ \/  \/ | | '_ \  
 / | (_) | |_| |  \  /\  /| | | | | 
 \_/\___/ \__,_|   \/  \/ |_|_| |_| 
                                    
  
---{hero_name} obtained the last artifact---
  """)
  time.sleep(1)
  cprint("The Courage", color = 'white', on_color = 'on_red')
  inventory.append("The Courage")
  print(f"""
------------------------------------------------
{hero_name}'s inventory is now: {inventory}
------------------------------------------------
  """)
  input("<Press enter to continue>\n")
  print(f"""
--You may return to your world now, {hero_name}--
  
Would you wish to finish the game?
1. Yes
2. No
  """)
  choice = input("<Input the number of the option you wish to go with> \n").lower()
  
  if "1" in choice or "yes" in choice or "y" in choice:
    print("Thank you for playing!")
    exit(0)
  elif "2" in choice or "no" in choice or "n" in choice:
    print("""
--Do you wish to play again?--
1. Yes
2. No
    """)
    
    play = input("<Input the number of the option you wish to go with> \n").lower()
    
    if "1" in play or "yes" in play or "y" in play:
      print("--OK, I'll take your artifacts and you have to start again--")
      input("<Press enter to continue> \n")
      start()
    else:
      print("Thank you for playing!")
      print("This game will auto-quit in 3 seconds")
      time.sleep(3)
      exit(0)
      
  else:   
    print("<Invalid command, try again>")
    win()
  
#basic fail function, allows players to restart from the beginning without exiting the app too  
def fail():
  cprint("You failed, enjoy your stay!", color = 'blue', on_color = 'on_white')
  print("""
Restart Game?
1. Yes
2. No
  """)
  restart = input("<Input the number of the option you wish to go with> \n").lower()
  
  if "1" in restart or "yes" in restart:
    print("So be it \n")
    start()
  
  elif "2" in restart or "no" in restart:
    print("SEE")
    time.sleep(1)
    print("YOU")
    time.sleep(1)
    print("SOON")
    exit(0)
  
  else:
    print("<Invalid input, try again>")
    fail()
  
start()

