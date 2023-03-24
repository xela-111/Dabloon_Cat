class npc:
        def __init__(self,  name, loc_x, loc_y, starting_dabloon,bag, pet):
                self.name = name
                self.loc_x = loc_x
                self.loc_y = loc_y
                self.starting_dabloon = starting_dabloon
                self.bag = bag
                self.pet = pet
        
        def takedabloon(self, amount):
               if self.starting_dabloon >= amount: 
                        self.starting_dabloon = self.starting_dabloon-amount
                        print("Success!")
                        return(amount)
               else:
                        print("Not enought dabloons")
                        return (0)      
        def adddabloon(self,amount):
                self.starting_dabloon = self.starting_dabloon+amount
                print("new amount" , self.starting_dabloon)

        def addpet(self,pet):
                self.pet.append(pet)
                print(f"{pet} add to your bag!")
                
        def givepet(self,requestedpet,username,player):
                if requestedpet in self.pet:
                        player.pet.append(requestedpet)
                        self.pet.remove(requestedpet)
                        print(f"Here's your {requestedpet} {username}!")
                else: print("I don't sell this pet, sorry.")

                        
                
                




