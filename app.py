from Utils import database

USER_PROMOT = '''
Options -
'a' - To add book
'l' - To list all books
'r' - To read a book
'd' - To remove a book
'q' - To quit
\nYour choice: '''


def menu():
    database.create_book_table()

    user_input = input(USER_PROMOT)

    while user_input != 'q':

        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            list_books()

        elif user_input == 'r':
            prompt_read_book()

        elif user_input == 'd':
            prompt_delete_book()

        else:
            print("Invalid input. Plz read the manual :)")

        user_input = input(USER_PROMOT)


def prompt_add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    database.add_book(name.title(), author.title())


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input("Enter the name of book you finished reading: ")

    database.mark_book_as_read(name.title())


def prompt_delete_book():
    name = input("Enter the name of book you wish to delete: ")

    database.delete_book(name.title())


menu()
