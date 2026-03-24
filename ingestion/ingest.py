from ingestion.parse_medline import parse_medlineplus_xml
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.db.vector_store import get_vector_store

DATA_PATH = "data/raw/mlplus_topics_2026-03-24.xml"


def ingest():
    print("Parsing XML...")
    documents = parse_medlineplus_xml(DATA_PATH)

    print(f"Loaded {len(documents)} structured documents")

    print("Splitting documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"Generated {len(chunks)} chunks")

    print("Storing in vector DB...")
    vectordb = get_vector_store()
    vectordb.add_documents(chunks)
    vectordb.persist()

    print("Ingestion complete.")