class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print("Buku berhasil ditambahkan!")

    def add_user(self, user):
        self.users.append(user)
        print("User berhasil ditambahkan!")

    def show_books(self):
        print("\n=== DAFTAR BUKU ===")

        for book in self.books:
            book.display_book()
            print("----------------")

    def show_users(self):
        print("\n=== DAFTAR USER ===")

        for user in self.users:
            user.display_info()
            print("----------------")