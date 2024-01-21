# imports necessary libraries & creates global variables
import os
import time
from timeit import default_timer as timer

vertical_position = 0
horizontal_position = 0
velocity = 1
h3_event = False
in_h3_event = False
computer_event = False
current_room = 0
door1 = ""
door2 = ""
door3 = ""
door4 = ""
hallway_description = ""
inventory = []
has_ladder = False
sneak = False
test_run = False
plant_watered = False

# for this code, I created a class to contain the attributes all rooms share, so that I could easily define shared attributes for all of them
class Room:
  def __init__(self, name, description, horizontal, vertical, doors):
    self.name = name
    self.description = description
    self.horizontal = horizontal
    self.vertical = vertical
    self.doors = doors
parking_garage1 = Room("first room in the parking garage", "You see a well lit, concrete room. There are no cars parked, and you suspect that everyone must have gone home for the night. All seems normal, but the strange feeling in your gut won't go away", 5, 6, [])
parking_garage2 = Room("second room in the parking garage", "This room appears very similar to the first room in the parking garage, except for the elevator in the northwest corner", 8, 8, [])
h1 = Room("first hallway", "It's a plain tiled hallway, at the end of which is a potted plant on it's last legs. It's clearly been neglected, which is strange considering the pristine state of everything else", 14, 1, [])
h2 = Room("second hallway", "You see a normal tiled hallway", 1, 3, [])
h3 = Room("third hallway", "You see a normal tiled hallway", 11, 1, [])
h4 = Room("fourth hallway", "You see a normal tiled hallway", 1, 5, [])
h5 = Room("fifth hallway", "You see a normal tiled hallway", 9, 1, [])
h6 = Room("sixth hallway", "You see a normal tiled hallway", 1, 5, [])
h7 = Room("seventh hallway", "You see a normal tiled hallway", 7, 1, [])
office1 = Room("first office", "The room looks like a normal office. Desk, file cabinets, chair. But there's a strange red-brown smear on the wall. If you didn't know better, you'd say it was blood", 3, 2, [])
office2 = Room("second office", "This one is a regular office, decked out with a chair, desk, and file cabinets. A piece of paper is stuck under computer, almost completely hidden.", 3, 2, [])
office3 = Room("third office", "The computer on the desk is on, and appears to be showing some sort of security footage. In it, a strange monster paces around, one that seems all too familiar...until you recognize it, and want to scream. You thought you were done with the hallucinations, and now, at the worst possible they're back. 'I don't have time for this', you mutter", 3, 2, [])
office4 = Room("fourth office", "This office resembles a normal one, with a desk, chair, and computer. On the computer is an email", 3, 4, [])
office5 = Room("fifth office", "It seems just a normal office", 4, 2, [])
computer_lab = Room("computer lab", "The computer lab consists of a long table in the middle of the room, with desktops set up along it and wheeled chairs", 4, 3, [])
employee_lounge = Room("employee lounge", "The employee lounge has a vending machine, and a coffeepot and mug lies off to one side, forgotten on a counter. A couple of couches provide places to sit, and there is a water cooler off to the side", 3, 4, [])
cafeteria = Room("cafeteria", "The cafeteria is a standard one, with tables for seating and a cafe off to one side.", 4, 5, [])
conference1 = Room("first conference room", "The room is set up like a normal conference room, with one long table and a tv screen on the north wall", 2, 4 , [])
conference2 = Room("second conference room", "The room is set up like a normal conference room, with one long table and a tv screen on the north wall", 3, 4, [])
maintenance = Room("maintenance hallway", "The maintenance hallway is lit by flickering fluorescent bulbs. A vent runs along the length of the hallway, and at 101, you can see a grate lying on the ground where there is an entrance into it", 12, 1, [])
supply1 = Room("first supply room", "The first supply closet has a couple of mops and brooms, and a ladder leaning up against the wall", 1, 2, [])
supply2 = Room("second supply room", "The second supply closet resembles the first, but with cleaning solutions on shelves instead of brooms and mops", 1, 2, [])

