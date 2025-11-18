# 💣 EMAIL BLASTER 3000
**Mass Email Sender**  
_The fastest, simplest and cleanest way to blast personalized emails in seconds._

---

## 👾 INTRODUCTION

**Email Blaster 3000** is a standalone graphical app built in Python.  
It allows you to send **customized mass emails** using a `.csv` contact list that includes email + recipient name.

Perfect for:

- DJs & producers sending promos 🎧  
- Small underground marketing pushes 💸  
- Startup/product announcement lists 🚀  
- Private crew/internal communications 👥  

> ⚠️ **Disclaimer:** This tool is not designed for illegal spam or unsolicited advertising.  
> Only use it with **confirmed contacts who agreed to receive your messages.**

---

## 🧩 FEATURES

✔ Load contact list from `.csv`  
✔ Personalized messages using `{name}` placeholder  
✔ Scrollable message editor  
✔ Standalone executable — no Python required  
✔ Secure Gmail App Password support  

---

## 📂 CSV FORMAT (MANDATORY)

Create a CSV file like this:

```csv
email,name
alex@example.com,Alex
nightdrive.djs@gmail.com,NightDrive
labelmanager@bass.com,Sara
```

Save it and load it via **Load CSV**.

---

## 🚀 HOW TO USE

1️⃣ Launch the application:
```
EmailBlaster3000.exe
```

2️⃣ Open **DJs List** tab → load your CSV contacts  

3️⃣ Open **Email** tab → write subject + message  
Use `{name}` to personalize, for example:

```
Hey {name}, hope you're doing great!
Here is a new private tool I'm sharing with you…
```

4️⃣ Open **Config** tab  
Enter your Gmail + **App Password**

5️⃣ Press **BLAST!** 💣

---

## 🔐 HOW TO GET YOUR GMAIL APP PASSWORD

Google blocks third-party apps using normal passwords, so you must create a **Gmail App Password**.

### Steps:

1. Go to: https://myaccount.google.com/
2. Open **Security**
3. Enable **2-Step Verification (2FA)** if not enabled
4. Return to **Security**
5. Click **App Passwords**
6. Select:
   - App: **Mail**
   - Device: **Windows / PC**
7. Copy the 16-character password shown

Example (paste without spaces):

```
abcd efgh ijkl mnop
```

---

## 🧪 TESTING RECOMMENDATION

| Step | Recipients | Purpose |
|------|------------|---------|
| 1 | Only yourself | Confirm SMTP works |
| 2 | 2–3 trusted friends | Proofreading |
| 3 | Full list | Final send |

---

## 📦 DOWNLOADS

Releases will appear here:

👉 https://github.com/Aniol24/EmailBlaster3000/releases

---

## 📜 LICENSE

**MIT License — Free to use, modify and distribute.**

---

## ❤️ CREDITS

**Developed by:** *Dokku — 2025*  
