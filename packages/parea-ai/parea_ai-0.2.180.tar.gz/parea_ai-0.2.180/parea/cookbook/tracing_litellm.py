import os

import openai
from dotenv import load_dotenv

from parea import Parea, trace

load_dotenv()

p = Parea(api_key=os.getenv("PAREA_API_KEY"))

client = openai.OpenAI(api_key="litellm", base_url="http://0.0.0.0:4000")
p.wrap_openai_client(client)


def llm_call(model: str):
    return client.chat.completions.create(model=model, messages=[{"role": "user", "content": "this is a test request, write a short poem"}])


@trace
def main():
    # request sent to model set on litellm proxy using config.yaml, `litellm --config config.yaml`
    response = llm_call(model="claude-3-haiku-20240307")
    response2 = llm_call(model="gpt-4o")
    response3 = llm_call(model="azure_gpt-3.5-turbo")
    return {"claude": response, "gpt": response2, "azure": response3}
    # response4 = llm_call(model="anthropic.claude-3-haiku-20240307-v1:0")
    # return {"claude": response, "gpt": response2, "azure": response3, "bedrock": response4}


if __name__ == "__main__":
    print(main())
