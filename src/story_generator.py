import json
from huggingface_hub import InferenceClient

TEXT_GEN_MODELS = [
    # Modelos tipo instruct / chat
    "tiiuae/falcon-7b-instruct",
    "tiiuae/falcon-40b-instruct",
    "OpenAssistant/oasst-sft-6-llama-30b",
    "mosaicml/mpt-7b-instruct",
    "mpt-30b-instruct",
    
    # Modelos tipo LLaMA
    "meta-llama/Llama-2-7b-chat-hf",
    "meta-llama/Llama-2-13b-chat-hf",
    "decapoda-research/llama-7b-hf",
    
    # Modelos especializados en creatividad o storytelling
    "stabilityai/stablelm-tuned-alpha-7b",
    "cerebras/Cerebras-GPT-6.7B",
    "TheBloke/vicuna-13b-delta-v1.1",
    
    # Modelos pequeños / rápidos para pruebas
    "EleutherAI/gpt-neo-2.7B",
    "EleutherAI/gpt-neo-1.3B",
    "gpt2"
]

def story_generator_all_models(story_data, prompt):
    all_outputs = []

    for model_name in TEXT_GEN_MODELS:
        try:
            client = InferenceClient(model=model_name)

            # Generar la historia
            response = client.text_generation(prompt, max_new_tokens=story_data['quantity_of_words'])
            story_text = response.generated_text

            # Crear JSON
            output = {
                "model": model_name,
                "title": story_data['title'],
                "word_count": story_data['quantity_of_words'],
                "genre": story_data['genre'],
                "characters": story_data['characters'],
                "story": story_text
            }

            all_outputs.append(output)

        except Exception as e:
            print(f"Error con el modelo {model_name}: {e}")
            # Guardar un JSON de error para este modelo
            all_outputs.append({
                "model": model_name,
                "error": str(e)
            })

    return all_outputs