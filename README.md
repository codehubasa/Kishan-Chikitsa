🌾 KisanChikitsa

🚜 Smart Agricultural Support & User Management System


📌 Overview
KisanChikitsa is a web application designed for user account management, allowing users to sign up and sign in to access various features related to agricultural support and information. It focuses on providing a secure, scalable, and user-friendly authentication system as the foundation for future agri-tech services.

✨ Key Features

🔐 User Registration & Authentication 
📱 Responsive Design (Mobile + Desktop) 
🛡️ Secure Password Handling & Validation 
⚡ Clean Django Backend Architecture 
🌐 Simple and Functional Frontend UI

⚙️ Backend

The backend is built using Django and contains the following components:

🔹 Core Files manage.py – Command-line utility for managing the Django project.

🔹 Main Project (kisan_chikitsa/) settings.py 

    Configuration settings for the Django project urls.py 
    
    URL routing for the project wsgi.py 
    
    Entry point for WSGI-compatible web servers

🔹 Accounts App (accounts/) models.py 

  Defines user account data models views.py 
  
  Contains logic for user registration and authentication serializers.py 
  
  Serializes user data for API responses urls.py 
  
  URL routing specific to account-related views
  
💻 Frontend

The frontend consists of HTML files for user interaction:

signup.html – User interface for creating a new account
signin.html – User interface for logging into an existing account

⚙️ Tech Stack

Layer Technology Backend Django Frontend HTML Database SQLite (default Django DB) API Layer Django REST Framework

🚀 Setup Instructions

1️⃣ Clone the Repository
git clone cd kisan-chikitsa

2️⃣ Create Virtual Environment python -m venv venv
Activate it:
Windows: venv\Scripts\activate Mac/Linux: source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python backend/manage.py migrate

5️⃣ Run Server
python backend/manage.py runserver

📍 Usage:

Navigate to http://localhost:8000/signup to create a new account.

Navigate to http://localhost:8000/signin to log into your account.

🎯 Future Scope (Optional Enhancements)

🌱 AI-based crop disease detection 
📊 Farmer dashboard & analytics
🌦️ Weather API integration 
💬 Chatbot for agricultural guidance


⭐ Why This Project Stands Out
Combines Agri-Tech + Web Development 
Clean separation of frontend & backend
Built with industry-relevant stack (Django) 
Strong base for scaling into a full AI-powered platform

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a new branch

Make your changes

Submit a Pull Request

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
