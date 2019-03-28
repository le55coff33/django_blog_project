# Django Blog project
Small and simple blog-like project which has helped me to get started and learn how to get things done with Django.

![alt text](https://github.com/le55coff33/django_blog_project/blob/master/image.png)

When I was creating this project I was focused only on backend side of the project. I have learned how to:
- handling request-response flow
- dealing with Model View Template architectural pattern
- dealing with forms
- creating function based views and generic class based views
- working with forms
- handling Django's signals

#### This project is not intended for production.

## Features
1. Registration of new users
2. Extended User Model
3. Every logged user can:
- Add posts and comments
- Edit and Delete their own posts and comments
4. Flash messages (Create, Update, Delete posts and comments)

## To do
- Tests
- Upgrade profile page
- Ability to follow other users

## Getting Started
1. Install Python 3.7.2
2. Clone this repository: `git clone https://github.com/le55coff33/django_blog_project.git`
3. Go into project directory: `cd django_blog_project`
4. Install virtualenv: `$pip install virtualenv`
5. Create a new virtualenv: `$virtualenv name_of_virtualenv`
6. Activate new virtualenv: change directory to `$cd name_of_virtualenv/scripts` and then `$activate`
7. Install the required packages: `$pip install -r requirements.txt`
8. Run migrations: `$python manage.py migrate`
9. Run development server `$python manage.py runserver`
10. You should see blog-home page at `http://localhost:8000/` At this point the database is empty.
