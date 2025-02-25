# LangChain



## Models

### 1、ollama

```python
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
    # other params...
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一名专业的分析师"),
    ("user", "{input}")
])
chain = prompt | llm | output_parser

print(chain.invoke({"input": "langchain的工作方式是什么？"}))
```

### 2、openai

```python
#使用openai的官方sdk
import openai
import os

openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("OPENAI_KEY")

messages = [
{"role": "user", "content": "介绍下你自己"}
]

res = openai.ChatCompletion.create(
    model="gpt-4-1106-preview",
    messages=messages,
    stream=False,
)
```

