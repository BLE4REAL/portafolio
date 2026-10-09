"""Check local routes, anchors and preservation of the supplied media."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
root=Path(__file__).resolve().parents[1]/'docs'
class Page(HTMLParser):
    def __init__(self,path):
        super().__init__();self.refs=[];self.ids=set();self.h1=0
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='h1':self.h1+=1
        if 'id' in attrs:self.ids.add(attrs['id'])
        for k in ('href','src','poster'):
            if attrs.get(k):self.refs.append(attrs[k])
pages={p.resolve():Page(p) for p in root.rglob('*.html')}
media=set();errors=[]
for path,page in pages.items():
    if page.h1!=1:errors.append(f'{path.name}: expected one h1')
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme:continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        if not target.exists():errors.append(f'{path.name}: missing {ref}')
        if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{path.name}: missing anchor {ref}')
        media.add(target.name)
expected={*(f'image{i}.webp' for i in range(1,40)),*(f'media{i}.mp4' for i in range(1,7)),*(f'model3d{i}.glb' for i in range(1,4))}
if expected-media:errors.append(f'Missing source media: {expected-media}')
if len(pages)!=13:errors.append('Expected homepage and 12 preserved case-study routes')
assert not errors,'\n'.join(errors)
print('PASS: 13 routes, local links and anchors; all 39 images, 6 videos and 3 GLBs referenced.')
