import requests

def query_huggingface_inference(api_key, user_input):
    # url = "https://api-inference.huggingface.co/models/gpt2"  # You can change the model to your preferred one
    url = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"inputs": user_input}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()[0]['generated_text'].strip()
    except requests.exceptions.RequestException as e:
        return f"Hugging Face query failed due to an error. Error: {e}"
