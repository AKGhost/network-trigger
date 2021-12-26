# network-trigger
Raspberry pi relay with Socat listening.

This is a project to allow remote trigger from Zabbix monitoring server to send messages to remote PI2 driving Red/Yellow/Green tower light via Relay Hat V1.0  </p>
Programming based on Python 3 and newer at this time. Added some fun console verbage that is basically un needed.   </p>
Enjoy </p>

--------------------------------------------------------------------------- </p>
--------------------------------------------------------------------------- </p>
Installing the scrtipt and running on Raspberry pi with Headless Mode setup.</p>
</p>
Install Raspberry pi OS</p>
Create blank file with no Extention called ssh </p> 
create file called wpa_supplicant.conf </p>

country=US</p>
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev</p>
update_config=1</p>

network={</p>
scan_ssid=1</p>
ssid="your_wifi_ssid"</p>
psk="your_wifi_password"</p>
} 

then boot unit. Allow boot and install to complete then log in via SSH using default pi Login  (pi / raspberry )</p>
After logging in it is always strongly suggested to change the default password before moving on as it does pose a security issue with connecing to your wifi network. </p>
At the time of this scripting (12/21) Raspbian comes with Python 3.9.2</p>
Not to update and start installing things</p>
sudo apt-get update</p>
sudo apt-get install -y git python3-pip python3-tk</p>
git clone https://github.com/AKGhost/network-trigger.git</p>
</p>
Now you should be ready to run the program</p>
cd network-trigger</p>
python StationAlert.py</p>
(Now i suggest installing screen so you can close your ssh window and be able to leave the programming running in the background)</p>
you should be greated with:</p>

|=====================================================|</p>
|                 Internet tower light                |</p>
|-----------------------------------------------------|</p>
|                                                     |</p>
|                  Internet monitoring                |</p>
|                  Remote Light station               |</p>
|                                                     |</p>
|                      Raspberry pi                   |</p>
|                      relay hat                      |</p>
|                                          Alaskaradar|</p>
|_____________________________________________________|</p>
|             System online and Standing by           |</p>
|_____________________________________________________|</p>


Once this is complete and running </p>
Now your pi is listening to all traffic found on port 50000 for the keywords set on lines 57 / 64 / 71 / 79  of the script. Change these how you want. </p>

That is the end of this part. I will eventually update to show intergration in Zabbix</p>
