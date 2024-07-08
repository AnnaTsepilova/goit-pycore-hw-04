from pathlib import Path

def total_salary(path: str) -> tuple | bool:
    """
    Function return total and avarage salary, or false on error
    """
    p = Path(path)
    if not p.exists():
        print(f"Error: file `{path}` not found")
        return False

    average = 0
    total_salary = 0
    processed_records = 0

    with open(path, "r", encoding="utf-8") as fh:
        lines = [el.strip() for el in fh.readlines()]

    ## Handle empty file
    if len(lines) == 0:
        print(f"Error: records not found. File `{path}`")
        return False

    for key, line in enumerate(lines):
        ## Skip empty lines
        if len(line) == 0:
            continue

        data = line.split(',')
        try:
            total_salary += int(data[1])
            processed_records += 1
        ## Catch file corruptions
        except Exception as e:
            print(f"Error: file corrupted on line {key}. Reason: {e}")
            return False

    ## Handle empty file
    if processed_records == 0:
        print(f"Error: records not found. File `{path}`")
        return False

    average = int(total_salary / processed_records)

    return (total_salary, average)

result = total_salary("./task_1/salary_file.txt")
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
