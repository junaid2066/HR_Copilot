import streamlit as st
from database.seed import init_db
from database.db_connection import get_connection
from agent.workflow import run_agent
init_db()
st.set_page_config(page_title='HR Copilot',page_icon='👥',layout='wide')
st.markdown('''<style>.block-container{padding-top:1.5rem}.hero{padding:1.4rem;border-radius:18px;background:linear-gradient(120deg,#102a43,#1f7a5c);color:white;margin-bottom:1rem}.small{opacity:.85}</style>''',unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>👥 HR Copilot</h1><div class="small">Agentic AI-Powered Human Resource Assistant</div></div>',unsafe_allow_html=True)
con=get_connection(); total=con.execute('select count(*) from employees').fetchone()[0]; avail=con.execute('select count(*) from employees where status="Available"').fetchone()[0]; depts=con.execute('select count(distinct department) from employees').fetchone()[0]; con.close()
a,b,c=st.columns(3); a.metric('Employees',total); b.metric('Available',avail); c.metric('Departments',depts)
with st.sidebar:
    st.header('HR Copilot')
    page=st.radio('Navigate',['AI Assistant','Employee Directory','HR Analytics','Policy Center','About'])
    st.divider(); st.caption('Human approval is required for consequential employment decisions.')
if page=='AI Assistant':
    st.subheader('Agentic HR Assistant')
    st.caption('Try: “Build a Python + ML team”, “What is the annual leave policy?”, or “Show workforce analytics”.')
    if 'messages' not in st.session_state: st.session_state.messages=[]
    for m in st.session_state.messages:
        with st.chat_message(m['role']): st.markdown(m['content'])
    if q:=st.chat_input('Ask HR Copilot...'):
        st.session_state.messages.append({'role':'user','content':q})
        with st.chat_message('user'): st.markdown(q)
        with st.chat_message('assistant'):
            with st.spinner('Agent is reasoning and selecting tools...'): r=run_agent(q)
            st.markdown(r['answer'])
            with st.expander('Agent execution trace'):
                for i,s in enumerate(r['steps'],1): st.write(f'{i}. {s}')
        st.session_state.messages.append({'role':'assistant','content':r['answer']})
elif page=='Employee Directory':
    import pandas as pd
    con=get_connection(); df=pd.read_sql_query('select * from employees',con); con.close()
    q=st.text_input('Search directory')
    if q: df=df[df.astype(str).apply(lambda r:r.str.contains(q,case=False).any(),axis=1)]
    st.dataframe(df,use_container_width=True,hide_index=True)
elif page=='HR Analytics':
    import pandas as pd
    con=get_connection(); df=pd.read_sql_query('select * from employees',con); con.close()
    st.subheader('Workforce Analytics'); st.bar_chart(df.groupby('department').size())
    st.dataframe(df.groupby('department').agg(Employees=('id','count'),Avg_Performance=('performance','mean'),Avg_Experience=('experience','mean')).round(2),use_container_width=True)
elif page=='Policy Center':
    st.subheader('HR Policy Knowledge Base'); st.text(open('data/hr_policies.txt',encoding='utf-8').read())
else:
    st.subheader('About the Capstone'); st.write('HR Copilot demonstrates agent reasoning, tool calling, structured employee data access, policy retrieval, team matching, analytics, safety guardrails, a Streamlit UI, tests, Docker deployment, and CI.')
