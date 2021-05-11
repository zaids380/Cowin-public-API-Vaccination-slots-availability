import requests
import datetime
import json

browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
pin=input('Enter Pincode')
response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={0}&date={1}'.format(pin,'09-05-2021'),headers=browser_header)

json_data=json.loads(response.text)

if len(json_data['centers'])==0:
	print("No slots available")
for slots in json_data['centers']:
	print('-----------------------------------------------------------------------------')
	print("\nCenter ID: "+str(slots['center_id']) +'\n' 
			+ "Name: "+str(slots['name']) +'\n' 
			+ "Address: "+str(slots['address']) +'\n' 
			+ "State Name: "+str(slots['state_name']) +'\n' 
			+ "District Name: "+str(slots['district_name']) +'\n' 
			+ "Pincode: "+str(slots['pincode']) +'\n' 
			+ "Opening time: "+str(slots['from']) +'\n' 
			+ "Closing Time: "+str(slots['to']) +'\n' 
			+ "fee type: "+str(slots['fee_type']))
	print('-----------------------------------------------------------------------------')


	for info in slots['sessions']:
		print("session_id: "+str(info['session_id'])+'\n' 
			+ "date: "+str(info['date'])+'\n' 
			+ "available capacity: "+str(info['available_capacity'])+'\n' 
			+ "min age limit: "+str(info['min_age_limit'])+'\n' 
			+ "vaccine: "+str(info['vaccine'])+'\n')
		print('Timings')
		for time in info['slots']:
			print(time)
		print('\n')

