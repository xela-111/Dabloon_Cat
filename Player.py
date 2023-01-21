class Player:
        """docstring for ClassName"""
        def __init__(self,  username, loc_x, loc_y, starting_dabloon,bag):
                self.username = username
                self.loc_x = loc_x
                self.loc_y = loc_y
                self.starting_dabloon = starting_dabloon
                self.bag = bag
        
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

        def addprize(self,prize):
                self.bag.append(prize)
                print(f"{prize} add to your bag!")
                




