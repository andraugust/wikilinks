# Welcome

Welcome to wikilinks, a project for visualizing the first-link structure of Wikipedia.

Q: Who wants to visualize the first-link structure of Wikipedia?

A: Anyone interested in seeing the abstraction structure of human knowledge...  First-links generally lead to an abstraction/generalization of the current page, so by visualizing first links we can approximate the abstraction structure of... _everything_.

# Quick start
This project aims to be a web app, so running it requires a server. I use
```
$ cd wikilinks
$ python -m http.server
```
Then browse to `localhost:8000/net.html`.

What's shown is a set of nodes and directed edges.  Each node represents a wikipedia page and each edge points to its first link.

In the end the visualization should be quick to initialize and show as many nodes as possible.

# Design
We use [vis.js](http://visjs.org/) (`vis-4.21.0`) to visualize the network.  

vis.js creates a network based on the data in `nodes.json` and `edges.json`.  Other information related to layout is in `net.html`.

The data in `nodes.json` and `edges.json` contains __only part of the network.__  The entire network is way too big to render right now. Big rendering is under construction...

You can test different sized networks by making your own `nodes.json` and `edges.json`.  To do this simply run

`$ python3 tab_delim2json.py <num_nodes>`

and then refresh the browser. (Be that the browser cache refreshes to relfect changes, e.g. press `ctrl+refresh` on mac with chrome).

# Todo
- __Figure out how to render lots of nodes efficiently__.  The entire network is really huge: 5,401,148 nodes.  Usually when the browser opens a physics simulation runs to find the optimal node positioning; this is intensive.  Ideally, the sim should only be done and then positions should be cached. Note: many nodes lead to deadends and most nodes are on the outskirts of the network; do we care about seeing these nodes?
- __Fix simpler stuff__
