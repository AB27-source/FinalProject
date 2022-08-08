# Web-based version of apple notes

## Inspiration:
I chose to make a simplified web-based version of the apple notes app so I can have my notes organized and at my disposal no matter what platform I am on.

## How to Use:
1. Go to [NotesApp](https://angad-notes-app.herokuapp.com/)
2. Register for an account on bottom right of page if you do not have a login
3. Once registered, click on the ' + ' on the bottom right of the page to create a new note
4. On the new note page add the title of your note and its content. Then click save.
5. The search bar found on the top of the page can be used to search for a note using the title.
6. click logout on the on the top right of the page to sign out


## Technologies used:
To make this application I used Django framework along with a couple python libraries such as gunicorn and django-on-heroku to deploy my application on heroku.
Most of the files for the application where auto-generated using the command **django-admin startproject**
I created an sqlite model for my notes page that has fields for user, title, body, and created. Next I have class based views for different components for my site such as the login page, RegisterPage, PageList, PageDetail, CreatePage, UpdatePage, and DeletePage.
The user login and registration is handled by the Django authentication system. I used the default forms to handle the user logins and registerations and its stored within the django created models.