#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://gpt4openaimodel.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

message_text = [{"role":"system","content":"Can you write a script in C# for unity for a 360 video manager. I would like to be able to upload 360 video clips organized by catetory. Each category might have 5-10 clips. I would like to assign them to a single skybox and render texture and have them assignable to button's on click. Also, there should be a method advance next or back in the category. ."}]

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
