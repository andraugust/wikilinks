import os
import sys

## Params
try:
	nnodes = int(sys.argv[1])  # more nodes may be generated in order to show connectivity (otherwise there are a bunch of nodes by themselves)
except:
	sys.exit('ERROR! Argument for number of nodes must be provided as input')
	
cwd = os.getcwd()
edges_output_path = os.path.join(cwd,'edges.json')
nodes_output_path = os.path.join(cwd,'nodes.json')

# make edge list and node list
edge_list = []
node_list = []
nodes = {}

with open(cwd+'/data/net.txt','r', encoding = 'latin10') as f:
    lines = f.read().rstrip().split('\n')
    for i,line in enumerate(lines):
        from_, to_ = line.split('\t')
        edge_list.append({"from": from_, "to": to_})
        # node_list.append({"id": from_, "name": from_})
        nodes[from_] = ''
        nodes[to_] = ''
        if i == nnodes:
            break

node_list = [{'id': n,'label': n} for n in nodes]

# save json
import json
with open(edges_output_path,'w') as f:
    json.dump(edge_list,f)
with open(nodes_output_path,'w') as f:
    json.dump(node_list,f)