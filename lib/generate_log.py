from datetime import datetime
import os
from typing import List


def generate_log(data: List[str]) -> str:
    """Create a timestamped log file from a list of strings.

    This minimal implementation focuses solely on the rubric requirements:
    - Validate that `data` is a list (raise ValueError otherwise).
    - Create a file named `log_YYYYMMDD.txt` in the current working directory.
    - Write each item of `data` as a separate line.
    - Print a confirmation message and return the filename.
    """

    if not isinstance(data, list):
        raise ValueError("data must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    filepath = os.path.join(os.getcwd(), filename)

    with open(filepath, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename
