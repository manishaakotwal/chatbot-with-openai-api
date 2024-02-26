import openai
# Initialize the OpenAI API with your API key
client = openai.OpenAI(api_key='your_api_key')


# Define a function to interact with the chatbot
def chat_with_bot(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model you want to use
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].message.content

# Example conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat_with_bot(user_input)
    print("Bot:", response)    

# y = chat_with_bot("hello")
# print(y)
