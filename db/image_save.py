import urllib.request
import csv
import os

with open('db/url.csv') as images:
    reader = csv.reader(images)
    num = 1
    for row in reader:
        try:
            url = row[2]
            filename = 'Plow_Pose_or_Halasana_/{}.jpg'.format(num)
            if not os.path.exists('Plow_Pose_or_Halasana_'):
                os.makedirs('Plow_Pose_or_Halasana_')
            print('Saving', url, 'to', filename)
            urllib.request.urlretrieve(url, filename)
            num += 1
        except Exception as e:
            print('Failed to download image:', e)
