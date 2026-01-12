from src.scraper import scrape_books
from src.data_loader import save_data

def main():
    url = "https://esempio.com/libri"
    df = scrape_books(url)
    save_data(df, "data/libri.csv")
    print("Web scraping completato con successo!")

if __name__ == "__main__":
    main()
