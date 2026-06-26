import requests
import re

# Fetch a random quote from free API
response = requests.get("https://zenquotes.io/api/random")
data = response.json()
quote = data[0]['q']
author = data[0]['a']

# Read current README
with open("README.md", "r") as f:
    content = f.read()

# Create new quote section
new_quote = f"\n\n## 💬 Today's DevOps Motivation\n> *\"{quote}\"*\n> — {author}\n"

# Replace old quote or add new one
if "## 💬 Today's DevOps Motivation" in content:
    content = re.sub(
        r"## 💬 Today's DevOps Motivation.*",
        new_quote,
        content,
        flags=re.DOTALL
    )
else:
    content += new_quote

# Save updated README
with open("README.md", "w") as f:
    f.write(content)

print(f"✅ Updated with quote: {quote} — {author}")
