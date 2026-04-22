from operations import add_book,show_book,borrow_book,return_book

def library():
    while True:
        print("menu")
        print("1-Add book")
        print("2-Show book")
        print("3-Borrow book")
        print("4-Return book")
        print("5-Exit")
        n=int(input("Enter your choice:"))
        if(n==1):
            add_book()
        elif(n==2):
            show_book()
        elif(n==3):
            borrow_book()
        elif(n==4):
            return_book()
        elif(n==5):
            print("Thank you! Visit again😊")
            break
        else:
            print("Invalid choice")

            
library()