
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what a Linux server does in simple terms"
)

print("**************************************************************************************************************")
print(response.output_text)
print("**************************************************************************************************************")
