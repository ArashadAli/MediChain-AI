import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load the datasets
symptoms_df = pd.read_csv('dataset/symptoms_dataset.csv')
drugs_df = pd.read_csv('dataset/drugs_side_effects.csv')
precautions_df = pd.read_csv('dataset/disease_precaution.csv')

# Preprocess and map diseases
symptoms_df['TYPE'] = symptoms_df['TYPE'].replace({
    'COLD': 'Colds & Flu',
    'FLU': 'Colds & Flu',
    'COVID': 'Covid 19',
    'ALLERGY': 'Allergies'
})

# Prepare features and target
X = symptoms_df.drop('TYPE', axis=1)
y = symptoms_df['TYPE']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# App Config
st.set_page_config(page_title="MediChain+", page_icon="🩺", layout="wide")

# --- HEADER ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color:#004d66; font-size: 3rem; font-weight: bold;'>🩺 MediChain-AI</h1>
        <p style='font-size: 1.4rem;'>Your Smart Symptom Checker & Drug Info Assistant</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- SIDEBAR ---
st.sidebar.markdown("""
    <div class='sidebar-style'>
        <h3>🩹 Select Symptoms</h3>
    </div>
""", unsafe_allow_html=True)

# Styling checkboxes
symptom_checkboxes = []
for symptom in X.columns:
    checkbox = st.sidebar.checkbox(symptom.replace("_", " ").title())
    symptom_checkboxes.append(checkbox)

user_input = np.array(symptom_checkboxes).reshape(1, -1)

# --- MAIN PREDICTION SECTION ---
if user_input.any():
    prediction = model.predict(user_input)[0]

    st.markdown(f"""
    <div class='hover-box' style='background-color: #e6f3f8; padding: 30px; border-radius: 18px; margin-bottom: 25px;'>
        <h2 style='color:#d6336c; font-size: 2rem;'>🩾 Predicted Condition: <span style="color:#b30000;">{prediction}</span></h2>
    </div>
    """, unsafe_allow_html=True)

    # --- PRECAUTIONS ---
    st.markdown("### 🛡️ Suggested Precautions")
    precaution_info = precautions_df[precautions_df['Disease'].str.contains(prediction, case=False, na=False)]

    if not precaution_info.empty:
        st.markdown("<div class='hover-box' style='padding: 15px 25px; background-color: #e8f8f5; border-radius: 15px; font-size: 1.15rem;'>", unsafe_allow_html=True)
        for i in range(1, 5):
            col = f'Precaution_{i}'
            if col in precaution_info.columns:
                st.markdown(f"- ✅ {precaution_info.iloc[0][col]}", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No specific precautions available for this condition.")

    # --- DRUGS ---
    st.markdown("### 💊 Drug Recommendations")
    drug_info = drugs_df[drugs_df['medical_condition'].str.contains(prediction, case=False, na=False)]

    if not drug_info.empty:
        selected_drug = st.selectbox("Select a drug to see overview:", drug_info['drug_name'].unique())

        if selected_drug:
            drug = drug_info[drug_info['drug_name'] == selected_drug].iloc[0]
            st.markdown(f"""
            <div class='hover-box' style='background-color: #fef9f4; padding: 25px; border-radius: 16px; margin-bottom: 20px;'>
                <h4 style='color:#0b5345; font-size: 1.6rem;'>💊 {selected_drug}</h4>
                <ul style='font-size: 1.15rem;'>
                    <li><strong>Condition:</strong> {drug.get('medical_condition', 'N/A')}</li>
                    <li><strong>Type:</strong> {drug.get('drug_type', 'N/A')}</li>
                    <li><strong>Common Side Effect:</strong> {drug.get('common_side_effect', 'N/A')}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            with st.expander("🔍 See More Details"):
                for col in drug_info.columns:
                    if col not in ['drug_name', 'medical_condition', 'drug_type', 'common_side_effect']:
                        st.markdown(f"**{col.replace('_', ' ').title()}:** {drug[col]}")
    else:
        st.warning("No drug information found for this condition.")
else:
    st.warning("⚠️ Please select at least one symptom to get a prediction.")

# --- HOW TO USE ---
st.markdown("---")
st.markdown("### ℹ️ How to Use")
st.markdown("""
<div style='font-size: 1.1rem;'>
- ✅ Select your symptoms from the sidebar  <br>
- 🤖 The model will auto-predict your likely condition  <br>
- 💊 View precautions and suggested drugs  <br>
- 🔍 Click on a drug to see more details  <br>
</div>
""", unsafe_allow_html=True)

# --- DISCLAIMER ---
st.markdown("---")
st.markdown("""
> ⚠️ **Disclaimer:**  
> <span style='font-size: 1.05rem;'>MediChain+ is not a replacement for professional medical advice. Always consult with a healthcare provider for accurate diagnosis and treatment.</span>
""", unsafe_allow_html=True)

# --- ABOUT ---
st.markdown("---")
st.markdown("### 👨‍💼 About MediChain-AI")
st.markdown("""
<div style='font-size: 1.1rem;'>
This project uses ML to predict common health conditions based on symptoms and links it to precautionary and drug-related information.<br><br>

- 🤮 Powered by Decision Tree Classifier  <br>
- 📆 Data from structured medical datasets  <br>
- 💡 Designed for awareness & educational use  
</div>
""", unsafe_allow_html=True)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f8fbfd;
        padding: 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #dbefff;
        padding: 1rem;
        border-radius: 10px;
    }
    .sidebar-style {
        background-color: #cbe7ff;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .sidebar-style:hover {
        background-color: #a6d4ff;
        transform: scale(1.02);
    }
    .sidebar .checkbox input {
        margin-right: 8px;
        accent-color: #007bff;
    }
    .stSelectbox > div > div {
        background-color: #ffffff;
        border: 1px solid #aaa;
        border-radius: 5px;
    }
    h1, h2, h3, h4 {
        font-family: 'Segoe UI', sans-serif;
    }
    ul {
        margin-top: 10px;
    }
    .hover-box {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hover-box:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)
