from pymongo import MongoClient

class LibMongo:
    
    def __init__(self, host: str, username: str, password:str, auth_source: str):
        client = MongoClient(
            host,
            username= username,
            password=password,
            authSource=auth_source
        )
        self.db = client.jose 
        self.users = self.db.users
    