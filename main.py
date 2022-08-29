import requests
import threading


def test_cv006(endpoint):
    url = 'https://100api.orai.dev/'+endpoint
    files = {'input_source': open('./text.png','rb'),
            'lang':'eng'}
    headers = {
            'Authorization': 'ai_market'
        }
    response = requests.post(url, files=files, headers=headers)
    print(response.json())
#test_cv006('cv006')



def run_test(endpoint):
    url = 'https://100api.orai.dev/'+endpoint
    files = {'input_source': open('./images.jpeg','rb')}
    headers = {
            'Authorization': 'ai_market'
        }
    response = requests.post(url, files=files, headers=headers)
    with open('image.png', 'wb') as f:
            for chunk in response:
                f.write(chunk)

def run_test1(endpoint):
    url = 'https://100api.orai.dev/'+endpoint
    data = {'input_source_hash': 'QmVMFbKgoG2r1BZQW5hpiYUAt2ZTJFFBs6tW6UCRqeKRrM'}
    headers = {
            'Authorization': 'ai_market'
        }
    response = requests.post(url, data=data, headers=headers)
    print(response.json())
def run(endpoint):
    x = []
    x.append(threading.Thread(target=run_test,args={endpoint,}))
    x.append(threading.Thread(target=run_test1,args={endpoint,}))
    for x1 in x:
        x1.start()