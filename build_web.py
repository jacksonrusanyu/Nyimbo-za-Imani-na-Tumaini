"""Rebuilds index.html from template.html + songs_lyrics_data.json.
Run:  python build_web.py            (needs only Python 3, no extra packages)"""
import json,os
here=os.path.dirname(os.path.abspath(__file__))
songs=json.load(open(os.path.join(here,'songs_lyrics_data.json'),encoding='utf-8'))
out=[]
for s in sorted(songs,key=lambda s:s['num']):
    secs=[]
    for sec in s['sections']:
        k={'verse':'v','chorus':'c'}.get(sec['type'],'o')
        d={'k':k,'l':sec.get('label') or '','ln':sec['lines']}
        if sec.get('chords') and any(sec['chords']):
            # one chord per position: the normal (no-capo) chord; the page transposes it for any capo
            d['ch']=[[[p[0],(p[2] or p[1])] for p in line if (p[2] or p[1])] for line in sec['chords']]
        secs.append(d)
    out.append({'n':s['num'],'t':s['title'],'st':s.get('subtitle'),'capo':s.get('capo'),'sec':secs,
                'notes':s.get('notes') or [],'credit':s.get('credit')})
data=json.dumps(out,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
tpl=open(os.path.join(here,'template.html'),encoding='utf-8').read()
html=tpl.replace('/*__DATA__*/[]',data)
open(os.path.join(here,'index.html'),'w',encoding='utf-8').write(html)
print('index.html written:',len(out),'songs,',round(len(html)/1024),'KB')
