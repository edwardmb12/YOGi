import urllib.request
import csv
import os

with open('db/url.csv') as images:
    reader = csv.reader(images)
    num = 1
    for row in reader:
        try:
            url = row[2]
            filename = 'Feathered_Peacock_Pose_or_Pincha_Mayurasana_/{}.jpg'.format(num)
            if not os.path.exists('Feathered_Peacock_Pose_or_Pincha_Mayurasana_'):
                os.makedirs('Feathered_Peacock_Pose_or_Pincha_Mayurasana_')
            print('Saving', url, 'to', filename)
            urllib.request.urlretrieve(url, filename)
            num += 1
        except Exception as e:
            print('Failed to download image:', e)
