# step1_loader.py
from langchain_community.document_loaders import UnstructuredExcelLoader
import pandas as pd
import re
# from langchain.docstore.document import Document

loader = UnstructuredExcelLoader("D:\\LLM_L\\LLM_L\\Project.xlsx", mode="elements")
docs = loader.load()  # list[Document]
from pprint import pprint

def inspect_docs(docs, n=5):
    print("docs type:", type(docs))
    print("num docs:", len(docs))
    if len(docs) == 0:
        print("No documents returned by loader. Check path, permissions, or loader mode.")
        return
    for i, d in enumerate(docs[:n]):
        print(f"\n--- doc {i} ---")
        print("element type:", type(d))
        # If it's a LangChain Document object:
        if hasattr(d, "metadata"):
            print("metadata keys:", list(d.metadata.keys()))
            pprint({k: (type(v), (str(v)[:200] + '...') if isinstance(v, str) else v)
                    for k, v in d.metadata.items()})
            ta = d.metadata.get("text_as_html")
            print("has text_as_html:", bool(ta), "length:", len(ta) if isinstance(ta, str) else None)
        else:
            print("No metadata attribute found on this element. Inspect repr:")
            print(repr(d)[:1000])
        pc = getattr(d, "page_content", None)
        print("page_content present:", bool(pc), "len:", len(pc) if pc else 0)
        if pc:
            # repr shows escaped newlines and hidden whitespace
            print("page_content repr snippet:", repr(pc[:500]).replace("\\n", "\\n"))
        # If loader returned lower-level table elements, show attributes
        for attr in ("type", "id", "tag", "text"):
            if hasattr(d, attr):
                print(f"has attr {attr}: {getattr(d, attr)}")

# Run the inspector
inspect_docs(docs, n=3)
