
#v1.1
#setup clear screen for multiple systems

# set debug to 1 to enable debugging - in code place if debug == 1: in front of your debug functions
debug=0
global currentloc_x 
currentloc_x = int(50)
global currentloc_y 
currentloc_y = int(47) 
global petprices
petprices = {'snake':40,'dog':20,'cat':35, 'rabbit':15, 'frog':15}
storeobjects = {'grappling hook':30, 'moutain boots':25, 'mountain jacket':45, 'food rations':20, 'dragon gear': 30}
dragonplaces = {"*******'s shop":[46,50], "starting location":[50,50], "REDACTED's store":[52,48],"CENSORED's store":[56,54]}
from os import system, name
from time import sleep
from room import Location
from Player import Player
from NPC import npc

def clear():
        if name =='nt':
                _ = system('cls')
        else:
                _ = system('clear')

def startingscreen():
        gamemode=input('Type 1 to start. Type 2 for an explaintion of the game. ')
        if gamemode=='1':
                peacefulgame()
        elif gamemode== '2':
                print("This is an adventure game with two ways to end the game and 3 total paths. You can try to tame the mysterious dragon, dive into the lake, attempt to save wonderland, or even just dig around and find artifacts and dabloons. The currency of the game is dabloons, with many oppurtunities to gain dabloons. It is a fantasy-based game with hudreds of ways to keep you entertained.")
                startingscreen()
        else:
                print('This is not a viable answer. Please retry!')
                sleep(3)
                startingscreen()

def createplayer():
        player = Player(username, 50,50,40,["Shovel", "jabberwock's head"],[],[])
        # print(f"You are starting with {player.starting_dabloon} dabloons. ")
        return(player)

