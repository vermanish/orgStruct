from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import requests
import json
import urllib2
import re
# Create your views here.
def home(request):
	url = 'https://api.zenefits.com/core/companies'
	headers = {"Content-Type":"application/x-www-form-urlencoded",'Authorization': 'Bearer h3DxXrAOTHW6V91MFlXN'}
	v=requests.get(url,headers=headers).json()
	companyId= v['data']['data'][0]['id']
	url ='https://api.zenefits.com/core/companies/'+companyId +'/people'
	v=requests.get(url,headers=headers).json()

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
	tree=json.dumps(tree)
	print tree
	
	# with open('/../static/orgView/js/finalJson.json', 'w') as outfile:  
	#     data=json.dump(tree, outfile)
	#     # print data


	return render_to_response('index.html', {"my_data":tree})