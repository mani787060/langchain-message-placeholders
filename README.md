# LangChain Message Placeholders

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Generative AI](https://img.shields.io/badge/Domain-Generative%20AI-purple)
![Prompt Engineering](https://img.shields.io/badge/Concept-Prompt%20Engineering-orange)

A hands-on Generative AI project demonstrating how to use `MessagesPlaceholder` in LangChain to build dynamic prompts that support conversational history and multi-turn interactions with large language models (LLMs).

## 📌 Project Overview

In a basic LLM application, a prompt may contain only the latest user input. However, a conversational chatbot often needs previous messages to understand follow-up questions and maintain context.

LangChain's `MessagesPlaceholder` provides a flexible way to insert a variable-length list of messages into a chat prompt. Instead of manually combining the entire conversation into a single string, developers can pass structured messages into a designated position in the prompt.

This project explores how message placeholders help organize prompts and prepare the foundation for context-aware conversational applications.

## 🎯 Project Objectives

- Understand the purpose of `MessagesPlaceholder` in LangChain.
- Create flexible chat prompts using `ChatPromptTemplate`.
- Insert conversation history as structured messages.
- Understand how prompt templates work with chat models.
- Explore LCEL for composing LLM application pipelines.
- Learn the basics of managing conversational context.

## ✨ Key Features and Concepts

### 1. Dynamic Chat Prompt Templates

`ChatPromptTemplate` helps define prompts containing different message roles, such as system instructions and user messages.

`MessagesPlaceholder` reserves a position where a list of messages can be inserted at runtime.

### 2. Structured Conversation History

LangChain provides message classes such as:

- `SystemMessage` — defines the model's instructions and behavior.
- `HumanMessage` — represents a user's message.
- `AIMessage` — represents an AI-generated response.

Using structured messages makes the conversation easier to organize and pass to compatible chat models.

### 3. Flexible Message Injection

A placeholder can receive a variable number of messages, making it useful for conversations that grow over multiple turns.

For example:

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

chat_history = [
    HumanMessage(content="What is machine learning?"),
    AIMessage(content="Machine learning enables systems to learn patterns from data.")
]

formatted_prompt = prompt.invoke({
    "chat_history": chat_history,
    "question": "Can you give me an example?"
})
```

In this example, the previous conversation is inserted into the prompt before the latest question. The example illustrates prompt construction; generating a response requires connecting the prompt to a chat model.

### 4. LangChain Expression Language (LCEL)

LangChain Expression Language provides a way to compose components into readable processing pipelines.

A typical pipeline may look like:

```python
chain = prompt | model
```

Here, the prompt prepares the messages, and the model generates a response. Additional components, such as output parsers, can be added when required.

### 5. Foundation for Conversational Memory

`MessagesPlaceholder` is not a complete memory system by itself. It provides a place to insert history supplied by your application or another component.

The application is responsible for storing, updating, and managing that history.

## 🧰 Tech Stack

- **Language:** Python
- **LLM Framework:** LangChain
- **Prompt Management:** `ChatPromptTemplate`
- **Message Handling:** `MessagesPlaceholder` and LangChain message classes
- **Pipeline Composition:** LangChain Expression Language (LCEL)
- **Configuration:** `python-dotenv`, if used in the implementation
- **LLM Provider:** Depends on the model integration configured in the project

## ⚙️ Getting Started

### Prerequisites

- Python 3.9 or a compatible version supported by your dependencies.
- An API key for the LLM provider used in the implementation.
- Basic familiarity with Python and LLM prompting.

### 1. Clone the Repository

```bash
git clone https://github.com/mani787060/langchain-message-placeholders.git
cd langchain-message-placeholders
```

### 2. Install Dependencies

Install the dependencies required by your Python file. A common starting point is:

```bash
pip install langchain-core langchain-google-genai python-dotenv
```

If your implementation uses OpenAI or another provider, install its corresponding LangChain integration instead.

### 3. Configure Environment Variables

If your implementation requires an API key, create a `.env` file in the project directory and add the appropriate variable, for example:

```env
GOOGLE_API_KEY=your_api_key_here
```

Use the variable name expected by your Python code. Add `.env` to `.gitignore` to avoid uploading credentials to GitHub.

### 4. Run the Python File

Run the actual Python filename in your repository:

```bash
python your_filename.py
```

Replace `your_filename.py` with the filename of your uploaded script.

## 🧠 What You Will Learn

By exploring this project, you can understand:

- How dynamic chat prompts are constructed.
- How previous messages can be injected into a prompt.
- Why structured messages are useful for multi-turn conversations.
- How prompts connect with chat models through LCEL.
- The difference between inserting history and managing persistent memory.

## 🔮 Future Improvements

- Build a complete chatbot with automatic history updates.
- Add conversation-history trimming or summarization.
- Persist conversations in a database.
- Add support for multiple LLM providers.
- Integrate retrieval-augmented generation (RAG) for document-based answers.
- Add error handling and automated tests.

## 🌍 Practical Applications

`MessagesPlaceholder` can be useful in:

- Multi-turn AI chatbots.
- Customer-support assistants.
- AI tutoring applications.
- Context-aware question-answering systems.
- RAG applications that combine conversation history with retrieved information.
- Agentic AI applications that need structured conversation context.

## 📝 Conclusion

`MessagesPlaceholder` is a useful building block for creating flexible conversational prompts in LangChain. By separating prompt structure from conversation history, developers can build cleaner and more maintainable LLM applications.

This project provides a foundation for progressing toward chatbots with managed conversation memory, RAG, and more advanced Generative AI workflows.
