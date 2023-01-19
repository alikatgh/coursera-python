class MyFirstClass:
    print('Who wrote this?')
    index = 'Author-Book'

    def __init__(self, philosopher, book):
        self.philosopher = philosopher
        self.book = book
        print(philosopher + ' wrote the book: ' + book)


book = MyFirstClass('Plato', 'Republic')
print(book)

# solution
# Sample Solution code


class MyFirstClass2():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass2.index)
        print(philosopher + " wrote the book: " + book)


whodunnit = MyFirstClass2()
whodunnit.hand_list("Sun Tzu", "The Art of War")
