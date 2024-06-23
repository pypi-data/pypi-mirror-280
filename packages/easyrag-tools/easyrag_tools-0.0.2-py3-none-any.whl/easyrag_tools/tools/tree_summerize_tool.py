from llama_index.core.base.query_pipeline.query import QueryComponent
from llama_index.core.response_synthesizers import TreeSummarize

from promptflow.core import ToolProvider, tool
from promptflow.connections import OpenAIConnection

from easyrag_tools.tools.utils import (
    gen_openai_like_model,
    base_model_to_dict,
    parse_node_with_score,
)


class BaseSynthesizer:
    def __init__(self, synthesizer):
        self.synthesizer = synthesizer

    def get_synthesizer_component(self) -> QueryComponent:
        return self.synthesizer.as_query_component()

    @base_model_to_dict
    def synthesize(self, query_str: str, raw_nodes: list) -> str:
        component = self.get_synthesizer_component()
        nodes = [parse_node_with_score(n) for n in raw_nodes]
        res = component.run_component(query_str=query_str, nodes=nodes)

        return res.get("output").response


class MyTreeSummarize(ToolProvider, BaseSynthesizer):
    def __init__(
        self,
        llm_conn: OpenAIConnection,
    ):
        self.llm = gen_openai_like_model(llm_conn)
        self.synthesizer = TreeSummarize(llm=self.llm)
        super(ToolProvider, self).__init__(synthesizer=self.synthesizer)

    @tool
    def synthesize(self, query_str: str, nodes: list) -> str:
        return super().synthesize(query_str=query_str, raw_nodes=nodes)
