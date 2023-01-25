import requests
from bs4 import BeautifulSoup

url = "https://livestormchasing.com/chasers/brad.arnold"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

video_element = soup.find("video", {"data-html5-video":""})

if video_element:
    video_url = video_element.get("src")
else:
    video_url = None


print(video_url)


src_url = 'blob:https://livestormchasing.com/fccd36f7-b81c-4656-9242-fee14b266dbf'
with open("video.html", "w") as f:
    f.write(f"""
    <html>
    <body>
    <iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>
    </html>
    """)