# Docker Network Graph

This tool can be used to draw a graph of connections and dependencies of your docker containers in your machine.

Reference:
- https://github.com/LeoVerto/docker-network-graph


How to use it:
```bash
git clone https://github.com/LeoVerto/docker-network-graph.git
cd docker-network-graph
pipenv install
pipenv run python docker-net-graph.py -o output.svg
```
