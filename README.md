GlobalGiGs – Job Portal Web Application

Overview
GlobalGiGs is a full‑stack job listing platform built with Django. It allows users to create an account, browse job opportunities, and post their own job listings. Each job includes a title, description, location, and price. The application features a personalized profile page where users can see all the jobs they have posted, alongside their account details.

The project is designed as a professional marketplace, distinct from the auction‑style bidding of Project 2 (Commerce) and the social‑media feed of Project 4 (Network). Instead, it offers a clean, business‑oriented interface for connecting service providers with potential clients.

Distinctiveness
GlobalGiGs is not a re‑skin of any previous CS50 Web project. It occupies a unique domain – a job board – which is fundamentally different from an auction house, an encyclopedia, an email client, or a social network.

Domain‑specific purpose: Whereas Commerce revolves around dynamic bidding and time‑limited auctions, GlobalGiGs is built around fixed‑price job postings. Users post a job with a clear price, and interested parties can view the details. There is no auction mechanism, no watchlist, and no bidding war – the focus is on straightforward service offerings.

User‑centric job management: Previous projects allowed users to create content (listings, posts, pages), but none provided a dedicated profile dashboard that aggregates a user’s own content in a structured way. In GlobalGiGs, every authenticated user has a profile page that lists only the jobs they have posted, along with their username and email. This gives users a clear overview of their activity and serves as a personal portfolio.

Interactive front‑end enhancements: While other projects used JavaScript for API calls or dynamic UI updates, GlobalGiGs integrates two distinctive client‑side features that improve usability: a dynamic heading changer (click a button to cycle through motivational messages) and a personalised welcome alert that greets the user by name upon login. These are not merely cosmetic – they demonstrate a conscious effort to make the interface engaging and responsive.

Tailored navigation: The navigation bar adapts intelligently based on authentication status. Unauthenticated visitors see “Register” and “Login”; authenticated users see their username, a “Profile” link, and a “Logout” button. This flow is simpler and more intuitive than the dual‑navigation systems seen in earlier projects.

In short, GlobalGiGs is a purposeful job‑listing ecosystem with a clean UI, personalised user spaces, and interactive front‑end touches that set it apart from the prior assignments.

Complexity
The project demonstrates significant complexity through the following aspects:

1. Custom Data Model with Relationships
The Jobs model is a custom Django model with five fields:

Title (CharField, max length 64)

Description (TextField)

Location (CharField, max length 64)

Price (IntegerField)

posted_by (ForeignKey to the built‑in User model, with on_delete=models.CASCADE)

This model is directly tied to Django’s authentication system, ensuring that every job is linked to its creator. This foreign‑key relationship is more complex than a simple one‑off model, as it requires careful handling in views to associate the current user with a new job.

2. Full Authentication Flow
The application implements a complete user authentication cycle: registration (with email validation), login, logout, and session management.

The registration view includes custom validation to ensure usernames are unique and passwords match.

Protected routes (e.g., posting a job) are guarded with the @login_required decorator, preventing unauthorised access.

3. CRUD Operations (Create & Read)
Create: The /new endpoint uses a Django ModelForm (NewJobsForm) with built‑in validation. Upon submission, the form saves a new Jobs instance, automatically assigning the posted_by field to the currently logged‑in user.

Read: The homepage (/) lists all jobs in a card‑based layout. The /detail/<int:job_id> route displays a full‑page view of a single job, pulling data via the primary key.

4. Personalised Profile Page
The /profile view is accessible only to logged‑in users. It retrieves the current user object and filters all jobs where posted_by matches that user.

The template displays the user’s username and email, followed by a list of their posted jobs – complete with titles, descriptions, prices, and locations. This aggregates data from two different tables (User and Jobs), demonstrating a many‑to‑one relationship.

5. JavaScript Interactivity
Two distinct JavaScript functions are included:

A heading changer that cycles through three pre‑defined phrases when a button is clicked.

A welcome alert that fires on page load, displaying a personalised greeting to the authenticated user (or a generic message to visitors).

These functions are triggered by DOM events and manipulate the page content dynamically, showing an understanding of client‑side scripting beyond simple form validation.

6. Django Best Practices
URL namespacing (app_name = "jobs") and named URL patterns are used throughout, making the code maintainable.

Templates inherit from a base layout.html using Django’s template inheritance, reducing repetition and centralising styling.

Inline styling is used consistently to maintain a cohesive visual theme without relying on external CSS frameworks (though this could be improved, it shows deliberate design choice).

Taken together, these features represent a substantial integration of Django’s ORM, authentication system, form handling, and template engine, combined with custom JavaScript – all of which exceeds the complexity of the course’s earlier projects.