# creates door class to store all doors
class Door:
  def __init__(self, room1,coordinates1,room2,coordinates2):
    self.room1 = room1
    self.coordinates1 = coordinates1
    self.room2 = room2
    self.coordinates2 = coordinates2
pgjoin1 = Door(parking_garage1,11,parking_garage2,81)
pgjoin2 = Door(parking_garage2,81,parking_garage1,11)
pghall1 = Door(parking_garage2,14,h1,141)
pghall2 = Door(h1,141,parking_garage2,14)
complabhall11 = Door(h1,31,computer_lab,31)
complabhall12 = Door(computer_lab,31,h1,31)
complabhall31 = Door(h3,31,computer_lab,33)
complabhall32 = Door(computer_lab,33,h3,31)
off1hall1 = Door(h3,71,office1,22)
off1hall2 = Door(office1,22,h3,71)
off2hall1 = Door(h3,101,office2,22)
off2hall2 = Door(office2,22,h3,101)
cafehall1 = Door(h4,13,cafeteria,43)
cafehall2 = Door(cafeteria,43,h4,13)
confer1hall1 = Door(h5,21,conference1,24)
confer1hall2 = Door(conference1,24,h5,21)
confer2hall1 = Door(h5,41,conference2,24)
confer2hall2 = Door(conference2,24,h5,41)
off4hall1 = Door(h5,71,office4,24)
off4hall2 = Door(office4,24,h5,71)
closet1hall1 = Door(h6,13,supply1,12)
closet1hall2 = Door(supply1,12,h6,13)
closetjoin1 = Door(supply1,11,supply2,12)
closetjoin2 = Door(supply2,12,supply1,11)
closet2main1 = Door(supply2,11,maintenance,41)
closet2main2 = Door(maintenance,41,supply2,11)
off3hall1 = Door(h7,21,office3,21)
off3hall2 = Door(office3,21,h7,21)
off5hall1 = Door(h7,51,office5,21)
off5hall2 = Door(office5,21,h7,51)
employeehall1 = Door(h3,111,employee_lounge,13)
employeehall2 = Door(employee_lounge,13,h3,111)

# adds doors to rooms
parking_garage1.doors = [pgjoin1]
parking_garage2.doors = [pgjoin2,pghall1]
h1.doors = [pghall2,complabhall11]
h3.doors = [complabhall31,off1hall1,off2hall1,employeehall1]
h4.doors = [cafehall1]
h5.doors = [confer1hall1,confer2hall1 ,off4hall1]
h6.doors = [closet1hall1]
h7.doors = [off3hall1,off5hall1]
office1.doors = [off1hall2]
office2.doors = [off2hall2]
office3.doors = [off3hall2]
office4.doors = [off4hall2]
office5.doors = [off5hall2]
supply1.doors = [closet1hall2,closetjoin1]
supply2.doors = [closetjoin2,closet2main1]
conference1.doors = [confer1hall2]
conference2.doors = [confer2hall2]
computer_lab.doors = [complabhall12,complabhall32]
employee_lounge.doors = [employeehall2]
maintenance.doors = [closet2main2]
cafeteria.doors = [cafehall2]

# functions
def print_center(string):
  x = (int(os.get_terminal_size().columns))
  print(string.center(x,))
def credits():
  print_center("Thank you for playing \033[31mParallels: Part 1\033[0m! We hope you enjoyed it!\n")
  time.sleep(1)
  print_center("Head Developer: \033[36mEmTheCoder49\033[0m\n")
  time.sleep(2)
  print_center("Concept Developers:")
  time.sleep(1)
  print_center("\033[31mMarZ")
  time.sleep(1)
  print_center("\033[32mSerena the Turtle")
  time.sleep(1)
  print_center("\033[35mScott")
  time.sleep(1)
  print_center("\033[33mThe girlyboss\n")
  time.sleep(2)
  print_center("\033[0mPlaytesters:")
  time.sleep(1)
  print_center("\033[30mSavage Chansin")
  time.sleep(1)
  print_center("\033[34mPercy Jackson")
  time.sleep(1)
  print_center("\033[31mMarZ")
  time.sleep(1)
  print_center("\033[35mScott")
  time.sleep(1)
  print_center("\033[33mThe girlyboss")
  time.sleep(1)
  print_center("\033[0mCalamityWaffles\n")
  time.sleep(1)
  print_center("\033[34mEd05\n")
  time.sleep(2)
  print_center("\033[0mCover Artist:\033[30m Savage Chansin\n\n\n\n")
