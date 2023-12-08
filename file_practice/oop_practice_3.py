class House:
    room_num = 7
    bathrooms = 4

    def cost_evaluation(self, rate):
        cost = rate * self.room_num
        return cost

house = House()

print('Bathrooms = ', house.bathrooms)
print('No. of rooms = ', House.room_num)



