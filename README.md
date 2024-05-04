Washington Post scraper

Project gathers the latest news headlines, descriptions, and links from The Washington Post website within the past 24 hours and saves them into a JSON file. The JSON file format includes the title of the news article, its description, and a direct link to the full article.


     Features
Web Scraping: The scraper utilizes BeautifulSoup and requests libraries to fetch the latest headlines and article details from The Washington Post's "Latest Headlines" page.
Data Extraction: It extracts key information such as the news headline, description, and article link from the HTML structure of the webpage.
JSON Serialization: Extracted data is serialized into a JSON file format for easy storage, retrieval, and further processing.
Automated Updates: The script can be scheduled to run periodically to keep the JSON file updated with the latest news from The Washington Post.
    
    How to Use
Make sure to install:
BeautifulSoup4, requests

To use the project, simply run the provided Python script. It will automatically scrape the latest news headlines from The Washington Post's website and save them into a JSON file named "latest_news.json". 
You can then access the JSON file to view the collected news articles and their details.
