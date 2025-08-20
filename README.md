# Python202 Library

Bu proje, Global AI Hub Python 202 Bootcamp kapsamında hazırlanmış bir uygulamadır.  
Proje aşamalar halinde ilerlemektedir ve her aşamada yeni özellikler eklenmiştir.

---

## 📂 Proje Yapısı

python202-library/  
├── main.py              # Projenin ana kod dosyası (Aşama 2 ile API entegrasyonu eklendi)  
├── library.json         # Kitap verilerini tutan JSON dosyası  
└── requirements.txt     # Gerekli kütüphaneler (httpx eklendi)

---

## 🚀 Çalıştırma

Projeyi çalıştırmak için:

```bash
python main.py

Uygulama başlatıldığında komut satırında aşağıdaki menü görüntülenecektir:

Kütüphane Menüsü
1) Kitap Ekle (ISBN ile)
2) Kitap Sil
3) Kitapları Listele
4) Kitap Ara
5) Çıkış

📌 Kitap eklerken yalnızca ISBN girmeniz yeterlidir, başlık ve yazar bilgisi Open Library API’den alınır.


---

🛠 Gereksinimler

requirements.txt dosyası güncellenmiştir:

httpx

Uygulamayı çalıştırmadan önce gerekli kütüphaneyi yüklemek için:

pip install -r requirements.txt


---

📌 Notlar

library.json dosyası, kitap verilerini saklamak için kullanılmaktadır.

Proje ilerledikçe yeni fonksiyonlar ve özellikler eklenecektir.



---

🛠 Gelecek Aşamalar

FastAPI ile web servisi oluşturulacak (Aşama 3)

requirements.txt güncellenecek

Daha detaylı kullanım rehberi hazırlanacak
