Web Scraping Mondadori Store
Descrizione

Questo progetto permette di estrarre informazioni sui libri dalla sezione Fantasy di Mondadori Store
 e salvare i dati in un file CSV.
I dati raccolti includono titolo del libro, autore e prezzo.

Il progetto è sviluppato in Python 3.13, utilizza BeautifulSoup per il parsing HTML e requests per le richieste HTTP.
Requisiti

Python 3.13

Pacchetti Python:
pandas
requests
beautifulsoup4
certifi


Creare l’ambiente virtuale
python -m venv .venv

Attivare l’ambiente virtuale

.\.venv\Scripts\Activate.ps1

Installare le dipendenze
pip install pandas requests beautifulsoup4 certifi

Uso

Modifica l’URL in src/main.py se vuoi cambiare categoria:
url = "https://www.mondadoristore.it/fantasy"
Avvia il progetto:
python -m src.main
I dati verranno salvati in data/libri.csv.
Nota SSL

Se dovessi riscontrare errori tipo: Se dovessi riscontrare errori tipo:
requests.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]

assicurati di aggiornare certifi:
pip install --upgrade certifi
e assicurati che nel tuo scraper.py la richiesta HTTP sia così:
response = requests.get(url, verify=certifi.where())


Se vuoi test veloci puoi anche bypassare SSL (solo per test):
response = requests.get(url, verify=False)

Autore

Giuseppe Agnello

Licenza

Questo progetto è open source e può essere utilizzato a scopo didattico.
