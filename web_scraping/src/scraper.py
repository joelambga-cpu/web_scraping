import requests
from bs4 import BeautifulSoup
import pandas as pd
import certifi

def scrape_books(url: str) -> pd.DataFrame:
    response = requests.get(url, verify=certifi.where())
    soup = BeautifulSoup(response.text, "html.parser")

    titoli = []
    autori = []
    prezzi = []

    # selettori corretti per i libri sui risultati Fantasy
    # ogni libro è contenuto in un elemento simile a questo
    items = soup.select("div.product-grid div.product-item")

    for item in items:
        titolo_tag = item.select_one("h4.product-name a")
        autore_tag = item.select_one("p.product-author")  
        prezzo_tag = item.select_one("span.price")

        titolo = titolo_tag.get_text(strip=True) if titolo_tag else "N/D"
        autore = autore_tag.get_text(strip=True) if autore_tag else "Autore sconosciuto"
        prezzo = prezzo_tag.get_text(strip=True) if prezzo_tag else "Prezzo non trovato"

        titoli.append(titolo)
        autori.append(autore)
        prezzi.append(prezzo)

    df = pd.DataFrame({
        "Titolo": titoli,
        "Autore": autori,
        "Prezzo": prezzi
    })

    return df
