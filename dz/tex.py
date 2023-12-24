import re
import requests
from bs4 import BeautifulSoup

url = 'https://api.r46.technodom.kz/search?did=Gz8YKlIvTM&extended=true&limit=24&locations=10&no_clarification=true&page=1&referer=https%3A%2F%2Fwww.technodom.kz%2Fsearch%3Frecommended_by%3Dinstant_search%26recommended_code%3DIphone%26r46_search_query%3DIphone%26r46_input_query%3DIphone&seance=9FEzeHqCJK&search_query=Iphone&shop_id=74fd3b613553b97107bc4502752749&sid=9FEzeHqCJK&sort_by=score&sort_dir=desc&type=full_search&filters=%7B%7D'
response = requests.get(url)
html_content = response.json()

soup = BeautifulSoup(html_content["html"], 'html.parser')

for li_element in soup.find_all('li', {'class': re.compile('^ProductCard')}):
  product_title = li_element.findAll('h4')[0].string

  if "256" in product_title:
      product_price = li_element.findAll('data')[0].string
      print(f'{product_title} {product_price}\n')