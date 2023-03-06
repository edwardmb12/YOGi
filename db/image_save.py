import urllib.request
import csv
import os

with open('db/url.csv') as images:
    reader = csv.reader(images)

    for row in reader:
        try:
            url = row[1]
            filename = 'images/{}'.format(row[0])
            if not os.path.exists('images'):
                os.makedirs('images')
            print('Saving', url, 'to', filename)
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print('Failed to download image:', e)
