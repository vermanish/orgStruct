import json
with open('out.json') as data_up:
	data1=json.load(data_up)
	fo=open('parsedFile.json','wb')
	for r in data1['data']['data']:
		fo.write('{')
		fo.write('"name":"' + r['preferred_name'] +'",')
		fo.write("\n")
		fo.write('"id": ' + r['id'] + '},')
		fo.write("\n")
		print (r['preferred_name'])