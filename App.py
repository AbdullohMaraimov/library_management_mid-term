from Book import Book
from User import User
from Library import Library


def show_all_users():
    for user in Library.users:
        print(user)


def register():
    username = input("Enter your username: ")
    password = input("Create new password: ")
    new_user = User(username, password)
    Library.users.append(new_user)
    print("\033[92m Successfully registered!!! \033[0m \n")


def add_book():
    print("\033[93m ------------Adding book------------- \033[0m")
    new_book_title = input("Enter new book title: ")
    new_book_author = input("Enter new book author: ")
    new_book_genre = input("Enter new book genre: ")
    new_book_price = input("Enter new book price: ")

    new_book = Book(new_book_title, new_book_author, new_book_genre, new_book_price, len(Library.books) + 1000)
    Library.books.append(new_book)
    print("\033[92m Added Successfully \033[0m")
    show_all_books()


def delete_book():
    is_deleted = False
    show_all_books()
    book_id_to_delete = input("Enter book id to delete: ")

    for book in Library.books:
        if str(book.book_id) == book_id_to_delete:
            Library.books.remove(book)
            is_deleted = True

    if is_deleted:
        print("\033[92m Deleted successfully!!! \033[0m")
    else:
        print("\033[91m Failed. No such book \033[0m")


def update_book():
    show_all_books()
    id_book_update = input("Enter the id of book to update: ")
    for book in Library.books:
        if str(book.book_id) == id_book_update:
            changed_title = input("Change the title: ")
            changed_author = input("Change the author: ")
            changed_genre = input("Change the genre: ")
            changed_price = input("Change the price: ")

            if changed_title == "":
                book.title = book.title
            else:
                book.title = changed_title

            if changed_author == "":
                book.author = book.author
            else:
                book.author = changed_author

            if changed_price == "":
                book.price = book.price
            else:
                book.price = changed_price

            if changed_genre == "":
                book.genre = book.genre
            else:
                book.genre = changed_genre

            print("\033[92m Book changed----------------------- \033[0m")
            print(book)
            print("\033[92m----------------------------------- \033[0m")


def admin_action_menu(current_user):
    next = True
    while next:
        print("\033[93m \n---------------Admin Menu--------------- \033[0m")
        print("1.See All Books")
        print("2.Search for book")
        print("3.Add Book")
        print("4.Delete Book")
        print("5.Update Book")
        print("0.Back to main menu")
        answer = input("Enter your option: ")

        if answer == "1":
            show_all_books()
        elif answer == "2":
            search_for_book()
        elif answer == "3":
            add_book()
        elif answer == "4":
            delete_book()
        elif answer == "5":
            update_book()
        elif answer == "0":
            next = False
        else:
            print("\033[91m Invalid input, try again \033[0m")


def show_all_books():
    print("\n \033[93m---------------All Books------------------- \033[0m")
    for i in range(len(Library.books)):
        print(i + 1, Library.books[i])


def search_for_book():
    book_exits = False
    found_book = Book("", "", "", 0, -1)
    print("\n ----------------Searching for book---------------")
    search_by = input("Search book by the following: \n\t\t1.Author\n\t\t2.Title\n\t\t3.Genre\n"
                      "\tEnter your answer: ")
    if search_by == "1":
        book_author = input("Enter author of the book: ")
        for book in Library.books:
            if book.author == book_author:
                found_book = Book(book.title, book.author, book.genre, book.price, book.book_id)
                print(found_book)
                book_exits = True
    elif search_by == "2":
        book_title = input("Enter title of the book: ")
        for book in Library.books:
            if book.title == book_title:
                found_book = Book(book.title, book.author, book.genre, book.price, book.book_id)
                print(found_book)
                book_exits = True
    elif search_by == "3":
        book_genre = input("Enter the genre of book: ")
        for book in Library.books:
            if book.genre == book_genre:
                found_book = Book(book.title, book.author, book.genre, book.price, book.book_id)
                print(found_book)
                book_exits = True

    if book_exits == True:
        print("\n \033[92m \tBook is found!!! \033[0m")
    else:
        print("\033[91m No such book found \033[0m")


def purchase_book(current_user):
    book_purchased = False
    book_id = input("Enter book id to buy: ")
    for book in Library.books:
        if str(book.book_id) == book_id:
            current_user.bought_books.append(book)
            book_purchased = True

    if book_purchased:
        print("\t \033[92m Purchased Successfully!!!\033[0m")
    else:
        print("\t \033[91m Failed 😒\033[0m")


def show_purchased_book(current_user):
    print("\033[93m --------------Purchased books------------------ \033[0m")
    for book in current_user.bought_books:
        print(book)


def user_action_menu(current_user):
    next = True
    while next:
        print("\033[93m \n---------------User Menu--------------- \033[0m")
        print("1.See All Books")
        print("2.Search for book")
        print("3.Purchase book")
        print("4.See my books")
        print("0.Back to main menu")
        answer = input("Enter your option: ")

        if answer == "1":
            show_all_books()
        elif answer == "2":
            search_for_book()
        elif answer == "3":
            purchase_book(current_user)
        elif answer == "4":
            show_purchased_book(current_user)
        elif answer == "0":
            next = False
        else:
            print("\033[91m Invalid input, try again \033[0m")


def log_in():
    is_user_found = False
    current_user = User("none", "000")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in Library.users:
        if user.username == username and user.password == password:
            is_user_found = True
            current_user = user

    if is_user_found:
        print("\033[92m Logged In Successfully \033[0m")

        if current_user.role == "admin":
            admin_action_menu(current_user)
        else:
            user_action_menu(current_user)

    else:
        print("\033[91m Your username or password did not match \033[0m")


print("\033[94m ----------Library management App------------- \033[0m")
next = True

while next:
    print("\033[93m ----------------MENU----------------- \033[0m")
    print("\t1.Register")
    print("\t2.Log in")
    print("\t0.Quit")
    answer = input("Choose your action: ")

    if answer == "1":
        register()
    elif answer == "2":
        log_in()
    elif answer == "0":
        next = False
    else:
        print("\033[91m Invalid option\n \033[0m")
