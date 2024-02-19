class Library:
    def __init__(self):
        self.file_book = book
        self.file = open(self.file_book, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file_book.seek(0)
        lines = self.file_book.readlines()
        if lines:
            print("- List of Books -\n")
            for line in lines:
                author, title, releaseYear, numOfPage = line.strip().split(',')
                print("Author: ", author)
                print("Title: ", title)
                print("Release Year: ", releaseYear)
                print("Number of Pages: ", numOfPage)
                print()
        else:
            print("Please add a book!")
        return True

    def add_book(self):
        author = input("name of book author: ") 
          title = input("book title: ")
            releaseYear = input("year: ")
              numOfPage = input("number of pages: ")

        self.file_book.write(f"{author},{title},{releaseYear},{numOfPage}\n")
        print("Book added successfully.")
        return True

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
         lines = self.file_book.readlines()
        self.file_book.seek(0)
      self.file_book.truncate()

        for line in lines:
            words = line.strip().split(',')
             if words and words[0] != title:
          self.file_book.write(line)

    lib = Library('books.txt')
     while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your key: ")
    if choice == '1':
        if lib.list_books():
            break 
          elif choice == '2':
        if lib.add_book():
            break
     elif choice == '3':
        lib.remove_book()
        print("Book remove.")
        break   
              elif choice == '4':
        print("Exit")
        break
    else:
            print("\n")
           else:
        pass 