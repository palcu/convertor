import arrow
import csv
from bs4 import BeautifulSoup


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
        writer.writerows(get_submission_results(soup))


with open('example_submission_page.html') as stream:
    parse_submission(1360382, stream.read())
