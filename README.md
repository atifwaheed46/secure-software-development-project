# Flask Students CRUD App with Login and Docker

## 📌 Description

This project is a secure, containerized Flask web application that allows authenticated users to manage student data. It features:

- User **Registration and Login**
- **CRUD** operations on student records
- Responsive UI with **Bootstrap 5**
- Input validation (client and server-side)
- **Dockerized** for platform-independent deployment

---

## 🧰 Technologies Used

- Python 3.8
- Flask 2.2.5
- Bootstrap 5 (CDN)
- Docker

---

## 🚀 Features

- ✅ User Registration (`/register`)
- ✅ User Login (`/login`)
- ✅ Session-based Authentication
- ✅ Add / View / Delete Student Data
- ✅ Flash Messages for UX Feedback
- ✅ Client + Server Side Validations
- ✅ Runs inside Docker Container

---

## 🖥️ Local Setup (Without Docker)

### 1. Install Flask (First time only)

```bash
pip install flask

so how to stup the docker  ? 

Setting Up Docker (Windows & Ubuntu WSL2)
Since most students use Windows, Docker is installed via WSL2 (Windows Subsystem for Linux).

✨ Step-by-step Instructions (from your lab):
✅ Step 1: Enable WSL2
Run this in PowerShell (Admin):

powershell

-dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
-dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
Then restart your PC.

✅ Step 2: Install Ubuntu
After restart, run:


-wsl --install -d Ubuntu
If there's a problem, update the kernel:
WSL2 Kernel Update MSI

✅ Step 3: Install Docker inside Ubuntu (WSL2)
Open Ubuntu terminal and run these commands:


-sudo apt-get update
-sudo apt-get install ca-certificates curl gnupg
-sudo install -m 0755 -d /etc/apt/keyrings
-curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
-sudo chmod a+r /etc/apt/keyrings/docker.gpg
Add Docker repository:


-echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
-https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
-sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

s-udo apt-get update
Now install Docker:


-sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
✅ Step 4: Verify Docker is Working
Run:


-sudo docker run hello-world
If it prints a welcome message, Docker is working! 🎉

🧪 PART 3: Running and Exploring Containers
🚀 Run a simple container:

docker run busybox echo "Hello from BusyBox"
This:

Downloads a small Linux image called busybox

Runs the echo command in it

Exits

📂 Interactive Mode:

-docker run -it busybox sh
Now you’re inside the container. Try:


-ls
-uptime
Exit with: exit

🧹 Clean Up Containers
To view exited containers:


-docker ps -a
To delete:
-docker rm [container_id]
Delete all stopped containers:
-docker container prune
