# Django User Management Application

A complete, production-ready Django web application for collecting, storing, and managing user information.

## ✨ Features

- ✅ Collect user information (Name, Email, Phone, Address)
- ✅ Store in SQLite database
- ✅ Display users in professional list
- ✅ View individual user profiles
- ✅ Create new users
- ✅ Edit existing users
- ✅ Delete users with confirmation
- ✅ Django admin panel
- ✅ Bootstrap 5 responsive UI

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/prince900max/Springer-API-project.git
cd Springer-API-project

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

Visit: http://localhost:8000/users/

## 📁 Structure

```
├── config/          (Django settings)
├── users/           (Main app)
│   ├── migrations/
│   ├── templates/   (5 HTML templates)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── manage.py
└── requirements.txt
```

## 🔧 Technologies

- Django 4.2+
- SQLite3
- Bootstrap 5
- Python 3.8+

## 📊 User Model

- name (required)
- email (required, unique)
- phone (optional)
- address (optional)
- created_at (auto timestamp)
- updated_at (auto timestamp)

## 🌐 URLs

- `/users/` - List all users
- `/users/create/` - Create user
- `/users/<id>/` - View user
- `/users/<id>/edit/` - Edit user
- `/users/<id>/delete/` - Delete user
- `/admin/` - Admin panel

## 📚 Documentation

Comprehensive documentation included in the repository with setup guides and architecture details.

## 🔐 Security

- CSRF protection
- Email validation
- SQL injection safe (Django ORM)
- XSS protection
- Delete confirmation

Happy coding! 🚀