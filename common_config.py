import os
from dotenv import load_dotenv
load_dotenv(override = True)

api_key = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")

model = "gpt-5.4-mini"
temperatuyre = 0
max_tokens = 2086

from langchain_openai import ChatOpenAI

def llm_connect(
    model: str = model,     # 기본값: 위에서 정의한 전역 model
    api_key: str = api_key,
    temperature: float = 0, # 기본값 고정.
    max_tokens: int = 512   # 기본값 고정.   
):
    return ChatOpenAI(
        model = model,
        api_key=api_key,
        base_url=BASE_URL,
        temperature=temperature,
        use_responses_api=False,
        max_tokens=max_tokens,
    )


from langchain_openai import OpenAIEmbeddings

def embedding_model():
    embeddings = OpenAIEmbeddings(
        api_key = api_key,
        base_url = BASE_URL,
        # use_responses_api=False, 에러 남
        model = "text-embedding-3-small"
        )
    return embeddings