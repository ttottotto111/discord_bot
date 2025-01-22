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

class Notification:
    # 5분간격 데이터 확인 진행 (시간 변동가능)
    # json파일 비교 후 변동이 있을 경우 json 업데이트 후 bot에 업데이트 메시지 출력
    # -> 5분간격 실행 코드 추가 예정
    def __init__(self):
        self.json = NewsJson()
        self.file = self.json.get()
    
    def update_news(self):
        '''
        네오 뉴스(업데이트 뉴스)
        '''
        response_size = 1   # 불러올 글의 개수
        response = requests.get(f"https://api-community.plaync.com/bns/board/neonews/article/search/moreArticle?isVote=true&moreSize={response_size}&moreDirection=BEFORE&previousArticleId=0")
        
        if response.status_code == 200:
            try:
                news = response.json()["contentList"][0]
                
                id = news["id"]
                title = news["title"]
                updatetime = news["timestamps"]["updateDateTime"]
                url = "https://bns.plaync.com/board/neonews/view?articleId="+id
                
                if self.file["neonews"]["id"] != id or self.file["neonews"]["title"] != title:
                    print("네오 뉴스 업데이트")
                    
                    self.file["neonews"]["id"] = id
                    self.file["neonews"]["title"] = title
                    self.file["neonews"]["updatetime"] = updatetime
                    self.file["neonews"]["url"] = url
                    self.json.write(self.file)
                    
                    # bot 연결코드 추가 예정
                    # > True 일경우 봇 메시지 출력 (봇에서 코드 작성검토 (5분간격 확인코드 포함))
                    
                    return True
                
                return 0
            except Exception as e:
                print("update news response error")
                print(e)
                return False
        else:
            print("Request Error")
            print("status code :", response.status_code)
            return False



#테스트 코드 (삭제 예정)
def test():
    note = Notification()
    j = NewsJson()
    note.update_news()

test()