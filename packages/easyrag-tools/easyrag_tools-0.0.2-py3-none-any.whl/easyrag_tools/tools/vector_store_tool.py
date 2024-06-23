from llama_index.core import StorageContext, load_index_from_storage, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.base.query_pipeline.query import QueryComponent

from promptflow.core import ToolProvider, tool
from promptflow.connections import CustomConnection

from easyrag_tools.tools.utils import (
    gen_dashscope_embed_model,
    base_model_to_dict,
    gen_adb_vector_store,
)


class BaseIndex:
    def __init__(self, index, embed_model, storage_ctx):
        self.index = index
        self.storage_context = storage_ctx
        self.embed_model = embed_model

    def get_retriever_component(self) -> QueryComponent:
        return self.index.as_retriever().as_query_component()

    @base_model_to_dict
    def retrieve(self, query: str) -> dict[str, any]:
        component = self.get_retriever_component()
        return component.run_component(input=query)


class MyVectorStoreIndex(ToolProvider, BaseIndex):
    def __init__(
        self,
        embed_conn: CustomConnection,
        adb_conn: CustomConnection = None,
        storage: str = None,
    ):
        self.index = None
        self.storage_path = storage

        if embed_conn:
            self.embed_conn = embed_conn
            self.embed_model = gen_dashscope_embed_model(embed_conn)

        if adb_conn:
            self.adb_conn = adb_conn
            self.vector_db = gen_adb_vector_store(adb_conn)
            self.storage_context = StorageContext.from_defaults(vector_store=self.vector_db)
            self.index = VectorStoreIndex.from_vector_store(
                vector_store=self.vector_db,
                embed_model=self.embed_model,
            )
        elif storage:
            self.storage_context = StorageContext.from_defaults(persist_dir=storage)
        else:
            raise ValueError("empty adb_conn and storage")

        super(ToolProvider, self).__init__(
            index=self.index,
            embed_model=self.embed_model,
            storage_ctx=self.storage_context,
        )

    @tool
    def build_index(self, content_path: str) -> str:
        reader = SimpleDirectoryReader(content_path)
        docs = reader.load_data()
        self.index = VectorStoreIndex.from_documents(
            documents=docs,
            embed_model=self.embed_model,
            storage_context=self.storage_context,
        )
        self.index.set_index_id("vector_index")
        if self.storage_path:
            self.storage_context.persist(self.storage_path)

        return "success"

    @tool
    def retrieve(self, query: str) -> dict:
        return super().retrieve(query=query)
