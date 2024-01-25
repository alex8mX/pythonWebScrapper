import requests
from bs4 import BeautifulSoup

url = "https://www.freeimages.com/search/dogs"
page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="content-wrapper")

image_elements = results.find_all("div", class_="grid-item")


for image_element in image_elements:
    image = image_element.find("img", class_="grid-thumb")
    
    if image:
        if image["alt"] != "iStock":

            print(image["src"])
            print("")
        else:
            print(image)
            print("")

    
