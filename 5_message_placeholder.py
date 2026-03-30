# Message placeholder is a special placeholder used inside a ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime. It allows you to create prompts that can adapt based on the conversation context, making it ideal for building chatbots or conversational agents that need to remember previous interactions.

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('C:\\Users\\munna\\Desktop\\langchain-models\\4.Prompts\\chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)

