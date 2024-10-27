import config
from openai import OpenAI
client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.moderations.create(
    model="omni-moderation-latest",
    input=[
        {"type": "text", "text": "John Wayne in a fist fight"},
        {
            "type": "image_url",
            "image_url": {
                "url": "https://media.baselineresearch.com/images/347693/347693_full.jpg",
            }
        },
    ],
)

print(response)
