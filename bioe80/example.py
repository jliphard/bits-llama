from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

# may need to run 
# pip install torch transformers sentencepiece Pillow
# pip install pypdf

import os

reuse = False

if os.path.isfile("./storage/index_store.json") & reuse :
	print("found precomputed index - loading")
	# rebuild storage context
	storage_context = StorageContext.from_defaults(persist_dir="./storage")
	# load index
	index = load_index_from_storage(storage_context)
else :
	print("generating new index")
	# only load markdown and pdf files
	required_exts = [".md", ".pdf"]
	reader = SimpleDirectoryReader(
		input_dir="./data",
		required_exts=required_exts, 
		recursive=True
	)
	documents = reader.load_data()
	print(f"Loaded {len(documents)} docs")
	index = VectorStoreIndex.from_documents(documents)
	index.storage_context.persist()

query_engine = index.as_query_engine()

response = query_engine.query("How can DNA be synthesized?")

print(response)