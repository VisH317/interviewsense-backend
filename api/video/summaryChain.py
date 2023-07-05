from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

map_reduce_examples = [
    {
        "information": "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.",
        "bullet_point_summary": "Python is easy to learn\nHas efficient data structures\nObject Oriented Programming Language\nUses dynamic typing\nFast Development"
    },
    {
        "information": "A marketing strategy is a plan for reaching a specific marketing-related goal (or goals) in a focused and achievable way. It takes into consideration what your business is currently doing well and what you're missing in regards to the objective you set, so you're more likely to accomplish it.",
        "bullet_point_summary": "Marketing Strategy: plan to reach marketing goal\nTake into consideration strengths and weaknesses of business"
    }
]

map_reduce_example_prompt = PromptTemplate(template="Information: {information}\n\nSummary in bullet points:\n{bullet_point_summary}", input_variables=["information", "bullet_point_summary"])

map_reduce_prompt = FewShotPromptTemplate(
    examples=map_reduce_examples,
    example_prompt=map_reduce_example_prompt
    prefix="You are a summarizer who receives text from a video, audio, or other transcript and converts the words into a bullet point summary consisting of important points, topics, and terms. You will receive an input"
)