import os

BASE_DIR = "." 

structure = {
    "app": {
        "main.py": "",
        "api": {
            "routes.py": "",
        },
        "core": {
            "config.py": "",
            "logger.py": "",
        },
        "rag": {
            "pipeline.py": "",
            "retriever.py": "",
            "generator.py": "",
            "prompt.py": "",
        },
        "db": {
            "vector_store.py": "",
        },
        "schemas": {
            "chat.py": "",
        },
    },
    "data": {
        "raw": {}
    },
    "ingestion": {
        "ingest.py": "",
    },
    "ui": {
        "streamlit_app.py": "",
    },
    "eval": {
        "evaluate.py": "",
    },
    "Dockerfile": "",
    "docker-compose.yml": "",
    "requirements.txt": "",
    ".env": "",
}


def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)

        # File
        if isinstance(content, str):
            if not os.path.exists(path):
                with open(path, "w") as f:
                    f.write(content)

        # Folder
        elif isinstance(content, dict):
            os.makedirs(path, exist_ok=True)

            # add __init__.py (important for imports)
            init_file = os.path.join(path, "__init__.py")
            if not os.path.exists(init_file):
                open(init_file, "w").close()

            create_structure(path, content)


if __name__ == "__main__":
    create_structure(BASE_DIR, structure)
    print("Project structure created in Hosi Bora AI root.")