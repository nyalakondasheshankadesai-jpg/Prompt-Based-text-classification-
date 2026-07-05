from google import genai

client = genai.Client(api_key="")

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input="hello"
)
print(interaction.output_text)