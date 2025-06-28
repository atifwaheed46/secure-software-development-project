# 📦 Flask Students App – CRUD + Login + Docker

This project is a secure, responsive, and Dockerized web application built with the Flask framework. It was developed as part of a semester project for the course **Secure Software Design and Development (SSDD)**. The application allows users to register, log in, and perform full CRUD (Create, Read, Delete) operations on student data in a secure environment. The UI is styled using Bootstrap 5 and additional custom CSS.

---

## 🎯 Objective

- Enhance an existing Flask CRUD application with secure authentication
- Improve the user interface and usability using Bootstrap 5
- Enforce strong password policies and input validation
- Add session-based user login with automatic session expiry
- Containerize the application using Docker for platform independence

---

## 🧱 Project Structure

```
flask-students-app/
├── app.py                 # Main Flask app logic with all routes and session handling
├── requirements.txt       # Flask dependency for pip installation
├── Dockerfile             # Instructions to build Docker container
├── .dockerignore          # Prevents unnecessary files from being added to Docker image
├── README.md              # Documentation and setup guide
├── templates/             # HTML files using Jinja2 templating engine
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── form.html
└── static/
    └── style.css          # Custom styles applied across pages
```

---

## 🧪 Technologies Used

- **Python 3.8** – Core programming language
- **Flask 2.2.5** – Lightweight web framework for Python
- **Bootstrap 5** – Frontend framework for responsive UI
- **Docker** – Container platform to isolate the app
- **Jinja2** – Template engine used with Flask

---

## 🚀 How to Run the Project

### 🧑‍💻 Option 1: Run Locally (without Docker)

#### Step 1 – Install Flask:

```bash
pip install flask
```

#### Step 2 – Run the App:

```bash
python app.py
```

#### Step 3 – Visit in Browser:

```
http://localhost:5000
```

---

### 🐳 Option 2: Run with Docker (Recommended)

#### Step 1 – Build the Docker Image:

```bash
docker build -t flask-students-app .
```

#### Step 2 – Run the Docker Container:

```bash
docker run -p 5000:5000 flask-students-app
```

#### Step 3 – Open in Browser:

```
http://localhost:5000
```

---

## 🔐 Security Features

### 1. Authentication & Access Control

- Login and registration implemented using Flask sessions
- Protected routes require authentication (e.g. student list, add, delete)
- Unauthorized access attempts redirect users to login page

### 2. Session Management

- Sessions are secured with Flask’s `secret_key`
- Timeout enforced via:

```python
app.permanent_session_lifetime = timedelta(minutes=10)
```

- Users are automatically logged out after 10 minutes of inactivity

### 3. Password Strength Enforcement

- Minimum 8 characters
- At least one uppercase, one lowercase, one number, one special character
- Enforced via regex in both `register.html` and `app.py`

### 4. Input Validation

- **Client-side** validation using HTML5 (`required`, `type`, `pattern`)
- **Server-side** validation using regex in Flask to protect backend
- Invalid or unsafe data is rejected with flash messages

### 5. Docker Isolation

- The app runs inside a Docker container isolated from host system
- Image includes only necessary files via `.dockerignore`

---

## ✨ Features

| Feature             | Description                                                 |
| ------------------- | ----------------------------------------------------------- |
| CRUD Operations     | Add, list, and delete students                              |
| Responsive UI       | Designed using Bootstrap 5 and custom CSS                   |
| Flash Messages      | Inform users about actions (login, logout, errors, success) |
| Form Validation     | Validates all user input before processing                  |
| Session Expiry      | Users auto-logged out after 10 minutes of inactivity        |
| Password Validation | Enforces strong password policy at registration             |
| Docker Support      | Build, run, and share the app easily via Docker             |

---

## 🛠️ Share the Docker Image with Others

#### Step 1 – Save the Image:

```bash
docker save -o flask-students-app.tar flask-students-app
```

#### Step 2 – Send the `.tar` file via USB, Google Drive, etc.

#### Step 3 – On your friend’s system:

```bash
docker load -i flask-students-app.tar

docker run -p 5000:5000 flask-students-app
```

They can now open it in their browser:

```
http://localhost:5000
```

---

---

## 💻 How to Set Up Docker in WSL (Ubuntu)

If you're using Docker inside Windows Subsystem for Linux (WSL) with Ubuntu, follow these steps to install and configure Docker correctly:

### ✅ Step 1: Update package index

```bash
sudo apt update && sudo apt upgrade -y
```

### ✅ Step 2: Install required packages

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
```

### ✅ Step 3: Add Docker’s official GPG key

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### ✅ Step 4: Add the Docker repository

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### ✅ Step 5: Install Docker Engine

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

### ✅ Step 6: Start Docker and enable it on boot

```bash
sudo service docker start
sudo systemctl enable docker
```

### ✅ Step 7: Run Docker without `sudo` (optional)

```bash
sudo usermod -aG docker $USER
newgrp docker
```

You can now run Docker commands in WSL Ubuntu like this:

```bash
docker run hello-world
```

✅ You are ready to build and run your Flask Docker app inside WSL.

---

## 📊 Testing and Validation

### 🔍 Manual Testing

- Each route was tested using form input with valid and invalid data.
- Registration attempts with weak passwords were blocked both client- and server-side.
- Redirects were tested to ensure login protection works correctly.
- Session timeout was simulated by waiting 10+ minutes and refreshing.

### ✅ Test Cases

| Action                  | Expected Result                                             |
| ----------------------- | ----------------------------------------------------------- |
| Visit `/` without login | Redirect to `/login`                                        |
| Register weak password  | Show error message (e.g. must include symbols, digits, etc) |
| Add student (invalid)   | Flash input validation message                              |
| Inactivity for 10 mins  | Redirected to login on refresh                              |
| Run container           | Flask app should start on `localhost:5000`                  |

📸 **Screenshots to Include:**

- Login page redirect on protected route access
- Invalid input message for name/email/age
- Weak password rejection during registration
- Terminal output for Docker build & run
- Web UI (form, list, login, registration)

---

## 📚 Future Improvements

- Add SQLite database to persist student and user data
- Add edit/update student record feature
- Deploy on Heroku, Render, or Railway
- Implement role-based access control (RBAC)
- Add password hashing (e.g. using `werkzeug.security`)

---

## 👨‍💻 Author Info

- **Student**: Atif Waheed
- **Course**: Secure Software Design and Development (SSDD)

