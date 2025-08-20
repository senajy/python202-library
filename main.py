# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 19:33:17 2025

@author: Sena
"""

import json
from pathlib import Path


# Book sınıfı: Kitap nesnesini temsil eder
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} - {self.author} (ISBN: {self.isbn})"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"])


# Library sınıfı: Kitapları yönetir ve dosyaya kaydeder
class Library:
    def __init__(self, storage_file="library.json"):
        self.storage_file = Path(storage_file)
        self.books = []
        self.load_books()

    def load_books(self):
        if not self.storage_file.exists():
            self.books = []
            self.save_books()
        else:
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(item) for item in data]
            except Exception:
                self.books = []

    def save_books(self):
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2, ensure_ascii=False)

    def add_book(self, book):
        if self.find_book(book.isbn):
            raise ValueError("Bu ISBN zaten var!")
        self.books.append(book)
        self.save_books()
        return book

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def list_books(self):
        return self.books

    def find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None


# Menü ve ana uygulama
def menu():
    print("Kütüphane Menüsü")
    print("1) Kitap Ekle")
    print("2) Kitap Sil")
    print("3) Kitapları Listele")
    print("4) Kitap Ara")
    print("5) Çıkış")


def main():
    lib = Library("library.json")
    print("{Kütüphane uygulaması başlatıldı.}")

    while True:
        menu()
        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            print("Yeni kitap eklemek için lütfen ilgili bilgileri giriniz.")
            title = input("Kitap adı: ")
            author = input("Yazar: ")
            isbn = input("ISBN: ")
            try:
                lib.add_book(Book(title, author, isbn))
                print("Kitap eklendi!\n")
            except Exception as e:
                print("Hata:", e)

        elif choice == "2":
            isbn = input("Silinecek ISBN: ")
            if lib.remove_book(isbn):
                print("Kitap silindi.")
            else:
                print("Kitap bulunamadı.")

        elif choice == "3":
            books = lib.list_books()
            if not books:
                print("Kütüphane boş.")
            else:
                for b in books:
                    print("-", b)

        elif choice == "4":
            isbn = input("Aranacak ISBN: ")
            book = lib.find_book(isbn)
            if book:
                print(book)
            else:
                print("Kitap bulunamadı.")

        elif choice == "5":
            print("Programdan çıkılıyor. İyi günler dileriz!")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
