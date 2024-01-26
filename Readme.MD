# Scrap Dog Images

This Python script allows you to scrape dog images from the website FreeImages and store the image URLs in a SQLite database. It is useful for collecting a dataset of dog images for various purposes, such as machine learning projects, data analysis, or simply for personal use.

## Prerequisites

Before running the script, make sure you have the following installed:

    Python (version 3.x)
    requests library
    sqlite3 library
    beautifulsoup4 library

You can install the required libraries using the following commands:

```
pip install requests
pip install beautifulsoup4

```

## How to Use

Clone the repository:

```
git clone https://github.com/alex8mX/pythonWebScrapper.git
```

Run the script:

```
python main.py
```
### Configuration

    base_url: The base URL of the website to scrape. Default is set to "https://www.freeimages.com/search/dogs".
    max_images: The maximum number of images to scrape. Default is set to 1000.
    db_file: The SQLite database file to store the image URLs. Default is set to "scrapped_dog_img.db".

### Database Schema

The script creates a SQLite database with the following table:

    dogs_urls: Table to store the scraped dog image URLs.
    id: Primary key.
    url: URL of the dog image.
    created_at: Timestamp indicating when the record was created.
    updated_at: Timestamp indicating when the record was last updated.

### Error Handling

The script handles errors gracefully during the scraping, database creation, insertion, and querying processes. If any error occurs, it is logged, and the script attempts to continue its execution.

#### Notes

    The script prints progress messages and error information to the console during execution.
    Make sure to adjust the base_url, max_images, and db_file variables in the script according to your requirements.

#### Contributors

    Alex Alvarado (alex8m@gmail.com)