def controls():
        global currentloc_y
        global currentloc_x
        combinedlocation_var = "location" + str(currentloc_x) + str(currentloc_y)
        currentroommove = str("location" + str(currentloc_x) + str(currentloc_y) + ".move")
        currentroomtakedabloon = str("location" + str(currentloc_x) + str(currentloc_y) + ".takedabloon")
        currentroomdescribe = str("location" + str(currentloc_x) + str(currentloc_y) + ".decribe")
        currentroomdebloons = eval(str("location" + str(currentloc_x) + str(currentloc_y) + ".starting_dabloon"))
        currentroomdig = str("location" + str(currentloc_x) + str(currentloc_y) + ".dig")
        currentroomadddabloon = str("location" + str(currentloc_x) + str(currentloc_y) + ".adddabloon")
        currentroommultichoice = ("location" + str(currentloc_x) + str(currentloc_y) + ".multienable")
        currentroommultichoiceopt = ("location" + str(currentloc_x) + str(currentloc_y) + ".multioptions")   
        decriberoomoptions = ("location" + str(currentloc_x) + str(currentloc_y) + ".decriberoomoptions")
        
        print("")
        print(eval(currentroomdescribe))
        if eval(currentroommultichoice):
                # here I used a loop to call each index of the list to print them togther - this concatenates the tex
                for i in range(len(eval(currentroommultichoiceopt))):
                        print(eval(currentroommultichoiceopt + "[" + str(i) + "]") + " - " + eval(decriberoomoptions + "[" + str(i) + "]"))
                        #print(location5050.multioptions[0] + location5050.decriberoomoptions[0])
        if debug == 1:print(f"This room has {currentroomdebloons} dabloons in it.")
        if debug == 1:print(f"debug: {currentloc_x, currentloc_y}")
        if currentloc_x == shopkeep.loc_x and currentloc_y == shopkeep.loc_y:
                print(f' You can sense a human presence in the area you entered. It apppears {shopkeep.name} is here.')
                #if shopkeep.pets != []:
                        #print(f'{shopkeep.name} has the following pets: {shopkeep.pets}')
        if currentloc_x == shopkeep2.loc_x and currentloc_y == shopkeep2.loc_y:
                print(f' You can sense a human presence in the area you entered. It apppears {shopkeep2.name} is here.')
                #if shopkeep2.pets != []:
                        #print(f'{shopkeep2.name} has the following pets: {shopkeep2.pets}')
        control=input('? ')
        control=control.lower()
        if control=="inventory":
                print(f"Current debloon amount is {player.starting_dabloon}. ") 
                print("")
                print(f"Your current items are:")
                print(*player.bag,sep='\n')
                print(f"Your current pets are:")
                print(*player.pet,sep='\n')
                print(f"Your current achivements are:")
                print(*player.achivements,sep='\n')
                controls()
        elif control == 'map':
                print(f'Current location is {currentloc_x, currentloc_y}.')
                showmap()
                controls()
        elif control == "up": 
                newcurrentloc_y = eval(currentroommove)('N', currentloc_y) 
                currentloc_y = newcurrentloc_y
                controls()
        elif control == "down": 
                newcurrentloc_y = eval(currentroommove)('S', currentloc_y) 
                currentloc_y = newcurrentloc_y
                controls()      
        elif control == "left": 
                newcurrentloc_x = eval(currentroommove)('E', currentloc_x) 
                currentloc_x = newcurrentloc_x
                controls()      
        elif control == "right": 
                newcurrentloc_x = eval(currentroommove)('W', currentloc_x) 
                currentloc_x = newcurrentloc_x
                controls()
        elif control == "ride dragon":
                if 'dragon' in player.pet:
                        print("As you get onto your dragons back, the question 'where do you wish to go' pops into your mind. The available locations to travel to are:")
                        for key in dragonplaces:
                              print(key)
                        dragonloc = input("Where do you wish to go? ")
                        if dragonloc in dragonplaces:
                               currentloc_x, currentloc_y = dragonplaces.get(dragonloc)
                               print(currentloc_x, currentloc_y)
                               controls()
                               
                        else:
                                print("The dragon can not fly to this location.")
                                controls()
                else:
                        print("Sorry, you are unable to complete this action.")
                controls()
        elif control=='take dabloon':
                amount = input(f'This room contains {currentroomdebloons}, How many do you want to take? ')
                if checkdablooninput(amount):
                        amount = int(amount)
                else:
                        print('That is not a number, please retry')
                        controls()
                dabloonstoadd = eval(currentroomtakedabloon)(amount)
                player.adddabloon(dabloonstoadd)
                controls()
        elif control=='dig':
                prize = eval(currentroomdig)()
                if prize == "":
                        controls()
                else:
                        player.addprize(prize)
                controls()

        elif control=='help':
                print("")
                print("Commonly used commands")
                print("'Inventory' - shows you your items bought, pets bought or found, achivements done, and dablooons found") 
                print("'Map' -  a map that gives you your x and y coordinates")
                print("'Take Dabloon' - picks up or recieves dabloons given")
                print("'Give Dabloon' - gives dabloon away to buy items")
                print("'Up' - moves player up") 
                print("'Down' -  moves player down")
                print("'Left' - moves player left")
                print("'Right' - moves player right")   
                print("'Dig' - dig for something")
                print("'Talk to NPC' - talk to an NPC")
                print("'Help' - shows player list of commands")
                print("'Ride Dragon'  - transports you to a different location using a dragon.")
                controls()
        elif control == 'talk to npc':
                talkingNPC= input("Which NPC do you wish to talk to? ")
                if talkingNPC == "*******" and currentloc_x == shopkeep.loc_x and currentloc_y == shopkeep.loc_y:
                        pickingpet = input(f'Welcome user {username}, do you wish to buy a pet from my wares? ')
                        if pickingpet.lower() == 'yes':
                                choosepet = input(f'Wonderful! I have many pets to choose from. I currently have a {shopkeep.pet} Unfortunately, you must only choose one pet. Who is your choice? ')
                                choosepet = choosepet.lower()
                                if choosepet in shopkeep.pet:
                                        print(f"The cost of {choosepet} is {petprices[choosepet]}.")
                                        if player.starting_dabloon >= petprices[choosepet]:
                                                player.starting_dabloon = player.starting_dabloon - petprices[choosepet]
                                                shopkeep.pet.remove(choosepet)
                                                player.pet.append(choosepet)
                                                print("Congrations on your new pet, I hope you wil enjoy countless adventures with eachother.")
                                                controls()
                                        else:
                                                print(f"You don't have enough money to afford a {choosepet}! Please come again.")
                                                controls()
                                        #add money transaction later
                                else:
                                        print("I don't have this pet in stock unfortunately, please come another rainy day.")
                                        controls()
                        else:
                                print("Sorry, it looks like my shop couldn't satify your needs. Please return at a later date.")
                                controls()
                elif talkingNPC == "REDACTED" and currentloc_x == shopkeep2.loc_x and currentloc_y == shopkeep2.loc_y:
                        tavernrequest = input(f'Howdy user {username}, do you want to {shopkeep2.pet}? ')
                        if tavernrequest == 'get a translator':
                                tablet1=input('Is this tablet the thing you wish for me to translate? ')
                                if tablet1 == 'Yes' and 'tablet' in player.bag:
                                        print(f"This tablet is giving a detailed guide on how to train a dragon and the area to find them. They suggest using riding gear to ride it after gaining trust with it. They advise to find a speacial fish in the sea and say the best place to find dragons is up northeast, in the mountains. If you wish to climb, my friend CENSORED has mountain gear in his store. Good luck traveler {username}!")
                                else:
                                        print(f"Sorry user {username}, I cant help you with your request.")
                        elif tavernrequest == 'have a beer':
                                print('Here you go! Enjoy your night and the beer is on the house.')
                                player.bag.append('beer')
                        elif tavernrequest == 'have a place to stay the night':
                                print(f"Sorry user {username}, there are no rooms availabe this night. However, my fellow friend CENSORED's inn is south and open for customers.")
                        elif tavernrequest == 'get directions to CENSORED':
                                print('You go east for about 4 miles, then hike up for about 2.')
                        controls()
                elif talkingNPC == "CENSORED" and currentloc_x == shopkeep3.loc_x and currentloc_y == shopkeep3.loc_y:
                        tavernrequest1 = input(f'Hello user {username}, do you want to buy an object from my shop? The mountains are impossible to climb without! ')
                        if tavernrequest1 == 'yes':
                                mountaingear = input(f'Wonderful! I have many objects to choose from. I currently have a {shopkeep3.pet}.')
                                if mountaingear in shopkeep3.pet:
                                        print(f"The cost of {mountaingear} is {storeobjects[mountaingear]}.")
                                        if player.starting_dabloon >= storeobjects[mountaingear]:
                                                player.starting_dabloon = player.starting_dabloon - storeobjects[mountaingear]
                                                shopkeep3.pet.remove(mountaingear)
                                                player.bag.append(mountaingear)
                                                print(f"Thank you for buying with me, have a nice day {username}")
                                                controls()
                                        else:
                                                print(f"You don't have enough money to afford a {mountaingear}! Please come again.")
                                                controls()
                                        #add money transaction later
                                else:
                                        print("I don't have this object in stock unfortunately, please come another rainy day.")
                                        controls()
                else:
                        print("This NPC can't be reached, please try again at a later date.")
                        controls()
                                        
        elif control=='give dabloon':
                amount = input(f'You have {player.starting_dabloon}, How many do you want to give? ')
                if checkdablooninput(amount):
                        amount = int(amount)
                else:
                        print('That is not a number, please retry')
                        controls()
                amountreturned = player.takedabloon(amount)
                givedabloon = eval(currentroomadddabloon)(amountreturned) 
                controls()

        
        #this statement must be the last elif please do not put choices below this or they won't work 
        elif eval(currentroommultichoice):
                for options in (eval(currentroommultichoiceopt)):
                        if options == control:
                                currentloc_x, currentloc_y = eval(str(combinedlocation_var + '.' + options +"(player)"))
                                controls()
                print('Not a valid letter choice. Please retry.')
                controls()
        else:
                print("")
                print("This is not a valid command!")
                controls()    

