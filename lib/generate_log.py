from datetime import datetime
import os
import requests

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # STEP 2: Generate filename with today's date (log_YYYYMMDD.txt)
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Ensure directory exists (file will be created in current working dir)
    dirname = os.getcwd()
    filepath = os.path.join(dirname, filename)

    # STEP 3: Write the log entries to a file using File I/O
    with open(filepath, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message and return the filename
    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch a sample post from a public API and return a list of strings."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
        response.raise_for_status()
        post = response.json()
        # Return title and body as separate log entries
        return [post.get("title", ""), post.get("body", "")]
    except Exception:
        # On any error, return an empty list
        return []


def main():
    # Fetch data using requests and write to a dated log file
    entries = fetch_data()
    if not entries:
        entries = ["No data fetched"]
    filename = generate_log(entries)
    print("Finished: wrote fetched data to", filename)


if __name__ == "__main__":
    main()
