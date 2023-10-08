import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain=LLMChain(prompt=prompt,
                     llm=HuggingFaceHub(repo_id="google/flan-t5-large",
                                        model_kwargs={"temperature":0,
                                                      "max_length":64}))

def LLm(question):
    return(llm_chain.run(question))

