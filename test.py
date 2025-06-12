from ollama import Client

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': '200'}
)

response = client.chat(model='gemma3:4b', messages=[
    {
        'role': 'user',
        'content': 'What is color of earth answer in 50 words.',
    },
], stream=True)

for chunk in response:
    print(chunk['message']['content'],end='',flush=True)

