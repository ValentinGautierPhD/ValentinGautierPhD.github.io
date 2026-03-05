#!/usr/bin/env python3

import yaml
import os
from datetime import datetime

if not os.path.exists('_publications'):
    os.makedirs('_publications')

# Charger le fichier généré par l'Action
with open('_publications/pubs.yml', 'r') as f:
    data = yaml.safe_load(f)

for work in data.get('works', []):
    # Nettoyage des données
    title = work['title']['value']
    date_info = work.get('publicationDate', {})
    year = date_info.get('year', '2024')
    # Formatage de la date pour Jekyll (YYYY-MM-DD)
    month = date_info.get('month', '01') or '01'
    day = date_info.get('day', '01') or '01'
    full_date = f"{year}-{month}-{day}"

    venue = work.get('journalTitle') or "Conference/Preprint"
    doi = work.get('doi', '')
    url = work.get('url', '')
    authors = ", ".join(work.get('authors', []))

    # Créer un nom de fichier propre
    filename = f"_publications/{year}-{title.replace(' ', '-').replace('/', '_').lower()[:30]}.md"

    # Contenu formaté pour academicpages
    content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{title.replace(' ', '-').lower()[:30]}
date: {full_date}
venue: '{venue}'
paperurl: '{url}'
citation: '{authors}. ({year}). "{title}." <i>{venue}</i>.'
---

More information about this work [here]({url}).
"""
    with open(filename, 'w') as f_out:
        f_out.write(content)
