from rakam_systems.components.vector_search.vector_store import VectorStore
from rakam_systems.components.data_processing.content_extractors import AdvancedPDFParser
from rakam_systems.core import Node, NodeMetadata, VSFile

# Create a vector store and add the documents (nodes)
base_index_path = "vector_store"
vector_store = VectorStore(base_index_path=str(base_index_path), embedding_model="sentence-transformers/all-MiniLM-L6-v2", initialising=True)


advanced_parser = AdvancedPDFParser()
vs_file = advanced_parser.parse_one_pdf("application/engine/agent_RAG/General_Terms_and_Conditions.pdf")
collection_name = "shop_information_pdf_text"
vector_store.create_collection_from_files(collection_name=collection_name, files=[vs_file])
