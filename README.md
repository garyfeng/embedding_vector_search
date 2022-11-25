# embedding_vector_search
prototyping global search for embedding vectors

# Introduction
The objective of this repo is to prototype a global search tool for embedding vectors of the scale of roughly:
- 1-10M vectors
- 200-2k dimensions
- Top 10 results, with recall of _???_
- SLA < 1 sec

# Datasets
For testing, we use the following strategy

## Synthetic datasets
Generate random vectors using `scikit-learn`, see examples in https://github.com/erikbern/ann-benchmarks/blob/14df47df72bb1deee5d9e68616ba03edf65d4680/ann_benchmarks/datasets.py#L473

Parameters: 

## Open source datasets
See https://github.com/erikbern/ann-benchmarks for available test vectors, in HDF5 format. Choose some that are closer to our needs.

## Proprietary datasets
We can generate our own embedding vectors.

# Loading/Enrolling
We need to load the embedding vectors to a proper data structure, either in memory or in a database. For the application we have in mind, we also need to link the vectors to some metadata, presummably in a JSON object. 

# Search
We conduct a 10-NN search over the full list that is *filtered based on the metadata*. 

