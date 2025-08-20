# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 23:06:25 2025

@author: Sena
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import Library  # Kendi Library sınıfımızı buradan alıyoruz

# FastAPI uygulaması
app = FastAPI(title="Kütüphane API")

# Ortak kullanılacak Library nesnesi
lib = Library("library.json")

# ISBN almak için model
class ISBNModel(BaseModel):
    isbn: str

# Kitap döndürmek için model
class BookModel(BaseModel):
    title: str
    author: str
    isbn: str

# Kitapları listeleme
@app.get("/books")
def get_books():
    books = lib.list_books()
    return [b.to_dict() for b in books]

# ISBN ile kitap ekleme
@app.post("/books")
def add_book(data: ISBNModel):
    try:
        book = lib.add_book(data.isbn)
        if book is None:
            raise HTTPException(status_code=404, detail="Kitap bulunamadı ya da API hatası")
        return book.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# ISBN ile kitabı silme
@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    ok = lib.remove_book(isbn)
    if not ok:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    return {"message": "Kitap silindi"}
