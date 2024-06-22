from llama_index.core import StorageContext, load_index_from_storage, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.base.query_pipeline.query import QueryComponent

from promptflow.core import ToolProvider, tool
from promptflow.connections import CustomConnection

from easyrag_tools.tools.utils import (
    gen_dashscope_embed_model,
    base_model_to_dict,
)


class BaseIndex:
    def __init__(self, index):
        self.index = index

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
        storage: str,
    ):
        if embed_conn:
            self.embed_conn = embed_conn
            self.embed_model = gen_dashscope_embed_model(embed_conn)

        if storage:
            self.storage_path = storage
            self.storage_context = StorageContext.from_defaults(persist_dir=storage)
            self.index = load_index_from_storage(
                self.storage_context,
                index_id="vector_index",
                embed_model=self.embed_model,
            )

        super(ToolProvider, self).__init__(index=self.index)

    @tool
    def build_index(self, content_path: str) -> str:
        reader = SimpleDirectoryReader(content_path)
        docs = reader.load_data()
        self.index = VectorStoreIndex.from_documents(documents=docs, embed_model=self.embed_model)
        self.index.set_index_id("vector_index")

        if self.storage_path:
            self.index.storage_context.persist(self.storage_path)

        return "success"

    @tool
    def retrieve(self, query: str) -> dict:
        return super().retrieve(query=query)
