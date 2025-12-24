from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

model1 = ChatOpenAI()
model2 = ChatAnthropic(model_name = 'claude-3-7-sonnet-20250219')

prompt1 = PromptTemplate(
    template = 'Generate a short & simple notes from the following \n {text}',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short question answer from the following text \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and questions into a single document \n notes-> {notes} and quiz-> {quiz}',
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merged_chain = prompt3 | model1 | parser
chain = parallel_chain | merged_chain

text = """Support Vector Machine (SVM) is a supervised machine learning algorithm used for class
ification and regression tasks that works by finding an optimal decision boundary,
 called a hyperplane, which best separates data points of different classes. The key idea behind 
 SVM is to maximize the margin—the distance between the hyperplane and the nearest data points from each class,
   known as support vectors—so that the model generalizes well to unseen data.
     SVM can handle both linearly separable and non-linearly separable data by using kernel functions such as
   linear, polynomial, and radial basis function (RBF) to map data into higher-dimensional space.
     It is effective in high-dimensional datasets and is robust to overfitting, especially when the number of features is large,
     but it can be computationally expensive for very large datasets.
"""

# result = chain.invoke({"text" : text})
# print(result)

chain.get_graph().print_ascii()