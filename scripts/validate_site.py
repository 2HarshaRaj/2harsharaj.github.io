#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import re, sys, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
PAGES=[Path('index.html'),Path('phis-termux-backup/index.html'),Path('phis-termux-backup/privacy.html'),Path('phis-termux-backup/terms.html')]
REQUIRED=PAGES+[Path('assets/site.css'),Path('robots.txt'),Path('sitemap.xml'),Path('google6327aedd63778de2.html')]
class Parser(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.tags=set(); self.lang=False; self.title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs); self.tags.add(tag); self.lang|=tag=='html' and bool(a.get('lang'))
  if tag in {'a','link'} and a.get('href'): self.links.append(a['href'])
 def handle_data(self,data): self.title|=self.lasttag=='title' and bool(data.strip())
errors=[]
for p in REQUIRED:
 if not (ROOT/p).is_file(): errors.append(f'missing: {p}')
for rel in PAGES:
 parser=Parser(); parser.feed((ROOT/rel).read_text())
 for tag in ('main','header','footer'):
  if tag not in parser.tags: errors.append(f'{rel}: missing {tag}')
 if not parser.lang or not parser.title: errors.append(f'{rel}: missing language/title')
 for href in parser.links:
  u=urlparse(href)
  if u.scheme or href.startswith('#'): continue
  target=ROOT/u.path.lstrip('/') if u.path.startswith('/') else ROOT/rel.parent/u.path
  if not u.path or u.path.endswith('/'): target/= 'index.html'
  if not target.resolve().is_file(): errors.append(f'{rel}: broken link {href}')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls={x.text for x in ET.parse(ROOT/'sitemap.xml').findall('s:url/s:loc',ns)}
expected={'https://2harsharaj.github.io/','https://2harsharaj.github.io/phis-termux-backup/','https://2harsharaj.github.io/phis-termux-backup/privacy.html','https://2harsharaj.github.io/phis-termux-backup/terms.html'}
if urls!=expected: errors.append('sitemap mismatch')
text='\n'.join((ROOT/p).read_text() for p in PAGES)
for pattern in (r'buildcon',r'google-analytics|googletagmanager|formspree',r'<script\b'):
 if re.search(pattern,text,re.I): errors.append(f'prohibited active content: {pattern}')
if errors: print(*errors,sep='\n');sys.exit(1)
print(f'Site validation passed: {len(PAGES)} pages, local links, sitemap, and retired content checked.')
