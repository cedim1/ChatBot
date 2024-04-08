print("Scratch project url")
x = imput()
cloud_data = requests.get('https://clouddata.scratch.mit.edu/logs?projectid=-' + x + '&limit=100&offset=0')
if cloud_data.ok:
    cloud_data_json = json.loads(cloud_data.content)
else:
    print("Error: " + cloud_data.reason)
