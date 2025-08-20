# Python202 Library

Bu proje, Global AI Hub Python 202 Bootcamp kapsamında hazırlanmış bir uygulamadır.  
Proje üç aşamadan oluşur ve her aşamada yeni özellikler eklenmiştir:

1. **Aşama 1:** OOP ile terminal kütüphane uygulaması  
2. **Aşama 2:** OpenLibrary API entegrasyonu (ISBN ile kitap ekleme)  
3. **Aşama 3:** FastAPI ile REST API kütüphane servisi  

## 📂 Proje Yapısı

python202-library/
├── main.py # Terminal uygulaması (Aşama 1-2)
├── api.py # FastAPI uygulaması (Aşama 3)
├── library.json # Kitap verilerini tutan JSON dosyası
├── requirements.txt # Gerekli kütüphaneler (httpx, fastapi, uvicorn)
└── README.md # Proje açıklamaları

## 🚀 Çalıştırma

### Aşama 1-2 (Terminal Uygulaması)
```bash
python main.py

Kütüphane Menüsü:

Kitap Ekle (ISBN ile)

Kitap Sil

Kitapları Listele

Kitap Ara

Çıkış

Aşama 3 (FastAPI Uygulaması)
uvicorn api:app --reload

Tarayıcıdan:
👉 http://127.0.0.1:8000/docs

📌 API Endpointleri

GET /books → Kütüphanedeki tüm kitapları listeler

POST /books → ISBN alır ({"isbn": "9780140328721"} gibi), kitabı ekler

DELETE /books/{isbn} → ISBN’e göre kitabı siler

🛠 Gereksinimler

requirements.txt içeriği:
httpx
fastapi
uvicorn

Kurulum:
pip install -r requirements.txt
