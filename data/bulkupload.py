from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)

# Connects to a server:
milvus_host = "host.docker.internal"
connections.connect("default", host=milvus_host, port="19530")

# Creates a collection:
fields = [
    FieldSchema(name="book_id", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="word_count", dtype=DataType.INT64),
    FieldSchema(name="book_intro", dtype=DataType.FLOAT_VECTOR, dim=2)
]
schema = CollectionSchema(fields, "sample books")
book_collection_name = "book2"
book_collection = Collection(book_collection_name, schema)

task_id = utility.do_bulk_insert(
    collection_name=book_collection_name,
    # partition_name="2022",
    files=["/data/books.json"]
)

index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}
book_collection.create_index("book_intro", index)

book_collection.load()


# #Inserts vectors in the collection:
# import random
# entities = [
#     [i for i in range(3000)],  # field pk
#     [float(random.randrange(-20, -10)) for _ in range(3000)],  # field random
#     [[random.random() for _ in range(8)] for _ in range(3000)],  # field embeddings
# ]
# insert_result = hello_milvus.insert(entities)

# # Builds indexes on the entities:
# index = {
#     "index_type": "IVF_FLAT",
#     "metric_type": "L2",
#     "params": {"nlist": 128},
# }
# hello_milvus.create_index("embeddings", index)

# # Loads the collection to memory and performs a vector similarity search:
# hello_milvus.load()
# vectors_to_search = entities[-1][-2:]
# search_params = {
#     "metric_type": "L2",
#     "params": {"nprobe": 10},
# }
# result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, output_fields=["random"])

# # Performs a vector query:
# result = hello_milvus.query(expr="random > -14", output_fields=["random", "embeddings"])

# #Performs a hybrid search:
# result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, expr="random > -12", output_fields=["random"])

# # Deletes entities by their primary keys:
# expr = f"pk in [{ids[0]}, {ids[1]}]"
# hello_milvus.delete(expr)

# # Drops the collection:
# utility.drop_collection("hello_milvus")





