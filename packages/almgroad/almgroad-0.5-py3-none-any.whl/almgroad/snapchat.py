import requests
def SnapChat_Download(url):
	cookies = {
	    '_lscache_vary': 'cd11052a02ea53c97b30994ffef5a4b1',
	    'pll_language': 'ar',
	    'cf_clearance': '_M2BCDtywlrZJgLBicXKGKyi1ZZOMfX10EtcD2jKPQU-1718796655-1.0.1.1-v_1o9JlkslJVNIOkIQl7VFhvqkPkMxFFwGXbYsA6NxkHS.E.7jxs6E07v.KWiAQ3acbfaje8Iu.LqLfiwwWbSQ',
	    'PHPSESSID': 'qenp9chlmpcn3i8pc0lb2dob3v',
	}
	
	headers = {
	    'authority': 'everyweb.net',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://everyweb.net',
	    'referer': 'https://everyweb.net/snapchat/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'url': url,
	    'token': '6235622d92256ff6593e5b095b331031af9e4fefced747eb9e8a7f5e65a6be5f',
	    'hash': 'aHR0cHM6Ly9zbmFwY2hhdC5jb20vdC9Ndk9JMzJ4bw==1031YWlvLWRs',
	}
	try:
		response = requests.post('https://everyweb.net/wp-json/aio-dl/video-data/', cookies=cookies, headers=headers, data=data).json()
		return {
		"response":response["medias"][0]["url"]
		}
	except Exception as e:
		return e
