import requests
from lxml import html

def concat_text(array_to_concat):
    str = ""
    for line in array_to_concat:
        str += line.text
    return str

response = requests.get('https://www.geartrade.com/hiking-and-camping/tents/four-season-tents')
tree = html.fromstring(response.text)
result = tree.xpath('/html/body/div[2]/main/div/section[2]/section/div/article/a')

for line in result:
    url = line.attrib["href"].strip()
    name = concat_text(line.xpath('div[2]/span')).strip()
    price = line.xpath('div[4]/div[1]')[0].text.strip()
    print(name + ", ", end="")
    print(url + ", ", end="")
    print(price)