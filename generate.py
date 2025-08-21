import json
import os
from jinja2 import Environment, FileSystemLoader

# Load JSONs
with open("data/hero.json", encoding="utf-8") as f:
    hero = json.load(f)

with open("data/contact.json", encoding="utf-8") as f:
    contact = json.load(f)

with open("data/papers.json", encoding="utf-8") as f:
    papers = json.load(f)

with open("data/projects.json", encoding="utf-8") as f:
    projects = json.load(f)

with open("data/projects_head.json", encoding="utf-8") as f:
    projects_head = json.load(f)

years = sorted(set(p["year"] for p in papers), reverse=True)
thumbs = {file.split('.')[0] : file for file in os.listdir('data/paper_thumbs')}

# Jinja2
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

# Render
html = template.render(
    hero=hero,
    contact=contact,
    papers=papers,
    projects=projects,
    projects_head=projects_head,
    years=years,
    thumbs=thumbs
)

# Write
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Página gerada com sucesso em 'index.html'")
