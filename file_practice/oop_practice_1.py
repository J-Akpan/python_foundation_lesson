class House:
    '''
    the concept is for the class to hold all
    the properties of the house such as ;
    room numbers, etc
    '''
    room_num = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.room_num)
    
    # initiate instance of the class
house = House()
print('No numbers of rooms ', house.room_num)
print('No. of bathrooms', House.bathrooms)

# update the instance of the class attributr and not the class attribute
house.room_num = 7
print(house.room_num)
print(House.room_num)

# updating the attribute of the class
House.bathrooms = 4
print(house.bathrooms)
print(House.bathrooms)