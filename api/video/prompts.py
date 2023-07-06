import os
from langchain.chains import LLMChain
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(os.environ["OPENAI_API_KEY"])


map_examples = [
    {
        "information": "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.",
        "bullet_point_summary": "Python is easy to learn\nHas efficient data structures\nObject Oriented Programming Language\nUses dynamic typing\nFast Development",
    },
    {
        "information": "A marketing strategy is a plan for reaching a specific marketing-related goal (or goals) in a focused and achievable way. It takes into consideration what your business is currently doing well and what you're missing in regards to the objective you set, so you're more likely to accomplish it.",
        "bullet_point_summary": "Marketing Strategy: plan to reach marketing goal\nTake into consideration strengths and weaknesses of business",
    },
]

map_example_prompt = PromptTemplate(
    template="Information: {information}\n\nSummary in bullet points:\n{bullet_point_summary}",
    input_variables=["information", "bullet_point_summary"],
)

map_prompt = FewShotPromptTemplate(
    examples=map_examples,
    example_prompt=map_example_prompt,
    prefix="You are a summarizer who receives text from a video, audio, or other transcript and converts the words into a bullet point summary consisting of important points, topics, and terms. You will receive an input that is a transcript from a video or audio, and might be in a conversational style. Convert the provided information into a summary in bullet point format. Include only the summarized points and nothing else, and have each point on its own newline",
    suffix="information: {information}\n\nSummary in bullet points:",
    input_variables=["information"]
)

reduce_prompt = PromptTemplate(
    "You are a summarizer and information extractor. You are given a list of bullet points about a certain topic and you must take all the bullet point information and create a combined list of bullet points and filter them out based on which ones are most relevant. Remove any redundant information and modify wording as necessary to be as clear as possible.\n\nBullet Info:\n{information}\n\nSummarized Bullet Point Info: ",
    input_variables=["information"]
)

map_llm_chain = LLMChain(llm=openai, prompt=map_prompt)
reduce_llm_chain = LLMChain(llm=openai, prompt=reduce_prompt)


