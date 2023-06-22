import streamlit as st
import openai

def generate_metaphors(content, api_key):
    # Make an API call to the OpenAI GPT-3 model to generate metaphors
    openai.api_key = api_key
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

    api_key = st.text_input("Enter your OpenAI API key:")
    
    content = st.text_area("Enter your content:")
    
    if st.button("Metaphorize"):
        content_pieces = content.split("\n")
        metaphors = generate_metaphors(content_pieces, api_key)

        for metaphor in metaphors:
            st.write(metaphor)

if __name__ == "__main__":
    main()
