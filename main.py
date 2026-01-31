from google import genai
import os

client = genai.Client(api_key=os.environ["Gemini_api"])

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Explain computer in one sentence"
)

print(response.text)
