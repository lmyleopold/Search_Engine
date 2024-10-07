import os, shutil, json
import lucene
#lucene.initVM() //not initVM here because other file while imports this file will initVM again and error
from java.io import File, StringReader # type: ignore
from java.nio.file import Path, Paths # type: ignore
from org.apache.lucene.store import ByteBuffersDirectory, MMapDirectory, NIOFSDirectory, FSDirectory # type: ignore
from org.apache.lucene.analysis.core import SimpleAnalyzer, WhitespaceAnalyzer, StopAnalyzer # type: ignore
from org.apache.lucene.analysis.en import EnglishAnalyzer # type: ignore
from org.apache.lucene.analysis.tokenattributes import PayloadAttribute # type: ignore
from org.apache.lucene.analysis.standard import StandardAnalyzer # type: ignore
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer, LimitTokenCountAnalyzer # type: ignore
from org.apache.lucene.util import Version, BytesRef, BytesRefIterator # type: ignore
from org.apache.lucene.document import Document, Field, StoredField, LongPoint, DoublePoint, StringField, TextField # type: ignore
from org.apache.lucene.index import IndexOptions, IndexWriter, IndexWriterConfig, DirectoryReader, FieldInfos, MultiFields, MultiTerms, Term # type: ignore
from org.apache.lucene.queryparser.classic import MultiFieldQueryParser, QueryParser # type: ignore
from org.apache.lucene.search import BooleanClause,  BooleanQuery, IndexSearcher, TermQuery # type: ignore

# create inverted index
def create_index(index_path, casefold = True, stemming = True, stopword = True):
    #lucene.initVM()

    print('---------- begin creating index ----------')
    # set index fold
    if os.path.exists(index_path):
        shutil.rmtree(index_path)
    os.makedirs(index_path)
    if not os.path.exists(index_path):
        print('ERROR, there is no index_path:', index_path)
        return

    #select analyser, default casefold, stem and stopward, all are true
    analyzer = StandardAnalyzer()
    if casefold == False:
        analyzer = WhitespaceAnalyzer()
    else:
        if stopword == False:
            analyzer = SimpleAnalyzer()
        else:
            if stemming == False:
                analyzer = StopAnalyzer()
    #setup the config of indexwriter
    config = IndexWriterConfig(analyzer)
    config.setOpenMode(IndexWriterConfig.OpenMode.CREATE_OR_APPEND) # the index can be appended
    config.setRAMBufferSizeMB(256.0)
    config.setCommitOnClose(True)

    index_writer = IndexWriter(FSDirectory.open(Paths.get(index_path)), config)

    data_path = ['business', 'review']
    for data in data_path:
        with open(f'./data/LA_{data}.jsonl', 'r') as f:
            for line in f:
                doc = Document()
                doc.add(TextField("json_type", data, Field.Store.YES))
                content = json.loads(line)
                for key, value in content.items():
                    if isinstance(value, int):     #store integer
                        doc.add(LongPoint(key, value))
                        doc.add(StoredField(key + "_display", value))
                    elif isinstance(value, float): #store float
                        doc.add(DoublePoint(key, value))
                        doc.add(StoredField(key + "_display", value))
                    else:                          
                        #store string, object or array, all change into str and token
                        doc.add(TextField(key, str(value), Field.Store.YES))
                        #not token, install the whole phrase for search? 
                        #doc.add(StringField(key, str(value), Field.Store.YES))
                index_writer.addDocument(doc)

    index_writer.close()
    print('--------- finish creating index ---------')

#insight the content of index
def insight_index(index_path):
    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    print("---------the function of index_directory-----------")
    print(dir(index_directory), '\n')
    print("---------the function of index_reader-----------")
    print(dir(index_reader), '\n')
    print("---------the number of document -----------")
    print(index_reader.maxDoc(), '\n')

    print("------the forward 10 businesses' name:------")
    for i in range(10):
        doc = index_reader.document(i)
        name = doc.get("name")
        print(f"document ID: {i}, business name: {name}")

if __name__ == "__main__":
    lucene.initVM()

    index_path = "./data/index"
    #if create new index, True create new
    if_create_index = False
    if not os.path.exists(index_path) or if_create_index:
        create_index(index_path, casefold = True, stemming = True, stopword = True)

    insight_index(index_path)