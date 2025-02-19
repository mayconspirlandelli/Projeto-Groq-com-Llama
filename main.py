#Exemplo que usar Groq com Llama3-70b
#fonte: https://replit.com/t/groqcloud/repls/Groq-Quickstart-Conversational-Chatbot/view#main.py

from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

# Create the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Set the system prompt
system_prompt = {
    "role": "system",
    "content":
    #"You are a helpful assistant. You reply with very short answers."
    "Você é um assistente inteligente. Você deve responder as perguntas do usuario."
}

# Initialize the chat history
chat_history = [system_prompt]

while True:
  # Get user input from the console
  user_input = input("You: ")

  # Append the user input to the chat history
  chat_history.append({"role": "user", "content": user_input})

  response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
  # Append the response to the chat history
  chat_history.append({
      "role": "assistant",
      "content": response.choices[0].message.content
  })
  # Print the response
  print("Assistant:", response.choices[0].message.content)