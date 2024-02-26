import requests

TOKEN = "YOUR TOKEN HERE"
ENDPOINT = "YOUR ENDPOINT HERE"


class DataManager:
    def __init__(self,token=TOKEN,endpoint=ENDPOINT):
       self.token = token
       self.endpoint = endpoint
       self.header = {
           "Authorization": f"Bearer {self.token}"
       }

    def post(self):
        pass
    def put(self,id,parameters):
        requests.put(f"{self.endpoint}/{id}",json=parameters ,headers=self.header)

    def delete(self):
        pass
    def get(self):
        return requests.get(self.endpoint, headers=self.header)




# lastword = ENDPOINT.split("/")[-1][:-1] // get the word in singular form from the endpoint which is how Sheet api works
# print(lastword)



