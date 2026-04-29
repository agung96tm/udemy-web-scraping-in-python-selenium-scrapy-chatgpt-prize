import requests
from bs4 import BeautifulSoup

base_website = "https://subslikescript.com"
website = f"{base_website}/movies"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")

links = []
box = soup.find("article", class_="main-article")
for link in box.find_all("a", href=True):
    links.append(link["href"])

for link in links:
    website = f"{base_website}/{link}"
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, "lxml")

    box = soup.find("article", class_="main-article")

    title = box.find("h1").get_text()
    transcript = box.find("div", class_="full-script").get_text(strip=True, separator=" ")

    with open(f"{title}.txt", "w") as file:
        file.write(transcript)
