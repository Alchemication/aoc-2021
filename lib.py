def read_file(file_path: str, ret_raw: bool = False):
    with open(file_path, "r") as f:
        f_content = f.read()
        if ret_raw:
            return f_content
        f_content = [l for l in f_content.split("\n") if l != ""]
    return f_content
