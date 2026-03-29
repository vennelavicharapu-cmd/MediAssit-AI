import streamlit as st
from PIL import Image
import pytesseract

# ------------------ OCR SETUP ------------------
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ------------------ AI LOGIC (NO API) ------------------
def get_ai_response(symptoms):
    symptoms = symptoms.lower()

    if ("chest" in symptoms and "pain" in symptoms) or "chestpain" in symptoms:
        return "🚨 This could indicate a serious cardiac condition. Immediate medical attention is required. (Critical classification)"

    elif "fever" in symptoms and "headache" in symptoms:
        return "Possible viral infection (basic classification). Stay hydrated, take rest, and monitor symptoms."

    elif "fever" in symptoms:
        return "This may be a mild infection (basic classification). Stay hydrated and rest."

    elif "headache" in symptoms:
        return "This could be due to stress, dehydration, or lack of sleep (basic classification)."

    elif "cough" in symptoms:
        return "This may be a common cold or respiratory issue (basic classification)."

    else:
        return "Symptoms are unclear. Unable to classify condition. Please consult a healthcare professional."

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="MediAssist AI", page_icon="🏥", layout="wide")

# ------------------ HEADER ------------------
st.title("🏥 MediAssist AI")
st.subheader("AI-powered Healthcare Support System with Safety & Compliance")

# ------------------ TABS ------------------
tab1, tab2, tab3 = st.tabs(["📄 Report Simplifier", "🩺 Symptom Checker", "ℹ️ About"])

# ------------------ TAB 1 (FIXED UPLOAD SECTION) ------------------
with tab1:
    st.header("📄 Upload Medical Report")

    st.info("📌 Please upload clear image (jpg/png) of medical report")

    file = st.file_uploader("Upload report image", type=["png", "jpg", "jpeg"])

    if file:
        try:
            image = Image.open(file)
            st.image(image, caption="Uploaded Report")

            # OCR extraction
            text = pytesseract.image_to_string(image)

            st.success("✅ Report processed successfully")

            st.subheader("📊 Extracted Data:")
            st.write(text)

            st.subheader("🧠 AI Explanation")

            if "fever" in text.lower():
                st.info("The report suggests possible infection or fever-related condition.")

            elif "glucose" in text.lower():
                st.info("The report indicates glucose levels. Monitor for diabetes risk.")

            elif "bp" in text.lower() or "pressure" in text.lower():
                st.info("The report may indicate blood pressure-related values. Monitor regularly.")

            else:
                st.info("Report analyzed. Please consult a doctor for detailed interpretation.")

        except:
            st.error("❌ Please upload a valid image file (jpg/png)")

# ------------------ TAB 2 ------------------
with tab2:
    st.header("🩺 Symptom Checker")

    symptoms = st.text_area("Enter your symptoms")

    if st.button("Analyze"):
        if symptoms.strip() == "":
            st.warning("⚠️ Please enter symptoms")

        else:
            with st.spinner("Analyzing symptoms..."):
                response = get_ai_response(symptoms)

                if "critical" in response.lower() or "🚨" in response:
                    st.error(response)
                else:
                    st.success(response)

# ------------------ TAB 3 ------------------
with tab3:
    st.header("ℹ️ About MediAssist AI")

    st.write("""
    **MediAssist AI** is a domain-specific healthcare assistant designed to:

    ✔ Execute symptom-based analysis workflows  
    ✔ Provide basic condition classification  
    ✔ Handle edge cases (e.g., chest pain detection)  
    ✔ Ensure safe and compliant AI responses  

    ### 🔒 Safety & Compliance
    - Built with healthcare safety guardrails  
    - Avoids harmful or misleading advice  
    - Recommends professional consultation when needed  

    ### 🎯 Goal
    Make healthcare understandable and accessible for everyone.

    ⚠️ This system does NOT replace doctors.
    """)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("⚠️ Disclaimer: This system provides educational guidance only. Always consult a healthcare professional.")
