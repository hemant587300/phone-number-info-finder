# 📱 Phone Number Information Finder

This is a simple Flask web application that allows users to find useful information about a phone number, including its:

- 📍 Region (Geographical area)
- 🕒 Time Zone(s)
- 📞 Mobile Carrier (Service provider)

---

## 🚀 Features

- Clean and responsive UI with HTML/CSS
- Takes a mobile number as input and detects:
  - Time zone
  - Mobile company
  - Region/city/state
- Handles invalid input gracefully
- Displays results in a user-friendly format

---

## 🛠️ Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| Backend       | Python 3, Flask    |
| Phone Parsing | `phonenumbers`     |
| Frontend      | HTML5, CSS3        |
| UI Styling    | Custom CSS         |
| Template Engine | Jinja2 (Flask)   |

---

## 📂 Project Structure

```
Phone_Location/
├── app.py                   # Main Flask application
├── static/
│   ├── style.css            # Styling for the app
│   └── location-arrow-solid.svg
├── templates/
│   ├── index.html           # Input form page
│   └── result.html          # Output display page
└── README.md                # You're reading it!
```

---

## 🖥️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Phone_Location.git
cd Phone_Location
```

### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask phonenumbers
```

### 4. Run the App
```bash
python app.py
```

Then open your browser and go to `http://127.0.0.1:5000/`.

---

## 🔐 Note on Privacy

This app uses only publicly available metadata from the phone number and **does not** track real-time location or collect any personal data.

---

## 📸 Screenshots

> *(Optional: Add screenshots of the home page and result page)*

---

## 📧 Contact / Contribute

If you want to suggest improvements or contribute:
- Raise an issue
- Submit a pull request
- Or contact me directly at: **[your_email@example.com]**

---

## 📄 License

This project is open-source and free to use under the **MIT License**.
