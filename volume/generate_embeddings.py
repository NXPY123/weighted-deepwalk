import os
import sys

def generate_embeddings():
    files = os.listdir('/app/Weighted Edges')
    for file in files:
        if file.endswith('.txt'):
            os.system(f"deepwalk --input '/app/Weighted Edges/{file}' --format weighted_edgelist --output '/app/Node Embeddings/{file}.embeddings'")
            print(f"Embeddings generated for {file}")

if __name__ == '__main__':
    generate_embeddings()