import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
# Access the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate content from Gemini
def generate_content(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    convo = model.start_chat()
    response = convo.send_message(prompt)
    return response.text

# Streamlit app
st.title("Aplicación de Información de Razas de Perros")

# Text input for dog breed
dog_breed = st.text_input("Ingrese una raza de perro:")

if dog_breed:
    # Generate prompt for Gemini
    prompt = f"Dime sobre la raza de perro {dog_breed}, incluyendo información sobre su alimentación, cuidado y otra información importante."

    # Generate content from Gemini
    dog_info = generate_content(prompt)

    # Display the information
    st.write(dog_info)

# Fixed footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0E1117;
        color: white;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        Desarrollado por Kevin Orellana
    </div>
    """,
    unsafe_allow_html=True,
)
