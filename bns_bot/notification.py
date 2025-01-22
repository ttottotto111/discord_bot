import requests
import json

import os.path

class NewsJson():
    def __init__(self):
        if not os.path.isfile("news.json"):
            print("Json file not found, create file...")
            with open("sample.json", "r") as samplefile:
                sample = json.load(samplefile)
            with open("news.json", "w") as createfile:
                json.dump(sample, createfile)
            print("Create \"news.json\" done")
        
        with open("news.json", "r", encoding="UTF-8") as f:
            self.newsjson = json.load(f)
            
    def get(self):
        print("get news.json")
        return self.newsjson
    
    def write(self, data):
        print("write news.json")
        
        with open("news.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False)
            
        print("write done")
        return True

