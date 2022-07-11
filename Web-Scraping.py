from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc/p/N82E16814137632?Description=rtx%20gpu&cm_re=rtx_gpu-_-14-137-632-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="$")
# print(prices)
parent = prices[0].parent
# print(parent)

strong = parent.find("strong")
print(strong.string)
