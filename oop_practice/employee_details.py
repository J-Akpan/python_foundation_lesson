class employee:
    def __init__(self, name, surname) -> None:
        self.name = name 
        self.surname = surname

class supervisor(employee):
    def __init__(self, name, surname, password) -> None:
        super().__init__(name, surname)
        self.password = password

class salesperson(employee):
    def leave_request(self, days):
        return "I hereby request for " + str(days) + "days leave as due"

joseph = supervisor("Joseph ", "A,  ", "slanga")

matt = employee("Matt ", "O")
james = employee("james ", "B")

print("Your supervisor deatails are as follows " + joseph.name + joseph.surname + joseph.password)
print(james.name + james.surname)


