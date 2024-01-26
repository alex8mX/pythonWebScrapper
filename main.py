import requests
import sqlite3

from datetime import datetime
from bs4 import BeautifulSoup

base_url = "https://www.freeimages.com/search/dogs"
max_images = 1000
db_file = 'scrapped_dog_img.db'

def scrap_data():
    
    page_index = 0
    images_array = []
    
    while len(images_array) < max_images:
        page_index += 1
        page_url = f"{base_url}/{page_index}"
        
        try:
            page = requests.get(page_url)
            page.raise_for_status()
    
        except requests.exceptions.RequestException as e:
            print(f"Error consltando url base: {e}")
            break
        
        soup = BeautifulSoup(page.content, "html.parser")
    
        results = soup.find(id="content-wrapper")
    
        not_contents_found_text_html = results.find_all(
            "p", string=lambda text: "no contents yet." in text.lower())
    
        if not_contents_found_text_html:
            break
    
        image_elements = results.find_all("div", class_="grid-item")
    
        for image_element in image_elements:
            image = image_element.find("img", class_="grid-thumb",
                                       alt=lambda alt: alt and alt != "iStock")
    
            if image:
                images_array.append(image["src"])
    
        print(f"Page index {page_index} scrapped")
        
    print(f"Total images: {len(images_array)}")
        
    return images_array

def insert_into_db(images_array=None):
    print("Connecting to db....")
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        create_table(cursor)
        print("Connected to database")

        for image in images_array:
            insert_image(cursor, image)

        conn.commit()
        fetch_records(cursor)
        
def create_table(cursor):
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS dogs_urls (
                         id INTEGER PRIMARY KEY,
                         url TEXT,
                         created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                         updated_at TEXT)''')
    except Exception as e:
        print(f"Error creando base de datos local: {e}")

    
def insert_image(cursor, image):
    try:
        cursor.execute("SELECT url FROM dogs_urls WHERE url = ?", (image,))
        result = cursor.fetchone()
        if result:
            print(f"Url already inserted: {result[0]}")
    
        cursor.execute('''INSERT INTO dogs_urls (url, created_at) 
                          VALUES (?, ?)''', (image, datetime.now()))
    except Exception as e:
        print(f"Error insertando url en la base de datos: {e}")
        print(image)

def fetch_records(cursor):
    try:
        cursor.execute('''SELECT * FROM dogs_urls''')
        results = cursor.fetchall()
        print(f"{len(results)} records inserted so far.")
    except Exception as e:
        print(f"Error consultando la base de datos: {e}")
    
    
def main():
    images_array = scrap_data()
    
    if images_array:
       insert_into_db(images_array)
    else:
        print("No data to insert into database")
       
       
if __name__ == "__main__":
    main()


