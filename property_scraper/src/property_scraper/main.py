import typer
from typing_extensions import Annotated
from typing import List, Optional
from . import config
from .scraper import run_scraper
from .database import create_db_and_tables

app = typer.Typer()

@app.callback()
def callback():
    """
    Property Scraper CLI
    """

@app.command()
def scrape(
    urls: Annotated[Optional[List[str]], typer.Option(help="List of URLs to scrape.")] = None,
    min_price: Annotated[Optional[float], typer.Option(help="Minimum property price.")] = 1_500_000,
    max_price: Annotated[Optional[float], typer.Option(help="Maximum property price.")] = 2_500_000,
):
    """
    Scrape property data from the specified URLs.
    """
    typer.echo("Initializing database...")
    create_db_and_tables()

    target_urls = urls if urls else config.DEFAULT_URLS
    if not urls:
        typer.echo(f"No URLs provided, using default: {target_urls}")

    typer.echo("Starting scraper...")
    run_scraper(urls=target_urls, min_price=min_price, max_price=max_price)
    typer.echo("Scraping finished.")


if __name__ == "__main__":
    app()
