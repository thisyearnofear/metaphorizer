import os
import streamlit as st
import openai

api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

def generate_metaphors(content):
    # Make an API call to the OpenAI GPT-3 model to generate metaphors
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=content,
        max_tokens=100,
        temperature=0.8
    )
    metaphors = response.choices[0].text.strip().split("\n")
    return metaphors

def main():
    st.title("Metaphorize App")
    
    content = st.text_area("Enter your content:")
    
    if st.button("Metaphorize"):
        content_pieces = content.split("\n")
        metaphors = generate_metaphors(content_pieces)

        for metaphor in metaphors:
            st.write(metaphor)

if __name__ == "__main__":
    main()
