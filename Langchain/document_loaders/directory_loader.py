from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = '/Users/arjun/Desktop/books/Pattern_Recp',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)
docs = loader.load()
print(docs[0].page_content)