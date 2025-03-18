
# 🔒 **Password Manager**

## 📌 **Project Overview**
The **Password Manager** is a full-fledged web application that allows users to securely store, retrieve, and generate strong passwords. The project is built with a **Flask backend (Python)** and a **beautifully designed frontend** using **HTML, CSS, and JavaScript**, making it both functional and visually appealing. It also features an **SQLite database** for storing password data securely, ensuring easy management of user credentials. 

---

## 📁 **Project Structure**

The project follows a modular and organized structure for better readability and maintainability:

```
password_manager/
├── app.py                      # Main Flask application (backend logic and routes)
├── database.py                  # Database handler (SQLite operations)
├── password_generator.py        # Random password generator logic
├── static/                      # Static files (CSS, JavaScript)
│   ├── css/
│   │   └── style.css            # Frontend styling (UI design)
│   └── js/
│       └── script.js            # Frontend interactivity and AJAX calls
├── templates/
│   └── index.html               # Main HTML file (user interface)
└── requirements.txt             # Python dependencies
```

---

## 🚀 **Features**

### ✅ **1. Store Password**
- Allows users to add new credentials, including **website name, username, and password**.  
- Uses **AJAX** to communicate with the backend, ensuring smooth, real-time interactions.  
- Credentials are stored securely in the **SQLite database**.  

### 🔍 **2. Retrieve Password**
- Users can search for stored credentials by **website name**.  
- The application fetches the matching username and password from the database.  
- Includes a **"copy to clipboard"** button for convenience.  

### 🔑 **3. Generate Password**
- A built-in **random password generator** creates strong passwords.  
- Users can specify **length and complexity** (uppercase, lowercase, digits, and special characters).  
- The generated password can be directly stored in the database.  

### 🎨 **4. Modern and Responsive UI**
- Beautiful, **mobile-friendly design** using **HTML, CSS, and JavaScript**.  
- **Smooth transitions** and stylish buttons for an intuitive experience.  
- Error messages and success alerts for improved UX.  

---

## 🔧 **Technologies Used**

### 🐍 **Backend:**
- **Python** (Flask): Handles the core backend logic, including routing and database interactions.  
- **SQLite**: Stores the user credentials in a local database file (`passwords.db`).  
- **Password Generator Module**: Generates random passwords with customizable strength.  

### 🌐 **Frontend:**
- **HTML**: Defines the structure and content of the web page.  
- **CSS**: Styles the web page with a clean, responsive design.  
- **JavaScript**: Handles frontend interactivity, including AJAX calls for real-time updates.  

---

## ⚙️ **Installation and Setup**

### 💻 **Prerequisites**
Ensure you have the following installed on your system:
- **Python 3.x**
- **pip** (Python package manager)
- **SQLite** (comes bundled with Python)

### 📥 **Installation Steps**

1. **Clone the Repository**
```bash
git clone <repository-url>
cd password_manager
```

2. **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate        # For Linux/macOS
venv\Scripts\activate           # For Windows
```

3. **Install Dependencies**
Install the required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
python app.py
```
The app will be accessible at:  
👉 `http://127.0.0.1:5000`

---

## 🗃️ **Database Schema**

The project uses **SQLite** for data storage. The schema includes a single table named `passwords` with the following fields:
- `id`: Unique ID (auto-incremented)  
- `website`: Website name  
- `username`: Username  
- `password`: Encrypted password  

---

## ⚙️ **Backend Functionality**

### 1️⃣ **app.py**
- **Flask Application:**  
   - Defines the core application routes.  
   - Handles requests for storing, retrieving, and generating passwords.  
- **Routes:**
    - `/`: Renders the main HTML page (`index.html`).  
    - `/store`: Stores the password in the database.  
    - `/retrieve`: Retrieves stored credentials by website name.  
    - `/generate`: Generates a random password based on user preferences.  

---

### 2️⃣ **database.py**
- Manages the **SQLite database** interactions.  
- Contains functions for:  
    - Creating the `passwords` table if it doesn't already exist.  
    - Storing new password entries.  
    - Retrieving credentials by website name.  

---

### 3️⃣ **password_generator.py**
- Generates **random, strong passwords** with customizable length and complexity.  
- Includes options for:
    - Uppercase letters  
    - Lowercase letters  
    - Numbers  
    - Special characters  

---

## 🌟 **Frontend Functionality**

### 1️⃣ **index.html**
- The main web page for the password manager.  
- Contains:
    - Input fields for **website, username, and password**.  
    - Buttons for storing, retrieving, and generating passwords.  
    - Stylish and responsive layout.  

---

### 2️⃣ **style.css**
- Styles the web page with a **modern and clean design**.  
- Includes:
    - Button hover effects.  
    - Form styling and alignment.  
    - Responsive design for mobile and desktop screens.  

---

### 3️⃣ **script.js**
- Handles frontend interactivity.  
- Uses **AJAX** to communicate with the backend without refreshing the page.  
- Includes functions for:
    - Storing new credentials.  
    - Retrieving saved passwords.  
    - Generating random passwords.  
    - Copying passwords to the clipboard.  

---

## 🔥 **Usage Instructions**

1. **Add a New Password:**  
   - Enter the website, username, and password.  
   - Click **"Store"** to save the password.  

2. **Retrieve a Password:**  
   - Enter the website name in the search bar.  
   - Click **"Retrieve"** to view the stored credentials.  

3. **Generate a Strong Password:**  
   - Click the **"Generate"** button.  
   - Choose the password length and complexity.  
   - Store the generated password if desired.  

---

## 🛠️ **Testing**

The project includes **pytest** tests to verify the core functionality:
- **Test Cases:**
    - `test_store_password`: Verifies if passwords are correctly stored in the database.  
    - `test_retrieve_password`: Ensures passwords are accurately retrieved.  
    - `test_generate_password`: Checks the strength and randomness of generated passwords.  

Run the tests using:
```bash
pytest
```

---

## ⚙️ **Customization and Improvements**

You can further enhance the project by:
- **Adding encryption** for enhanced security.  
- **Integrating authentication** (e.g., login system) for multi-user support.  
- **Exporting passwords** as a CSV or JSON file.  
- **Adding password strength validation** and warnings.  

---

## ✅ **Conclusion**

The **Password Manager** project offers a secure and user-friendly solution for storing, retrieving, and generating passwords. It is built with **Flask, SQLite, HTML, CSS, and JavaScript**, ensuring both functionality and a beautiful, responsive design. With AJAX-powered interactions and a modern UI, it provides a seamless user experience. This project is modular, well-structured, and easy to extend or modify.

---

## 📌 **Author**
👤 **Umar Iqbal**  
📧 [LinkedIn](https://www.linkedin.com/in/umar-iqbal)  
🚀 *Passionate about Python, IoT, and AI Development*
