#define a class
class MyFirstClass:
    print("Who wrote this?")

    index = "Author-Book"

    #define a function
    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book + " in " + year)

whodunnit = MyFirstClass()
whodunnit.hand_list("Joseph Akpan", "Youth's Diary", str(2023) )
