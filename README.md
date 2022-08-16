# Um What Day Is It?
Because seriously, what day is it? Live at https://rest-backend.umwhatdayisit.com/

## Background
In early 2020 I built this side project to capture how a lot of people were feeling during the pandemic. The original project was built using one of my favorite static website generators called Gatsby.

I recently revisited this project and decided to write a new backend using a stack that I didn't have much experience with. I chose to build the REST API with Django, a Python web framework, and MongoDB as the database. I chose these because they are two technologies that I have heard about quite often and sometimes see on job listings.

## API
I built the API using the [Django REST Framework](https://www.django-rest-framework.org/) with routes to perform all the basic CRUD operations.

### Routes
- POST: /api/content/
- GET: /api/content/
- PUT: /api/content/`<id>`/
- DELETE: /api/content/`<id>`/

### Hosting
The backend is deployed on Heroku and the endpoints are called from the frontend. The frontend was modified to call the REST API to source data. You can [learn more about those changes here.](https://github.com/levibrooke/um-what-day-is-it/tree/rest-backend)
