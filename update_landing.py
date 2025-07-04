import openai
import os

# === Load environment ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Generate new text ===
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You write engaging landing page content for a startup called OrganicNews that turns recent scientific papers about nature and health into short, friendly daily articles."},
        {"role": "user", "content": "Write a punchy headline, a one-sentence subheadline, and a short call to action to replace the current homepage of OrganicNews."}
    ],
    temperature=0.7,
)

generated = response["choices"][0]["message"]["content"]

# === Parse output ===
lines = generated.strip().split("\n")
headline = lines[0].strip()
subheadline = lines[1].strip() if len(lines) > 1 else ""
cta = lines[2].strip() if len(lines) > 2 else ""

# === Replace homepage content ===
file_path = "./app/page.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Replace markers in the file (add these markers once if not there)
content = content.replace(
    "// HEADLINE_START", f'"{headline}"'
).replace(
    "// SUBHEADLINE_START", f'"{subheadline}"'
).replace(
    "// CTA_START", f'"{cta}"'
)

with open(file_path, "w") as f:
    f.write(content)
