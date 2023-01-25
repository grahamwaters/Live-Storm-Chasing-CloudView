"""
1. Check the website https://livestormchasing.com/map for the video streams that are live. These can be found using selenium in headless mode at the css selector: #stream > div > div.container > video > src
2. The chasers are listed on the left in divs with this class <div class="p-2 relative">
within that div there is a button to share the link to their feed. It has the class "rounded-full h-8 w-8 flex items-center justify-center bg-grey-darker hover:bg-blue cursor-pointer"
Find these share buttons.
2. For each share button
2a. click the share button to copy the link. Then reload the page.
2b. open the link (that was copied)
2c. extract the video and add it to our dashboard in the `dashboard.html` file that will show the feed if it is live. Else it is black.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import shutil
from pathlib import Path
import panel as pn
from panel.interact import interact
from panel import widgets
import time
import datetime

# Set up the chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--dns-prefetch-disable")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-accelerated-2d-canvas")
chrome_options.add_argument("--disable-gpu-sandbox")
chrome_options.add_argument("--disable-breakpad")
chrome_options.add_argument("--disable-client-side-phishing-detection")
chrome_options.add_argument("--disable-cast")
chrome_options.add_argument("--disable-cast-streaming-hw-encoding")

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

# Get the page
driver.get("https://livestormchasing.com/map")

# Get the share buttons
share_buttons = driver.find_elements_by_class_name("rounded-full")

# Get the links
share_links = []
for button in share_buttons:
    share_links.append(button.get_attribute("href"))

# Get the video links
video_links = []
for link in share_links:
    driver.get(link)
    video_links.append(driver.find_element_by_tag_name("video").get_attribute("src"))

# Get the names of the chasers
names = []
for link in share_links:
    names.append(link.split("/")[-1])

# Show the video links
for name, link in zip(names, video_links):
    print(name, link)

# Close the driver
driver.close()

# Create the dashboard
import panel as pn
from panel.interact import interact
from panel import widgets
import time
import datetime

# Create the dashboard
dashboard = pn.Column()

# Add the video links
for name, link in zip(names, video_links):
    dashboard.append(pn.pane.HTML(
        f"""<h1>{name}</h1>
        <video src="{link}" controls autoplay loop></video>"""))

# Show the dashboard
dashboard.show()
