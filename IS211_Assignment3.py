import argparse
import csv
import re
from collections import Counter
from datetime import datetime
from urllib.request import urlretrieve

def main():
    parser = argparse.ArgumentParser(description='Process web log file.')
    parser.add_argument('url', help='The URL of the web log file.')
    args = parser.parse_args()

    filename = 'weblog.csv'
    urlretrieve(args.url, filename)

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    image_extensions = ['.jpg', '.gif', '.png']
    image_hits = [row for row in data if any(ext in row[0] for ext in image_extensions)]
    image_hits_percent = len(image_hits) / len(data) * 100
    print(f"Image requests account for {image_hits_percent:.1f}% of all requests")

    browsers = ['Firefox', 'Chrome', 'Internet Explorer', 'Safari']
    browser_hits = [row[2] for row in data if any(browser in row[2] for browser in browsers)]
    most_common_browser = Counter(browser_hits).most_common(1)[0][0]
    print(f"The most popular browser is {most_common_browser}")

    hours = [datetime.strptime(row[1], '%m/%d/%Y %H:%M:%S ').hour for row in data]
    hour_hits = Counter(hours)
    sorted_hour_hits - sorted(hour_hits.items(), key=lambda x: x[1], reverse=True)
    for hour, hits in sorted_hour_hits:
        print(f"Hour {hour} has {hits} hits")

if __name__ == "__main__":
    main()