def restart():
  vertical_position = 0
  horizontal_position = 0
  velocity = 1
  h3_event = False
  computer_event = False
  current_room = 0
  door1 = ""
  door2 = ""
  door3 = ""
  door4 = ""
  hallway_description = ""
  has_ladder = False
  sneak = False
  os.system("clear")
  continu = input("Restart? (y/n)\n")
  if continu == "y":
    sneak = False
  else:
    exit()
def map(c_room, v_pos, h_pos):
  # creates 2D array in the right shape with " " in all spaces
  room_map = []
  for i in range(c_room.vertical):
    i = []
    for j in range(c_room.horizontal):
      i.append(" ")
    room_map.append(i)
    
  # adds doors
  for d in c_room.doors:
    h = int(d.coordinates1 / 10)
    v = d.coordinates1 % 10
    room_map[v-1][h-1] = "D"
    
  # adds hallway joiners
  if c_room == h1:
    room_map[0][4] = "H"
  elif c_room == h2:
    room_map[0][0] = "H"
    room_map[2][0] = "H"
  elif c_room == h3:
    room_map[0][4] = "H"
  elif c_room == h4:
    room_map[0][0] = "H"
    room_map[4][0] = "H"
  elif c_room == h5:
    room_map[0][0] = "H"
    room_map[0][8] = "H"
  elif c_room == h6:
    room_map[0][0] = "H"
    room_map[4][0] = "H"
  elif c_room == h7:
    room_map[0][0] = "H"
    
  # adds player position
  room_map[v_pos-1][h_pos-1] = "P"
  
  # prints result
  border = ""
  for k in range(c_room.horizontal + 2):
    border = border + "*"
  print_center(border)
  for i in room_map:
    map_string = ""
    for u in i:
      map_string = map_string + u
    print_center("*" + map_string + "*")
  print_center(border)
  print_center("\nH = hallway joiner, D = door, P = player\n")

# trigger warning
continu = input("Warning: This game is a horror game. It includes non-graphic depictions of violence, guns, and monsters, as well as themes revolving around mental illness. If you are triggered by these subjects, please do not play this game. Continue? (y/n)\n\n")

