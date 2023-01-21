class Location:
        """docstring for ClassName"""
        def __init__(self, decribe, loc_x, loc_y, starting_dabloon, north, south, west, east,digenable,prize):
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
                        print(f"You found a {self.prize}!!")
                        return(self.prize)
                else:
                        print("The gound is too hard to dig!")
                        return()
