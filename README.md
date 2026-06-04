<div align="center">

# 🧟 Resident Evil Fan Website

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django)](https://djangoproject.com)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)](https://mysql.com)
[![Railway](https://img.shields.io/badge/Deployed-Railway-purple?style=for-the-badge)](https://railway.app)

> **A fully functional fan website dedicated to the Resident Evil franchise, built with Django and styled with a dark Umbrella Corporation theme.**

[🌐 Live Website](https://resident-evil-site-production.up.railway.app) • [👤 Developer](https://t.me/NOOB_comeback) • [🤖 Telegram Bot](https://github.com/hojiakbaroktamov89-cpu/resident-evil-bot)

</div>

---

## 🌐 Live Demo

> 🔗 **[resident-evil-site-production.up.railway.app](https://resident-evil-site-production.up.railway.app)**

The website is live and deployed on Railway — available 24/7!

---

## 📸 About the Project

This is my **first full-stack web project**, built from scratch using Django. The website is themed around the iconic **Umbrella Corporation** from the Resident Evil franchise, featuring a dark, atmospheric design that matches the horror game aesthetic.

The project was built as a university assignment and demonstrates real-world web development skills including backend logic, database integration, and responsive frontend design.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Custom UI** | Dark Umbrella Corporation themed interface |
| 📱 **Responsive Design** | Works on desktop, tablet, and mobile |
| 🗄️ **MySQL Database** | Full database integration for dynamic content |
| 🔐 **Django Backend** | Secure and scalable Python backend |
| ☁️ **Cloud Deployed** | Live on Railway — always accessible |
| 🧟 **RE Content** | Resident Evil franchise fan content |

---

## 🛠 Tech Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.11 | Core backend language |
| ![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white) | 4.x | Web framework |
| ![MySQL](https://img.shields.io/badge/-MySQL-4479A1?logo=mysql&logoColor=white) | 8.x | Database |
| ![HTML](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white) | 5 | Page structure |
| ![CSS](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white) | 3 | Styling & animations |
| ![Railway](https://img.shields.io/badge/-Railway-0B0D0E?logo=railway&logoColor=white) | — | Cloud hosting |

---

## 📂 Project Structure

resident-evil-site/
│
├── 📁 resite/                  # Main Django project folder
│   ├── ⚙️  settings.py         # Django configuration
│   ├── 🌐 urls.py              # URL routing
│   ├── 🚪 wsgi.py              # WSGI entry point
│   └── 📁 apps/                # Django applications
│       ├── 🏠 templates/       # HTML templates
│       ├── 🎨 static/          # CSS, JS, images
│       └── 🗄️  models.py       # Database models
│
├── 🚂 Procfile                 # Railway deployment config
└── 📖 README.md                # Project documentation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- MySQL Server
- pip

### 1. Clone the repository
```bash
git clone https://github.com/hojiakbaroktamov89-cpu/resident-evil-site.git
cd resident-evil-site/resite
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure database
Open `settings.py` and update:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` 🎉

---

## ☁️ Deployment on Railway

This project is deployed on [Railway.app](https://railway.app) with MySQL database.

### Deploy your own:
1. Fork this repository
2. Go to [railway.app](https://railway.app) → **New Project**
3. Add **MySQL** plugin
4. Connect your GitHub repo
5. Add environment variables:
SECRET_KEY=your_django_secret_key
DB_NAME=railway
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=your_railway_mysql_host
DB_PORT=3306

6. Deploy! ✅

---

## 🎯 What I Learned

- ✅ Full-stack web development with Django
- ✅ Database design and MySQL integration
- ✅ Frontend development with HTML & CSS
- ✅ Cloud deployment with Railway
- ✅ Git version control workflow
- ✅ Environment variable management
- ✅ Responsive web design principles

---

## 🔗 Related Projects

| Project | Description | Link |
|---------|-------------|------|
| 🤖 **RE Telegram Bot** | Telegram bot about RE universe | [View](https://github.com/hojiakbaroktamov89-cpu/resident-evil-bot) |
| 🌐 **RE Website** | This project | [View](https://github.com/hojiakbaroktamov89-cpu/resident-evil-site) |

---

## 👨‍💻 Developer

<div align="center">

### Hojiakbar Oktamov

[![GitHub](https://img.shields.io/badge/GitHub-hojiakbaroktamov89--cpu-181717?style=for-the-badge&logo=github)](https://github.com/hojiakbaroktamov89-cpu)
[![Telegram](https://img.shields.io/badge/Telegram-@NOOB__comeback-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/NOOB_comeback)

*"just young creator"*

</div>

---

<div align="center">

**Made with ❤️ and Django**

*⭐ Star this repo if you like it!*

🌐 **[Visit Live Site](https://resident-evil-site-production.up.railway.app)**

</div>

## 📊 Language Stats
