import csv, re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Scrapes jokes from http://jokes.cc.com/
if __name__ == '__main__':
    cc_url = 'http://jokes.cc.com/'
    cc = urlopen(cc_url).read()
    ccsoup = BeautifulSoup(cc, 'html.parser')
    links = [link.get('href') for link in ccsoup.find_all('a')]
    category_links = [link for link in links if re.match('http://jokes.cc.com/funny-.*', link)]
    for category_link in category_links[2:]:
        category_soup = BeautifulSoup(urlopen(category_link), 'html.parser')
        category_title = re.match('http://jokes.cc.com/(.*)', category_link).group(1)
        category_title = category_title.replace('/', '-')
        with open('data/' + category_title + '.txt', 'w+') as f:
            joke_links = [x.get('href') for x in category_soup.find_all('a') if re.match(category_link + '/.*', x.get('href'))]
            for joke_link in joke_links[:100]:
                joke_soup = BeautifulSoup(urlopen(joke_link), 'html.parser')
                joke = joke_soup.find(class_='content_wrap').p.get_text()
                joke = joke.replace('\n', '\\n ')
                f.write(joke + '\n')
                print(joke)
            f.close()

