from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def get_model():
    model = ChatOpenAI(model="gpt-4o-mini")
    return model

def __main__():
    try:
        llm = get_model()
        query = input("Enter your question: ")

        messages = [
            SystemMessage(content="You are an AI assistant with expertise in data analysis and automation."),
            HumanMessage(content=query),
        ]
        response = llm.invoke(messages)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    __main__()