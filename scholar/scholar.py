from serpapi import GoogleSearch
from pprint import pprint
import json

params = {
  "engine": "google_scholar_author",
  "author_id": "AuizbbAAAAAJ",
  "api_key": "95ca7aae091854a35cc44b69b44f10f449f6af94357c1a8dc83442eb7d6d1953"
}

search = GoogleSearch(params)
results = []

pages = search.pagination(page_size=39)

for page in pages:
    results.extend(page.get("articles", []))

results = sorted(results, key=lambda x: x['year'], reverse=True)

for paper in results:
    paper['google-scholar'] = paper.pop('link')

# dump results to a JSON file
with open('scholar.json', 'w') as f:
    json.dump(results, f, indent=4)