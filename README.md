# Django Portfolio Website

A beautiful and responsive portfolio website built with Django, HTML, CSS, and JavaScript. Perfect for showcasing your projects and skills.

## Features

- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Project Showcase**: Display your projects with descriptions and links
- **Skills Section**: Highlight your technical skills with proficiency levels
- **Contact Form**: Simple contact form for visitors to reach out
- **Admin Panel**: Easy management of projects and skills through Django admin
- **Smooth Animations**: Beautiful CSS animations and transitions
- **Dark/Light Theme**: Modern color scheme

## Requirements

- Python 3.8 or higher
- Django 4.2.7
- SQLite (included with Django)

## Installation & Setup

### 1. Navigate to Project Directory

```bash
cd portfolio_project
```

### 2. Create a Virtual Environment (Recommended)

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

The website will be available at: **http://localhost:8000/**

## Using the Admin Panel

1. Go to **http://localhost:8000/admin/**
2. Log in with your superuser credentials
3. Add Projects and Skills
4. The homepage will automatically display your projects and skills

### Adding a Project:

1. Click "Projects" in the admin panel
2. Click "Add Project"
3. Fill in:
   - **Title**: Your project name
   - **Description**: Project details
   - **Technology**: Technologies used (e.g., Python, Django, React)
   - **Link**: (Optional) URL to your project
   - **Image URL**: (Optional) URL to project image

### Adding a Skill:

1. Click "Skills" in the admin panel
2. Click "Add Skill"
3. Fill in:
   - **Name**: Skill name (e.g., Python, JavaScript, Django)
   - **Proficiency**: Percentage (0-100%)

## Project Structure

```
portfolio_project/
├── portfolio/                    # Django app
│   ├── migrations/              # Database migrations
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # Main stylesheet
│   │   └── js/
│   │       └── script.js        # JavaScript functionality
│   ├── templates/portfolio/     # HTML templates
│   │   ├── index.html           # Homepage
│   │   └── project_detail.html  # Project detail page
│   ├── admin.py                 # Admin configuration
│   ├── models.py                # Database models
│   ├── views.py                 # Views logic
│   ├── urls.py                  # URL routing
│   └── apps.py                  # App configuration
├── portfolio_site/              # Django project settings
│   ├── settings.py              # Configuration
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # WSGI configuration
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database
└── requirements.txt             # Python dependencies
```

## Customization

### Change Site Colors

Edit [portfolio/static/css/style.css](portfolio/static/css/style.css) and modify the CSS variables:

```css
:root {
    --primary-color: #3498db;       /* Main color */
    --secondary-color: #2c3e50;     /* Text color */
    --accent-color: #e74c3c;        /* Highlight color */
    --text-color: #333;             /* Text color */
    --light-bg: #ecf0f1;            /* Light background */
    --white: #fff;                  /* White color */
    --dark-bg: #2c3e50;             /* Dark background */
}
```

### Customize Content

Edit [portfolio/templates/portfolio/index.html](portfolio/templates/portfolio/index.html) to change:
- Hero section text ("Hello, I'm Developer")
- Section titles
- Footer information
- Social media links

### Modify Functionality

Edit [portfolio/static/js/script.js](portfolio/static/js/script.js) to add:
- Email integration for contact form
- Additional animations
- More interactive features

## Adding Static Images

1. Create a folder for images: `portfolio/static/images/`
2. Add your images to that folder
3. Reference them in templates: `{% static 'images/your-image.jpg' %}`

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, run:

```bash
python manage.py runserver 8080
```

Then access the site at **http://localhost:8080/**

### Database Issues

To reset the database:

```bash
# Delete db.sqlite3
rm db.sqlite3  # On macOS/Linux
del db.sqlite3  # On Windows

# Re-run migrations
python manage.py migrate
```

### Static Files Not Loading

Run:

```bash
python manage.py collectstatic
```

## Deployment

For production deployment, refer to Django's deployment checklist:
- Change `DEBUG = False` in settings.py
- Set `ALLOWED_HOSTS` properly
- Use a production database (PostgreSQL recommended)
- Set up proper security settings
- Use a production web server (Gunicorn, uWSGI)

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, feel free to create an issue in the repository.

---

Happy portfolio building! 🚀
