import arrow
import csv
import time
from bs4 import BeautifulSoup
import requests


LAST_UNINDEXED_ENTRY = 20


def get_timestamp_from_romanian_locale(s):
    date_parts = s.split()
    month = {
        'februarie': 2,
        'ianuarie': 1
    }
    time_parts = date_parts[3].split(':')
    datetime = arrow.Arrow(int(date_parts[2]), month[date_parts[1]],
                           int(date_parts[0]), int(time_parts[0]),
                           int(time_parts[1]), int(time_parts[0]))
    return datetime.timestamp


def get_submission_details(soup):
    username = soup.find('span', class_='username').get_text()
    score = soup.find('td', class_='score').get_text().strip()
    date = get_timestamp_from_romanian_locale(
        soup.find('td', class_='submit-time').get_text().strip())
    return [username, score, date]


def get_submission_results(soup):
    results = []

    table = soup.find('table', class_='job-eval-tests')
    rows = table.find('tbody').find_all('tr')

    for row in rows[:-1]:
        cells = [cell.text.strip() for cell in row.find_all('td')]
        results.append(cells)

    return results


def parse_submission(submission_id, html):
    soup = BeautifulSoup(html)

    with open('submissions.csv', 'a') as stream:
        writer = csv.writer(stream)
        writer.writerow([submission_id] + get_submission_details(soup))

    with open('submissions/{0}.csv'.format(str(submission_id)), 'w') as stream:
        writer = csv.writer(stream)
        try:
            writer.writerows(get_submission_results(soup))
        except:
            print("Could not get table with submission results")


infoarena_cookie = ''
with open('cookie.txt') as stream:
    infoarena_cookie = stream.read().strip()


with open('entries.txt') as stream:
    entries = stream.readlines()[LAST_UNINDEXED_ENTRY:]
    for i, entry in enumerate(entries):
        entry_id = int(entry)
        print("Parsing {0} ({1}/{2})".format(entry_id, i, len(entries)))

        url = 'http://www.infoarena.ro/job_detail/{0}'.format(entry_id)
        response = requests.get(url,
            cookies={'infoarena2_session': infoarena_cookie})

        if response.status_code != 200:
            raise Exception('Status code was {0}'.format(response.status_code))

        parse_submission(entry_id, response.content)
        time.sleep(1)
