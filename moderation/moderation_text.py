from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.moderations.create(
    model="omni-moderation-latest",
    input="I want to hurt myself",
)

print(response.results)

