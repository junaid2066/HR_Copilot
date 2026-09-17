import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY','')
OPENAI_MODEL=os.getenv('OPENAI_MODEL','gpt-4o-mini')
DB_PATH=os.getenv('DB_PATH','data/hr_copilot.db')
