import requests
import string
import re
import json
import simplejson
import time
import socket
from time import sleep
last_update = 0

### 
# token = ''
# url = 'https://api.telegram.org/bot%s/' % token



while True:
	r = requests.get("https://api.telegram.org/bot<TOKEN>/getUpdates")
	a =  r.text
	resp_dict =simplejson.loads(a)
	for update in resp_dict["result"]:
	 	if last_update<resp_dict["result"][-1]["update_id"]:
	 	 	if last_update < resp_dict["result"][-1]["update_id"]:
	 	 		last_update = resp_dict["result"][-1]["update_id"]
	 	 		if 'message' in update:
	 	 			id = resp_dict["result"][-1]["message"]["chat"]["id"]
	 	 			text=resp_dict["result"][-1]["message"]["text"]
	 	 			requests.post("https://api.telegram.org/bot<TOKEN>/sendMessage?text=%s&chat_id=%s"%(text,id))

	##optional
	# sleep(3)
