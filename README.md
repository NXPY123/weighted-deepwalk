# weighted-deepwalk
Weighted Random Walk Implementation for DeepWalk (in Python) 

The deepwalk [1] with weighted edge graph is implemented here. 

# Installation: 

## Using docker-compose:

1. Run the following command to build the docker image: 

      `docker-compose build`

## Manual Installation:

1. Install original deepwalk package: 

      `pip install deepwalk`

2. Move 'main.py' and 'weighted_random_walk.py' into the python lib directory for deepwalk 

# Usage:

## Using docker-compose:

1. Place the Weighted Edges in the volume/Weighted Edges directory.

2. Run the following command to execute the deepwalk with weighted edges:

      `docker-compose up`

## Manual Installation:

      deepwalk --input input.file --format weighted_edgelist --output output.file

Reference: 

[1] deepwalk: https://github.com/phanein/deepwalk
