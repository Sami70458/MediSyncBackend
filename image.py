from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import time

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro Vision Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get AI response
def get_gemini_response(image, user_prompt):
    input_prompt = """
    You are a medical AI assistant specializing in analyzing medical images such as X-rays, MRIs, CT scans, and other diagnostic images. Your task is to accurately analyze the given medical image and provide the following details:

    1️⃣ **Diagnosis:** Identify any medical condition or abnormality visible in the image.
    2️⃣ **Disease Name:** Provide the name of the detected disease (if applicable).
    3️⃣ **Symptoms:** List common symptoms associated with the detected condition.
    4️⃣ **Possible Causes:** Explain potential causes of the condition.
    5️⃣ **Treatment & Cure:** Suggest possible treatments, including medication, therapy, lifestyle changes, or surgical options if necessary.
    6️⃣ **Urgency:** Indicate whether the patient should seek immediate medical attention or consult a specialist.

    ⚠️ **Guidelines:**  
    - If the image is unclear, ask the user to upload a higher-quality scan.  
    - If the condition is not identifiable, advise the user to consult a medical professional.  
    - Be professional, concise, and medically accurate.  

    🔥 **Note:** You should ONLY provide medical insights. Do NOT generate random descriptions unrelated to medical analysis.
    """

    response = model.generate_content([input_prompt, image[0], user_prompt])
    return response.text

# Function to process uploaded image
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="Medical Diagnosis AI")

st.header("🔬 Medical Image Diagnosis Chatbot")

# Sidebar for image upload
uploaded_file = st.sidebar.file_uploader("📂 Upload a medical image (X-ray, MRI, CT, etc.)", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="📷 Uploaded Image", use_column_width=True)

# Initialize session state for chat history and timeout
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_response' not in st.session_state:
    st.session_state.last_response = None
if 'last_question' not in st.session_state:
    st.session_state.last_question = None
if 'last_interaction_time' not in st.session_state:
    st.session_state.last_interaction_time = time.time()

# Session timeout (2 minutes)
if time.time() - st.session_state.last_interaction_time > 120:
    st.session_state.chat_history = []
    st.session_state.last_response = None
    st.session_state.last_question = None

# User input for symptoms or additional details
input_text = st.text_input("📝 Describe any symptoms or concerns (optional):", key="input")
submit = st.button("🩺 Analyze Medical Image")

# Process request on button click
if submit and uploaded_file is not None:
    st.session_state.last_interaction_time = time.time()  # Update session timer
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(image_data, input_text)

    # Store the last interaction
    st.session_state.last_response = response
    st.session_state.last_question = input_text

# Display last response
if st.session_state.last_question and st.session_state.last_response:
    st.subheader("📢 Diagnosis Report")
    st.write(f"**🧑‍⚕️ Patient Symptoms:** {st.session_state.last_question}")
    st.write(f"**🤖 AI Diagnosis:** {st.session_state.last_response}")

# Store and show chat history
if submit and uploaded_file is not None:
    st.session_state.chat_history.append({"user": st.session_state.last_question, "ai": st.session_state.last_response})

st.subheader("📜 Previous Diagnoses")
for interaction in st.session_state.chat_history:
    st.write(f"**🧑‍⚕️ Patient Symptoms:** {interaction['user']}")
    st.write(f"**🤖 AI Diagnosis:** {interaction['ai']}")
