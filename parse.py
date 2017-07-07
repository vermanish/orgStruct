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
	
with open('finalJson.json', 'w') as outfile:  
    data=json.dump(tree, outfile)
    # print data