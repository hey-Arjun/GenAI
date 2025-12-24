from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model ='claude-3-5-sonnet',temperature =1.5 , max_completion_tokens=10)
result = model.invoke("What is the Capital of India")

print(result.content)
