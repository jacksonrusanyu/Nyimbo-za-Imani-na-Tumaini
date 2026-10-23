# Nyimbo za Tumaini na Imani - Toleo la Web (maelezo)

## 1. Faili zilizopo kwenye folda hii
| Faili | Kazi |
|---|---|
| `index.html` | **Web page yenyewe.** Nyimbo zote 144 na chords zimo ndani ya faili hili moja (KB ~230). Inafanya kazi bila internet. |
| `songs_lyrics_data.json` | **Data ya nyimbo** (maneno, vitenzi vya ubeti/kiitikio, chords). Hapa ndipo unarekebisha maneno au chords. |
| `template.html` | Muundo wa ukurasa (muonekano na programu). `index.html` hutengenezwa kutoka hapa + data. |
| `build_web.py` | Script ya kuunda upya `index.html` baada ya kubadilisha data. |
| `manifest.webmanifest`, `sw.js`, `icon-192.png`, `icon-512.png` | Zinaruhusu simu kuiweka web hii kama app ("Add to Home screen") na kuifungua bila internet. |

## 2. Jinsi web page inavyofanya kazi
- **Orodha ya nyimbo:** tafuta kwa namba (mfano `61`), jina, au neno lolote la ndani ya wimbo.
- **Kitufe `Chords`:** huonyesha chords za gitaa juu ya maneno. Kwa kawaida ni **chords moja tu** - chords za kawaida (bila capo), ambazo ndizo "mstari wa chini" wa kitabu cha asili.
- **Chaguo `Capo` (0 hadi 9):** mtumiaji akichagua nafasi ya capo, **chords zote hubadilika zenyewe** kuonyesha umbo la kupiga kwa capo hiyo (mfano wimbo 8: chords za kawaida G, C, D; na Capo 5 huonyesha D, G, A - sawa na mstari wa juu wa kitabu). Chaguo hubaki kwa nyimbo zote hadi abadilishe.
- **Kitufe `Tumia capo ya kitabu (Capo n)`:** hutokea ndani ya wimbo; kinaweka capo kama ilivyoandikwa kwenye kitabu cha asili kwa wimbo huo.
- `A-` / `A+` hubadilisha ukubwa wa herufi. Kitufe cha duara (juu kulia) hubadilisha mwanga/giza.
- Mshale wa kushoto/kulia (au vitufe vya chini) huenda wimbo uliopita/unaofuata. Kila wimbo una link yake: `index.html#/8` hufungua wimbo namba 8.
- Chaguo la mtumiaji (chords, capo, ukubwa wa herufi, rangi) hukumbukwa kwenye simu/kompyuta yake.

## 3. Jinsi ya kuiweka kwenye web (ili watu waifungue kwa link)
Ni faili za kawaida (static), hazihitaji server wala database. Njia rahisi, zote bure:

**A. Netlify Drop (rahisi kuliko zote, dakika 2)**
1. Fungua https://app.netlify.com/drop
2. Buruta **folda nzima ya `WEB`** kwenye ukurasa. Utapata link kama `https://jina-lako.netlify.app`.
3. Kubadilisha jina au kutumia domain yako: Site settings -> Domain management.

**B. GitHub Pages**
1. Tengeneza repository mpya kwenye GitHub, pakia faili za folda `WEB` (au angalau `index.html`, `manifest.webmanifest`, `sw.js`, `icon-192.png`, `icon-512.png`).
2. Settings -> Pages -> Source: `main` / root -> Save. Link: `https://jina-lako.github.io/jina-la-repo/`.

**C. Cloudflare Pages / hosting yoyote (cPanel, n.k.)**
Pakia faili hizo kwenye folda ya `public_html` (au ya website). Hakuna usanidi mwingine.

Muhimu: kupata "Add to Home screen" na kufanya kazi bila internet, link lazima iwe `https://` (Netlify na GitHub Pages zinatoa hiyo kiotomatiki). Kufungua `index.html` kwa kubofya mara mbili kwenye kompyuta pia kunafanya kazi, ila bila sehemu ya app.

