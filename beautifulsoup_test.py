from bs4 import BeautifulSoup

html = '''
<html>
  <head>
    <title>Testseite</title>
  </head>
  <body>
    <h1>Titel</h1>
    <p class="intro">Einleitung</p>
    <p class="content">Haupttext</p>
    <a href="/next">Weiter</a>
    <a href="/prev" class="nav">Zurück</a>
    <ul id="liste">
      <li>Erstes Element</li>
      <li>Zweites Element</li>
      <li>Drittes Element</li>
    </ul>
    <img src="bild.jpg" alt="Beispielbild" />
    <div class="container">
      <span>Text im Span</span>
      <p>Verschachtelter Absatz</p>
    </div>
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

# Finde Elemente nach Klasse
intro_p = soup.find('p', class_='intro')
print("\n<p> mit Klasse 'intro':", intro_p.text)

content_p = soup.find('p', class_='content')
print("<p> mit Klasse 'content':", content_p.text)

nav_a = soup.find('a', class_='nav')
print("<a> mit Klasse 'nav':", nav_a.text)

container_div = soup.find('div', class_='container')
print("<div> mit Klasse 'container':", container_div.prettify())

# Hole den Wert des href-Attributs des <a>-Tags
href = soup.a['href']
print("href des <a>-Tags:", href)

# Experimentiere mit soup.prettify()
print("\nPrettified HTML:")
print(soup.prettify())
