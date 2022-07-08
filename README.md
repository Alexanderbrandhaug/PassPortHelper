# PassPortHelper
PassPortHelper: Uses two rest-api endpoints from the police authorities in Norway to retrieve information about available pass-port appointments. 
Endpoints was found on their website when trying to order passport-appointment by inspecting said website. 

The script only console-write when/if a given appointment is found on a given day. Made this code in a rush when I was in need for a passport-appointment and didnt have time to check for appointments every 5th minute myself. 

The idea is that you will have to order the appointment as soon as you find an available appointment. You will have to specify a range og dates you want to search within, and specify which police-station you want to search available appointments for. 

Tip: Use the 1st endpoint in postman/insomnia/browser and look for the exact name of the police-station you're trying to book appointments for, then pass it as a argument in the function-call. 
