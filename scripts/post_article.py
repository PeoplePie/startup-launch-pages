import openai
from datetime import datetime
import os
import re

# --- CONFIGURATION ---
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this as a GitHub secret later
TOPIC = "Recent scientific findings about how nature improves physical and mental health"
POSTS_DIR = "../posts"  # Relative path from scripts/ folder

# --- GENERATE ARTICLE ---
def generate_article():
    prompt = (
        f"Write a blog post for a general audience about {TOPIC}. "
        "Use simple language, cite at least 2 real scientific sources (with URLs if available), "
        "and explain why the findings are important. Make it feel inspiring and trustworthy."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content

# --- FORMAT TITLE + FILE ---
def make_filename(title):
    # Convert title to kebab-case filename
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')
    today = datetime.today().strftime("%Y-%m-%d")
    return f"{today}-{slug}.md"

# --- MAIN ---
if __name__ == "__main__":
    article = generate_article()
    lines = article.strip().split("\n")
    title = lines[0].replace("#", "").strip()  # Assume title is first line
    filename = make_filename(title)
    filepath = os.path.join(POSTS_DIR, filename)

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(article)

    print(f"✅ Article saved to {filepath}")
