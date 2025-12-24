📚 Book Port

Buy, sell, and exchange books effortlessly

Book Port is a Django-based web application designed as the foundation for a real-world book marketplace and exchange platform. It allows users to browse a curated catalogue of books, enquire about availability, and suggest new titles, while administrators manage inventory, categories, and incoming requests through a structured backend.

This project focuses on clean architecture, scalable patterns, and practical Django features rather than demo-only functionality.


✨ Key Features
Public Experience

Browse books with pagination

Search by title or author

Filter by availability and category

Detailed book pages with pricing and status

Submit enquiries for specific books

Suggest new books for review

Consistent, responsive UI with modern styling


✨ Admin & Backend

Full CRUD management of books via Django Admin

Category management (many-to-many)

Track and review book enquiries

Moderate book suggestions with status workflow

Admin search, filters, and optimized list views



🧠 Technical Highlights

Clean separation of concerns (models, views, templates)

Class-Based Views (ListView, DetailView, CreateView)

Reusable template structure with inheritance

ModelForms with validation and custom widgets

Custom Django Admin configuration

Pagination, filtering, and query optimization

Production-oriented UI consistency 


🛠 Tech Stack

Backend: Django 5.x (Python)

Database: SQLite (development)

Frontend: Django Templates (DTL), HTML5, CSS3

Forms: Django ModelForms

Views: Class-Based Views

Admin: Customized Django Admin

Styling: Custom CSS (modern, dark-themed UI)


⚙️ Setup (Local Development)

git clone https://github.com/hasnathg/mylibrary_project
cd mylibrary_project

python -m venv venv
venv\Scripts\activate   # Windows

pip install django

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Open: http://127.0.0.1:8000/



🗺 Roadmap

User authentication & seller accounts

Image uploads (media storage)

Book exchange workflows

Book condition & location metadata

Automated tests

REST API (Django REST Framework)



👤 Author

Md Hasnath Karim
Frontend / Full-Stack Software Developer (UK)

LinkedIn: https://www.linkedin.com/in/md-hasnath-karim/

GitHub: https://github.com/hasnathg