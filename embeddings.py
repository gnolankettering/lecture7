import config
from openai import OpenAI
client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.embeddings.create(
    input="The Godfather",
    model="text-embedding-3-small"
)

# Print the embedding values
print(response.data[0].embedding)

