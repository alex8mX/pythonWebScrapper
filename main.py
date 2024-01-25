import requests
from bs4 import BeautifulSoup

base_url = "https://www.freeimages.com/search/dogs"
max_images = 1000

page_index = 0
images_array = []

while len(images_array) < max_images:
    page_index += 1
    page_url = f"{base_url}/{page_index}"
    page = requests.get(page_url)
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

    print(f"page index {page_index}")
    print(f"total images: {len(images_array)}")
