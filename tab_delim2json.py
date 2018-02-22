import os
import sys

## Params
nnodes = int(sys.argv[1])  # more nodes may be generated in order to show connectivity (otherwise there are a bunch of nodes by themselves)

cwd = os.getcwd()
edges_output_path = cwd+'/edges.json'
nodes_output_path = cwd+'/nodes.json'

# make edge list and node list
edge_list = []
node_list = []
nodes = {}

with open(cwd+'/data/net.txt','r') as f:
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