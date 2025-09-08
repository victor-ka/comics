# XKCD Comic Downloader & BeautifulSoup HTML Demo

## Overview
This repository contains two Python scripts:
- `app.py`: Downloads XKCD comics and saves both the images and their alt-texts.
- `beautifulsoup_test.py`: Demonstrates HTML parsing and element selection using BeautifulSoup.

---

## `app.py` - XKCD Comic Downloader

**Features:**
- Downloads up to 20 XKCD comics starting from the latest.
- Saves each comic image in the `xkcd` folder.
- Stores the alt-text (title text) of each comic in a `.txt` file next to the image.
- Uses a custom User-Agent to mimic a browser.
- Waits 0.5 seconds between downloads to avoid overloading the server.

**Usage:**
1. Make sure you have Python 3 and the required packages installed:
   ```bash
   pip install requests beautifulsoup4 lxml
   ```
2. Run the script:
   ```bash
   python app.py
   ```
3. Downloaded images and alt-texts will appear in the `xkcd` directory.

---

## `beautifulsoup_test.py` - BeautifulSoup HTML Demo

**Features:**
- Loads a sample HTML string.
- Extracts and prints:
  - The text of the `<h1>` heading.
  - All `<p>` element texts.
  - Elements by class (e.g., `intro`, `content`, `nav`, `container`).
  - The `href` attribute of the first `<a>` tag.
  - The prettified (formatted) HTML structure.

**Usage:**
1. Make sure you have Python 3 and the required packages installed:
   ```bash
   pip install beautifulsoup4 lxml
   ```
2. Run the script:
   ```bash
   python beautifulsoup_test.py
   ```
3. Review the output in your terminal to see how BeautifulSoup parses and extracts data from HTML.

---

## License
This project is for educational purposes.
