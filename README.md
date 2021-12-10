# network-trigger
Raspberry pi relay with Socat listening.

This is a project to allow remote trigger from Zabbix monitoring server to send messages to remote PI2 driving Red/Yellow/Green tower light via Relay Hat V1.0 
Programming based on Python 3 and newer at this time. Added some fun console verbage that is basically un needed.  
Enjoy

---------------------------------------------------------------------------
---------------------------------------------------------------------------
Installing the scrtipt and running on Raspberry pi with Headless Mode setup.

Install Raspberry pi OS
Create blank file with no Extention called ssh 
create file called wpa_supplicant.conf

country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
scan_ssid=1
ssid="your_wifi_ssid"
psk="your_wifi_password"
} 

then boot unit. Allow boot and install to complete then log in via SSH using default pi Login  (pi / raspberry )
After logging in it is always strongly suggested to change the default password before moving on as it does pose a security issue with connecing to your wifi network. 
At the time of this scripting (12/21) Raspbian comes with Python 3.9.2
Not to update and start installing things
sudo apt-get update
sudo apt-get install -y git python3-pip python3-tk
git clone https://github.com/AKGhost/network-trigger.git

Now you should be ready to run the program
cd network-trigger
python StationAlert.py
(Now i suggest installing screen so you can close your ssh window and be able to leave the programming running in the background)
you should be greated with:

|=====================================================|
|                 Internet tower light                |
|-----------------------------------------------------|
|                                                     |
|                  Internet monitoring                |
|                  Remote Light station               |
|                                                     |
|                      Raspberry pi                   |
|                      relay hat                      |
|                                          Alaskaradar|
|_____________________________________________________|
|             System online and Standing by           |
|_____________________________________________________|


Once this is complete and running
Now your pi is listening to all traffic found on port 50000 for the keywords set on lines 57 / 64 / 71 / 79  of the script. Change these how you want. 

That is the end of this part. I will eventually update to show intergration in Zabbix
