
 FINAL PROJECT CAPSTONE – Tool Manager


Why this project is sufficiently distinct from previous projects

This project is not a variation of the e-commerce (Project 2), social network (Project 4), or any other previous project. Unlike the prior assignments, this application focuses tool management

OWNERSHIP
  .Each tool is owned by the user who created it. Only the owner can edit or delete a tool.
  .Only authenticated users can create a tool
Custom tool attributes 
  Tools have fields like `Description` , `product name`, and `id`.
  The home page shows notjust a list of tools  but also counts of tools.


Why this project meets the complexity requirement

 .Responsive UI – Uses Bootstrap 5 with a custom CSS file for consistent styling across devices.

How to Run the Project

1.Clone the repository 
   `git clone https://github.com/kellysimiyu/web50/projects/2020/x/capstone`

2.Navigate into the project folder  
   `cd capstone`

3.activate a virtual environment  
   source venv/bin/activate    
Install dependencies
 pip install django ,pillow 
 
Run migrations

python manage.py makemigrations
python manage.py migrate
Create a superuser 
python manage.py createsuperuser

Start the development server
python manage.py runserver

Visit http://127.0.0.1:8000

Authentication & Features
 .Users must register and log in to view tools.

 .Unauthenticated users only see a login/register prompt.

 .The Account page shows the  name of the logged in user  and email address 



