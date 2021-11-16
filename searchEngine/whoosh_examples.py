import os.path
# import Classes.Path
if not os.path.exists("indexdir"):
    os.makedirs("indexdir")
# store_path = os.path
from whoosh.fields import *
from whoosh.analysis import StemmingAnalyzer, RegexAnalyzer
from whoosh.index import create_in


class MyIndexWriter:
    def __init__(self):
        schema = Schema(
            doc_no = ID(store=True),
            doc_comtemnt= TEXT(analyzer=RegexAnalyzer(),stored=True),
            title=TEXT())
        indexing = create_in("indexdir", schema)

        self.writer = indexing.writer()

    def index(self, docNo, title, content):

writer.add_document(title=u"First document", path=u"/a",
                    content=u"This is the first document we've added!")
writer.add_document(title=u"Second document", path=u"/b",
                    content=u"The second one is even more interesting!")
writer.commit()
from whoosh.qparser import QueryParser

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    results[0]
    print(results[0])

# {"title": u"First document", "path": u"/a"}
