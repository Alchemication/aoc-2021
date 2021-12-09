from typing import Union


def read_file(f_path: str, ret_raw: bool = False) -> Union[list, str]:
    with open(f_path, "r") as f:
        f_content = f.read()
        if ret_raw:
            return f_content
        return [r for r in f_content.split("\n") if r != ""]
