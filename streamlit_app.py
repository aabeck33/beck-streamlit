import base64
import vanna as vn
import streamlit as st
from vanna.remote import VannaDefault
from tokens import QAS_TOKEN, QAS_DBSERVER, QAS_DATABASE, QAS_DBUSER, QAS_DBPASSWD, DEV_TOKEN, DEV_DBSERVER, DEV_DATABASE, DEV_DBUSER, DEV_DBPASSWD, PRD_TOKEN, PRD_DBSERVER, PRD_DATABASE, PRD_DBUSER, PRD_DBPASSWD


AMBIENTE = 'QAS'

#if __name__ == '__main__':
if AMBIENTE == 'QAS':
    urlbase = 'https://sesuiteqas.uniaoquimica.com.br'
    userToken = base64.b64decode(QAS_TOKEN).decode("utf-8")
    server = base64.b64decode(QAS_DBSERVER).decode("utf-8")
    database = base64.b64decode(QAS_DATABASE).decode("utf-8")
    username = base64.b64decode(QAS_DBUSER).decode("utf-8")
    passwd = base64.b64decode(QAS_DBPASSWD).decode("utf-8")
elif AMBIENTE == 'PRD':
    urlbase = 'https://sesuite.uniaoquimica.com.br'
    userToken = base64.b64decode(PRD_TOKEN).decode("utf-8")
    server = base64.b64decode(PRD_DBSERVER).decode("utf-8")
    database = base64.b64decode(PRD_DATABASE).decode("utf-8")
    username = base64.b64decode(PRD_DBUSER).decode("utf-8")
    passwd = base64.b64decode(PRD_DBPASSWD).decode("utf-8")
elif AMBIENTE == 'DEV':
    urlbase = 'https://sesuitedev.uniaoquimica.com.br'
    userToken = base64.b64decode(DEV_TOKEN).decode("utf-8")
    server = base64.b64decode(DEV_DBSERVER).decode("utf-8")
    database = base64.b64decode(DEV_DATABASE).decode("utf-8")
    username = base64.b64decode(DEV_DBUSER).decode("utf-8")
    passwd = base64.b64decode(DEV_DBPASSWD).decode("utf-8")
else:
    urlbase = ''
    userToken = ''


#vn = VannaDefault(model='chinook', api_key=vn.get_api_key('alvaroabeck@gmail.com'))

vn = VannaDefault(model='chinook', api_key='a020d36d58a541dbbef6dd8ce47e57f1')

vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')

#conn_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={passwd}'
#vn.connect_to_mssql(conn_string)

#vn.ask('What are the top 10 artists by sales?')

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()

'''
vn.set_api_key(st.secrets["vanna_api_key"])
vn.set_model('chinook')
my_question = st.session_state.get("my_question", default=None)
if my_question is None:
    st.image("chinook-schema.png", use_column_width=True)
    my_question = st.text_input("Ask me a question that I can turn into SQL", key="my_question")
else:
    st.title(my_question)
    sql = vn.generate_sql(my_question)
    st.code(sql, language='sql')
    df = vn.run_sql(sql)    
    st.dataframe(df, use_container_width=True)
    fig = vn.get_plotly_figure(plotly_code=vn.generate_plotly_code(question=my_question, sql=sql, df=df), df=df)
    st.plotly_chart(fig, use_container_width=True)
    st.button("Ask another question", on_click=lambda: st.session_state.clear())
'''

'''
# Modelo básico para testes.
from vanna.remote import VannaDefault
vn = VannaDefault(model='chinook', api_key='a020d36d58a541dbbef6dd8ce47e57f1')
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')
vn.ask('What are the top 10 artists by sales?')

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()
'''

'''
# usando um modelo meu.
from vanna.remote import VannaDefault
vn = VannaDefault(model='beck', api_key='a020d36d58a541dbbef6dd8ce47e57f1')
vn.connect_to_...() # Connect to your database here

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()
'''