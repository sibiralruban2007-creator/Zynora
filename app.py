import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Zynora",
    page_icon="✨",
    layout="centered"
)

st.title("✨ Zynora")
st.subheader("Your AI-Powered Student Assistant")
st.write("Learn. Explore. Create.")

@st.cache_resource
def load_model():
    generator = pipeline(
        "text-generation",
        model="HuggingFaceTB/SmolLM2-135M"
    )
    return generator

generator = load_model()

question = st.text_area(
    "Ask me anything:",
    placeholder="Type your question here..."
)

if st.button("Generate Response ✨"):
    if question:
        with st.spinner("Zynora is thinking... 🤔"):
            response = generator(
                question,
                max_new_tokens=100,
                do_sample=True,
                temperature=0.7
            )

            st.subheader("🤖 Zynora's Response")
            st.write(response[0]["generated_text"])
    else:
        st.warning("Please enter a question first!")

st.markdown("---")
st.caption("✨ Zynora | Learn. Explore. Create.")
