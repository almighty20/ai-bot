import openai

# Initialize the OpenAI API client
openai.api_key = ""

# Define a function to generate text based on input prompt
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Example usage
while True:
    user_input = input("You: ")
    response = generate_text(user_input)
    print(f"Chatbot: {response}")