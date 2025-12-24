from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader = PyPDFLoader('matrice_ai.pdf')
# pypdf loader not performing  better fror scanned pdfs
# if working with pdf in which so many tables and column are present  then use -> PDFPlumberloader
docs = loader.load()
print(len(docs))
print(docs[0].metadata)
