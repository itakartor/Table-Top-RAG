import requests
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "https://en.1jour-1jeu.com"
RULES_URL = f"{BASE_URL}/rules"
OUTPUT_DIR = Path("downloaded_rules")
OUTPUT_DIR.mkdir(exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_game_links_for_lang():
    print("🔍 Recupero lista giochi...")
    links_for_lang = {}
    page = 1
    while len(links_for_lang.items()) <= 3000:
        res = requests.get(f"{RULES_URL}?page={page}", headers=headers, timeout=500)
        # with open("response.txt", "w", encoding="utf-8") as file:
        #     file.write(res.text)
        soup = BeautifulSoup(res.text, "html.parser")
        cards = soup.find_all("a", class_="btn btn-sm btn-secondary mb-1", href=True)
        if not cards:
            break
        for card in cards:
            #print(card)
            #print(len(links))
            href = card.get("href")
            title_lang = card.get("title")
            #print(f"Link trovato: {href}")
            #print(f"Lingua trovato: {title_lang}")
            if href:
                if title_lang not in links_for_lang:
                    links_for_lang[title_lang] = []
                links_for_lang[title_lang].append(href)
        page += 1
    return links_for_lang

def download_rule_pdf(p_rule_page_url, p_lang):
    #print(rule_page_url)
    filename = p_rule_page_url.split("/")[-1]
    # with open(filename, "wb") as f:s
    #     f.write(res.content)
    # print(f"✅ Scaricato {filename}")
    game_folder = OUTPUT_DIR / p_lang
    game_folder.mkdir(parents=True, exist_ok=True)

    res = requests.get(p_rule_page_url, timeout=500)
    with open(game_folder / filename, "wb") as f:
        f.write(res.content)
    print(f"✅ Scaricato {filename} in {p_lang}")
    return True
# MAIN
def main():
    print("🚀 Inizio download delle regole dei giochi...")
    all_game_links = get_game_links_for_lang()
    print(f"🎲 Trovati {len(all_game_links)} giochi. Inizio download...")
    for lang in all_game_links.keys():
        for url in all_game_links[lang]:
            try:
                download_rule_pdf(url, lang)
            except Exception as e:
                print(f"Errore con {url}: {e}")
    print("✅ Download completato!")

if __name__ == "__main__":
    main()
