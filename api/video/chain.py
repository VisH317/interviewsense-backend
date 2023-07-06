from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import MapReduceChain
from langchain.text_splitter import CharacterTextSplitter

from prompts import map_llm_chain, reduce_llm_chain


reduce_chain = StuffDocumentsChain(llm_chain=reduce_llm_chain, document_variable_name="information")

map_chain = MapReduceDocumentsChain(
    llm_chain=map_llm_chain,
    reduce_documents_chain=reduce_chain,
    document_variable_name="information",
)

chain = MapReduceChain(
    combine_documents_chain=map_chain,
    text_splitter=CharacterTextSplitter(separator="\n\n", chunk_size=500, chunk_overlap=50, length_function=len)
)
