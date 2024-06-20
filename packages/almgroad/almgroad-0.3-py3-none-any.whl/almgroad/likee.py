import requests
def Likee_Download(url):
	cookies = {
	    'pll_language': 'ar',
	    'PHPSESSID': 'g0p72g1h0bg6l5h29vbtasamd4',
	    '__gads': 'ID=57f190b29f32eec4:T=1718799372:RT=1718799372:S=ALNI_MZ8whUXTuB9ODcKl9DGYJoIWcB7IQ',
	    '__gpi': 'UID=00000e5e88984f42:T=1718799372:RT=1718799372:S=ALNI_Mb297zOt6o1Xg9g8M0wMvMYolMn8w',
	    '__eoi': 'ID=bfef46a406cf6b89:T=1718799372:RT=1718799372:S=AA-AfjYp6nEVU9F1SsptE8_uTE8a',
	    'FCNEC': '%5B%5B%22AKsRol_0ePwaDlzS7PgG0IstEq0OjyamLPeDuj6XV455faYU8gDuM7K8qIjptzX7RY0szR1C6ktHEssj7Tuai8x75KiohHZLAwQdDdPg-LHMc8hO2tGwyn_-jL622ZxMDhXnN_og9P3K1N6CB93OHvyYDY1oZFIj6A%3D%3D%22%5D%5D',
	}
	
	headers = {
	    'authority': 'savevideofrom.me',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://savevideofrom.me',
	    'referer': 'https://savevideofrom.me/likee-%D8%AA%D8%AD%D9%85%D9%8A%D9%84-%D9%88%D8%AD%D9%81%D8%B8-%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%85%D9%86-%D9%84%D8%A7%D9%8A%D9%83%D9%8A',
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
	    'token': '20574223f4195024150363c17b6525c1f7f199234042df8ab157921585381484',
	}
	try:
		response = requests.post('https://savevideofrom.me/wp-json/aio-dl/video-data/', cookies=cookies, headers=headers, data=data).json()
		return {
		"response":response["medias"][0]["url"]
		}
	except Exception as e:
		return e
