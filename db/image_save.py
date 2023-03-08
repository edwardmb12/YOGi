import urllib.request
import csv
import os

with open('db/url.csv') as images:
    reader = csv.reader(images)
    num = 1
    for row in reader:
        try:
            url = row[2]
            filename = 'Fish_Pose_or_Matsyasana_/{}.jpg'.format(num)
            if not os.path.exists('Fish_Pose_or_Matsyasana_'):
                os.makedirs('Fish_Pose_or_Matsyasana_')
            print('Saving', url, 'to', filename)
            urllib.request.urlretrieve(url, filename)
            num += 1
        except Exception as e:
            print('Failed to download image:', e)
