# Recipe App with React.js Frontend and Django Backend

This project demonstrates the development of a Recipe Management App using a React.js frontend and a Django backend. The frontend is deployed on AWS S3, while the backend is hosted on AWS EC2. The application features CRUD operations for managing recipes, with data served through API endpoints created with Django and consumed by the React.js frontend.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup (Django)](#backend-setup-django)
  - [Frontend Setup (React.js)](#frontend-setup-reactjs)
- [Deployment Instructions](#deployment-instructions)
  - [Deploying Frontend to AWS S3](#deploying-frontend-to-aws-s3)
  - [Deploying Backend to AWS EC2](#deploying-backend-to-aws-ec2)
- [API Endpoints](#api-endpoints)


## Project Overview

The Recipe Management App is a simple web application that allows users to add, update, and delete recipes. The frontend, built with React.js, communicates with a Django backend to perform these operations. The app is fully deployed using AWS services, ensuring it is accessible to the public.

## Technologies Used

- **Frontend**: React.js
- **Backend**: Django
- **Deployment**: AWS S3 (Frontend), AWS EC2 (Backend)

## Features

- **Fetch and Display Recipes**: View a list of all recipes.
- **Add New Recipes**: Submit a form to add a new recipe to the list.
- **Update Existing Recipes**: Edit details of an existing recipe.
- **Delete Recipes**: Remove a recipe from the list.

## Project Structure

```plaintext
simple-recipe-app/
├── backend/
│   ├── manage.py
│   ├── api/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   └── simple_recipe/
│       ├── settings.py
│       ├── urls.py
│       └── ...
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── RecipeList.js
│   │   │   ├── RecipeForm.js
│   │   │   ├── RecipeItem.js
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│   └── ...
└── README.md
```

# Setup Instructions

## Backend Setup (Django)

1. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver


## Frontend Setup (React.js)
```bash
cd frontend
npm install
npm start
```

## Deploying Frontend to AWS S3
Build the React app for production:
upload the build files to an S3 bucket:

- Create an S3 bucket using the AWS Management Console.
- Upload the contents of the build directory to the bucket.
- Configure the bucket for static website hosting.
- Set the bucket policy to allow public access.

**Configure the S3 bucket for static website hosting**:

- Set the index document to index.html.
- Ensure that all files are publicly accessible.

## Deploying Backend to AWS EC2
   Launch an EC2 instance:

- Use the "Ubuntu Server 20.04 LTS" AMI.
- Select the t2.micro instance type.
- Configure the security group to allow HTTP (port 80) and SSH (port 22).
- Connect to the EC2 instance and set up the environment.
- Clone the project and set up the virtual environment.
- Set up Gunicorn and Nginx for production.

## API Endpoints
- **GET** /api/recipes/: Fetch all recipes.
- **POST** /api/recipes/: Add a new recipe.
- **PUT** /api/recipes/<id>: Update a recipe.
- **DELETE** /api/recipes/<id>/: Delete a recipe.



