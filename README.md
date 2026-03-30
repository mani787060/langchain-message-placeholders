# LangChain Message Placeholders
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green)](https://www.langchain.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

## 🏗️ Project Overview
This repository demonstrates how to use **MessagesPlaceholder** in LangChain to build flexible, stateful AI applications. While standard prompt templates use fixed strings, `MessagesPlaceholder` allows for a variable number of messages (like a full chat history) to be injected into a specific spot in the prompt, making it the industry standard for building conversational agents with memory.

---

## 🛠️ Key Technical Implementations

### 1. Dynamic Prompt Architectures
* **`ChatPromptTemplate` Integration:** Designing prompts that accommodate a `SystemMessage` at the start and a `MessagesPlaceholder` for the evolving conversation.
* **Variable Injection:** Passing lists of `BaseMessage` objects (HumanMessage, AIMessage) into the placeholder at runtime.

### 2. LCEL Pipeline Construction
* **Chain Composition:** Building a clean, readable pipeline using LangChain Expression Language (LCEL): `prompt | model | output_parser`.
* **Contextual Awareness:** Enabling the model to view the entire chat history as a structured sequence of messages rather than a single flattened string.

### 3. State Management
* **Memory Simulation:** Demonstrating how placeholders serve as the "input slot" for external memory components or manual history lists.

### 4. Enterprise Best Practices
* **Environment Security:** Protecting API keys with `.env` files.
* **Type Safety:** Utilizing LangChain's internal message classes to ensure structural consistency.

---

## 💻 Tech Stack
* **Language:** Python
* **Orchestration:** LangChain
* **LLM Providers:** OpenAI / Google Gemini
* **Environment:** `python-dotenv`



