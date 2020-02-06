import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtexts):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None) #default=None in case of no link
    vote = subtexts[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)

def scrape_page(link):
  res = requests.get(link) 
  soup = BeautifulSoup(res.text, 'html.parser') # BS also parse xml

  links = soup.select('.storylink')
  subtexts = soup.select('.subtext')

  return create_custom_hn(links, subtexts)

def get_link_by_page(link, page=1):
  if page == 1:
    return link
  else:
    return f'{link}?p={page}'

page = 1
hacker_news = []
while True:
  hacker_news.extend(scrape_page(get_link_by_page('https://news.ycombinator.com/news', page)))
  
  choice = input('Do you want to add next page to your searches(y/n)?')
  if 'n' in choice:
    break
  page += 1

print(f'Results from {page} pages:')
pprint.pprint(sort_stories_by_votes(hacker_news))
print(len(hacker_news))
# pprint.pprint(create_custom_hn(links, subtexts))


