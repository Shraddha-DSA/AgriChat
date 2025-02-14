import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the gemini-pro model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Streamlit app UI
st.set_page_config(page_title="Agriculture Expert", page_icon="🔐", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Set background and text colors */
        body {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        
        /* Title and Subheading Styling */
        .stTitle {
            color: #00ff00;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }

        /* Chat input and response styling */
        .stTextInput, .stTextArea {
            background-color: #333333;
            color: #00ff00;
            border: 1px solid #00ff00;
        }

        /* Chat history message styling */
        .user-message {
            background-color: #006400;
            padding: 10px;
            margin: 5px;
            border-radius: 10px;
        }
        
        .bot-message {
            background-color: #ff4500;
            padding: 10px;
            margin: 5px;
            border-radius: 10px;
        }

        /* Style for the text area where the bot responds */
        .stTextArea {
            background-color: #222222;
            color: #ff4500;
            border: 1px solid #ff4500;
        }

        /* Stylize the Chat History container */
        .chat-container {
            max-height: 400px;
            overflow-y: auto;
            padding: 10px;
        }
        
        /* Button Styling */
        .stButton>button {
            background-color: #00ff00;
            color: #1e1e1e;
            border: none;
            padding: 10px;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #228b22;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app UI
st.title("Ask me your doubt")
st.write("Ask questions about Agriculture.")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# User input
user_input = st.text_input("You:", "")

# Generate response
if user_input:
    # Append user input to chat history
    st.session_state["chat_history"].append(("User", user_input))
    
    # Generate response from gemini-pro model
    response = model.generate_content(f"As a Agriculture expert, give advice for: {user_input}")
    
    # Append bot response to chat history
    bot_reply = response.text
    st.session_state["chat_history"].append(("Bot", bot_reply))
    
    # Display the response
    st.text_area("Expert:", bot_reply, height=150)

# Display chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for role, message in st.session_state["chat_history"]:
    if role == "User":
        st.markdown(f'<div class="user-message"><b>You:</b> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message"><b>Agriculture Expert:</b> {message}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)