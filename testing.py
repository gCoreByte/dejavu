from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
import warnings
import json
import os
#warnings.filterwarnings("ignore")

if __name__ == "__main__":
    config = {
        "database": {
            "host": "127.0.0.1",
            "user": "root",
            "passwd": "bba23",
            "db": "dejavu_db"
        },
    }

    djv = Dejavu(config)


    djv.fingerprint_directory("mp3", [".mp3"], 2)
    print(djv.db.get_num_fingerprints())

    #print(djv.recognize(FileRecognizer, "test/test.mp3"))

    #files = []

    list = os.listdir("mp3")
    for f in list:
        print(f)
        print(djv.recognize(FileRecognizer, "mp3/" + f))