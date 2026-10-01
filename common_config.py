import os
from dotenv import load_dotenv
load_dotenv(override = True)

api_key = os.getenv("LLM_API_KEY")
BASE_URL = "https://monogpt.kr/api/monorouter/v1"

from langchain_openai import ChatOpenAI

def llm_connect(
    model: str,
    api_key: str = api_key,
    temperature: float = 0, # 기본값 고정.
    max_tokens: int = 512   # 기본값 고정.   
):
    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=BASE_URL,
        temperature=temperature,
        use_responses_api=False,
        max_tokens=max_tokens,
    )