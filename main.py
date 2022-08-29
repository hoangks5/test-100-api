import requests
import threading

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
    data = {'input_source_hash': 'QmahGzqFngQnQ81gpWf5o6UkPWEH9BYWUigoeCTxSqAFsV'}
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


run('cv001')