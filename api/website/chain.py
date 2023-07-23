from combine import combine_llm
from map import map_llm
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains import MapReduceChain
# from langchain.document_loaders import 
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


reduce_chain = StuffDocumentsChain(llm_chain=combine_llm, document_variable_name="doc")

map_chain = MapReduceDocumentsChain(
    llm_chain=map_llm,
    reduce_documents_chain=reduce_chain,
    document_variable_name="doc"
)

chain = MapReduceChain(
    combine_documents_chain=map_chain,
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
)


def get_chain_output(html: str, desc: str) -> str:
    return chain.run(input_text=html, job_description=desc)