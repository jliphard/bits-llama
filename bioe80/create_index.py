from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

import os

print("Generating new index")

required_exts = [".md", ".pdf", ".txt"]

reader = SimpleDirectoryReader(
	input_dir="./data",
	required_exts=required_exts, 
	recursive=True
)

documents = reader.load_data()
print(f"Loaded {len(documents)} docs. Please be patient...")

index = VectorStoreIndex.from_documents(documents)

print(f"Indexing completed. Writing index to file...")
index.storage_context.persist()

print("All done - you can now query a BioE80 fine-tuned ChatGPT")