from langchain_text_splitters import RecursiveCharacterTextSplitter
text = """

Verification services powered by SheerID
You are receiving this email because you submitted a verification request with YouTube and its verification service provider, SheerID.
SheerID will only contact you in regard to confirming your verification status. Your email address will not be added to any mailing list without your explicit request.
"""

# initialize the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0,
)
# perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)