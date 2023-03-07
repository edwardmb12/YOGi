import urllib.request
import csv
import os

with open('db/url.csv') as images:
    reader = csv.reader(images)
    num = 1
    for row in reader:
        try:
            url = row[2]
            filename = 'Yogic_sleep_pose/{}'.format(num)
            if not os.path.exists('images'):
                os.makedirs('images')
            print('Saving', url, 'to', filename)
            urllib.request.urlretrieve(url, filename)
            num += 1
        except Exception as e:
            print('Failed to download image:', e)
