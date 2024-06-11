import vanna as vn
import streamlit as st
from vanna.remote import VannaDefault

#vn = VannaDefault(model='chinook', api_key=vn.get_api_key('alvaroabeck@gmail.com'))

vn = VannaDefault(model='chinook', api_key='a020d36d58a541dbbef6dd8ce47e57f1')
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')
vn.ask('What are the top 10 artists by sales?')

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
    st.button("Ask another question", on_click=lambda: st.session_state.clear())'''



'''
# Modelo básico para testes.
from vanna.remote import VannaDefault
vn = VannaDefault(model='chinook', api_key='a020d36d58a541dbbef6dd8ce47e57f1')
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')
vn.ask('What are the top 10 artists by sales?')

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()'''

'''
# usando um modelo meu.
from vanna.remote import VannaDefault
vn = VannaDefault(model='beck', api_key='a020d36d58a541dbbef6dd8ce47e57f1')
vn.connect_to_...() # Connect to your database here

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()'''