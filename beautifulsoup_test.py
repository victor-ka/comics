from bs4 import BeautifulSoup

html = '''
<html>
  <body>
    <h1>Titel</h1>
    <p class="intro">Einleitung</p>
    <p class="content">Haupttext</p>
    <a href="/next">Weiter</a>
  </body>
</html>
'''

# Lade den HTML-Text mit BeautifulSoup
soup = BeautifulSoup(html, "lxml")

# Gib den Text der Überschrift <h1> aus
h1_text = soup.h1.text
print("Überschrift:", h1_text)

# Finde alle <p>-Elemente und gib deren Texte aus
p_elements = soup.find_all('p')
print("Alle <p>-Texte:")
for p in p_elements:
    print("-", p.text)

# Hole den Wert des href-Attributs des <a>-Tags
href = soup.a['href']
print("href des <a>-Tags:", href)

# Experimentiere mit soup.prettify()
print("\nPrettified HTML:")
print(soup.prettify())
