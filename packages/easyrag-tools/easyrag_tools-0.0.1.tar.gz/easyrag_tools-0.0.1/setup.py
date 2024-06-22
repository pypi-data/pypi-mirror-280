from setuptools import find_packages, setup

PACKAGE_NAME = "easyrag_tools"

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    description="This is my tools package",
    packages=find_packages(),
    entry_points={
        "package_tools": ["hello_world_tool = easyrag_tools.tools.utils:list_package_tools"],
    },
    install_requires=[
        'llama_index-llms-openai_like==0.1.3',
        'llama_index.embeddings.dashscope==0.1.3',
        'llama_index==0.10.29',
    ],
    include_package_data=True,  # This line tells setuptools to include files from MANIFEST.in
)
