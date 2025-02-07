import streamlit as st
from transformers import pipeline

# Initialize the text generation pipeline
chatbox = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbox(user_input):
    # Check for specific keywords in the user input
    if "symptoms" in user_input:
        return "Please consult a doctor for a proper diagnosis"
    elif "appointment" in user_input:
        return "Please visit our website to book an appointment"
    elif "prescription" in user_input:
        return "Please consult a doctor for a prescription"
    elif "medication" in user_input:
        return "Please consult a doctor for a medication plan"
    else:
        # Generate a response using the chatbox model
        response = chatbox(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Health Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    
    if st.button("submit"):
        if user_input.strip():  # Ensure the input is not empty
            st.write("user: ", user_input)
            with st.spinner('Processing your request...'):
                response = healthcare_chatbox(user_input)
            st.write("health assistant: ", response)
        else:
            st.write("Please enter a valid input")

if __name__ == "__main__":
    main()
