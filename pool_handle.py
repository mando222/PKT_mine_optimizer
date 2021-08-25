#!/usr/bin/env python3

from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

wallet_address="pkt1q6aut4088e0fz3qx0flyle9m6rr23dy6e6daxdu"


class Pool:
    name = ""
    win_percent = 
    xPath=""

site_url="http://pkt.world/explorer?wallet=&blocks=60"

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

pool1 = Pool()
pool2 = Pool()
pool3 = Pool()
driver.get(site_url)

print(driver.page_source)

# nohup ./target/release/packetcrypt ann -p pkt1q6aut4088e0fz3qx0flyle9m6rr23dy6e6daxdu http://pool.pktpool.io http://pool.pkteer.com http://pktco.in &
