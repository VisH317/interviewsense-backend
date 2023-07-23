from prompt import llm
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
# from langchain.document_loaders import 
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

chain = StuffDocumentsChain(llm_chain=llm, document_variable_name="doc")

def get_chain_output(html: str, desc: str) -> str:
    text_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.HTML, chunk_size=250, chunk_overlap=10)
    docs = text_splitter.create_documents([html])

    output = chain.run(input_documents=docs, job_description=desc)

    return output