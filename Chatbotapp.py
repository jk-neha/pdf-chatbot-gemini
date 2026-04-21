import streamlit as st
import google.generativeai as genai
import PyPDF2

# ✅ CONFIGURE API KEY
genai.configure(api_key="AIzaSyCrIxwxz2W8DTMSHG201W4HEthceMpmDT0")  # Replace with your actual key

# ✅ LOAD THE RIGHT MODEL (Gemini-Pro)
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# ✅ EXTRACT PDF TEXT
def extract_pdf_text(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# ✅ STREAMLIT UI
st.title("📄 Chat with your PDF (Gemini-powered)")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_pdf:
    pdf_text = extract_pdf_text(uploaded_pdf)
    st.success("PDF uploaded and text extracted!")

    question = st.text_input("❓ Ask a question based on the PDF content:")
    if st.button("Get Answer"):
        if question.strip():
            with st.spinner("Generating answer..."):
                prompt = f"PDF Content:\n{pdf_text}\n\nQuestion: {question}"
                response = model.generate_content(prompt)
                st.markdown(f"*Answer:* {response.text}")
        else:
            st.warning("Please enter a question.")