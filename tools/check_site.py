"""Check static navigation, metadata, contact links, and content boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,subprocess
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.ids=[];self.links=[];self.h1=0;self.main=0;self.lang=None;self.title=False;self.description=False;self.canonical=False;self.text=[];self.feed(s)
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='html':self.lang=d.get('lang')
  if t=='h1':self.h1+=1
  if t=='main':self.main+=1
  if t=='title':self.title=True
  if t=='meta' and d.get('name')=='description':self.description=bool(d.get('content'))
  if t=='link' and d.get('rel')=='canonical':self.canonical=True
  if t in ['a','link'] and d.get('href'):self.links.append(d['href'])
 def handle_data(self,s):self.text.append(s)
files=list(ROOT.rglob('*.html'));pages={p:Page(p.read_text()) for p in files}
for p,page in pages.items():
 assert page.h1==page.main==1,(p,'landmarks')
 assert len(page.ids)==len(set(page.ids)),(p,'duplicate IDs')
 assert page.lang=='en' and page.title and page.description and page.canonical,(p,'metadata')
 for link in page.links:
  u=urlsplit(link)
  if u.scheme:continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  if target.is_dir():target=target/'index.html'
  assert target.is_file(),(p,link,'missing target')
  if u.fragment:assert unquote(u.fragment) in pages[target].ids,(p,link,'fragment missing')
 visible=' '.join(page.text).lower()
 for phrase in ['small business','small companies','24/7','99.9%','40% fewer','18% cost','30% cloud','aws certified']:
  assert phrase not in visible,(p,'unsupported or excluded content',phrase)
 assert 'tel:+17793791260' in (p.read_text()),(p,'phone')
assert subprocess.check_output(['git','show','origin/main:CNAME'],cwd=ROOT)==(ROOT/'CNAME').read_bytes()
assert not subprocess.check_output(['git','diff','origin/main','--','.github'],cwd=ROOT)
print(f'PASS: {len(files)} pages; local links and fragments; IDs and landmarks; metadata; excluded-content checks; phone; unchanged CNAME and workflows.')
