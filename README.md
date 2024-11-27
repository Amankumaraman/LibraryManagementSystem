# Library Management System with MongoDB and Cookie-Based Authentication

## Overview

This is a Library Management System built using **Django** and **MongoDB** as the database. It includes features such as role-based access control, cookie-based authentication with a "Remember Me" feature, and the ability to perform CRUD operations on books. Admin users have full access, while members can only view available books.

## Features

- **Roles & Permissions**:
  - **Admin**: Full CRUD operations on books and file uploads.
  - **Member**: Can only view the list of books and download them.
  
- **Authentication**:
  - Cookie-based authentication with "Remember Me" functionality.
  - Sessions last 7 days when "Remember Me" is selected; otherwise, they expire after the browser is closed.
  
- **Database**:
  - MongoDB for storing data.
  - **Users** collection: Stores usernames, passwords, and roles (Admin or Member).
  - **Books** collection: Stores book details (title, author, description) and file uploads.

- **Endpoints**:
  - Admins can add, update, and delete books.
  - Members and admins can view the list of books and download individual books.

## Requirements

1. **Python 3.x**  
2. **Django**  
3. **djongo** (Django-MongoDB connector)  
4. **MongoDB** (as the database)

### Installing Dependencies

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/library-management-system.git
    cd library-management-system
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install MongoDB**:
   - Make sure you have MongoDB installed and running on your machine. If not, follow the [installation guide](https://docs.mongodb.com/manual/installation/).

---

## Configuration

1. **Database**:  
   The project uses MongoDB. You can configure your database connection in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'library_db',
       }
   }
