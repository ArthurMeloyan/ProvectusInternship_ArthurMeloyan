import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")
print(HF_TOKEN)
assert HF_TOKEN, "Hugging Face API token is not set!"

client = InferenceClient(
    model='HuggingFaceH4/zephyr-7b-beta',
    token=HF_TOKEN
)


def generate_answer(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for answering questions about concert tours."},
                {"role": "user", "content": prompt},
            ],
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during generation: {str(e)}"