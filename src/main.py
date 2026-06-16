import streamlit as st
import json
import data_processing as data_processing
import prompt_generator as prompt_generator
import story_generator as story_generator
import image_generator as image_generator

# All available genres
GENRES = [
    "Fantasy", "Science Fiction", "Mystery", "Thriller", "Romance", "Horror",
    "Historical Fiction", "Adventure", "Comedy", "Drama", "Western", "Dystopian",
    "Crime", "Mythology", "Slice of Life", "Tragedy"
]
st.set_page_config(page_title="AI Story Generator", layout="wide")

def main():
    st.title("📖 AI Story Generator (Open Source via Hugging Face)")

    # Sidebar inputs
    with st.sidebar:
        st.header("Story Parameters")
        story_title = st.text_input("Story Title", "Enter your story title...")
        quantity_of_words = st.slider("Quantity of Words", min_value=450, max_value=550, value=500)
        genre = st.selectbox("Genre", GENRES, index=0)
        characters = st.text_input("Characters (comma separated)", "Alice, Bob, The Dragon")

    # Procesar datos y generar prompt
    story_data = data_processing.data_processing(story_title, quantity_of_words, genre, characters)
    prompt = prompt_generator.prompt_generator(story_data)

    # Botón para generar historias
    if st.button("Generate Story for All Models"):
        with st.spinner("Generating stories for all models..."):
            # Llamamos a tu función que recorre todos los modelos
            all_story_jsons = story_generator.story_generator_all_models(story_data, prompt)

            st.subheader("📦 Generated Stories JSON")
            for story_json in all_story_jsons:
                st.markdown(f"### Model: {story_json.get('model', 'Unknown')}")
                if "error" in story_json:
                    st.error(f"Error: {story_json['error']}")
                else:
                    st.json(story_json)

                    # Generar imagen para cada historia (opcional)
                    st.subheader(f"🎨 Generated Image for {story_json['model']}")
                    story_image = image_generator.image_generator(story_json, model_name="stabilityai/stable-diffusion-2")
                    if story_image:
                        st.image(story_image, use_column_width=True)

if __name__ == "__main__":
    main()