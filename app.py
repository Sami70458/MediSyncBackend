from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# AI Analysis function
def analyze_medical_image(image_data, user_prompt):
    """
    Analyze the medical image and provide AI-based insights.
    """
    input_prompt = """
    You are a medical AI assistant analyzing diagnostic images (X-rays, MRIs, CT scans).
    Provide:
    1️⃣ **Diagnosis:** Identify visible conditions.
    2️⃣ **Disease Name:** Name of detected disease.
    3️⃣ **Symptoms:** Common symptoms of the condition.
    4️⃣ **Possible Causes:** Causes of the detected condition.
    5️⃣ **Treatment & Cure:** Possible treatment methods.
    6️⃣ **Urgency:** Whether immediate medical attention is needed.

    ⚠️ **Guidelines:**  
    - If unclear, ask for a better-quality scan.  
    - If uncertain, advise consulting a doctor.  
    - Be professional, concise, and medically accurate.
    """

    response = model.generate_content([input_prompt, image_data, user_prompt])
    return response.text

# API route for AI diagnosis
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        file = request.files["file"]
        user_prompt = request.form.get("user_prompt", "")
        
        if file:
            image_data = file.read()
            response_text = analyze_medical_image(image_data, user_prompt)
            return jsonify({"status": "success", "analysis": response_text}), 200
        else:
            return jsonify({"status": "error", "message": "No file uploaded"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Run server
if __name__ == "__main__":
    app.run(debug=True, port=5000)
