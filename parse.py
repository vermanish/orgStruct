import requests
import json
import urllib2
import re
def extracting_data():
	from requests_oauthlib import OAuth1

	url = 'https://api.zenefits.com/core/companies'
	headers = {"Content-Type":"application/x-www-form-urlencoded",'Authorization': 'Bearer h3DxXrAOTHW6V91MFlXN'}
	v=requests.get(url,headers=headers).json()
	companyId= v['data']['data'][0]['id']
	url ='https://api.zenefits.com/core/companies/'+companyId +'/people'
	v=requests.get(url,headers=headers).json()

	# with open('dynamicData.json','w') as data_json:
	# 	data=json.dump(v,data_json);

	# with open('dynamicData.json') as data_up:
	data1=v
	dict={}
	dict['data']=[]
	for r in data1['data']['data']:
		s=r['manager']['url']
		parentId=[""]
		if s:
			parentId=re.findall("D*(\d+)", s)
					#print (parentId[0])
				
		dict['data'].append({
			"text":r['preferred_name'] ,
			"id":r['id'],
			"manager":parentId[0],
			"nodes":[]
			})

	# with open('parsedFile.json', 'w') as outfile:  
	#     data=json.dump(dict, outfile)
	#     # print data

	# with open('parsedFile.json') as json_data:
	# 	data1=json.load(json_data)
		#data2=json.dumps(json.load(json_data))
	dataMap={}
	for r in dict['data']:
		dataMap[r['id']]=r;
	tree=[]
	for r in dict['data']:
		s=r['manager']
		if s:
			parent=dataMap[s]
			children=parent['nodes']
			children.append(r)
			dataMap[s]['nodes']=children
			parent['nodes']=children
		else:
			tree.append(dataMap[r['id']])
	print("tree: ")
	print tree
		
	with open('heirarchy view/hierarchyData.json', 'w') as outfile:  
	    data=json.dump(tree, outfile)
	    # print data
extracting_data()
