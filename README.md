  ✅ Todo App
---

🌟 **Todo App** — bu foydalanuvchilarga o‘z vazifalarini boshqarish, ularni teglar bilan belgilash, ahamiyati va holatiga qarab tartiblash imkonini beruvchi RESTful API ilovadir.

---

## 🎯 Loyiha maqsadi

> Foydalanuvchilarga o‘z ish faoliyatini samarali tashkil qilish imkonini beruvchi REST API yaratish. 

🔐 JWT orqali autentifikatsiya, 🏷 teglar, 📌 muhimlik darajasi, 📅 muddati bilan filtrlash, 🔍 qidiruv, 📈 statistikalar — hammasi bir joyda!

---

## 🚀 Texnologiyalar

| Texnologiya         | Tavsif                              |
|---------------------|--------------------------------------|
| Django              | Backend framework                    |
| Django REST Framework | API uchun                          |
| PostgreSQL          | Ma'lumotlar bazasi                  |
| JWT                 | Foydalanuvchi autentifikatsiyasi     |
| Swagger / drf-yasg  | API dokumentatsiyasi                 |
| Docker (ixtiyoriy)  | Deploy uchun                         |

---

## 🔐 Autentifikatsiya endpointlari

| Endpoint                  | Metod | Tavsif                          |
|--------------------------|-------|---------------------------------|
| `/api/auth/register/`    | POST  | Ro‘yxatdan o‘tish               |
| `/api/auth/login/`       | POST  | Tizimga kirish (JWT token)      |
| `/api/auth/refresh/`     | POST  | Tokenni yangilash               |
| `/api/auth/verify/`      | POST  | Tokenni tekshirish              |

---

## 👤 Foydalanuvchi profili

| Endpoint         | Metod | Tavsif                   |
|------------------|-------|--------------------------|
| `/api/profile/`  | GET   | Profil ma'lumotlari      |
| `/api/profile/`  | PATCH | Profilni yangilash       |

---

## 🏷 Taglar (Teglar)

| Endpoint            | Metod   | Tavsif              |
|---------------------|---------|---------------------|
| `/api/tags/`        | GET/POST| Teglar ro'yxati/yaratish |
| `/api/tags/{id}/`   | GET/DELETE | Bitta tegni olish/o'chirish |

---

## 📋 Ro'yxatlar (Todo Lists)

| Endpoint                     | Metod     | Tavsif                     |
|------------------------------|-----------|----------------------------|
| `/api/todo-lists/`           | GET/POST  | Ro'yxatlarni olish/yaratish |
| `/api/todo-lists/{id}/`      | GET/PATCH/DELETE | Ro'yxatga oid amallar |
| `/api/todo-lists/{id}/items/`| GET       | Ro'yxatdagi vazifalarni olish |

---

## ✅ Vazifalar (Todo Items)

| Endpoint                             | Metod       | Tavsif                         |
|--------------------------------------|-------------|--------------------------------|
| `/api/todo-items/{id}/`              | GET/PATCH/DELETE | Vazifani ko‘rish/yangi/tahrir |
| `/api/todo-items/{id}/status/`       | PATCH       | Vazifa holatini o‘zgartirish  |
| `/api/todo-items/{id}/complete/`     | POST        | Vazifani bajarilgan deb belgilash |
| `/api/todo-items/{id}/start/`        | POST        | Vazifani bajarilmoqda deb belgilash |

---

## 🔎 Filtrlash & Qidiruv

✅ Teg bo‘yicha  
✅ Muhimlik darajasi bo‘yicha  
✅ Holat (kutilmoqda, bajarilmoqda, bajarildi)  
✅ Qidiruv (vazifa nomi, tavsifi)  
✅ Muddat (deadline) bo‘yicha

---

## ⚙️ O‘rnatish

```bash
# 1. Repositoryni klonlash
git clone https://github.com/Bunyodjon-Mamadaliyev/Todo-App.git
cd Todo-App

# 2. Virtual environment yaratish
python -m venv venv
source venv/bin/activate

# 3. Talablar faylini o‘rnatish
pip install -r requirements.txt

# 4. Ma’lumotlar bazasini sozlash
python manage.py migrate

# 5. Superuser yaratish
python manage.py createsuperuser

# 6. Serverni ishga tushirish
python manage.py runserver
```

## 📄 Swagger API Dokumentatsiyasi

Swagger oynasi:
```bash
http://localhost:8000/swagger/
```
Redoc:
```bash
http://localhost:8000/redoc/
```
## 🧪 Testlar
```bash
# Testlarni ishga tushiring
python manage.py test
```
## 📊 Qo‘shimcha funksiyalar
- ✅ Foydalanuvchilar o‘rtasida vazifa tayinlash

- 📎 Vazifalar uchun fayl yuklash

- 💬 Izoh qoldirish imkoniyati

- 📈 Vazifa statistikasi & hisobotlar


## 🔒 Xavfsizlik
- 🔐 JWT autentifikatsiya

- 🚨 Throttling (so‘rovlar sonini cheklash)

- 🛡️ SQL Injection & XSS & CSRF himoyasi

- 📥 Input validatsiyasi

## 🧠 Kod Talablari
- PEP8 standartlariga mos

- DRY prinsipi

- Fat Models, Skinny Views

- select_related, prefetch_related yordamida query optimizatsiyasi

- Annotatsiyalar va izohlar bilan toza kod

## 📁 Loyiha tuzilmasi
```bash
📦 Todo-App
├── 📁 common               
│   ├── 📁 migrations  
│   ├── 📄 admin.py        
│   ├── 📄 apps.py          
│   ├── 📄 models.py        
│   ├── 📄 pagination.py   
│   ├── 📄 serializers.py   
│   ├── 📄 urls.py         
│   └── 📄 views.py      
│          
├── 📁 config/                  
│   ├── 📄__init__.py
│   ├── 📄asgi.py             
│   ├── 📄settings.py         
│   ├── 📄urls.py              
│   └── 📄wsgi.py          
│           
├── 📁 tags               
│   ├── 📁 migrations
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 models.py        
│   ├── 📄 serializers.py
│   ├── 📄 urls.py
│   └── 📄 views.py
│
├── 📁 todos                 
│   ├── 📁 migrations
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 models.py        
│   ├── 📄 serializers.py
│   ├── 📄 urls.py
│   └── 📄 views.py
│
├── 📁 users               
│   ├── 📁 migrations
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 models.py         
│   ├── 📄 serializers.py
│   ├── 📄 urls.py
│   └── 📄 views.py
│
├── 📄 .gitignore           
├── 📄 manage.py            
├── 📄 README.md            
└── 📄 requirements.txt     
```