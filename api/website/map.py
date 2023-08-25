import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
# from langchain.document_loaders import UnstructuredHTMLLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from dotenv import load_dotenv

load_dotenv()

openai = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.7)

# map_examples = [
#     {
#         'doc': "Leonardo di ser Piero da Vinci[b] (15 April 1452 – 2 May 1519) was an Italian polymath of the High Renaissance who was active as a painter, draughtsman, engineer, scientist, theorist, sculptor, and architect.[3] While his fame initially rested on his achievements as a painter, he also became known for his notebooks, in which he made drawings and notes on a variety of subjects, including anatomy, astronomy, botany, cartography, painting, and paleontology. Leonardo is widely regarded to have been a genius who epitomized the Renaissance humanist ideal,[4] and his collective works comprise a contribution to later generations of artists matched only by that of his younger contemporary, Michelangelo.",
#         'job_description': "Art historian who studies the art of the Renaissance period",
#         'output': "Leonardo Da Vinci was an Italian Polymath\nLeonardo Da Vinci was a painter, engineer, scientist, and many other things",
#     },
#     {
#         'doc': "The analytical engine was a proposed mechanical general-purpose computer designed by English mathematician and computer pioneer Charles Babbage.[2][3] It was first described in 1837 as the successor to Babbage's difference engine, which was a design for a simpler mechanical calculator.[4] The analytical engine incorporated an arithmetic logic unit, control flow in the form of conditional branching and loops, and integrated memory, making it the first design for a general-purpose computer that could be described in modern terms as Turing-complete.",        
#         'job_description': 'Computer historian and computer scientist who catalogues the history of computers',
#         'output': "The analytical engine was proposed by Charles Babbage\nIt was the first Turing-complete device\nIt had an arithmetic logic unit, branching, and conditionals",
#     },
# ]

examples = [
    {
        'doc': "Leonardo di ser Piero da Vinci[b] (15 April 1452 – 2 May 1519) was an Italian polymath of the High Renaissance who was active as a painter, draughtsman, engineer, scientist, theorist, sculptor, and architect.[3] While his fame initially rested on his achievements as a painter, he also became known for his notebooks, in which he made drawings and notes on a variety of subjects, including anatomy, astronomy, botany, cartography, painting, and paleontology. Leonardo is widely regarded to have been a genius who epitomized the Renaissance humanist ideal,[4] and his collective works comprise a contribution to later generations of artists matched only by that of his younger contemporary, Michelangelo.",
        # 'job_description': "Art historian who studies the art of the Renaissance period",
        'output': "Leonardo Da Vinci was an Italian Polymath\nLeonardo Da Vinci was a painter, engineer, scientist, and many other things"
    },
    {
        'doc': "The analytical engine was a proposed mechanical general-purpose computer designed by English mathematician and computer pioneer Charles Babbage.[2][3] It was first described in 1837 as the successor to Babbage's difference engine, which was a design for a simpler mechanical calculator.[4] The analytical engine incorporated an arithmetic logic unit, control flow in the form of conditional branching and loops, and integrated memory, making it the first design for a general-purpose computer that could be described in modern terms as Turing-complete.",        
        # 'job_description': 'Computer historian and computer scientist who catalogues the history of computers',
        'output': "The analytical engine was proposed by Charles Babbage\nIt was the first Turing-complete device\nIt had an arithmetic logic unit, branching, and conditionals",
    },
]

example_template = "Document info: {doc}\n\nJob Description: {job_description}\n\nOutput:\n{output}"
example_prompt = PromptTemplate(template=example_template, input_variables=['doc', 'job_description', 'output'])

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="You are a summarizer who receives text extracted from a webpage and converts the words into notes consisting of important and key points separated by new lines. Format your curated information as a list of information where each piece of information is separated by a newline.",
    suffix="Document info: {doc}\n\nOutput:",
    input_variables=['doc']
)

map_llm = LLMChain(llm=openai, prompt=prompt)

def create_map_llm(job_desc: str):
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="You are a summarizer who receives text extracted from a webpage and converts the words into notes consisting of important and key points separated by new lines. Format your curated information as a list of information where each piece of information is separated by a newline.",
        suffix="Document info: {doc}\n\nOutput:",
        input_variables=['doc']
    )

    return LLMChain(llm=openai, prompt=prompt)