# literally entire game part 1
if continu == "y":
  # initial instructions
  os.system("clear")
  continu = input("Before you begin, please note the controls. This is a text based game. If you would like your character to do something, type it in. \n\nBasic controls include walk, which sets movement speed at one square per movement, run, which sets it at two. Sneak allows you to move at the same rate as walk, but makes you harder to see. To move around in the environment, type move, then the direction you would like to move. \n\nAdditionally, at the start of each action, the computer will tell you which doors are in the the room, and will give you the coordinates of each room. In these coordinates, the first number is the horizontal, second vertical. If the number is three digits, the first two are horizontal. Same goes for hallway joiners. \n\nSome events are timed, and you have a limited amount of time to act. Bcause this is a survival horror game, your character is extremely weak, and attacking is ill advised. If you wish to see this message again at any point in the main game loop (once you are inside the building) type 'help'. Good luck! ")
  if continu == "test":
    os.system('clear')
    player_name = "Evelyn"
    player_gender = "girl"
    player_hair = "black"
    significant_name = "Jaclyn"
    significant_gender = "girl"
    significant_hair = "white"
    significant_status = "significant other"
    test_run = True
  else:
    while True:
      os.system("clear")
      # customizes player
      player_name = input("What would you like your character name to be?: ")
      player_gender = input("What would you like your character gender to be? 1: Male, 2: Female, 3: Non-binary: ")
      if player_gender == "1":
        player_gender = "boy"
      elif player_gender == "2":
        player_gender = "girl"
      else:
        player_gender = "teenager"
      player_hair = input("What would you like your character hair color to be?: ").lower()
      # customizes significant person
      os.system("clear")
      continu = input("Now, we will create a significant person for you that will be important to your story later.")
      significant_status = input("Would you like this person to be 1: your best friend or 2: a person you are dating?: ")
      if significant_status == "2":
        significant_status = "significant other"
      else:
        significant_status = "best friend"
      significant_name = input("What would you like to name this person?: ")
      significant_gender = input("What would you like " + significant_name + "'s this person's gender to be? 1: Male, 2: Female, 3: Non-binary: ")
      if significant_gender == "1":
        significant_gender = "boy"
      elif significant_gender == "2":
        significant_gender = "girl"
      else:
        significant_gender = "teenager"
      significant_hair = input("What would you like their hair color to be?: ").lower()
      os.system("clear")
      continu = input("Initializing game with " + player_name + ", a " + player_gender + " with " + player_hair + " hair, and " + significant_name + ", their " + significant_status + " who is a " + significant_gender + " with " + significant_hair + " hair. Confirm? (y/n) \n\n" )
      os.system("clear")
      if continu == "y":
        break
  print("Confirmed. Initializing.")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)

  # opening sequence outside
  if test_run == True:
    current_room = h4
    horizontal_position = 1
    vertical_position = 1
  else:
    while True:
      os.system("clear")
      print("You find yourself in the middle of the woods, outside of a concrete building. Although all the windows are well lit in the darkness of the night, you see no movement within it's walls. You have no idea how you got here, or how to go back, but are wary of going inside. \n")
      time.sleep(3)
      continu = input("Suddenly, you see a flash of movement in one of the upper windows. A face, " + significant_hair + "-haired and terrified, stares out at you. But then, it vanishes. \n\n'" + significant_name + "?' you ask, heart hammering in your chest. They had disappeared weeks ago, and you'd given up any hope of finding your " + significant_status + " again. Suddenly desperate to enter the building, you scan the layout, and see two potential entrances. In the front of the building, a door that is likely the main entrance, and further back to your right, a loading dock. Where would you like to go?\n\n1: Main Entrance\n2: Loading Dock\n3: Run away\n\n")
      while continu != "2":
        if continu == "1":
          os.system("clear")
          continu = input("You walk up to the door, and try to open it. However, the door is locked. 2 or 3?")
        elif continu == "3":
          os.system("clear")
          continu = input("Terrified, you turn around, and blindly flail your way through the forest, until you seem light peeking through the trees. Relieved, you run out of the forest, only to realize your mistake. The honk of a car horn is the last thing you hear before you collapse to the ground.")
          restart()
          break
        else:
          continu = input("Please pick one of the 3 options available. 1, 2, or 3?\n\n")
      if continu == "2":
        os.system("clear")
        continu = input("You make your way to the loading dock, but upon arrival, you find yourself unable to open the large door blocking it. However, there is a small parking garage to the right of it, which's only impediment to opening is a bar meant to keep cars out without proper authorization. You duck inside, and are now in the parking garage.")
        current_room = parking_garage1
        horizontal_position = 5
        vertical_position = 4
        break
  
  # open world
  while True:
    os.system("clear")
    # set up for doors
    if len(current_room.doors) == 1:
      door1 = "There is one door at " + str(current_room.doors[0].coordinates1) + " that leads to the " + str(current_room.doors[0].room2.name + ".")
      door2 = ""
      door3 = ""
      door4 = ""
    elif len(current_room.doors) == 2:
      door1 = "There is one door at " + str(current_room.doors[0].coordinates1) + " that leads to the " + str(current_room.doors[0].room2.name + ".")
      door2 =  "Another one is at " + str(current_room.doors[1].coordinates1) + " that leads to the " + str(current_room.doors[1].room2.name + ".")
      door3 = ""
      door4 = ""
    elif len(current_room.doors) == 3:
      door1 =  "There is one door at " + str(current_room.doors[0].coordinates1) + " that leads to the " + str(current_room.doors[0].room2.name + ".")
      door2 =  "Another one is at " + str(current_room.doors[1].coordinates1) + " that leads to the " + str(current_room.doors[1].room2.name + ".")
      door3 =  "Another one is at " + str(current_room.doors[2].coordinates1) + " that leads to the " + str(current_room.doors[2].room2.name + ".")
      door4 = ""
    elif len(current_room.doors) == 4:
      door1 =  "There is one door at" + str(current_room.doors[0].coordinates1) + " that leads to the " + str(current_room.doors[0].room2.name + ".")
      door2 =  "Another one is at " + str(current_room.doors[1].coordinates1) + " that leads to the " + str(current_room.doors[1].room2.name + ".")
      door3 =  "Another one is at " + str(current_room.doors[2].coordinates1) + " that leads to the " + str(current_room.doors[2].room2.name + ".")
      door4 =  "Another one is at " + str(current_room.doors[3].coordinates1) + " that leads to the " + str(current_room.doors[3].room2.name + ".")
    else:
      door1 = ""
      door2 = ""
      door3 = ""
      door4 = ""

    # set up for hallways
    if current_room.name == "first hallway":
      hallway_description = "There is a hallway joiner at coordinates 51."
    elif current_room.name == "second hallway":
      hallway_description = "There is a hallway joiner at coordinates 11 and 13."
    elif current_room.name == "third hallway":
      hallway_description = "There is a hallway joiner at coordinates 51."
    elif current_room.name == "fourth hallway":
      hallway_description = "There is a hallway joiner at coordinates 11 and 15."
    elif current_room.name == "fifth hallway":
      hallway_description = "There is a hallway joiner at coordinates 11 and 91."
    elif current_room.name == "sixth hallway":
      hallway_description = "There is a hallway joiner at coordinates 11 and 15."
    elif current_room.name == "seventh hallway":
      hallway_description = "There is a hallway joiner at coordinates 11."
    else:
      hallway_description = ""

    # map
    map(current_room, vertical_position, horizontal_position)
    
    # description
    # computer lab is special
    if h3_event == False and current_room.name == "computer lab" and computer_event == False:
      continu = input("You are in the computer lab. In the center is a table filled with desktops, on which someone types out code, lines scrolling across the computers. They are deeply ingrained in their work, and have not noticed you...yet...\n\nWhat would you like to do?\n\n")
    else:
      continu = input("You are in the " + current_room.name + ". " + current_room.description + ". The horizontal limit to the room is " + str(current_room.horizontal) + ". The vertical limit is " + str(current_room.vertical) + ". Your current horizontal position is " + str(horizontal_position) + " and your vertical position is " + str(vertical_position) + ". " + door1 + " " + door2 + " " + door3 + " " + door4 + " " + hallway_description + "\n\nWhat would you like to do?\n\n")

    # moving options
    if continu.lower() == "move left":
      if horizontal_position - velocity < 1:
        continu = input("You cannot move left. There is a wall there. idiot")
      else:
        horizontal_position = horizontal_position - velocity
    elif continu.lower() == "move right":
      if horizontal_position + velocity > current_room.horizontal:
        continu = input("You cannot move right. There is a wall there. idiot")
       
      else:
        horizontal_position = horizontal_position + velocity
    elif continu.lower() == "move down":
      if vertical_position + velocity > current_room.vertical:
        continu = input("You cannot move down. There is a wall there. idiot")
      else:
        vertical_position = vertical_position + velocity
    elif continu.lower() == "move up":
      if vertical_position - velocity < 1:
        continu = input("You cannot move up. There is a wall there. idiot")
      else:
        vertical_position = vertical_position - velocity
    elif continu.lower() == "run":
      velocity = 2
      sneak = False
    elif continu.lower() == "walk":
      velocity = 1
      sneak = False
    elif continu.lower() == "help":
      continu = input("This is a text based game. If you would like your character to do something, type it in. Basic controls include walk, which sets movement speed at one square per movement, run, which sets it at two. Sneak allows you to move at the same rate as walk, but makes you harder to see. To move around in the environment, use move north to decrease vertical position, move south to increase vertical position, move west to decrease horizontal position, and move east to increase horizontal position. Keep in mind that direction will not change when you change direction you move, as I am lazy and do not want to code that. Additionally, at the start of each action, the computer will tell you which doors are in the the room, and will give you the coordinates of each room. In these coordinates, the first number is the horizontal, second vertical. If the number is three digits, the first two are horizontal. Same goes for hallway joiners. Some events are timed, and you have a limited amount of time to act. Additionally, because this is a survival horror game, your character is extremely weak, and attacking is ill advised. If you wish to see this message again at any point in the main game loop (once you are inside the building) type 'help'. Good luck!")
    elif continu.lower() == "sneak":
      sneak = True
      velocity = 1
        
    # special commands
    if not h3_event and current_room.name == "computer lab":
      if continu.lower() == "attack":
        continu = input("The figure whips around, and in this instant, you vaguely resister that they're armed. Before you can defend yourself, there's a bullet in your chest. Your vision fades to black.")
        restart()
        break
      elif sneak == False and computer_event == False:
        computer_event = True
        print("The figure whips around as they hear your movement, despite your efforts to stay silent. Before you can react, there's a gun to your head. You freeze, and slowly raise your hands above your head.")
        time.sleep(4)
        print("\nYour heart hammers in your head, and you stare at the figure in front of you. They're female, and hold themselves like a soldier, dressed in dark greys. Finally, they seem to acknowledge that you aren't a threat, and lower their gun, and swear, looking at you. Afraid to move, you stay where you are.\n")
        time.sleep(4)
        continu = input("'You're just a kid. What're you doing in this stinkin' mess?' she say, surprised, after a pause. Before you can speak, she continues, 'No, that's not important. Just get out of here. Believe me, you don't want anything to do with what's happening here.' She drags you out of the room with surprising ease, and you find yourself in the first hallway again. 'Look,' she tells you, not unkindly, 'I'm not going to ask who you are, or why you're here. But this is life or death, kid. So run for the exit, and don't look back.' With that, she leaves you, and enters back into the computer lab.")
        current_room = h1
        horizontal_position = 3
        vertical_position = 1
    elif current_room.name == "first supply room" and continu.lower() == "take ladder":
      continu = input("You take the ladder.")
      inventory.append("ladder")
    elif current_room.name == "fourth office" and continu.lower() == "read email":
      os.system("clear")
      continu = input("The email reads: \n\nFrom: Isabelle Simons\nTo: Allan Kysiuk\nSubject: Maintenance Hallway\n\nAllan,\n\nI'm concerned about the liability of the maintenance hallway. We've had problems owing to it's connection to the underground compound, and the doors to the supply closets have been left unlocked in the past. Please address when possible.\n\n- Isabelle")
    elif current_room.name == "second office" and continu.lower() == "read note":
      os.system("clear")
      print("The note appears as if it was torn from a book, like a journal of some sort. The handwriting is neat and easily read:\n\nI have no idea what these off-brand Parallels are that they're making down there are. I signed up for experimenting on monsters, not humans. Note to self, investigate further.")
    elif current_room.name == "first office" and continu.lower() == "search cabinets":
      continu = input("\nYou rifle through the file cabinets, and while you find nothing major of note, extended searching revels an old photograph of a " + significant_gender + " with " + significant_hair + " hair. It almost resembles " + significant_name + ", but the photograph is blurry, and it's stained with blood.")
    elif current_room.name == "first office" and continu.lower() == "search file cabinets":
      continu = input("\nYou rifle through the file cabinets, and while you find nothing major of note, extended searching revels an old photograph of a " + significant_gender + " with " + significant_hair + " hair. It almost resembles " + significant_name + ", but the photograph is blurry, and it's stained with blood.")
    elif current_room.name == "first hallway" and continu.lower() == "look at plant":
      continu = input("Hi Ed. It's just a plant.")
    elif current_room.name == "employee lounge" and continu.lower() == "take water":
      continu = input("You take a paper cup from next to the water cooler, and fill it up. You now have water.")
      inventory.append("water")
    elif current_room.name == "first hallway" and continu.lower() == "water plant":
      if "water" in inventory:
        continu = input("The plant looks much happier. Good job.")
        plant_watered = True
        inventory.remove("water")
      else:
        continu = input("You don't have any water.")
    elif current_room.name == "first hallway" and continu.lower() == "eat plant":
      continu = input("The plant is poisonous. Nice one.")
      restart()
        
      
    # doors
    door_position = horizontal_position * 10 + vertical_position
    for item in current_room.doors:
      if item.coordinates1 == door_position:
        continu = input("\nYou are at the door to " + item.room2.name + ". Would you like to enter? (y/n)\n")
        if continu == "y":
          current_room = item.room2
          horizontal_position = int(item.coordinates2/10)
          vertical_position = item.coordinates2 - horizontal_position * 10
          continu = input("\nYou are now in the " + current_room.name)

    # hallway joiners
    if current_room.name == "first hallway":
      if door_position == 51:
        continu = input("You are at the joiner between the first hallway and the second hallway. Enter second? (y/n)\n")
        if continu == "y":
          current_room = h2
          horizontal_position = 1
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
    elif current_room.name == "second hallway":
      if door_position == 11:
        continu = input("You are at the joiner between the first hallway and the second hallway. Enter first? (y/n)\n")
        if continu == "y":
          current_room = h1
          horizontal_position = 5
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
      elif door_position == 13:
        continu = input("You are at the joiner between the second hallway and the third hallway. Enter third? (y/n)\n")
        if continu == "y":
          current_room = h3
          horizontal_position = 5
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
    elif current_room.name == "third hallway":
      if door_position == 51:
        continu = input("You are at the joiner between the second, third, and fourth hallways. Would you like to \n1: Enter second\n2: Enter fourth\n3: Stay in third?\n")
        if continu == "1":
          current_room = h2
          horizontal_position = 1
          vertical_position = 3
          print("\nYou are now in the " + current_room.name)
        elif continu == "2":
          current_room = h4
          horizontal_position = 1
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
    elif current_room.name == "fourth hallway":
      if door_position == 11:
        continu = input("You are at the joiner between the third hallway and the fourth hallway. Enter third? (y/n)\n")
        if continu == "y":
          current_room = h3
          horizontal_position = 5
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
      elif door_position == 15:
        continu = input("You are at the joiner between the fourth hallway and the fifth hallway. Enter fifth? (y/n)\n")
        if continu == "y":
          current_room = h5
          horizontal_position = 1
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
    elif current_room.name == "fifth hallway":
      if door_position == 11:
        continu = input("You are at the joiner between the fourth hallway and the fifth hallway. Enter fourth? (y/n)\n")
        if continu == "y":
          current_room = h4
          horizontal_position = 1
          vertical_position = 5
          print("\nYou are now in the " + current_room.name)
      elif door_position == 91:
        continu = input("You are at the joiner between the fifth hallway and the sixth hallway. Enter sixth? (y/n)\n")
        if continu == "y":
          current_room = h6
          horizontal_position = 1
          vertical_position = 5
          print("\nYou are now in the " + current_room.name)
    elif current_room.name == "sixth hallway":
      if door_position == 15:
        continu = input("You are at the joiner between the fifth hallway and the sixth hallway. Enter fifth? (y/n)\n")
        if continu == "y":
          current_room = h5
          horizontal_position = 9
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
      elif door_position == 11:
        continu = input("You are at the joiner between the sixth hallway and the seventh hallway. Enter seventh? (y/n)\n")
        if continu == "y":
          current_room = h7
          horizontal_position = 1
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)
    elif current_room.name == "seventh hallway":
      if door_position == 11:
        continu = input("You are at the joiner between the sixth hallway and the seventh hallway. Enter sixth? (y/n)\n")
        if continu == "y":
          current_room = h6
          horizontal_position = 1
          vertical_position = 1
          print("\nYou are now in the " + current_room.name)

    # special events
    if current_room.name == "maintenance hallway":
      if door_position == 101:
        print("You see an open vent above your head.")
        if "ladder" in inventory:
          continu = input("You place the ladder underneath it. Would you like to enter the vent? (y/n)\n ")
          inventory.remove("ladder")
          if continu == "y":
            os.system("clear")
            print("You climb through the vents, until eventually you reach what your internal sense of direction tells you is the loading dock. But this time, you're inside. You open a grate, and drop to the floor, ready to continue your search for " + significant_name + ", whatever it takes.")
            time.sleep(5)
            os.system("clear")
            credits()
            break
        if has_ladder == False:
          continu = input("Unfortunately, it is too tall for you to reach. You would need a ladder.")
    if current_room.name == "third hallway" and h3_event == False:
      continu = input("You hear footsteps coming toward you, and panic. You have about 30 seconds until they reach you. Act fast!")
      h3_event = True
      in_h3_event = True
      start = timer()
    if in_h3_event == True and timer() - start > 30:
      in_h3_event = False
      if current_room == h1 or current_room == h2 or current_room == h3 or current_room == h4 or current_room == h5:
        print("The footsteps get louder, and you back up in the hallway, out of time. A well-dressed businessman in a suit approaches, followed by what appears a bodyguard. The bodyguard grabs you, and you find yourself unable to move, staring helplessly at the businessman.")
        if player_gender == "boy":
          pronoun = "him"
        elif player_gender == "girl":
          pronoun = "her"
        else:
          pronoun = "them"    
        continu = input("\n'What do I do with " + pronoun + "?' the bodyguard asks. The businessman cockes his head, and smiles, 'The Uni's have no use for a child. Get rid of " + pronoun + ".' They're the last words you hear before everything goes black.")
        restart()
        break
      elif current_room == computer_lab:
        os.system("clear")
        if computer_event == True:
          continu = input("You rush into the room, only to see the woman from before, now slightly more alert and holding a gun. She almost shoots you, but recognizes you first.\n\n'Kid? What're you still doing here? It isn't safe.'\n\nSuddenly, a burly man bursts into the room, and shoots the woman before she can react, distracted as she is by you. He seems to be ignoring you for now, and you slowly back toward the exit, but you barely make it a step before another bullet finds your shoulder, and you fall to the group.\n\n The woman winces with pain, but manages to speak 'Don't hurt the kid. They have nothing to do with this.'\n\nBefore the burly man can respond, a well-dressed businessman steps into the room.\n\nThe other man, who you presume to be his bodyguard, questions him, 'What do I do with them?'\n\nThe businessman smiles for a second, then speaks, 'Take her to the Uni's. As for the kid, we've no use for them. Get rid of them.' You hear a loud noise, and a second later pain blossoms in your chest. \n\nThe last thing you hear is the woman's voice, cold but furious, 'You won't get away with this.'")
          restart()
        else:
          continu = input("You rush into the room, and see a woman, alert and holding a gun. She fires at you, taken aback, and you fall to the ground, your vision going black")
          restart()
      else:
        os.system("clear")
        print("In the nick of time, you get into a room, and pause at the door, hoping your heart isn't as loud as it sounds in your chest. You press your ear to the door, hoping to hear something.\n")
        time.sleep(2)
        print("Suddenly, you hear the noise of a gunshot, and a cry of pain.")
        time.sleep(1)
        if computer_event == True:
          continu = input("With a jolt, you realize the voice is that of the person you saw in the computer lab. You have no further time to ponder it before two distinct voices speak.\n")
          print("You faintly make out a distinctly male voice. You presume he's talking to the person you saw before, but can't be sure. 'Listen,' he says, anger underlying his tone, 'I don't know who you are, or what you're doing here, but we'll find out. And then you're going to pay.'\n")
          time.sleep(2)
          print("You hear the figure from before, reply with a humourless laugh, 'You can try.'\n")
          time.sleep(2)
          continu = input("'I daresay we're more capable than you think. Take her to the Uni's!' You hear another grunt of pain, and the footsteps recede away from you. After a couple of minutes, you judge it to be safe.")
        else:
          print("You faintly make out a distinctly male voice. 'Listen,' he says, anger underlying his tone, 'I don't know who you are, or what you're doing here, but we'll find out. And then you're going to pay.'\n")
          time.sleep(2)
          print("You hear another voice, which you can't determine the gender of, reply with a humourless laugh, 'You can try.'\n")
          time.sleep(2)
          continu = input("'I daresay we're more capable than you think. Take her to the Uni's!' You hear another grunt of pain, and the footsteps recede away from you. After a couple of minutes, you judge it to be safe.")
          
# irrelevant
else:
  print("Game software closed.")
  exit()
