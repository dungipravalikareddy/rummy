import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import initialize_agent

load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DATABASE')}"
)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True  # 👈 Add this
)

def ask_query(query: str):
    return agent_executor.run(query)
