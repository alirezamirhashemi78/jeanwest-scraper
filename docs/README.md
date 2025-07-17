# Jeanwest Scraper

This project is a simple scraper to collect product details and reviews from the Jeanwest website API.

## Project Structure

- `main.py` — Entry point of the application  
- `config.py` — Configuration and settings  
- `scraper/` — Core scraping modules  
  - `retrieve.py` — Responsible for fetching data from the API  
  - `process.py` — Processing and saving data  
  - `storage.py` — Managing file storage  
- `requirements.txt` — Project dependencies  

## Installation and Usage

1. Install dependencies:

```bash
pip install -r requirements.txt```

1. Run scraper:

```bash
python3 main.py

## Important

**Make sure to run this project with Python 3.**  
Using Python 2 or other versions may cause errors.
