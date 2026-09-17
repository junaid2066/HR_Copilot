from database.seed import init_db
from agent.workflow import run_agent
init_db()
print(run_agent('Show workforce analytics')['answer'])
