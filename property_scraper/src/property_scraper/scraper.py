import time
import os
from markdownify import markdownify as md
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .models import Property
from .database import get_db, PropertyDB
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional
import typer
import re

def get_webdriver():
    """Initializes and returns a Selenium WebDriver."""
    # This function is now a placeholder, as the user will run this in an env with a browser.
    # The user should ensure that the webdriver is correctly installed and configured.
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        typer.echo(f"Could not initialize webdriver: {e}", err=True)
        typer.echo("Please ensure that you have a working browser and webdriver installed.", err=True)
        raise e


def get_property_id_from_url(url: str) -> Optional[str]:
    """Extracts the property ID from the URL."""
    match = re.search(r'/(\d+)', url)
    if match:
        return match.group(1)
    return None

def parse_property_html_stub(html_content: str, url: str) -> Optional[Property]:
    """
    This is a stub function that you need to complete.
    It takes the HTML content of a property page and should return a Property object.

    Args:
        html_content: The full HTML of the property detail page.
        url: The url of the property page.

    Returns:
        A Property object with the extracted data.
    """
    typer.echo("---")
    typer.echo("Inside `parse_property_html_stub`. Please complete this function.")
    typer.echo("You need to parse the `html_content` to extract the property details.")
    typer.echo("---")

    # Placeholder implementation:
    # You should use a library like BeautifulSoup to parse the HTML.
    # from bs4 import BeautifulSoup
    # soup = BeautifulSoup(html_content, 'html.parser')
    #
    # Then, find the elements containing the data you need.
    # location = soup.find('h1').text
    # price_text = soup.find(class_='Price').text
    # ... and so on for all the other fields.

    # For now, returning placeholder data.
    return Property(
        url=url,
        location="Placeholder Location - Please Implement Parsing",
        price=0.0,
        rooms=0.0,
        livable_area=0.0,
        total_area=0.0,
        description="Placeholder description.",
        date_found=datetime.utcnow()
    )


def scrape_property_details(url: str, driver) -> Optional[Property]:
    """
    Scrapes the details of a single property page.
    It saves the HTML and Markdown, then calls the stub function to parse the data.
    """
    typer.echo(f"Fetching property page: {url}")
    driver.get(url)

    html_content = driver.page_source
    md_content = md(html_content)

    property_id = get_property_id_from_url(url)
    if not property_id:
        typer.echo(f"Could not extract property ID from URL: {url}", err=True)
        return None

    base_path = "properties/geneva"
    prop_dir = os.path.join(base_path, property_id)
    os.makedirs(prop_dir, exist_ok=True)

    html_path = os.path.join(prop_dir, "property.html")
    md_path = os.path.join(prop_dir, "property.md")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    # Call the stub function to parse the HTML
    property_data = parse_property_html_stub(html_content=html_content, url=url)

    if property_data:
        # Add the file paths to the property object
        property_data.html_path = html_path
        property_data.markdown_path = md_path

    return property_data


def scrape_search_results(url: str, driver) -> List[str]:
    """
    Scrapes a search results page to get all property URLs.
    This function will need to be completed by the user with the correct selectors.
    """
    typer.echo(f"Fetching search results from: {url}")
    driver.get(url)

    # The user needs to find the correct selector for the property links.
    # This is a placeholder that is unlikely to work.
    property_link_selector = "a[data-cy='listing-item-link']" # This is a guess

    typer.echo(f"Waiting for property links with selector: {property_link_selector}")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, property_link_selector))
        )

        link_elements = driver.find_elements(By.CSS_SELECTOR, property_link_selector)
        property_links = [elem.get_attribute('href') for elem in link_elements]

        # Make links absolute
        property_links = [
            ("https://www.immoscout24.ch" + link) if link.startswith('/') else link
            for link in property_links
        ]

        return list(set(property_links))

    except (NoSuchElementException, TimeoutException):
        typer.echo("Could not find property links. The website structure may have changed.", err=True)
        typer.echo("Please update the CSS selectors in `scrape_search_results`.", err=True)
        # Save page source for debugging
        with open("search_results.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        typer.echo("Saved page source to search_results.html for debugging.")
        return []


def run_scraper(urls: List[str], min_price: Optional[float], max_price: Optional[float]):
    """Main function to run the scraper."""
    driver = get_webdriver()
    db: Session = next(get_db())

    all_property_urls = []
    for url in urls:
        property_urls = scrape_search_results(url, driver)
        all_property_urls.extend(property_urls)

    typer.echo(f"Found {len(all_property_urls)} unique properties to scrape.")

    for prop_url in all_property_urls:
        existing_property = db.query(PropertyDB).filter(PropertyDB.url == prop_url).first()

        property_data = scrape_property_details(prop_url, driver)

        if property_data:
            if existing_property:
                typer.echo(f"Updating existing property: {prop_url}")
                existing_property.last_seen = datetime.utcnow()
                # Update fields from new scrape
                update_data = property_data.dict(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(existing_property, key, value)
            else:
                typer.echo(f"Adding new property: {prop_url}")
                db_property = PropertyDB(
                    **property_data.dict(exclude_unset=True),
                    first_seen=datetime.utcnow(),
                    last_seen=datetime.utcnow()
                )
                db.add(db_property)

            db.commit()

    driver.quit()