## 4. Jinsi ya kurekebisha nyimbo baadaye
1. Fungua `songs_lyrics_data.json` kwa kihariri cha maandishi (VS Code / Notepad++).
2. Kila wimbo una muundo huu:
```json
{ "num": 8, "title": "Ibada ya Asubuhi", "subtitle": null, "capo": 5,
  "sections": [
    { "type": "verse",  "label": "1", "lines": ["Namwendea Yesu kila asubuhi,", "..."],
      "chords": [ [[0,"D","G"], [10,"G","C"]], [], ... ] },
    { "type": "chorus", "label": "Kiitikio", "lines": ["..."] } ],
  "notes": [], "credit": null }
```
   - `type`: `verse` (ubeti), `chorus` (kiitikio) au `other`.
   - `chords` ni orodha moja kwa kila mstari wa `lines`. Kila chord ni `[nafasi, "chord ya capo ya kitabu", "chord ya kawaida"]`. **Nafasi** ni namba ya herufi kwenye mstari ambapo chord inaanzia (0 = herufi ya kwanza). Kwa mfano `[10,"G","C"]`: juu ya herufi ya 11 kuna chord C (kawaida; G ni umbo lake kwa capo ya kitabu). **Web hutumia chord ya kawaida (ya tatu)** na kuihamisha yenyewe kulingana na capo aliyochagua mtumiaji; hivyo ukirekebisha chord, rekebisha ya kawaida.
3. Hifadhi, kisha endesha: `python build_web.py` (Python 3 inatosha). Itaandika upya `index.html`.
4. Pakia tena `index.html` kwenye hosting. Kama unatumia Netlify/GitHub, buruta/pakia upya faili tu.

## 5. Mambo ya kukagua kabla ya kuzindua (uaminifu wa data)
Maneno yote yalitolewa moja kwa moja kutoka kwenye PDF ya asili na kulinganishwa neno kwa neno (maneno 7 tu kati ya takriban 1,700 mistari yalitofautiana, hasa nafasi kati ya maneno). Lakini kagua haya:
- **Nyimbo zenye mpangilio mgumu:** 3, 4, 16, 18, 19 (marudio/canon), 32, 38 (sauti za ziada). Mpangilio wa mistari umerahisishwa.
- **Mstari wa mwangwi wa sauti ya chini** mara nyingi umeachwa; kwa nyimbo 77, 96, 99, 100, 73 sehemu kubwa kuliko nyingine.
- **Chords:** takriban 90% (4,205 kati ya 4,647) zimewekwa kwenye silabi. Chords za sehemu zisizo na maneno (muziki tu) hazionekani. Nyimbo 63, 100, 135 zimepoteza nyingi zaidi. Chord huonekana kwenye silabi ya karibu zaidi kwenye ukurasa wa asili, hivyo mara chache inaweza kuwa silabi moja mbele au nyuma.
- Wimbo 59 hauna jina lake kwenye "Yaliyomo Kialfabeti" ya kitabu cha asili (kasoro ya kitabu chenyewe).
- Makosa ya uchapaji ya kitabu cha asili yameachwa kama yalivyo (mfano "wagu" wimbo 6, "Dinini" wimbo 12). Kuyarekebisha, hariri `songs_lyrics_data.json`.
- Kiitikio huonyeshwa mara moja mahali kilipochapishwa kwenye kitabu (hakirudiwi baada ya kila ubeti).

## 6. Hatua zinazofuata (kuelekea application)
1. **Rahisi kuliko zote:** web hii tayari ni **PWA** - mtu akiifungua kwenye Chrome ya simu anaweza kuchagua "Install app / Add to Home screen". Inakaa kama app, na inafanya kazi bila internet baada ya kufunguliwa mara ya kwanza.
2. **App halisi ya Android/iOS:** funika folda hii kwa **Capacitor** (https://capacitorjs.com): `npm init`, `npm i @capacitor/core @capacitor/cli`, `npx cap init`, weka faili za `WEB` kama `webDir`, kisha `npx cap add android` na ufungue kwenye Android Studio. Data (`songs_lyrics_data.json`) inaweza kutumika kama ilivyo.
3. **Mawazo ya kuongeza:** vipendwa (favorites), kubadilisha ufunguo wa chords (transpose), kuonyesha mwanga mkubwa kwa ajili ya projector, kurudia kiitikio baada ya kila ubeti kwa kitufe.
