import json
import re
with open('out.json') as data_up:
	data1=json.load(data_up)
	dict={}
	dict['data']=[]
	for r in data1['data']['data']:
		s=r['manager']['url']
		parentId=[""]
		if s:
			parentId=re.findall("D*(\d+)", s)
				#print (parentId[0])
			
		dict['data'].append({
			"name":r['preferred_name'] ,
			"id":r['id'],
			"manager":parentId[0],
			"children":[]
			})
	
with open('parsedFile.json', 'w') as outfile:  
    data=json.dump(dict, outfile)
    # print data

with open('parsedFile.json') as json_data:
	data1=json.load(json_data)
	#data2=json.dumps(json.load(json_data))
	dataMap={}
	for r in data1['data']:
		dataMap[r['id']]=r;
	tree=[]
	for r in data1['data']:
		s=r['manager']
		if s:
			parent=dataMap[s]
			children=parent['children']
			children.append(r)
			dataMap[s]['children']=children
			parent['children']=children
		else:
			tree.append(dataMap[r['id']])
	print("tree: ")
	print tree
	
with open('finalJson.json', 'w') as outfile:  
    data=json.dump(tree, outfile)
    # print data