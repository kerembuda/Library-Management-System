class Library:

    def __init__(self):
       self.file=open("books.txt","a+")
       print("\n***** *****  Welcome to the Library Management System!  ***** *****")

    def __del__(self):
        print("Library closed\n***** *****")
        self.file.close()

    def add_book(self):
        
        def get_input():
            while True:
                book_title = input("Please enter book title: ")
                author = input("Please enter book author: ")
                release_year = input("Please enter release year: ")
                page_number = input("Please enter the total number of pages: ")

                if not all([book_title, author, release_year, page_number]):
                    print("Error: All fields must be filled. Please try again.")
                else:
                    line = f"{book_title},{author},{release_year},{page_number}\n"
                    self.file.write(line)
                    self.file.flush()
                    print(f"***** *****\nBook added successfully to the library!\n***** *****\nBook name: {book_title}\nBook author: {author}\nRelease year: {release_year}\nPage number: {page_number}\n***** *****")
                    break

            
        while True:
            get_input()
            user_input = input("Do you want to enter another book? (yes/no): ")
            if user_input.lower() != 'yes':
                break

    def list_books(self):
        
        self.file.seek(0)

        book_data = self.file.read()
        lines = book_data.splitlines()
        if len(lines) == 0:
            print("Not a single book at the library at the moment.")
        elif len(lines) == 1:
            print("There is only one book at the library:")
        else:
            print("The library contains "+ str(len(lines)) + " book(s).\nList of books available at the library:")
        
        for i in lines:
            title = i.split(',')[0]
            author = i.split(',')[1]
            print(f"Book title: {title:<40} Author: {author}")

    def remove_book(self):
        title_to_be_deleted = input("Please write the full title of the book you want to remove: ").lower()

        try:
            self.file.seek(0)
            lines = self.file.readlines()
            self.file.seek(0)
            self.file.truncate()

            found = False

            for line in lines:
                if title_to_be_deleted != line.split(',')[0].strip().lower():
                    self.file.write(line)
                else:
                    found = True

            if not found:
                raise ValueError(f"Book titled '{title_to_be_deleted}' not found in the library, please try again.")

            self.file.flush()
            print(f"Book '{title_to_be_deleted}' has been removed from the library.")
        except ValueError as e:
            print(f"Error: {e}")
        
    def print_user_menu(self):
        print('''
    ***  MENU  ***
    1) List Books
    2) Add Book 
    3) Remove Book
    Press "Q" to exit the program.
    ''')


library = Library()
while True:
    
    library.print_user_menu()
    user_selection = input("Please select: ")
    print("***** *****")
    if user_selection == "1":
        library.list_books()
    elif user_selection == "2":
        library.add_book()
    elif user_selection == "3":
        library.remove_book()
    elif user_selection == "Q":
        break
    elif user_selection == "q":
        break
    else:
        print("Wrong input, try again!!!")

    

