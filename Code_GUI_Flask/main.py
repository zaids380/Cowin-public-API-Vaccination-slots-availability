from flask import Flask, render_template, request, session, redirect
import requests
import datetime
import json
import ast

with open('district_dict.txt') as f:
	data = f.read()
	districts = ast.literal_eval(data)

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/cowin_district_calender',methods = ['POST','GET'])
def cowin_district_calender():
	try:
		if(request.method=='POST'):
			dc_data = {}
			district_name = request.form.get('district')
			d_code= districts[district_name.lower()]
			browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
			for i in range(0,10):
				date=datetime.datetime.today() + datetime.timedelta(days=i)
				date=date.strftime("%d-%m-%Y")
				response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={0}&date={1}'.format(d_code,date),headers=browser_header)
				json_data=json.loads(response.text)
				if len(json_data['centers']) != 0:
					dc_data[date] = json_data['centers']
			return render_template("cowin_district_calender.html",dc_data = dc_data)
		return render_template("cowin_district_calender.html")
	except:
		return render_template("cowin_district_calender.html")

@app.route("/cowin_pincode_calender",methods = ['POST','GET'])
def cowin_pincode_calender():
	try:
		if(request.method=='POST'):
			pc_data = [] 
			browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
			pin = request.form.get('cowin_pincode_calender')
			response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={0}&date={1}'.format(pin,'09-05-2021'),headers=browser_header)
			json_data=json.loads(response.text)
			if len(json_data['centers']) == 0:
				pc_data.append("No slots Available")
		return render_template("cowin_pincode_calender.html",center = json_data['centers'],pc_data = pc_data)
	except:
		return render_template("cowin_pincode_calender.html")

@app.route("/cowin_slots_by_district",methods = ['POST','GET'])
def cowin_slots_by_district():
	try:
		if(request.method=='POST'):
			ds_data = {}
			district_name = request.form.get('cowin_slots_by_district')
			d_code= districts[district_name.lower()]
			browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
			for i in range(0,10):
				date=datetime.datetime.today() + datetime.timedelta(days=i)
				date=date.strftime("%d-%m-%Y")
				response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={0}&date={1}'.format(d_code,date),headers=browser_header)
				json_data=json.loads(response.text)
				if len(json_data['sessions']) != 0:
					ds_data[date] = json_data['sessions']
				else:
					ds_data[date] = "No slots Available"
			return render_template("cowin_slots_by_district.html",ds_data = ds_data)
		return render_template("cowin_slots_by_district.html")
	except:
		return render_template("cowin_slots_by_district.html")
@app.route("/cowin_slots_by_pincode",methods = ['POST','GET'])
def cowin_slots_by_pincode():
	try:
		if(request.method == 'POST'):
			sp_data = {}
			pincode = request.form.get('cowin_slots_by_pincode').lower()
			browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
			for i in range(0,10):
				date=datetime.datetime.today() + datetime.timedelta(days=i)
				date=date.strftime("%d-%m-%Y")
				response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}'.format(pincode,date),headers=browser_header)
				json_data=json.loads(response.text)
				if len(json_data['sessions']) != 0:
					sp_data[date] = json_data['sessions']
				else:
					sp_data[date] = "No slots Available"
			return render_template("cowin_slots_by_pincode.html",sp_data = sp_data)
		return render_template('cowin_slots_by_pincode.html')
	except:
		return render_template('cowin_slots_by_pincode.html')

@app.route("/cowin_states_and_districts")
def cowin_states_and_districts():
	try:
		url='https://cdn-api.co-vin.in/api/v2/admin/location/states'
		browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
		state_resp=requests.get(url, headers=browser_header)
		state_json=json.loads(state_resp.text)
		state_codes={}
		state_codes1={}
		final_districts = {}
		for data in state_json["states"]:
			state_codes[data['state_id']] = data['state_name']
			state_codes1[data['state_name'].lower()] = data['state_id']
		
		for state_code in range(1,36):
			ds={}
			if state_code == 38:
				continue
			state_name = state_codes[state_code]
			district_resp=requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(state_code), headers=browser_header)
			district_json=json.loads(district_resp.text)

			for districts in district_json["districts"]:
				ds[districts['district_name'].lower()] = districts['district_id']
			final_districts[state_name] = ds
		return render_template("cowin_states_and_districts.html",final_districts=final_districts)
	except:
		return render_template("cowin_states_and_districts.html")

if __name__ =='__main__':
    app.run(debug=True)