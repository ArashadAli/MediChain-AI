# 🩺 MediChain-AI

**MediChain-AI** is a simple and smart web-based symptom checker built with **Streamlit**. It allows users to predict minor illnesses by selecting symptoms and gives insights into related **precautions** and **drug information**. This project is a demo tool for educational and awareness purposes.

👉 **Live Demo:** *Coming Soon*  
📷 **Image preview**
![image](https://github.com/user-attachments/assets/65fa980c-df86-498d-9567-bf565d423010)

---

## 🔍 Overview

- Select symptoms from a sidebar list  
- Get predicted health conditions using a trained **Decision Tree Classifier**  
- View suggested **precautions** and **drug information** (e.g. side effects, usage)  
- Clean and responsive UI – works on both mobile and desktop  
- Easy error handling and friendly experience  

---

## 🚀 Features

- ✅ **User-friendly Interface** – Just click and get results!  
- 🧠 **ML-Powered Prediction** – Decision Tree Classifier model trained on real symptom data  
- 💊 **Drug & Side Effects Info** – Helpful suggestions from drug dataset  
- 📱 **Responsive Design** – Accessible on all screen sizes  
- ⚠️ **Error Handling** – Warns users if no symptom is selected  

---

## ⚙️ Getting Started

### 🔧 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ArashadAli/MediChain-AI.git
   cd MediChain-AI
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add required datasets:**

   Download and place the following files into the `dataset/` folder:
   - `symptoms_dataset.csv`
   - `drugs_side_effects.csv`
   - `disease_precaution.csv`

---

### ▶️ Running the App

```bash
streamlit run symptoms_checker.py
```

Replace `app.py` with your main Python file name if different.

---

## 📁 Project Structure

```bash
MediChain/
│
├── dataset/
│   ├── symptoms_dataset.csv
│   ├── drugs_side_effects.csv
│   └── disease_precaution.csv
│
├── symptoms_checker.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Disclaimer

> MediChain-AI is an educational project and **not a substitute for medical advice**. Always consult a healthcare provider for medical concerns.

---

## 🙌 Credits

- 💻 Built using [Streamlit](https://streamlit.io/)  
- 🧠 ML Model: Decision Tree Classifier (scikit-learn)  
- 📊 Datasets: Public datasets of symptoms, drugs, and precautions
