# College Paper Evaluation Platform 🎓

A comprehensive web-based platform built with Flask for managing academic evaluations in educational institutions. This system facilitates the management of question papers, subjects, and evaluators with role-based access control.

## 🚀 Features

### Admin Panel
- **Evaluator Management**: Add, edit, and manage evaluator accounts
- **Subject Management**: Create and organize academic subjects by department and semester
- **Question Paper Management**: Upload, review, and approve question papers
- **Dashboard**: Overview of system statistics and pending approvals

### Evaluator Portal
- **Subject Access**: View assigned subjects and related materials
- **Question Bank**: Access to approved question papers by subject
- **Profile Management**: Update personal information and credentials

### Security & Authentication
- Role-based access control (Admin/Evaluator)
- Secure session management
- User authentication and authorization

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, JavaScript with Bootstrap
- **Migration**: Flask-Migrate for database versioning
- **Authentication**: Flask sessions

## 📁 Project Structure

```
├── app.py                          # Main Flask application
├── config/                         # Configuration files
├── db/                            # Database models and utilities
├── blueprints/                    # Flask blueprints (routes)
│   ├── auth_routes/              # Authentication routes
│   ├── admin_routes/             # Admin panel routes
│   └── evaluator_routes/         # Evaluator panel routes
├── templates/                     # HTML templates
├── static/                        # CSS, JS, and static assets
├── migrations/                    # Database migration files
└── datastore/                     # SQLite database storage
```

## 🔧 Setup Instructions

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd cp-evaluation-platform-python
```

### 2. Set up Virtual Environment
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
```

### 5. Database Setup
Initialize and create the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the Application
```bash
# Development mode
flask --app app run --debug

# Or simply
python app.py
```

### 7. Access the Application
Open your browser and navigate to: [http://localhost:5000](http://localhost:5000)

## 👥 Default Login Credentials

The system creates a default admin account on first run:
- **Email**: Check the `db/default_admin.py` file for credentials
- **Role**: Admin

## 🗂️ Database Models

### User Model
- Stores admin and evaluator information
- Fields: email, password, role, name, department, designation, phone

### Subject Model  
- Academic subjects with department and semester info
- Fields: code, name, description, department, semester

### Question Paper Model
- Question paper storage with file uploads
- Fields: title, subject, exam_date, duration, marks, status

## 🔄 Database Migration Commands

```bash
# Initialize migrations (first time only)
flask db init

# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations to database
flask db upgrade

# Rollback to previous migration
flask db downgrade
```

## 📝 Usage Guidelines

### For Administrators
1. Login with admin credentials
2. Manage evaluators through the evaluator management panel
3. Create and organize subjects by department
4. Review and approve uploaded question papers
5. Monitor system activity through the dashboard

### For Evaluators
1. Login with evaluator credentials
2. Access assigned subjects
3. View and download approved question papers
4. Update profile information as needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is developed as part of academic coursework.

## 🐛 Troubleshooting

### Common Issues

**Database not found error:**
```bash
flask db upgrade
```

**Module not found error:**
```bash
pip install -r requirements.txt
```

**Port already in use:**
```bash
flask run --port 5001
```

## 📞 Support

For technical support or questions about this evaluation platform, please create an issue in the repository or contact the development team.
