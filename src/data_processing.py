import json

def data_processing(story_title, quantity_of_words, genre, characters):
    """
    Procesa los datos de entrada para estructurarlos en un formato adecuado para la generación de historias.
    """
    story_data = {
        "title": story_title,
        "quantity_of_words": quantity_of_words,
        "genre": genre,
        "characters": [char.strip() for char in characters.split(",") if char.strip()]
    }
    return story_data