File-by-File Breakdown
Below is a comprehensive description of every file I created or modified for this project.

Project Root
manage.py – Django’s command‑line utility. Used for running the server, making migrations, and interacting with the project. I did not modify this file.

requirements.txt – Lists all Python dependencies (Django, etc.). Ensures the project can be easily set up on any machine.

README.md – This document.

Configuration (capstone/)
capstone/settings.py – Contains project‑wide settings. I added 'jobs' to the INSTALLED_APPS list and configured the database (SQLite by default). No other core settings were changed.

capstone/urls.py – The main URL configuration. I included the line:

python
path('', include('jobs.urls'))
This routes all base‑URL requests to the jobs app, keeping the project root clean.

capstone/wsgi.py – Standard WSGI configuration for deployment. Not modified.

Jobs Application (jobs/)
Models (jobs/models.py)
Defines the single data model:

python
class Jobs(models.Model):
    Title = models.CharField(max_length=64)
    Description = models.TextField()
    Location = models.CharField(max_length=64)
    Price = models.IntegerField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")

    def __str__(self):
        return f"{self.Title} (by {self.posted_by})"
The related_name="jobs" allows easy reverse lookup from a User instance (e.g., user.jobs.all()).

The __str__ method provides a human‑readable representation for the admin interface.

Views (jobs/views.py)
Contains seven view functions:

index(request) – Retrieves all Jobs objects ordered by ID (or could be modified to order by date) and renders index.html with a context containing the list of jobs.

detail(request, job_id) – Uses get_object_or_404 to fetch a single job by its primary key. Passes the job object to detail.html.

new(request) – Handles both GET and POST.

On GET: displays an empty NewJobsForm.

On POST: validates the form; if valid, saves the job with commit=False, assigns posted_by = request.user, then saves to the database. Redirects to the job’s detail page.

Decorated with @login_required to restrict access.

login_view(request) – Authenticates using authenticate and login. If credentials are valid, redirects to index; otherwise, re‑renders login.html with an error message.

logout_view(request) – Calls logout and redirects to index.

register(request) – Creates a new user using User.objects.create_user. Validates that the username is not taken and that the password and confirmation match. On success, logs the user in and redirects to index.

profile(request) – Decorated with @login_required. Retrieves request.user and filters Jobs.objects.filter(posted_by=request.user). Passes the user object and the filtered job list to profile.html.

URL Configuration (jobs/urls.py)
Defines four URL patterns with names:

"" → index (name = "index")

"detail/<int:job_id>" → detail (name = "detail")

"new" → new (name = "new")

"login" → login_view (name = "login")

"logout" → logout_view (name = "logout")

"register" → register (name = "register")

"profile" → profile (name = "profile")

An app_name = "jobs" is set to enable namespacing (e.g., {% url 'jobs:index' %}).

Forms (jobs/forms.py)
Contains NewJobsForm, a ModelForm for the Jobs model:

python
class Meta:
    model = Jobs
    fields = ['Title', 'Description', 'Location', 'Price']
The posted_by field is intentionally excluded – it is set in the view. The form provides automatic validation for required fields and data types (e.g., Price must be an integer).


Templates (jobs/templates/jobs/)
All templates inherit from layout.html using {% extends "jobs/layout.html" %}.

layout.html – The base template. Contains:

HTML <head> with a consistent title.

A navigation bar (<nav>) with conditional links based on user.is_authenticated.

A {% block body %} placeholder for page‑specific content.

Inline CSS (within <style> tags) that defines colours, card styles, button appearances, and layout rules.

A JavaScript block at the bottom that defines two functions: changeHeading() and a window.onload welcome alert.

index.html – The homepage.

Extends layout.html.

Displays a list of all jobs using a for loop. Each job is rendered as a card with title, description, location, and price.

The title is a hyperlink to the job’s detail page.

detail.html – Shows a single job.

Displays all fields of the job in a clear, centred layout.

Includes a “Back to all jobs” link.

new.html – The job‑posting form.

Uses {{ form.as_p }} to render the Django form.

Contains a “Submit” button and a CSRF token.

login.html – Login form.

Username and password fields.

Displays an error message if authentication fails.

register.html – Registration form.

Username, email, password, and confirmation fields.

Inline validation messages (e.g., password mismatch) are handled in the view and passed via context.

profile.html – User profile.

Shows the user’s username and email.

Lists all jobs posted by that user, each with title, description, location, and price.

If the user has no jobs, a friendly message is shown.
 

How to Run the Application
Clone the repository and navigate to the project directory.

Create a virtual environment 


python3 -m venv venv
source venv/bin/activate  
Install dependencies:


pip install -r requirements.txt
Apply migrations:


python manage.py makemigrations
python manage.py migrate
Run the server:


python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.