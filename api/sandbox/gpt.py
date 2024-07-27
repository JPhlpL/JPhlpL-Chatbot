from decouple import config
from openai import OpenAI, OpenAIError, RateLimitError

api_key = config('OPENAI_KEY')

client = OpenAI(api_key=api_key)

try:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    print(completion.choices[0].message['content'])
except RateLimitError as e:
    print("Rate limit exceeded. Please check your OpenAI quota and try again later.")
except OpenAIError as e:
    print(f"An error occurred: {e}")