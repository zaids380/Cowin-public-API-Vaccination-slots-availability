import requests
import datetime
import json
import ast

with open('district_dict.txt') as f:
	data = f.read()
	districts = ast.literal_eval(data)
f.close()

district_name=input('Enter District Name: ')

d_code= districts[district_name.lower()]
browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

#showing slots for next 10 days
for i in range(0,10):
	date=datetime.datetime.today() + datetime.timedelta(days=i)
	date=date.strftime("%d-%m-%Y")
	response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={0}&date={1}'.format(d_code,date),headers=browser_header)
	# print(response.status_code)
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
			print('......................................................')



