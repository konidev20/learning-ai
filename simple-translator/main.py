from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def get_model():
    model = ChatOpenAI(model="gpt-4o-mini")
    return model

def __main__():
    try:
        llm = get_model()


        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that translates sentences from English to {language}, use latin letters for the response."),
            ("user", "{text}")
        ])

        query = input("Enter sentence to translate: ")

        prompt = prompt_template.format(language="Kannada", text=query)

        response = llm.invoke(prompt)
        print(f"Response: {response.content}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    __main__()