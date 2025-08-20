# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 19:33:17 2025

@author: Sena
"""

import json
from pathlib import Path
import httpx  # Aşama 2 için ekledik

# Book sınıfı
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def str(self):
        return f"{self.title} - {self.author} (ISBN: {self.isbn})"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"])


# Library sınıfı
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

    # Open Library API’den kitap çekme
    def fetch_book_from_api(self, isbn):
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                title = data.get("title", "Bilinmeyen Başlık")
                authors = data.get("authors", [])
                if authors:
                    names = []
                    for a in authors:
                        a_resp = httpx.get(f"https://openlibrary.org{a['key']}.json")
                        if a_resp.status_code == 200:
                            names.append(a_resp.json().get("name", "Bilinmeyen Yazar"))
                    author = ", ".join(names)
                else:
                    author = "Bilinmeyen Yazar"
                return Book(title, author, isbn)
            else:
                return None
        except Exception:
            return None

    # ISBN ile kitap ekleme
    def add_book(self, isbn):
        if self.find_book(isbn):
            raise ValueError("Bu ISBN zaten var!")

        book = self.fetch_book_from_api(isbn)
        if book:
            self.books.append(book)
            self.save_books()
            return book
        else:
            return None

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

# Menü
def menu():
    print("\nKütüphane Menüsü")
    print("1) Kitap Ekle ")
    print("2) Kitap Sil")
    print("3) Kitapları Listele")
    print("4) Kitap Ara")
    print("5) Çıkış")

# Ana uygulama
def main():
    lib = Library("library.json")
    print("{Kütüphane uygulaması başlatıldı.}")

    while True:
        menu()
        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            isbn = input("ISBN giriniz: ")
            book = lib.add_book(isbn)
            if book:
                print("Kitap eklendi:", book)
            else:
                print("Kitap bulunamadı veya API hatası.")

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