class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_book(self):
        status = "Dipinjam" if self.is_borrowed else "Tersedia"

        print(f"Judul   : {self.title}")
        print(f"Penulis : {self.author}")
        print(f"Status  : {status}")