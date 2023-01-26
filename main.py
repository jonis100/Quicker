import requests
import names
import string
import random
import threading
THRADS_NUM = 50

url = "URL_WHICH_DATA_SEND_TO_BY_YOUR_SUBMIT_CLICK"


def generate_nums(n):
    chars = string.digits
    return ''.join(random.choice(chars) for i in range(n))


def do_request():
    while True:
        data = {
            '1': random.choice(names.names_list),
            '2': generate_nums(16),
            '3': '20' + str(random.randint(22, 30)) + '/' + '{:02d}'.format(random.randint(0, 9)),
            '4': generate_nums(3)
        }
        response = requests.post(url, data=data).text
        print (data)
        print(response[0: 20])


threads = []

for i in range(THRADS_NUM):
    t = threading.Thread(target=do_request())
    t.daemon=True
    threads.append(t)

for i in range(THRADS_NUM):
    threads[i].start()

for i in range(THRADS_NUM):
    threads[i].join()
