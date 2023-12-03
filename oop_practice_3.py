class House:
    room_num = 7
    bathrooms = 4

    def cost_evaluation(self, rate):
        cost = rate * self.room_num
        return cost

house = House()

print('Bathrooms = ', house.bathrooms)
print('No. of rooms = ', House.room_num)



bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)