def peacefulgame():
        print("If you want to learn more about the game controls, please type 'Help'")
        print("---")
        controls()

def showmap():
        print("45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 X")
        print("60 *            *               ^")    
        print("59   *       *    *           /   \       ^ ")
        print("58      *  *       *               ^    /   \ ")
        print("57       []       *              /   \ ")  
        print("56    [] [] []  *                 ^       [] []")
        print("55  * []    [] *                /   \     []")
        print("54   *[] [] []*                  [] [] [] [] ^")
        print("53     * [] *  []                []    ^   /   \ ")
        print("52        *    [] [] [] [] [] [] []  /   \ ")          
        print("51             [] []       []  _   -     -    -") 
        print("50 [] [] [] [] [] []  -   -         ~        -")
        print("49             []   -      [] [] []       -")
        print("48             []  -    [] []     ~ []       -")
        print("47             []   -      [] [] []        _")
        print("46             []      _        -")
        print("45 ")
        print('Y')

def checkdablooninput(input_str):
        if input_str.strip().isdigit():
                return True
        else:
                return False
#all functions defined above this line
clear()
print('Hello user! Welcome to the game.')
username=input('What is your name? ' )
print(f'Welcome {username}.')

#build locations for level 1 (up,down,left,right)
location5050=Location('You are in a large green forest. You spot dabloons that float gently up to greet you. They led a path to the east as they glint in the sunlight',50,50,10,1,1,1,1,"no", 0,0,'','')
location4950=Location('As you turn left, you see smoke in the distance and a gentle breeze sway around you.',49,50,10, 0, 0, 1, 1,"no",0,0,'','')
location5151=Location('You spot a overgrown oak tree that is seemingly shielded something from your view and a strange feeling to dig.',51,51,30, 1, 1, 1, 0,'yes','gem',1, ['digindirt','lookattree','lookatsky'],['dig in dirt with shovel', 'look at the mysterious tree object' ,'look up into the sky'])
location5051=Location('You approach a hill as you walk . The forest thins out as you stand on top of a hill.',50,51,10, 1, 1, 0, 1,"no",0, 1,['lookwest','looksouth', 'lookup'],['look west','look south', 'look into the sky'])
location5049=Location('You haphazardly kick some fallen leaves as you walk, noting the lack of animals around.',50,49,5, 1, 1, 0, 0,"no",0,0,'','')
location5048=Location('You tumble into a dark pit, an apparant hog trap. You see something logded into the dirt besides you.',50,48,0, 1, 1, 0, 1,"no","",0, '','')
location5047=Location('As you venture father, you sense something that compells you to dig.',50,47,0, 1, 1, 0, 0,"yes",'fishing gear',0,'','')
location4650=Location('You see a storefront seem to appear in the blink of an eye. Its signs read "Welcome to *******s store. Please come in around the back." As you walk to the back, you see a open door and you smell a hint of sulfer and magic.',46,50,6,0,0,0,1,"no",0,0,'','')
location4750=Location('As you walk through the fall leaves, you spot more dabloons floating as they sway with the wind.',47,50,15,0,0,1,1,"yes",'necklace',0,'','')
location4850=Location('As you stroll in the seemingly neverending forest, you accidentally hit a mound that rises unexpectedly out of the ground. As you wince and look up, you see a beautitful butterfly flutter above.',48,50,0,0,0,1,1,"yes",'tablet', 1,['donothing','diginmound','reachforbutterfly'], ['do nothing and walk away', 'dig into the curious mound of poorly hidded dirt', 'reach for the mesmerizing butterfly'])
location5150=Location('Coming into this clearing, you see a hint of glimmering water ahead just over the hill.',51,50,2,1,0,1,0,"no",'', 0,'','')
location5252=Location('You see a tavern ahead. Its smoke makes plumes in the wintery air. As you enter, the owner of the tavern, REDACTED greets you warmly.',51,48,0,0,0,1,1,"no",'', 0,'','')
location5046=Location('The scenery seems to be leading into a sea. As you near it, the water laps at your ankles as you see dabloons glinting under the sun.',50,46,10, 1, 0, 0, 0,"no",0, 1, ['dropgem','gointowater','fish'],['drop the gem into the water', 'dive into the inviting water', 'cast your line in the sea'])                                                                                                                                                                                                                  
location5451=Location('The scenery seems to be leading into a sea. As you near it, the water laps at your ankles as you see dabloons glinting under the sun.',54,51,10, 1, 0, 0, 0,"no",0, 1,['dropgem','gointowater','fish'],['drop the gem into the water', 'dive into the inviting water', 'cast your line in the sea'])
location5654=Location("As your breath creates smoky plumes into the air, you finally see a cabin, with steam rising from the chimmney. As you approach the door, the sign reads 'Welcome to CENSORED's mountain gear and shoppe.' ",56,54,0, 0, 1, 0, 1,"no",0, 0, '','')
location5053=Location("You see the pulsating barrier that goes all long as the eye can see. ",50,53,0, 0, 1, 0, 0,"no",0, 1, ['touchbarrier','lookup'], ['Touch the pulsating barrier','Look upwards'])
location5052=Location('As you continue of the hill, you spot a large wall of vibrating energy.',50,52,0, 1, 1, 0, 1,"no",0,0,'','')
location5552=Location('You walk along the path as it leads into snowy mountains that glint in the faint sunshine.',55,52,0, 0, 0, 1, 1,"no",0,0,'','')
location5652=Location('You spot a plume of smoke in the near distance.',56,52,0, 1, 0, 1, 0,"no",0,0,'','')
location4853=Location('You appear in a liminal space, a neverending hallway. Three doors are in front of you. One is a rabbithole digused as a door, the second has a trail of dabloons that you can barey see in the dim lightening, and the third is a massive door that dwarfs you.',48,53,10, 0, 0, 0, 0,"no",0,1,['rabbithole','dabloondoor', 'largedoor'],['the first door', 'the second door', 'the third door'])
location4854=Location(f"As you look around, you see massive mushrooms the size of trees growing around you in what appears to be a forest. As you look ahead, you see a gorgeous rushing river with bridges that connects to a desolate charred up area. In the distance, you can see a massive castle. As you look down, you see a twitching rabbit. It begins to speak 'Hello user {username}, All the civilans of Wonderland implore you to try to defeat the Jabberwock and free us from the reign of the red queen. To do this, you must become extraordinarly skilled at fighting.' ",48,54,0, 0, 0, 1, 1,"no",0,0,'','')
location4857=Location("As you look around, you see this is the Red queen's castle. It's extraordinarly gorgeous, with deep red undertones, tall white ceilings  and fablous stained glass windows. It appears almost churchlike in its glory. As you look forward, you realise you are in the queen's throne hallway.",48,57,0,0, 1, 0, 0,"no",0,1,['bringthejabberwockhead'],["bring the queen the jabberwock's head"])
location4855=Location("As you fall into the river, you realize it is much deeper than you previously belived. You slowly get sucked into a vortex of swirling water, and it spits you into a store. No one is in sight but one bag of wrapped hard candy lay on the table. The bag says 'This candies contain the ability to extend your fighting skills to help you on your journey. Take 3 at most.'  ",48,55,0, 0, 1, 0, 0,"no",0,1,['takeone','takethree'],['take one candy', 'take three candies'])
location4756=Location("The area you walk into is charred and scarred beyond belief. A barely-standing sign reads 'Home to the Jabberwock'. ",47,56,0, 1, 1, 0, 1,"no",0,0,'','')
location4955=Location('As you walk over the small bridge, you can just about touch the mysterious barrier that surrounds you.',47,55,0, 1, 1, 1, 0,"no",0,1,['touchthebarrier','jumpintotheriver','crossthebridge'], ['try to touch the barrier to your right', 'jump into the rushing water', 'slowly cross the bridge'])
location4954=Location('The area you come into is a forest of massive mushrooms leading into a bridge over a raging river. ',47,54,0, 1, 0, 1, 0,"no",0,0,'','')
location4755=Location('As you walk over the small bridge, you can just about touch the mysterious barrier that surrounds you.',47,55,0, 1, 1, 0, 1,"no",0,1,['touchthebarrier','jumpintotheriver','crossthebridge'], ['try to touch the barrier to your left', 'jump into the rushing water', 'slowly cross the bridge'])
location4754=Location('You appear to be in a large forest of mushrooms. Baby mushrooms pop in and within your foots reach.',47,54,0, 1, 0, 0, 1,"no",0,0,'','')
location4956=Location("The area you walk into is charred and scarred beyond belief. A barely-standing sign reads 'Home to the Jabberwock'. ",47,56,0, 1, 1, 1, 0,"no",0,0,'','')
location4856=Location('As you enter the prime territory of Jabberwock, the air around you feels hotter. The jabberwock finally appears, a horrid chimera beast with the body of a dragon, a fish-like head, and a pair of talon-like hands on both its arms and its wings.',48,56,0, 1, 0, 1, 1,"no",0,1,['fightjabberwock'],['try to fight the jabberwock'])
location5754=Location('As you walk, you can sense the cold air and the path becomes rocky on the edges.',57,53,0, 0, 0, 1, 1,"no",0,0,'','')
location5653=Location('The father you venture into the mountains, the more you see the rapidly appearing shop.',56,53,0, 1, 1, 0, 0,"no",0,0,'','')
location5854=Location('As you walk, you spot dabloons frozen in the air.',58,54,30, 0, 0, 1, 1,"no",0,0,'','')
location5954=Location('As you climb, the pathway leads into rocky area, and gains more turns.',59,53,0, 1, 0, 1, 0,"no",0,0,'','')
location5955=Location('The surrounding path becomes almost unclimbable, the rocks becoming slippery and the ground covered in icey snow slush.',59,55,0, 1, 1, 0, 0,"no",0,0,'','')
location5956=Location('As you continue on the mountain path, you see a wall of rock in font of you. To get to the top, you will need grappling hook.',59,56,0, 1, 0, 0, 0,"no",0,1,['climbupwithyourhands','turnaround', 'climbwithgrapplinghook'],['attempt to climb up without mountain gear','turn back', 'attempt to climb up with mountain gear'])
location6056=Location('As you use your grappling hook to climb up, you spot a majestic dragon, its breath curling into smoke in the bitter air.',60,56,0, 0, 0, 0, 0,"no",0,1,['tamedragon', 'petdragon', 'slowlybackaway'], ['attempt to tame dragon', 'pet the dragon', 'slowly back away from the dragon'])
location5152=Location('As you walk, you can sense the area getting colder and the leaves on the foest floor crumpling.',51,52,0, 0, 0, 1, 1,"no","",0,'','')
location5352=Location('As you forest clearing thins out, you see the snowy mountain peaks and spot some dabloons in the wind.',53,52,30, 0, 0, 1, 1,"no",0,0,'','')
location5452=Location('Coming into this clearing, you see a hint of glimmering water ahead just over the hill.',54,52,0,0,1,1,1,"no",'', 0,'','')
location5748=Location("You see what appears to be a gorgeous castle. Pearls and sanstone line the rich and grand interior. Countless gems and treasure from sunken ships make up the throne, looking as if it may fall over due to the weight of it's treasures. On the throne, a beautitful pale mermaid sits. She is decorated richly, with many swirling fabrics and shells on her frail body. As trumpets sound and countless other mermaids come in, you realize she is the only mermaid without dark or tanned skin. She stands out as otherworldly. ",57,48,0, 0, 0, 0, 0,"no",0,1,['bowtoher', 'bringherthenecklace','stayback'],['Bow down to the queen', 'Give her the necklace', 'stay in the back of the crowd of mermaids.'])
location5447=Location('You observe the many shops in the clearing. They seem to be trading with shells and the open air market was teeming with objects.',54,47,0, 1, 0, 0, 1,"no",0,0,'','')
location5449=Location('As the area comes into view, you realise this is a neighborhood, with many houses lining the street.',54,47,0, 0, 1, 0, 1,"no",0,0,'','')
location5549=Location('The neighborhood continues on as you stroll. You spot a bustling school, park with swishing kelp, and a playground filled with mini mermaids.',55,49,0, 0, 0, 1, 1,"no",0,0,'','')
location5547=Location('As you walk, you realize this is the town section of this kingdom. Many adult meraids work to extract edible kelp and teens mermaids swim to find suken treasures from lost ships.',55,47,0, 0, 0, 1, 1,"no",0,0,'','')
location5649=Location('the neighborhood ends as you approach a cliffside decorated with coral with many fishes swimming in and out.',56,49,0, 0, 0, 1, 0,"no",0,0,'','')
location5647=Location('As you look out on the cliffside, you spot hundreds of suken ships expanding far past the eye can see as the sea.',56,47,0, 0, 0, 1, 0,"no",0,0,'','')
location5348=Location('The surronding area is stunningly gorgeous. Sea coral and sea fans decorate the area. There is a castle ahead with marble pillars and gold trimming.',53,48,0, 0, 0, 0, 1,"no",0,0,'','')
location5448=Location('A mermaid swims up to you as you float closer to the magical castle in the far distance.',54,48,0, 1, 1, 1, 0,"no",0,1,['talktoher','swimaway'],['Talk to the mermaid', 'Swim away towards the bustling market.'])
player = createplayer()
shopkeep = npc('*******', 46, 50, 0, [],['rabbit', 'frog', 'snake', 'dog', 'cat'])
shopkeep2 = npc('REDACTED',52,52, 0, [],['get a translator', 'have a beer', 'have a place to stay the night'])
shopkeep3 = npc('CENSORED',56,54, 0, [],['grappling hook', 'moutain boots', 'dragon gear', 'mountain jacket', 'food rations'])
if debug ==1:print(shopkeep.pets)
startingscreen()
