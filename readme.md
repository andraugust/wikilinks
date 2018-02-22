# Welcome

Welcome to wikilinks, a project for visualizing the first-link structure of Wikipedia.

Q: Who wants to visualize the first-link structure of Wikipedia?

A: Anyone interested in seeing the abstraction structure of human knowledge!  First links generally lead to an abstraction/generalization of the current page, so by visualizing first links we can approximate the abstraction structure of... _everything_.

# Quick start: running the app
This project aims to be a web app, so running it requires a server. I use
```
$ cd wikilinks
$ python -m http.server
```
Then browse to `localhost:8000/net.html`.

What's shown is a set of nodes and directed edges.  Each node represents a wikipedia page and each edge points to its first link.

In the end the visualization will be sweet and cool.

# Design
We use [vis.js](http://visjs.org/) (`vis-4.21.0`) to visualize the network.  

vis.js creates a network based on the data in `nodes.json` and `edges.json`.  Other information related to layout is in `net.html`.

The data in `nodes.json` and `edges.json` contains __only part of the network.__  The entire network is way too big to render right now. Big rendering is currently under construction.

You can test your own sizes by running `$ python3 tab_delim2json.py <num_nodes>` and then open `net.html`. (Be sure to refresh browser cache to show changes, e.g. with `ctrl+refresh` on mac chrome).

# Todo
- __Figure out how to render lots of nodes efficiently__.  The entire network is really huge: 5,401,148 nodes.  Usually when the browser opens a physics simulation finds the final node positions.  This is intensive.  Ideally, the sim should be done once and positions should be cached. Note: many nodes lead to deadends, most nodes are on the outskirts of the network.  Do we care about seeing these nodes?
- __Fix simpler stuff__
