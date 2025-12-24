from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template= 'answer the following question \n {question} from the following {text}',
    input_variables = ['question', 'text']
)
parser = StrOutputParser()

url = 'https://www.amazon.in/iPhone-Pro-256-Promotion-Breakthrough/dp/B0FQFYYPZF/ref=sr_1_2?crid=SBCKLHILVITU&dib=eyJ2IjoiMSJ9.fe1aCgDuqmbrzMipWrLkoX92o7ZIdNMO2-cPKM7B0CQ23kv6v4U8mE-nnAI4nvng4I1Zzx7ymUk_rgT9x4qjgScBHduvjnej28Gp2wtWvLBH_y2xMi5wCk609QGu6IbXbzWDdD92OtVXijNSes1tzYRL9ckS14sPq6rCZmBnIGhfaywZcuH8pCiDwUBd2vVwmqSNZLDbujukc1O3WXuCgJ1VnHHBvEHP2bjGsW9IHmc.O-b7BKKu8N4Dw3YeJP4Akyv7-Sxk_YMDOb9ezBOhPlU&dib_tag=se&keywords=iphone+17b+pro&qid=1766419754&sprefix=iphone+17b+pro%2Caps%2C229&sr=8-2'
loader = WebBaseLoader(url)

docs = loader.load()
# print(len(docs))
# # print(docs[0].page_content)

chain = prompt | model | parser
print = chain.invoke({'question': 'what is brand of the product', 'text':docs[0].page_content})