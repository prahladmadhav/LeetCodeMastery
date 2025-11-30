import os
import re
from datetime import datetime

ROOT = "."

TOPICS = [
    "array",
    "string",
    "dp",
    "graph",
    "binary-tree",
    "binary-search",
    "sliding-window",
    "heap",
    "backtracking",
    "math",
]

rows = []
count_easy = count_medium = count_hard = 0

for topic in TOPICS:
    if not os.path.isdir(topic):
        continue
    
    for folder in sorted(os.listdir(topic)):
        path = os.path.join(topic, folder)
        if not os.path.isdir(path):
            continue

        # Parse number + name
        match = re.match(r"(\d+)-(.*)", folder)
        if not match:
            continue

        number, name = match.groups()
        name = name.replace("-", " ").title()

        # Read difficulty & date from README.md
        readme_path = os.path.join(path, "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()

            diff_match = re.search(r"Difficulty:[*]+\s*(\w+)", content)
            date_match = re.search(r"Date:[*]+\s*(.*)", content)

            difficulty = diff_match.group(1) if diff_match else "Unknown"
            date = date_match.group(1) if date_match else "-"
        else:
            difficulty = "Unknown"
            date = "-"

        # Difficulty count
        if difficulty.lower() == "easy": count_easy += 1
        if difficulty.lower() == "medium": count_medium += 1
        if difficulty.lower() == "hard": count_hard += 1

        link = f"{topic}/{folder}"
        rows.append(f"| {int(number)} | {name} | {topic} | {difficulty} | {date} | [View]({link}) |")

# Sort rows by problem number
rows.sort(key=lambda r: int(r.split("|")[1].strip()))

# Update README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = readme.find("| No.")
end = readme.find("## 📁 Folder Structure")  # end of table

new_table = (
    "| No. | Problem | Topic | Difficulty | Date Completed | Link |\n"
    "|-----|---------|--------|-------------|----------------|------|\n"
    + "\n".join(rows)
)

updated = readme[:start] + new_table + "\n\n" + readme[end:]

start = updated.find("- **Total Problems:**")
end = updated.find("## 📚 Index of Problems")  # end of table

summary = (
    f"- **Total Problems:** {len(rows)}  \n"
    f"- **Easy:** {count_easy}  \n"
    f"- **Medium:** {count_medium}  \n"
    f"- **Hard:** {count_hard}  \n"
    f"- **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n\n"
    "--- \n\n"
)

updated = updated[:start] + summary + "\n\n" + updated[end:]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)

print("Index updated successfully.")
