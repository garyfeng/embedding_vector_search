from pymilvus import utility
task_id = utility.do_bulk_insert(
    collection_name="book",
    partition_name="2022",
    files=["books.json"]
)
