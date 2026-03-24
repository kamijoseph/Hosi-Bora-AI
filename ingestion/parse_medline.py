import xml.etree.ElementTree as ET
from langchain_core.documents import Document
import re

def parse_medlineplus_xml(file_path: str):
    tree = ET.parse(file_path)
    root = tree.getroot()

    documents = []

    for topic in root.findall(".//health-topic"):
        title_elem = topic.find("title")
        summary_elem = topic.find("full-summary")

        title = title_elem.text if title_elem is not None else "Unknown"
        summary = summary_elem.text if summary_elem is not None else ""

        # 1. Add summary as a document
        if summary:
            documents.append(
                Document(
                    page_content=summary.strip(),
                    metadata={
                        "title": title,
                        "section": "summary",
                        "source": "MedlinePlus"
                    }
                )
            )

        # 2. Extract sections
        for group in topic.findall("group"):
            section_title_elem = group.find("title")
            section_text_elem = group.find("text")

            if section_title_elem is None or section_text_elem is None:
                continue

            section_title = section_title_elem.text
            section_text = section_text_elem.text

            if section_text:
                documents.append(
                    Document(
                        page_content=section_text.strip(),
                        metadata={
                            "title": title,
                            "section": section_title,
                            "source": "MedlinePlus"
                        }
                    )
                )

    return documents


def clean_text(text: str) -> str:
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()