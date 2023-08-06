from llama_index import StorageContext, load_index_from_storage
import os

if os.path.isfile("./storage/index_store.json") :
	print("Found index - loading - this may take a few seconds")
	# rebuild storage context
	storage_context = StorageContext.from_defaults(persist_dir="./storage")
	# load index
	index = load_index_from_storage(storage_context)
else :
	print("please generate an index first")
	quit()

query_engine = index.as_query_engine()
response = query_engine.query("What's the best way to synthesize DNA?")
print(response)

query_engine = index.as_query_engine()
response = query_engine.query("Can you explain more about oligo assembly")
print(response)