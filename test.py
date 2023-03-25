import openai
from configs import configs

openai.api_key = configs.openai_apikey

prompt = "bikin resep nasi rendang"
max_tokens = 4000 - len(prompt.split(" "))
result = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0,
    suffix=">>> Bot Menjawab:\n"
)

print(result.choices[0].text)