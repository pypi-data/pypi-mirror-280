import requests
def Kwai_Download(url):
	cookies = {
	    '_lscache_vary': 'cd11052a02ea53c97b30994ffef5a4b1',
	    'pll_language': 'ar',
	    'cf_clearance': '_M2BCDtywlrZJgLBicXKGKyi1ZZOMfX10EtcD2jKPQU-1718796655-1.0.1.1-v_1o9JlkslJVNIOkIQl7VFhvqkPkMxFFwGXbYsA6NxkHS.E.7jxs6E07v.KWiAQ3acbfaje8Iu.LqLfiwwWbSQ',
	}
	
	headers = {
	    'authority': 'everyweb.net',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': '_lscache_vary=cd11052a02ea53c97b30994ffef5a4b1; pll_language=ar; cf_clearance=_M2BCDtywlrZJgLBicXKGKyi1ZZOMfX10EtcD2jKPQU-1718796655-1.0.1.1-v_1o9JlkslJVNIOkIQl7VFhvqkPkMxFFwGXbYsA6NxkHS.E.7jxs6E07v.KWiAQ3acbfaje8Iu.LqLfiwwWbSQ',
	    'origin': 'https://everyweb.net',
	    'referer': 'https://everyweb.net/kwai/',
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
	    'token': '06b5b1f03963bb161830e2f3eb5cef9bbe0d05a6f7d3a6c137bb65aa2ba7f28d',
	    'hash': 'aHR0cHM6Ly9tLmt3YWlhcHBzLmNvbS9waG90by8xNTAwMDE1OTU4NTE4MzMvNTIzMDIzNjY0OTMzOTU3MzAxOT91c2VySWQ9MTUwMDAxNTk1ODUxODMzJnBob3RvSWQ9NTIzMDIzNjY0OTMzOTU3MzAxOSZjYz1DT1BZX0xJTksmdGltZXN0YW1wPTE3MTg3OTY2MDM4NjImbGFuZ3VhZ2U9YXItaXEmc2hhcmVfZGV2aWNlX2lkPUFORFJPSURfYjJmMGE4ZDU2MThjMDk0MCZzaGFyZV91aWQ9MCZzaGFyZV9pZD1BTkRST0lEX2IyZjBhOGQ1NjE4YzA5NDBfMTcxODc5NjU5NDc0OCZzaGFyZVBhZ2U9cGhvdG8mc2hhcmVfaXRlbV90eXBlPXBob3RvJnNoYXJlX2l0ZW1faW5mbz01MjMwMjM2NjQ5MzM5NTczMDE5JmZpZD0wJmV0PTFfYSUyRjQ4MDg4MjM3NDM5MjczMjkyNTNfc3Aw1381YWlvLWRs',
	}
	try:
		response = requests.post('https://everyweb.net/wp-json/aio-dl/video-data/', cookies=cookies, headers=headers, data=data).json()
		return {
		"url":response["medias"][0]["url"]
		}
	except Exception as e:
		return e
