# Web-Scraper-for-IndiaCorpLaw

Sure, here's a sample README file:

# Web Scraper for IndiaCorpLaw

This Python script scrapes articles from the first five pages of [IndiaCorpLaw](https://indiacorplaw.in/) and saves the data in a JSON file. The script is scheduled to run every day at 10:30.

## How to Run the Script

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```

3. Run the script:

    ```
    python scraper.py
    ```

The script will start running and will scrape the website every day at 10:30.

## Notes

- The script uses BeautifulSoup to parse the HTML of the website and extract the data.
- The script also converts any HTML tables in the articles to Markdown format.
- The scraped data includes the title and content of each article, as well as a timestamp of when the data was scraped.
- The script needs to be running continuously for the scheduling to work. If you need to run this on a server or in the cloud, you might need to set up a more robust scheduling solution, such as a cron job or a cloud function.

## Requirements

- Python 3.10.9
- BeautifulSoup4
- requests
- schedule

And here's the `requirements.txt` file:

```
beautifulsoup4==4.11.1
requests==2.28.1
schedule==1.2.0
```

These are the versions of the packages that the script was tested with. Newer versions should also work, but if you encounter any issues, try installing these specific versions.
