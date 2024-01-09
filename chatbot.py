import os
import openai

openai.api_type = "azure"
openai.api_base = "https://gpt4openaimodel.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

message_text = [{"role":"system","content":"I am working on a new strategic plan for our office of academic excellence. What are some suggestions for organizing this?"}]

completion = openai.ChatCompletion.create(
  engine="GPT4-32k",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion.choices[0].message.content)
