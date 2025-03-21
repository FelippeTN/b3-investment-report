from groq import Groq
import os

def groq_call(asset_name, message):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é um bot profissional e analises sobre ações do Brasil com base nas informações fornecidas. Sua analise é bem clara e em apenas 1 parágrafo, utilizando as estratégias do Barsi, maior investidor PF Brasileiro."
            },
            {
                "role": "user",
                "content": f"Analise a seguinte ação {asset_name}: {message}"
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content