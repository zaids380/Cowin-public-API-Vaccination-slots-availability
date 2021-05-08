import requests
import json

url='https://cdn-api.co-vin.in/api/v2/admin/location/states'
browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
state_resp=requests.get(url, headers=browser_header)
# print(state_resp.status_code)
state_json=json.loads(state_resp.text)
# print(json_resp)

state_codes={}
state_codes1={}

for data in state_json["states"]:
	print(data['state_id'],"\t",data['state_name'],"\n")
	state_codes[data['state_id']] = data['state_name']
	state_codes1[data['state_name'].lower()] = data['state_id']

# print(state_codes1)
# print(state_codes)


# fetching all states
ds={}

for state_code in range(1,36):
	if state_code == 38:
		continue
	print('--------------------------------------------------------------------------------')
	print('District Codes'+'\t'+'District Names'+'\t\t'+ 'State: '+ str(state_codes[state_code]))
	print('--------------------------------------------------------------------------------')

	district_resp=requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(state_code), headers=browser_header)
	district_json=json.loads(district_resp.text)

	for districts in district_json["districts"]:
		print(districts['district_id'],"\t\t", districts['district_name'],'\n' )
		ds[districts['district_name'].lower()] = districts['district_id'] 
# print(ds)