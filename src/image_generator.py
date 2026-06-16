from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO

def image_generator(output_json, model_name="stabilityai/stable-diffusion-2"):
    """
    Genera una imagen basada en los datos de un relato (JSON) usando un modelo de texto a imagen.
    """
    try:
        prompt = (
            f"Illustration for a {output_json['genre'].lower()} story titled '{output_json['title']}'. "
            f"Main characters: {', '.join(output_json['characters'])}. "
            f"Atmosphere of the story: {output_json['story'][:300]}..."
        )

        client = InferenceClient(model=model_name)
        image_bytes = client.text_to_image(prompt)
        image = Image.open(BytesIO(image_bytes))

        return image

    except Exception as e:
        print(f"Error generating image with model {model_name}: {e}")
        return None
