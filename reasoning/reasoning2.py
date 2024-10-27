import config
from openai import OpenAI
client = OpenAI(api_key=config.OPENAI_API_KEY)

prompt = """
What are three compounds we should consider investigating to advance research 
into new antibiotics? Why should we consider them?
"""

response = client.chat.completions.create(
    model="o1-preview",
    messages=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)