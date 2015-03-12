from bs4 import BeautifulSoup


entries = []

def parse_webpage(page):
    soup = BeautifulSoup(page)
    table = soup.find('table', class_='monitor')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        entries.append(cols[0][1:])

for i in range(1, 13):
    with open('webpages/pag{0}.html'.format(i)) as stream:
        parse_webpage(stream.read())

for entry in entries:
    print entry
