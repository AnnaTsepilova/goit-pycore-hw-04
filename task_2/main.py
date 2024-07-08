from pathlib import Path

def get_cats_info(path: str) -> list | bool:
    """
    Function return dict with info
    """
    p = Path(path)
    if not p.exists():
        print(f"Error: file `{path}` not found")
        return False

    with open(path, "r", encoding="utf-8") as fh:
        lines = [el.strip() for el in fh.readlines()]

    ## Handle empty file
    if len(lines) == 0:
        print(f"Error: records not found. File `{path}`")
        return False

    parsed = []
    for key, line in enumerate(lines):
        ## Skip empty lines
        if len(line) == 0:
            continue

        data = line.split(',')

        try:
            ## Check if no data on line
            if not data[0] or not data[1] or not data[2]:
                print(f"Warning: absent data on line {key}. Skipping")
                continue

            ## Check if additional comas on line
            if len(data) != 3:
                print(f"Warning: probably corrupted line {key}. Skipping")
                continue

            parsed.append({"id":data[0], "name":data[1], "age":data[2]})
        ## Catch file corruptions
        except Exception as e:
            print(f"Error: file corrupted on line {key}. Reason: {e}")
            return False

    return parsed

cats_info = get_cats_info("./task_2/cats_file.txt")
print(cats_info)
