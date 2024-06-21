# Python Library for Conva AI

This is the python library for using Conva AI Co-pilots

## Examples

### 1. A simple example for generating response using Conva Co-pilot
```
import asyncio
from conva_ai import AsyncConvaAI
client = AsyncConvaAI(
    assistant_id="<YOUR_ASSISTANT_ID>", 
    assistant_version="<YOUR_ASSISTANT_VERSION>", 
    api_key="<YOUR_API_KEY>"
)
async def generate_with_capability_group(client: AsyncConvaAI, query: str, capability_group: str = "default", stream: bool = "True"):
  if stream:
    response = await client.invoke_capability_group_stream(query, capability_group=capability_group)
    out = ""
    async for res in response:
        out = res
    return out
  else:
    response = await client.invoke_capability_group(query, capability_group=capability_group)
    return response

final_response = asyncio.run(generate_with_capability_group(client, "how are you", stream=True))
print(final_response)
```

The above snippet of code is used for invoking a capability group. 

Similarly, a particular capability can be invoked by
```
import asyncio
from conva_ai import AsyncConvaAI
client = AsyncConvaAI(
    assistant_id="<YOUR_ASSISTANT_ID>", 
    assistant_version="<YOUR_ASSISTANT_VERSION>", 
    api_key="<YOUR_API_KEY>"
)
async def generate_with_capability_name(client: AsyncConvaAI, query: str, capability_name: str, stream: bool):
  if stream:
    response = await client.invoke_capability_stream(query, capability_name=capability_name)
    out = ""
    async for res in response:
        out = res
    return out
  else:
    response = await client.invoke_capability(query, capability_name=capability_name)
    return response

final_response = asyncio.run(generate_with_capability_name(client, "buy 10 shares", "order_management", True))
print(final_response)
```

You can try out the co-pilot on [Google Colab](https://colab.research.google.com/drive/1WtbARTRQ9wCvztrAQuEhQUvwImhtPZXd#scrollTo=ZSVBQsOelgfv)

### 2. How to keep track of conversation history

The response contains the conversation history, You can can send the history as part of the your next request to continue your previous conversation. Below given is a small code snippet of the same.

```
history = "{}"
while True:
    query = input("Enter your query: ")
    response = asyncio.run(generate_with_capability_group(client, query, stream=False, history=history))
    history = response.conversation_history
    print(response.message)
```

### 3. Debugging responses

Conva AI uses generative AI to give you the response to your query. In order for you to understand the reasoning behind the response. We also provide you with AI's reasoning

```
final_response_dict = json.loads(final_response)
print(final_response_dict["reason"])
```