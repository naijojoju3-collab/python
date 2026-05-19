# Quick Start Guide

## For Windows Users

### Option 1: Using the Setup Script (Recommended)

1. Open PowerShell or Command Prompt
2. Navigate to the project folder:
   ```
   cd c:\Users\User\Desktop\TEST\portfolio_project
   ```

3. Run the setup script:
   ```
   .\setup.bat
   ```

4. Follow the prompts to create a superuser account

5. The server will start automatically at http://localhost:8000/

### Option 2: Manual Setup

1. Open PowerShell and navigate to the project:
   ```powershell
   cd "c:\Users\User\Desktop\TEST\portfolio_project"
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```powershell
   python manage.py migrate
   ```

4. Create a superuser:
   ```powershell
   python manage.py createsuperuser
   ```
   Then enter:
   - Username: (choose a username)
   - Email: (your email)
   - Password: (create a password)
   - Confirm password: (repeat the password)

5. Start the development server:
   ```powershell
   python manage.py runserver
   ```

---

## For macOS/Linux Users

1. Open Terminal and navigate to the project:
   ```bash
   cd ~/Desktop/TEST/portfolio_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## Access Your Portfolio

Once the server is running:

- **Website**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

---

## Add Your First Project

1. Go to http://localhost:8000/admin/
2. Log in with your superuser credentials
3. Click "Add Project" under the Projects section
4. Fill in:
   - Title: Your project name
   - Description: What the project does
   - Technology: Technologies used (e.g., "Python, Django")
   - Link: (Optional) Project link
   - Image URL: (Optional) Project image URL

5. Click Save

Your project will now appear on the homepage!

---

## Troubleshooting

### Port 8000 Already in Use?
```
python manage.py runserver 8080
```
Then access at http://localhost:8080/

### Module Not Found?
Make sure Django is installed:
```
pip install -r requirements.txt
```

### Database Error?
Reset the database:
```
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## Customizing Your Portfolio

- **Colors**: Edit `portfolio/static/css/style.css` (look for the `:root` section)
- **Content**: Edit `portfolio/templates/portfolio/index.html`
- **Functionality**: Edit `portfolio/static/js/script.js`

---

Enjoy your new portfolio website! 🚀
