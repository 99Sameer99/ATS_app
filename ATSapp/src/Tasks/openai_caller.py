from typing import Any
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import LanceDB
from langchain.docstore.document import Document
import lancedb
from langchain.document_loaders import PyMuPDFLoader
import openai
from src.Utils.config import Config


class OpenAICaller:
    def __init__(self):
        # self.encoder = HuggingFaceEmbeddings(
        #     model_name='sentence-transformers/all-MiniLM-L6-v2',
        #     model_kwargs={'device': 'cpu'}
        #     )

        self.encoder = OpenAIEmbeddings(openai_api_key= Config.OPENAI_KEY,
                                        model="text-search-ada-doc-001")

        vdb_conn = lancedb.connect(Config.VDB_LOCATION)
        # try:
        #     self.table = vdb_conn.create_table(
        #         name = Config.VDB_TABLENAME,
        #         data = [
        #             {
        #                 "vector": self.encoder.embed_query("Hello World"),
        #                 "text": Config.VDB_DUMMYTEXT,
        #                 "id": "1",
        #                 "source": ""
        #             }
        #         ],
        #         mode = "overwrite"
        #     )
        # except Exception as e:
        #     print(f"[ERROR] {str(e)}")
        #     self.table = vdb_conn.open_table(name = Config.VDB_TABLENAME)
        self.table = vdb_conn.create_table(
                name = Config.VDB_TABLENAME,
                data = [
                    {
                        "vector": self.encoder.embed_query("Hello World"),
                        "text": Config.VDB_DUMMYTEXT,
                        "id": "1",
                        "source": ""
                    }
                ],
                mode = "overwrite"
            )
    
    
    def get_relevant_resumes(self, job_description: str):
        retriver = LanceDB(
                embedding = self.encoder,
                connection = self.table
            )
        resume_objs = retriver.search(
            job_description,
            search_type = "similarity",
            k = Config.NUM_TOP_RESUMES
        )
        return resume_objs
    
    def handle_pdf_push(self, file_path : str) -> Any:
        
        documents = PyMuPDFLoader(file_path).load()
        return LanceDB.from_documents(
            documents = documents,
            embedding = self.encoder,
            connection = self.table
        )
    
