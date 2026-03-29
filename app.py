import streamlit as st

st.set_page_config(page_title="MediAssist AI", layout="centered")

st.title("🩺 MediAssist AI")
st.subheader("Your Intelligent Healthcare Assistant")

st.write("Enter your medical report or prescription below:")

user_input = st.text_area("📝 Medical Text")

if st.button("Explain in Simple Words"):
    if user_input:
        st.subheader("📖 Simplified Explanation")

        explanation = f"""
        🤖 AI Explanation:
        This medical report indicates a health condition that requires attention.

        ✔️ Follow the prescribed medication properly.
        ✔️ Maintain a healthy diet and rest.
        ✔️ Regularly consult your doctor if symptoms continue.

        💊 Reminder:
        Take medicines on time as advised.

        ⚠️ Note:
        This is a simplified explanation. Please consult a doctor for accurate diagnosis.
        """

        st.success(explanation)
    else:
        st.warning("Please enter some medical text.")
