# Cowin-public-API-Vaccination-slots-availability

As the cowin app doesn't notifies for new available slots, this python script can be used to get notification for new posted vaccination slots through mail/sms/whatsapp/telegram, notification part is not done, a simple python code can be used to include notification 



the program uses the cowin's public api to fetch data using python requests



A simple python script to check available vaccination slots for a pincode/district




Requirements:

                requests
                datetime

#files

1. cowin_states_and_districts.py

        this files prints all the states and districts along with their id's
 
2. cowin_slots_by_pincode.py

        this file prints all the available vaccination slots in next 10 days for the provided pincode:
    
        input: pincode
    
        example: 282001 
 
3. cowin_slots_by_district.py

        this file prints all the available vacccination slots in next 10 days for the provided district:
    
        input: district name
    
        example: mumbai
 
4. district_codes.txt

        this file contains a dictionary of all the districts along with their id's
