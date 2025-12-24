from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/Users/arjun/Desktop/books/Pattern_Recp/Clustering.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator= ''
)

result = splitter.split_documents(docs)

print(result[0])