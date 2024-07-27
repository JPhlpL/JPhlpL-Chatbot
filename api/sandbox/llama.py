from llamaapi import LlamaAPI
from decouple import config
import json

# Load API key from environment variable
api_key = config('LLAMA_KEY')

# Initialize LlamaAPI with the provided API key
llama = LlamaAPI(api_key)

# API Request JSON Cell
api_request_json = {
  "model": "llama3-70b",
  "messages": [
    {"role": "user", "content": "Who is doctor jose rizal"}
  ]
}

# Make the API request and handle the response
response = llama.run(api_request_json)
response_data = response.json()

# Function to format the content for readability
def format_content(content):
    lines = content.splitlines()
    formatted_lines = []
    in_code_block = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            formatted_lines.append(line)
        elif in_code_block:
            formatted_lines.append(line)
        else:
            formatted_lines.append(line.strip())

    return "\n".join(formatted_lines)

# Format the 'content' field of the response for readability
for choice in response_data.get('choices', []):
    message = choice.get('message', {})
    if 'content' in message:
        message['content'] = format_content(message['content'])

# Save the formatted response to a JSON file
with open('formatted_response.json', 'w') as f:
    json.dump(response_data, f, indent=2)

# Print the formatted response
print(json.dumps(response_data, indent=2))
