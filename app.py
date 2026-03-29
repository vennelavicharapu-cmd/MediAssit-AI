import streamlit as st
from PIL import Image
import pytesseract

# ------------------ AI LOGIC (NO API) ------------------
def get_ai_response(symptoms):
    symptoms = symptoms.lower()

    if ("chest" in symptoms and "pain" in symptoms) or "chestpain" in symptoms:
        return "🚨 This could indicate a serious cardiac condition. Immediate medical attention is required. (Critical classification)"

    elif "fever" in symptoms and "headache" in symptoms:
        return "Possible viral infection (basic classification). Stay hydrated and rest."

    elif "fever" in symptoms:
        return "This may be a mild infection (basic classification). Stay hydrated and rest."

    elif "headache" in symptoms:
        return "This could be due to stress or dehydration."

    elif "cough" in symptoms:
        return "This may be a common cold or respiratory issue."

    else:
        return "Symptoms are unclear. Please consult a healthcare professional."

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="MediAssist AI", page_icon="🏥", layout="wide")

# ------------------ HEADER ------------------
st.title("🏥 MediAssist AI")
st.subheader("AI-powered Healthcare Support System with Safety & Compliance")

# ------------------ TABS ------------------
tab1, tab2, tab3 = st.tabs(["📄 Report Simplifier", "🩺 Symptom Checker", "ℹ️ About"])

# ------------------ TAB 1 (FINAL FIXED) ------------------
with tab1:
    st.header("📄 Upload Medical Report")

    st.info("📌 Upload clear image (jpg/png only)")

    file = st.file_uploader("Upload report image", type=["png", "jpg", "jpeg"])

    if file:
        # STEP 1: OPEN IMAGE
        try:
            image = Image.open(file)
            st.image(image, caption="Uploaded Report")
        except Exception as e:
            st.error("❌ Invalid image file")
            st.write(e)
            st.stop()

        # STEP 2: OCR EXTRACTION
        try:
            text = pytesseract.image_to_string(image)

            st.success("✅ Report processed successfully")

            st.subheader("📊 Extracted Data:")
            st.write(text)

        except Exception as e:
            st.error("⚠️ OCR failed (Tesseract issue)")
            st.write(e)
            st.stop()

        # STEP 3: SMART EXPLANATION
        st.subheader("🧠 AI Explanation")

        text_lower = text.lower()

        if "glucose" in text_lower or "sugar" in text_lower:
            st.info("Blood sugar levels detected. This relates to diabetes monitoring.")

        elif "bp" in text_lower or "pressure" in text_lower:
            st.info("Blood pressure values detected. Monitor regularly.")

        elif "hemoglobin" in text_lower:
            st.info("Hemoglobin levels detected. Important for anemia diagnosis.")

        elif "rbc" in text_lower:
            st.info("RBC values detected. Important for oxygen transport in blood.")

        elif "wbc" in text_lower:
            st.info("WBC values detected. Related to immune system function.")

        elif "platelet" in text_lower:
            st.info("Platelet count detected. Important for blood clotting.")

        else:
            st.info("Basic analysis completed. Please consult a doctor for detailed interpretation.")

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

    ✔ Execute symptom-based workflows  
    ✔ Provide basic medical classification  
    ✔ Handle edge cases (e.g., chest pain)  
    ✔ Ensure safe and compliant AI responses  

    ⚠️ This system does NOT replace doctors.
    """)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("⚠️ Educational purposes only. Always consult a doctor.")
