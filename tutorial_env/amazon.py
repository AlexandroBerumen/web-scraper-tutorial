# connect to website
from bs4 import BeautifulSoup
import requests
import os
import sys
os.path.dirname(sys.executable)


URL = "https://www.amazon.com/dp/B000QSTBNS?ref=nb_sb_ss_w_as-reorder-t1_k0_1_4&amp=&crid=35EADCRXXQ7EL&amp=&sprefix=prot"



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

Soup1 = BeautifulSoup(page.content, "html.parser")


print(Soup1)
# print('hi')