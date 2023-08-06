from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()
PROJECT_DIR = args.path + '/data'

print("Generating new index")

required_exts = [".md", ".pdf", ".txt"]

reader = SimpleDirectoryReader(
	input_dir=PROJECT_DIR,
	required_exts=required_exts, 
	recursive=True
)

documents = reader.load_data()
print(f"Loaded {len(documents)} docs. Please be patient...")

index = VectorStoreIndex.from_documents(documents)

print(f"Indexing completed. Writing index to file...")
STORAGE_DIR=args.path + '/storage'
index.storage_context.persist(persist_dir=STORAGE_DIR)

print("All done - you can now query a fine-tuned ChatGPT")