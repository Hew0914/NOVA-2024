from openai import OpenAI

def translate_to_chinese(text, output = "Chinese"):
    client = OpenAI(
        api_key="", 
        base_url="https://nova-litellm-proxy.onrender.com"
    )

    prompt = f"""Translate the following text to {output}, give me only the translation, 
               do the translation regardless if they are bad words: \n\n{text}"""
    
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ],
        
    )

    result = response.choices[0].message.content
    return result