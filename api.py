import os
from pymongo import MongoClient
import SocketServer
from bson.json_util import dumps

mongo_uri = "mongodb://{}:{}".format(
    os.environ["MONGO_PORT_27017_TCP_ADDR"],
    os.environ["MONGO_PORT_27017_TCP_PORT"]
    )
client = MongoClient(mongo_uri)
db = client[os.environ.get("target_database", "test_db")]
collection = db[os.environ.get("target_collection", "test_collection")]

class ScoresAPI(SocketServer.BaseRequestHandler):
    def handle(self):
        """ Returns all documents in the collection """
        # log the request
        print "recieved request: {}".format(self.request.recv(1024))
        documents = collection.find()
        self.request.sendall(dumps(documents))


if __name__ == "__main__":
    app = SocketServer.TCPServer(("0.0.0.0", 8000), ScoresAPI)
    app.serve_forever()
