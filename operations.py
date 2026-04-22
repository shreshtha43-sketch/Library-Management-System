from utilis import books,issuedbook
def add_book():
    name=input("Enter the name of the book:")
    books.append(name)
    print(f"{name} is added to the library")
def show_book():
    if(books==[]):
        print("No books available")
    else:
        for i in books:
            print(i)
def borrow_book():
    n=input("Enter the book you want to borrow")
    if(n in books):
        issuedbook.append(n)
        books.remove(n)
        print(f"{n} is issued")
    else:
        print(f"{n} is not available")
def return_book():
    n=input("Enter the book name u want to return")
    if(n in issuedbook):
        issuedbook.remove(n)
        books.append(n)
        print(f"{n} is returned")
    else:
        print("No such book was issued")
