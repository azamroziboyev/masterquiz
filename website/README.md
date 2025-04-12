# MasterQuiz Bot Dashboard

Bu loyiha MasterQuiz Telegram bot uchun statistikalarni va ma'lumotlarni real vaqtda ko'rsatib turadigan veb-sayt.

## Imkoniyatlar

* Real vaqt statistikasi
* Foydalanuvchilar ma'lumotlarining boshqaruvi
* Test ma'lumotlarining boshqaruvi
* Referral tarmoq tahlili
* Grafikli ma'lumotlarni vizualizatsiya qilish

## O'rnatish

1. Kerakli paketlarni o'rnatish:

```bash
cd website
pip install -r requirements.txt
```

2. Veb-saytni ishga tushirish:

```bash
python app.py
```

3. Veb-sayt http://localhost:5000 manzilida ishlaydi

## Netlify'ga yuklash

Bu veb-saytni Netlify'ga yuklash uchun quyidagi qadamlarni amalga oshiring:

1. Netlify hisobingizga kiring
2. "Add new site" va "Import an existing project" tugmasini bosing
3. GitHub yoki boshqa git provayderga ulaning va ushbu repozitoriyni tanlang
4. Deploy sozlamalarini tekshiring va "Deploy site" tugmasini bosing

Eslatma: Bot ma'lumotlar bazasiga ulanish uchun ma'lumotlar bazasi kredensiallarini Netlify'ga o'rnatishingiz kerak. Netlify boshqaruv panelida "Site settings" -> "Environment variables" bo'limiga o'ting va quyidagi muhit o'zgaruvchilarini o'rnating:

- `DATABASE_URL`: Ma'lumotlar bazasiga ulanish URL

## Ma'lumotlar bazasi

Veb-sayt botning mavjud SQLite ma'lumotlar bazasidan foydalanadi, lekin PostgreSQL'ga ham ulash mumkin. `DATABASE_URL` muhit o'zgaruvchisi orqali ma'lumotlar bazasi bilan ulanishni sozlang.

## Xavfsizlik

Veb-saytga kirish faqat ma'murlar uchun bo'lishi uchun asosiy sahifani himoya qilish tavsiya etiladi. Netlify Identity xizmatidan foydalanish yoki oddiy URL usuli bilan himoyalash mumkin.