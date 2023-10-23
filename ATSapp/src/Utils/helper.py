import os
from functools import lru_cache
from src.Tasks.openai_caller import OpenAICaller


async def create_dir(dir_path: str):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


async def delete_dir(dir_path: str):
    if not os.path.exists(dir_path):
        os.system(f"rm -rf {dir_path}")


@lru_cache(maxsize = 1)
def get_openaicaller_instance():
    return OpenAICaller()