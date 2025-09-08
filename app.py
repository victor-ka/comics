# downloadXkcdComics.py - XKCD-Comics automatisch herunterladen

import os, time, requests
from bs4 import BeautifulSoup

# Basis-URL der Webseite
BASE = "https://xkcd.com"
url = BASE  # Startseite (aktueller Comic)

# Ordner 'xkcd' erstellen, falls er nicht existiert
os.makedirs('xkcd', exist_ok=True)

# Zähler: wie viele Comics schon heruntergeladen wurden
num_downloads, MAX_DOWNLOADS = 0, 20

# User-Agent, um uns als "normaler Browser" auszugeben
headers = {"User-Agent": "Mozilla/5.0 (XKCD-scraper for learning)"}


# Solange es noch Comics gibt und wir das Limit nicht erreicht haben
while not url.endswith('#') and num_downloads < MAX_DOWNLOADS:
    # 1. Seite laden
    res = requests.get(url, headers=headers, timeout=20)
    res.raise_for_status()  # Fehler melden, wenn Seite nicht geladen werden kann

    # 2. HTML parsen
    soup = BeautifulSoup(res.text, "lxml")

    # 3. Comic-Bild und Alt-Text finden: <div id="comic"><img src="..."></div>
    comic_img = soup.select_one("#comic img")
    img_url = "https:" + comic_img["src"]  # vollständige Bild-URL bauen
    alt_text = comic_img.get("title", "")  # Alt-Text (Titeltext) holen

    # 4. Bild herunterladen
    img_res = requests.get(img_url, headers=headers, timeout=20)

    # 5. Bild speichern im Ordner ./xkcd
    filename = os.path.join("xkcd", os.path.basename(img_url))
    with open(filename, "wb") as f:
        f.write(img_res.content)

    # Alt-Text speichern
    txt_filename = filename + ".txt"
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(alt_text)

    num_downloads += 1
    print(f"[{num_downloads}] saved: {filename}, alt-text saved: {txt_filename}")

    # 6. Link zum vorherigen Comic finden: <a rel='prev' href="...">
    prev = soup.select_one("a[rel='prev']")
    href = prev["href"].strip("/")  # z. B. "/2901/" → "2901"
    url = f"{BASE}/{href}"

    # kleine Pause, um die Webseite nicht zu überlasten
    time.sleep(0.5)

print("Done.")