# Property Scraper

This project contains a Python script to scrape real estate properties for sale in the Geneva canton of Switzerland. It uses Selenium to fetch property pages, saves their content as HTML and Markdown, and stores metadata in a SQLite database.

## Features

- Fetches property data from ImmoScout24.
- Saves the full HTML and a Markdown version of each property page.
- Stores property metadata (URL, price, etc.) in a SQLite database.
- Structured to be run daily to identify new properties.
- Includes a stub function for you to complete the HTML parsing logic.

## How it Works

The scraper is designed to be run from the command line. It will:
1.  Launch a web browser using Selenium.
2.  Navigate to a search results page on ImmoScout24.
3.  (You will need to complete this part) Extract the URLs of individual property listings.
4.  For each property page:
    -   Save the full HTML.
    -   Convert the HTML to Markdown and save it.
    -   Call a stub function (`parse_property_html_stub`) with the HTML content.
5.  (You will need to complete this part) The stub function should be filled in to parse the HTML and return structured data about the property.
6.  The returned data is then saved to a SQLite database.

## Setup and Usage

1.  **Install Dependencies:**
    I will generate a `requirements.txt` file for you. You can install the dependencies with:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Complete the Code:**
    -   **`src/property_scraper/scraper.py`**:
        -   In `scrape_search_results`, you need to provide a valid CSS selector to find the links to the individual property listings.
        -   In `parse_property_html_stub`, you need to implement the logic to parse the HTML of a property page and return a `Property` object.

3.  **Run the Scraper:**
    ```bash
    python -m src.property_scraper.main scrape
    ```

## Important Notes

-   This script requires a working installation of a web browser (like Chrome or Firefox) and the corresponding WebDriver. The script attempts to manage this with `webdriver-manager`, but you may need to handle the installation manually depending on your environment.
