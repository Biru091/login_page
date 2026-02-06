- **User Registration**
  - Create an account with username, email, and password
  - Password confirmation to avoid mistakes
  - Checks for duplicate usernames
  - Secure password hashing

- **User Login**
  - Authenticate users with username and password
  - Shows appropriate error messages:
    - Username does not exist
    - Incorrect password
  - Redirects to a protected main page after successful login

- **Security**
  - CSRF protection for all POST forms
  - Uses Django's built-in authentication system
  - Passwords stored securely using hashing
