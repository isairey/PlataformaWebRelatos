def prompt_generator(story_data):
    
    # Create a prompt for the model
    prompt = (
        f"Write a {story_data['genre'].lower()} story titled '{story_data['title']}' with around {story_data['quantity_of_words']} words. "
        f"The story should include the following characters: {', '.join(story_data['characters'])}. "
        f"Make it coherent, engaging, and well-structured."
    )
    return prompt