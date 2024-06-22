from ruamel.yaml import YAML
from pathlib import Path

from llama_index.core.bridge.pydantic import BaseModel
from llama_index.core.schema import BaseNode, NodeWithScore
from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.dashscope import (
    DashScopeEmbedding,
    DashScopeTextEmbeddingModels,
    DashScopeTextEmbeddingType,
)

from promptflow.connections import OpenAIConnection, CustomConnection


def gen_openai_like_model(conn: OpenAIConnection):
    return OpenAILike(
        model="default",
        api_key=conn.api_key,
        api_base=conn.base_url,
        max_tokens=2048,
        context_window=4096,
        temperature=0.3,
    )


def gen_dashscope_embed_model(conn: CustomConnection):
    return DashScopeEmbedding(
        model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2,
        text_type=DashScopeTextEmbeddingType.TEXT_TYPE_DOCUMENT,
        api_key=conn.secrets["api_key"]
    )


def base_model_to_dict(component):
    def wrapper(*args, **kwargs) -> dict:
        res = component(*args, **kwargs)
        return format_base_model(res)

    return wrapper


def format_base_model(output):
    if isinstance(output, dict):
        for key, value in output.items():
            if isinstance(value, (dict, list)):
                format_base_model(value)
            elif isinstance(value, BaseModel):
                output[key] = value.to_dict()
    elif isinstance(output, list):
        for i in range(len(output)):
            element = output[i]
            if isinstance(element, (dict, list)):
                format_base_model(element)
            elif isinstance(element, BaseModel):
                output[i] = element.to_dict()

    return output


def parse_node_with_score(data: dict) -> NodeWithScore:
    if isinstance(data, NodeWithScore):
        return data

    return NodeWithScore(
        node=load_node(data.get("node", None)),
        score=data.get("score"),
    )


def load_node(data: dict) -> BaseNode:
    """Load BaseNode by name."""

    recognized_nodes = {
        cls.__name__: cls for cls in BaseNode.__subclasses__()}

    if isinstance(data, BaseNode):
        return data
    name = data.get("class_name", None)
    if name is None:
        raise ValueError("BaseNode loading requires a class_name")
    if name not in recognized_nodes:
        raise ValueError(f"Invalid BaseNode name: {name}")

    return recognized_nodes[name].from_dict(data)


def collect_tools_from_directory(base_dir) -> dict:
    tools = {}
    yaml = YAML()
    for f in Path(base_dir).glob("**/*.yaml"):
        with open(f, "r") as f:
            tools_in_file = yaml.load(f)
            for identifier, tool in tools_in_file.items():
                tools[identifier] = tool
    return tools


def list_package_tools():
    """List package tools"""
    yaml_dir = Path(__file__).parents[1] / "yamls"
    return collect_tools_from_directory(yaml_dir)
