# GlobalGiGs - Job Portal Web Application

## Distinctiveness and Complexity

GlobalGiGs is a job portal web application that stands apart from previous course projects in several significant ways. Unlike Project 2 (Commerce), which focuses on auction listings and bidding, GlobalGiGs creates a job marketplace where users can post and browse job opportunities. This is fundamentally different from Project 4 (Network), which is essentially a social media platform, whereas GlobalGiGs is a professional job listing service.

The complexity of GlobalGiGs is demonstrated through its complete user authentication system and personalized user profiles. The application features a Job model with fields including Title, Description, Location, and Price, all linked to users through a foreign key relationship. The project implements a full authentication system with registration, login, and logout functionality, along with a user profile page that displays personal information and user statistics.

The front-end implementation showcases JavaScript-powered features that enhance user experience, including a dynamic heading changer and interactive elements that respond to user actions. These JavaScript features work seamlessly with the Django back-end, creating a responsive and engaging user interface.

The project also incorporates Django features including custom form handling with validation, proper URL routing with named URL patterns, and user authentication with session management. The use of inline styling throughout the templates demonstrates a consistent design approach while keeping the code structure clean and maintainable.

## Files and Directories

### Project Root
- `manage.py` - Django's command-line utility for administrative tasks
- `requirements.txt` - Lists all Python dependencies needed to run the application
- `README.md` - This comprehensive documentation file

### Configuration Files
- `capstone/settings.py` - Django project settings including database configuration, installed apps, and middleware
- `capstone/urls.py` - Main URL routing configuration that includes the jobs app URLs
- `capstone/wsgi.py` - WSGI configuration for deployment

### Jobs Application
- `jobs/models.py` - Contains the database models:
  - `Jobs` - Main model storing job listings with Title, Description, Price, Location, and posted_by fields
  - `posted_by` - Foreign key linking jobs to users who posted them

- `jobs/views.py` - Contains all view functions:
  - `index()` - Renders the homepage displaying all available jobs
  - `detail()` - Shows detailed information for a specific job
  - `new()` - Handles the creation of new job listings with form validation and user association
  - `login_view()` - Authenticates users and logs them into the system
  - `logout_view()` - Logs users out of the system
  - `register()` - Creates new user accounts with validation
  - `profile()` - Displays a personalized profile page for authenticated users

- `jobs/urls.py` - URL routing specific to the jobs app with named URL patterns and app namespace
- `jobs/forms.py` - Contains the NewJobsForm for creating job listings with validation

### Templates
- `jobs/templates/jobs/layout.html` - Base template with common HTML structure and navigation bar
- `jobs/templates/jobs/index.html` - Homepage displaying all job listings in styled cards
- `jobs/templates/jobs/detail.html` - Detailed view of individual job listings
- `jobs/templates/jobs/new.html` - Form page for adding new job listings
- `jobs/templates/jobs/login.html` - User login page with authentication form
- `jobs/templates/jobs/register.html` - User registration page with validation
- `jobs/templates/jobs/profile.html` - User profile page displaying personal information and posted jobs

## Features

### User Authentication System
- **Registration**: Users can create new accounts with username, email, and password
- **Login/Logout**: Secure authentication system with session management
- **User Profile**: Personalized profile page showing user information
- **User Association**: All jobs are linked to the user who posted them

### Job Management
- **Browse Jobs**: All users can view available job listings on the homepage
- **Job Details**: Click on any job to view complete information
- **Post Jobs**: Authenticated users can post new job listings
- **Job Cards**: Each job displays Title, Description, Location, and Price

### User Profile
- **Personal Information**: Displays username, email.


### Interactive Features
- **JavaScript Heading Changer**: Interactive button to change page heading
- **Welcome Alert**: Personalized welcome message on page load
- **Responsive Navigation**: Navbar adapts based on user authentication status
- **Inline Styling**: Consistent design approach using inline CSS

## How to Run the Application

### Prerequisites
- Python 3.8  installed on your system
- pip package manager
- Virtual environment 

### Installation Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd capstone




User Guide
Registration and Login
Click "Register" in the navigation bar

Fill in username, email, and password

Click "Register" to create your account

You will be automatically logged in

The navigation bar will update to show your username

Profile Page
After logging in, click "Profile" in the navigation bar

View your personal information (username, email)


Posting a Job
Click "Post" in the navigation bar

Fill in the job details (Title, Description, Location, Price)

Click "Submit" to post the job

The job will appear on the homepage and in your profile

Viewing Jobs
All jobs are displayed on the homepage

Click on any job title to view full details

The detail page shows complete job information

Technology Stack
Backend: Django

Database: SQLite 

Frontend: HTML5, CSS3, JavaScript 

Styling: Inline CSS 

Form Handling: Django forms with built-in validation

Authentication: Django's built-in authentication system

