from library import Library
from book import Book
from user import User

library = Library()

# Tambah buku
book1 = Book("Laskar Pelangi", "Andrea Hirata")
book2 = Book("Bumi", "Tere Liye")

library.add_book(book1)
library.add_book(book2)

# Tambah user
user1 = User("Hafidz", "U001")
user2 = User("Andi", "U002")

library.add_user(user1)
library.add_user(user2)

# Tampilkan data
library.show_books()
library.show_users()