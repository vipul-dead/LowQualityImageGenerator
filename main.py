import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve


def fetch_google_images(query, num_images=10, save_folder="images"):
    base_url = "https://www.google.com/search"
    params = {"q": query, "tbm": "isch", "ijn": "0"}

    response = requests.get(
        base_url, params=params, headers={"User-Agent": "Mozilla/5.0"}
    )
    soup = BeautifulSoup(response.text, "html.parser")

    image_links = []
    for img in soup.find_all("img", {"src": re.compile(r"^https://")}):
        image_links.append(img["src"])

    os.makedirs(save_folder, exist_ok=True)

    for i, link in enumerate(image_links[:num_images], 1):
        filename = os.path.join(save_folder, f"image_{i}.jpg")
        urlretrieve(link, filename)
        print(f"Image {i} saved to {filename}")


query = input("query ")
fetch_google_images(query, num_images=10, save_folder=query)
