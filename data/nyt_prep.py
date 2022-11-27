import h5py

input_fn = "/data/nytimes-256-angular.hdf5"
output_fn = "/data/nyt_test.hdf5"

data = h5py.File(input_fn, 'r')

with h5py.File(output_fn,'w') as f_dest:
    f_dest.create_dataset("embeddings", data=data["test"])
