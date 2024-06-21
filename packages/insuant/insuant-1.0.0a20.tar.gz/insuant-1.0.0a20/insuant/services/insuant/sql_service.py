# pip install --upgrade --quiet  langchain langchain-community langchain-openai

import os
from dotenv import load_dotenv
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
import yaml
from langchain_community.vectorstores import FAISS
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import UnstructuredExcelLoader
from onnxruntime.transformers.shape_infer_helper import file_path
from insuant.database import prestoDb
from langchain.sql_database import SQLDatabase


import pandas as pd

from insuant.services.insuant.prompt_parameters import PromptService


class SQL_Service():
    db = None
    # db = SQLDatabase.from_uri("presto://localhost:8080/mongodb/bank")
    format = 'simple'
    examples = None
    db_schema = None
    def __init__(self):
        print("SQL Agent Initialized")
        ps = PromptService()
        # Rest of the code remains unchanged
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

        self.db = SQLDatabase.from_uri(ps.getConfig('connection_string'))
        self.examples = ps.getConfig('examples')
        self.db_schema = ps.getConfig('db_schema_str')
        # self.db = prestoDb
        # self.db =  SQLDatabase.from_uri("presto://localhost:8080/mongodb/bank")
        self.format = 'simple'

    def set_format(self, format='simple'):
        self.format = format

    def run_query(self, query):
        print('Running query:', query)
        try:
            list_of_tuples = eval(self.db.run(query))
            # Convert the list to a list of lists, because JSON doesn't support tuples
            return [list(tup) for tup in list_of_tuples]
        except Exception as e:
            print('Error run_query : ', e)
            return []
        # finally:
        # Optional finally block that always executes, regardless of whether an exception occurred
        # print("Finally block executed.")

    def get_catalogs(self):
        query = "SHOW Catalogs"
        return self.run_query(query)

    def get_schemas(self, catalog):
        query = f"SHOW SCHEMAS FROM {catalog}"
        return self.run_query(query)

    def get_tables(self, catalog, schema):
        query = f"SHOW TABLES FROM {catalog}.{schema}"
        return self.run_query(query)

    def get_columns(self, catalog, schema, table):
        query = f"SHOW COLUMNS FROM {catalog}.{schema}.{table}"
        return self.run_query(query)

    def get_top_rows(self, catalogname, schemaname, tablename):
        query = f"SELECT * FROM {catalogname}.{schemaname}.{tablename} LIMIT 1"
        return self.run_query(query)

    # Retrieve the schema from the database
    def db_schema_str_from_db(self, client, format='simple'):

        catalogs = self.get_catalogs(client)
        if format == 'detailed':
            catalog_hierarchy = {
                'type': 'presto',
                'name': 'catalogs',
                'children': []
            }
        else:
            catalog_hierarchy = []

        for catalog in catalogs:
            catalogname = catalog[0]
            if (catalogname == 'jmx' or catalogname == 'tpch' or catalogname == 'system'):
                continue
            if format == 'detailed':
                catalog_dict = {
                    'type': 'database',
                    'name': catalogname,
                    'children': []
                }
            schemas = self.get_schemas(client, catalogname)
            for schema in schemas:
                schemaname = schema[0]
                if (schemaname == 'information_schema' or schemaname == 'pg_catalog'):
                    continue
                if format == 'detailed':
                    schema_dict = {
                        'type': 'schema',
                        'name': schemaname,
                        'children': []
                    }
                tables = self.get_tables(client, catalogname, schemaname)
                for table in tables:
                    tablename = table[0]
                    if format == 'detailed':
                        table_dict = {
                            'type': 'table',
                            'name': tablename,
                            'children': self.get_columns(catalogname, schemaname, tablename),
                            'sample': self.get_top_rows(catalogname, schemaname, tablename)
                        }
                        schema_dict['children'].append(table_dict)
                    else:
                        table_dict = {
                            'table_name': catalogname + '.' + schemaname + '.' + tablename,
                            'table_columns': self.get_columns(catalogname, schemaname, tablename),
                            'sample_row_data': self.get_top_rows(catalogname, schemaname, tablename)
                        }
                        catalog_hierarchy.append(table_dict)
                if format == 'detailed':
                    catalog_dict['children'].append(schema_dict)
            if format == 'detailed':
                catalog_hierarchy['children'].append(catalog_dict)

        return catalog_hierarchy

    def db_schema_str(self):
        #sr = self.db_schema_str_from_db("mongodb")
        #print ("#### DB Asc", sr)

        return self.db_schema
    def run_chain_query(self, query):

        query = query.strip()  # Trim leading and trailing spaces
        if query.endswith(";"):  # Check if query ends with a semicolon
            query = query[:-1]  # Remove the semicolon
        result = self.run_query(self.db, query)
        print('Result:', result)

        return result

    def excel_to_text(self, fpath):
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Convert the DataFrame to text
        text = df.to_string(index=False)

        return text

    def sql_custom_agent(self):

        # Large Database
        from langchain.chains.openai_tools import create_extraction_chain_pydantic
        from langchain_core.pydantic_v1 import BaseModel, Field
        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

        class Table(BaseModel):
            """Table in SQL database."""
            name: str = Field(description="Name of table in SQL database.")

        # table_names = "\n".join(db.get_usable_table_names())
        table_names = self.db_schema_str()

        if format == 'detailed':
            system = f"""Based on the table schema below, return the names of ALL the SQL tables that MIGHT be relevant to the user question. 

                The schema is from a Presto SQL engine and contains multiple databases. You need to identify which database and its table to query based on the user's question.

                Schema Insights:
                Engine: Presto
                Catalogs: 
                - Database: postgresql
                    - Schema: public
                    - Table: document
                        - Description: Contains the details of the documents uploaded in the system. document.texts column contains the text extracted from the document and name column contains the name of the document.
                        - Columns: id (integer), name (varchar), description (varchar), doc_summary (varchar), owner_id (integer), is_active (boolean), chat_history (varchar), texts_4k_token (varchar), texts (varchar), tables (varchar), table_summary (varchar)
                    - Table: items
                        - Columns: id (integer), title (varchar), description (varchar), owner_id (integer), is_active (boolean)
                - Database: mongodb
                    - Schema: public     
                    - Table: orders
                        - Columns: orderkey (bigint), orderstatus (varchar), totalprice (double), orderdate (varchar)
                        - Sample Data: [1, 'San Francisco', 13.0, '']

                Presto catalog schema with table names; {table_names}

                Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed.

                Output format: 'database name'.'schema name'.'table name' for each table.
                """
        else:
            system = f"""Based on the table schema below, return the names of ALL the SQL tables that MIGHT be relevant to the user question. 
                The table_names is from a Presto SQL engine and contains multiple databases in the format of catlog.database.table format. 
                Use all database name, table name, column name and the sample data provided to identify the relevent tables.

                /nTable and column names; {table_names}

                /nRemember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed.
                """

        table_chain = create_extraction_chain_pydantic(Table, llm, system_message=system)
        response = table_chain.invoke({"input": "Get all the details about the customer = Lindsay Cowan"})
        # print(response)

        # Chain

        if format == 'simple':
            template = """Based on the table schema below, question, sql query, and sql response, write a natural language response like chatting with the user:
                The table_names is from a Presto SQL engine and contains multiple databases in the format of catlog.database.table format. 

                /nTable and column names; {table_names}

                /n Question: {question}
                /n SQL Query: {query}
                /n SQL Response: {response}"""
        else:
            template = """Based on the table schema below, question, sql query, and sql response, write a natural language response like chatting with the user:

                The schema is from a Presto SQL engine and contains multiple databases. You need to identify which database and its table to query based on the user's question.

                Schema Insights:
                    Engine: Presto
                    Catalogs: 
                    - Database: postgresql
                    - Schema: public
                        - Table: document
                        - Columns: id (integer), name (varchar), description (varchar), doc_summary (varchar), owner_id (integer), is_active (boolean), chat_history (varchar), texts_4k_token (varchar), texts (varchar), tables (varchar), table_summary (varchar)
                        - Sample Data: [147, '20240308_Bundle045401_Intapp_ALGoodbodyLLP_v1.pdf', '(/Users/prem/Prem/projects/gds/ai-saas/data/in/,20240308_Bundle045401_Intapp_ALGoodbodyLLP_v1.pdf," document text and table summaries.")','pdf extract in text format' , '', None]
                        - Table: items
                        - Columns: id (integer), title (varchar), description (varchar), owner_id (integer), is_active (boolean)
                    - Database: mongodb
                    - Schema: public     
                        - Table: orders
                        - Columns: orderkey (bigint), orderstatus (varchar), totalprice (double), orderdate (varchar)
                        - Sample Data: [1, 'San Francisco', 13.0, '']
                        - Table: users
                        - Columns: id (integer), email (varchar(50)), password (varchar(50)), is_active (varchar(50)), is_superuser (varchar(50)), is_verified (varchar(50))
                        - Table: worksheet
                        - Columns: id (integer), title (varchar), description (varchar), owner_id (integer), is_active (boolean)

                Schema:{schema}

                Question: {question}
                SQL Query: {query}
                Output: {response}"""

            # prompt_response = ChatPromptTemplate.from_template(template)

    ######## SQL Agent #####

    # def chat_

    def init_sql_agent(self, histroy=[]):

        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        # agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)



        selector = SemanticSimilarityExampleSelector.from_examples(
            self.examples,
            OpenAIEmbeddings(),
            FAISS,
            k=5,
            input_keys=["input"],
        )

        system_prefix = """You are an agent designed to interact with a SQL database.
                Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
                Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
                You can order the results by a relevant column to return the most interesting examples in the database.
                Never query for all the columns from a specific table, only ask for the relevant columns given the question.
                You have access to tools for interacting with the database.
                Only use the given tools. Only use the information returned by the tools to construct your final answer.
                You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

                DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
                DO NOT add semi colon(;) at the end of the query.
                Use REGEXP_LIKE for joining array columns, instead of UNNEST.  

                If the question does not seem related to the database, just return "I don't know" as the answer.\n """

        system_prefix += "Here is the chat history with user, user will ask questions based on this so reffer history and form the query: [ \n " + str(
            histroy) + " ]\n"

        system_prefix += 'Here is the table schema for the database: [/n'

        # Add the schema to the system prefix
        system_prefix += self.db_schema_str()

        system_prefix += " /n] Here are some examples of user inputs and their corresponding SQL queries:"

        few_shot_prompt = FewShotPromptTemplate(
            example_selector=selector,
            example_prompt=PromptTemplate.from_template(
                "User input: {input}\nSQL query: {query}"
            ),
            input_variables=["input", "dialect", "top_k"],
            prefix=system_prefix,
            suffix="",
        )

        # print(few_shot_prompt)

        full_prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(prompt=few_shot_prompt),
                ("human", "{input}"),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )

        agent = create_sql_agent(
            llm=llm,
            db=self.db,
            prompt=full_prompt,
            verbose=True,
            agent_type="openai-tools",
        )

        # agent.invoke({"input": "get all details about customer Leslie Martinez like sales, airnab listing and accounts"})
        # agent.invoke({"input": "how many documents are there in the database. List all the contracts from DealCloud"})

        return agent
        # schema=db_schema_str(""),

    def processFiles(self, files):
        text = ""
        print('Processing Files: ', files)

        for file in files:
            loader = UnstructuredExcelLoader(file)
            print('Loader: ', loader)
            docs = loader.load()
            print('Docs: ', docs)
            # for page in pdf_reader.pages:
            text += docs
        return text

    def processCvsFiles(self, files):
        text = ""
        print('Processing Files: ', files)

        for file in files:
            loader = UnstructuredExcelLoader(file)
            print('Loader: ', loader)
            docs = loader.load()
            print('Docs: ', docs)
            # for page in pdf_reader.pages:
            text += docs
        return text


def main():
    sagent = SQL_Service()
    # Method 1 - LC SQL Agent
    sql_agent = sagent.init_sql_agent()

    ## Streamlit App
    import streamlit as st
    st.set_page_config(page_title="SQL Agent", layout="wide")
    st.header("Retrieve Customer Information")

    question = st.text_input("Input: ", key="input")
    submit = st.button("Ask the question")

    # if submit is clicked
    if submit:
        response = sql_agent.invoke({"input": question});
        print('Method 1: /n', response)
        st.header(response)

        # st.subheader("The Response is")
        # for row in response:
        #    for key, value in row.items():
        #        print(key, value)
        #        if key == 'output': 
        #            st.header(value)

    with st.sidebar:
        st.title("Menu:")
        files = st.file_uploader("Upload your Files and Click on the Submit & Process Button", type="xls",
                                 accept_multiple_files=False)
        print('Files on main: ', files)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                text = sagent.processFiles(files)
                st.text_area("Text", text, height=200)
                st.success("Done")

# if __name__ == "__main__":
#    main()
