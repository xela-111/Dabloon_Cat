from Player import Player

class Location:
        
        def __init__(self, decribe, loc_x, loc_y, starting_dabloon, north, south, west, east, digenable ,prize, multienable, multioptions, decriberoomoptions):
                self.decribe = decribe  
                self.loc_x = loc_x
                self.loc_y = loc_y
                self.starting_dabloon = starting_dabloon
                self.north = north
                self.south = south
                self.west = west
                self.east = east 
                self.digenable = digenable
                self.prize = prize
                self.multienable = multienable
                self.multioptions = multioptions
                self.decriberoomoptions = decriberoomoptions
        def adddabloon (self, amount):
                self.starting_dabloon = self.starting_dabloon+amount
                
        def takedabloon(self, amount):
                if self.starting_dabloon >= amount: 
                        self.starting_dabloon = self.starting_dabloon-amount
                        print("Success!")
                        return(amount)
                else:
                        print(" not enought dabloons")
                        return (0)

        def move(self, direction, currentloc):
                if direction == ('N')   and self.north == 1:
                        currentloc = currentloc + 1
                        return (currentloc)
                elif direction == ('S') and self.south == 1:
                        currentloc = currentloc - 1
                        return (currentloc)
                elif direction == ('E') and self.west == 1:
                        currentloc = currentloc - 1
                        return (currentloc)     
                elif direction == ('W') and self.east == 1:
                        currentloc = currentloc + 1
                        return (currentloc)
                else: 
                        print("You can not move in this direction!")
                        return (currentloc)     
                
        def dig(self):
                if self.digenable == "yes":
                        print(f"You found a {self.prize}.")
                        return(self.prize)
                else:
                        print("The ground is too hard to dig!")
                        return("")
        def multichoice(self):
                if multienable:
                        print(multioptions)
                else:
                        print('No multiable choice')

        def lookatsky(self,player):
                print('You see a whispy vapor of smoke in the east.It appears there is a house in the far distance')
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def lookattree(self,player):
                print("As you round the tree, you spot a pouch swinging in the breeze. As you open it, you see it holds 30 dabloons.")
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def digindirt(self,player):
                print("As you continue to dig into the rocky ground, you spot something sparkingly in the ground. You can now see it is clearly a gem of some kind. It's inscription says to drop into a body of water.")
                self.multienable = 0
                if 'gem' in player.bag:
                        print('You have already dug here.')
                else:
                        player.bag.append('gem')
                return(self.loc_x,self.loc_y)
        def looksouth(self,player):
                print("As you look out, you spot asea sparkling in the sunlight. It goes on for as long as the eye can see.")
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def lookup(self,player):
                print("As you peer into the sky, you see a oddly shaped dragon in the tops of the clouds.")
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def lookwest(self,player):
                print("You see a shop or a house in the west as it produces puffs of vapor in the twilight sky.")
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def diginmound(self,player):
                print("As you dig into the mound, you see a dig-covered bag. As you open it, you see it is a tablet that holds the infomation on how to tame a dragon, and the directions to a local tavern.")
                if 'tablet' in player.bag:
                        print('You have already dug here.')
                else:
                        player.bag.append('tablet')
                        print("The tablet is now in your bag")
                return(self.loc_x,self.loc_y)
        def reachforbutterfly(self,player):
                print("The butterfly calls to you with its brillant patterns of blue and orange. It fluters away into the north and something in you is desperate to follow it.")
                return(48,53)
        def donothing(self,player):
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def touchbarrier(self,player):
                alice = player.starting_dabloon
                player.starting_dabloon = player.starting_dabloon - alice
                self.adddabloon(alice)
                print("As you touch the barrier, you get shooked by the wall of energy and your dabloons fall out of your bag and onto the ground.")
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def dropgem(self, player):
                if 'gem' in player.bag:
                        print("As you drop the gem into the water, it creates a swirling vortex and takes you with it. You sink into the depths of the murky sea. As you struggle to hold your breathe, you realise with a start, that you can suddenly breathe underwater. As you open  your eyes, you see a breathetaking kingdom in frount of you.")
                        return(53,48)
                else:
                        print("This item isn't in your possession, please gain it and retry.")
                        return(self.loc_x,self.loc_y)
        def gointowater(self, player):
                print("As you jump into the inviting water, your foot brushes against a shell. You pick it up and watch as it glints in the sunlight.")
                player.bag.append("shell")
                return(self.loc_x,self.loc_y)
        def fish(self,player):
                if "fishing gear" in player.bag:
                        print("You caught a golden fish. It flops around until you wrap it up and place it in your bag.")
                        player.bag.append("golden fish")
                else:
                        print("You can not fish since you don't have a rod.")
                return(self.loc_x,self.loc_y)
        def tamedragon(self, player):
                if 'golden fish' in player.bag and  'dragon gear' in player.bag :
                        print("As you approach the dragon, you throw the fish in front of it. It begins to eat it as you place the gear onto its back. After finishing its snack, it places its nose onto your hand.")
                        player.pet.append('dragon')
                        player.achivements.append("Dragon Tamer")
                        self.multienable = 0
                else:
                        print("You do not have a fish or the correct gear. Please gain said items and retry.")
                        self.multienable = 0
                return(self.loc_x,self.loc_y)
        def petdragon(self, player):
                print("As you go to touch the dragon, it backs up into the cave, unfamilar with your prestence. You trip on a rock  and all your dabloons spill out.")
                dragon = player.starting_dabloon
                player.starting_dabloon = player.starting_dabloon - dragon
                self.adddabloon(dragon)
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def slowlybackaway (self, player):
                print('As you spot the dragon, you slowly climb back down.')
                self.multienable = 0
                return(59,56)
        def climbwithgrapplinghook(self, player):
                if  'grappling hook' in player.bag :
                        print("As you head up, assisted by your hook, you begin the terrifying ascent.")
                        self.multienable = 0
                        return(60,56)
                else:
                        print("You do not have a grappling hook.")
                        self.multienable = 0
                        return(self.loc_x,self.loc_y)
        def turnaround(self, player):
                print('You assess the rock wall is too dangerous and begin to retrace your steps back.')
                self.multienable = 0
                return(59,55)
        def climbupwithyourhands(self, player):
                print('You try to climb up without any gear, but the rock is too steep and lacks any large cracks to place your hands in.')
                self.multienable = 0
                return(self.loc_x,self.loc_y)
        def talktoher(self, player):
                print("She says:'You must be the human the empress foretold. Come with me!'")
                self.multienable = 0
                return(57,48)
        def swimaway(self, player):
                if 'shell' in player.bag:
                        print("As you swim away from the odd mermaid, you observe the many shops. They seem to be trading with shells. You spot a facsinating bracelet made with barnacles. As you attempt to pay for it with your shell, murmurs break out. The final one you hear before getting dragged towards the castle is: 'The explorer has arrived'.")
                        return(57,48)
                        self.multienable = 0
                else:
                        print("As you look around the open air market, a looming shadow of a massive shark arrives. Mermaids begin to scream, and you get caught in the crowd as they swarm to the castle.")
                        return(57,48)
                        self.multienable = 0
                return(54,47)
        def bowtoher(self, player):
                print("As you bow down, a mermaid shoves you to the front. The empress says: 'There's no need to bow, explorer. I'm requiring your services. I need you to create and find the materials to make a shell necklace. The shell should be on one of the sea's shores and necklace rope is near a shop, hidden in the ground. I require this so I can become a human. My body wasn't build for the water. If you do these, you will be rewarded hansomely.'")
                self.multienable = 0
                return(50,46)
        def stayback(self,player):
                print("As you attempt to back up, a mermaid pushes you to the front. The empress says: 'There's no need to shove the explorer. I'm requiring their services. I need you to create and find the materials to make a shell necklace. The shell should be on one of the sea's shores and necklace rope is near a shop, hidden in the ground. I require this so I can become a human. My body wasn't build for the water. If you do these, you will be rewarded hansomely.'")
                self.multienable = 0
                return(50,46)
        def bringherthenecklace(self, player):
                if 'shell' in player.bag and 'necklace' in player.bag :
                        options45 = input(f"You have done me something that was claimed to be impossible, explorer {username}. This is massive debt to pay back, so to pay, I offer you a throne or an end. The remaining of my magic can send you home or you can rule the throne in my place. To choose, say your option: 'Go home' or 'Rule the throne'.  ")
                        if options45 == "Go home":
                                print(f"Gooodbye, traveler {username}. I hope you enjoyed the time you spend here.")             
                                quit()
                        elif options45 == "Rule the throne":
                                print(f"Congrations, {username}. You now rule the throne of Nysaxera. I hope you rule wisely.")
                                player.achivements.append("The throne of Nysaxera")
                                player.starting_dabloon = 1000
                                self.multienable = 0
                                return(54,51)
                        else:
                                print("That is not a viable option, please retry.")
                                self.multienable = 1
                        
                else:
                        print("As you look around the open air market, a looming shadow of a massive shark arrives. Mermaids begin to scream, and you get caught in the crowd as they swarm to the castle.")
                        return(57,48)
                        self.multienable = 0
                return(54,47)
        def rabbithole(self,player):
                print("As you lower yourself into the rabbit hole, hundreds of dabloons swirl around you, just out of your reach as you fall.")
                self.multienable = 0
                return(48,54)
        def dabloondoor(self,player):
                alice2 = player.starting_dabloon
                player.starting_dabloon = player.starting_dabloon - alice2
                self.adddabloon(alice2)
                print("You reach for the second door and as you do, you hand touches pure static eletricity and you are unable to pass though. As you get shocked, all of your dabloons fall out of your sachel.")
                return(48,53)
        def largedoor(self,player):
                print("As you pass though the massive door that dwarfs even dragons, you feel the biting cold and feel frigid.")
                self.multienable = 0
                return(60,56)
        def takeone(self,player):
                print("As you eat one, you can feel the fighting prowess in you increase but only incrimenally. As you eat it, the swirling vortex comes back and deposits you onto the nearest river bank.")
                player.bag.append('1 candy')
                self.multienable = 0
                return(48,56)
        def takethree(self,player):
                print("As you eat the candies, you can feel the fighting prowess in you increase massively. As you eat it, the swirling vortex comes back and deposits you onto the nearest river bank.")
                player.bag.append('3 candies')
                self.multienable = 0
                return(48,56)
        def touchthebarrier(self,player):
                print("As you touch the pulsating barrier, you get shocked and fall into the river. You slowly get sucked into a vortex of swirling water.")
                self.multienable = 0
                return(48,55)
        def jumpintotheriver(self,player):
                print("As you jump into the river, the current picks you up quickly and you slowly get sucked into a vortex of swirling water.")
                self.multienable = 0
                return(48,55)
        def crossthebridge(self,player):
                print("As you slowly cross the bridge, you arrive in a wasteland.")
                self.multienable = 0
                return(self.loc_x,self.loc_y + 1)
        def fightjabberwock(self, player):
                if 'sword' in player.bag and '3 candies' in player.bag :
                        print("As you fight you feel invigorated. You feel like you can beat anything and as you get loss in the feeling, you realize you have beaten the jabberwock. As you lay down your sword with the jabberwock's head still attached, cheers fill the sky and you get transported to the castle. ")
                        player.bag.append("jabberwock's head")
                        return(48,57)
                elif 'sword' in player.bag and '1 candy' in player.bag :
                        print("As you fight you feel invigorated, but you feel you lack the true amount of power necessary to beat it. As you clambor onto its back, it tosses you into the river.")
                        return(48,55)
                else:
                        print("As you fight you feel you lack the true amount of power necessary to beat it. As you clambor onto its back, it tosses you into the river")
                        return(48,55)
                return(self.loc_x,self.loc_y)
        def bringthejabberwockhead(self,player):
                if "jabberwock's head" in player.bag:
                        alicechoice = input(f"As you arrive in the palace, you roll the jabberwock's head to the red queen. She stares at it in utter shock and watches helplessly as your previous loyal knights begin to arrest her. As she eats arrested for high treason, a silverly cat appears. It says 'The choice is yours player {username}. You may transport back to the land you came from or you may end the game now. End the Game or Continue On.'")
                        if alicechoice == "Continue On":
                                player.achivements.append("Ruler of Wonderland")
                                return(50,50)
                        elif alicechoice == "End the Game":
                                quit()
                        else:
                                print("This isn't a viable answer, please retry.")
                else:
                        print("You don't have the jabberwock's head, please come back and get it.")
                        self.multienable = 0
                return(self.loc_x,self.loc_y)
        
                


                
        
                
