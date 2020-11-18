path = r"/etc/network/interfaces"
edit = open(path,"r")
data = edit.read()
edit.close()
name = "NicksDrone"
new =''
#Checks if in regular mode then toggles to adhoc
if "#allow-hotplug wlan0" not in data:
    print("You are in Regular mode. Switching to Ad-Hoc")
    insert = "auto wlan0\niface wlan0 inet static\n  address 10.49.5.128\n  netmask 255.255.255.0\n  wireless-channel 1\n  wireless-essid "+name+"\n  wireless-mode ad-hoc"
    comment = "\n#allow-hotplug wlan0\n#iface wlan0 inet manual\n#        wpa-conf/etc/wpa_supplicant.conf"
    place = data.find("#auto wlan0")
    new = data[:place]+insert+"\n"+comment
else:
    print("You are in Ad-Hoc mode. Switching to Regular")
    insert = "\nallow-hotplug wlan0\niface wlan0 inet manual\n        wpa-conf/etc/wpa_supplicant.conf"
    comment = "#auto wlan0\n#iface wlan0 inet static\n#  adress 10.49.5.128\n#  netmask 255.255.255.0\n#  wireless-channel 1\n#  wireless-essid "+name+"\n#  wireless-mode ad-hoc"
    place = data.find("auto wlan0")
    new = data[:place]+comment+"\n"+insert

edit = open(path,"w")
edit.write(new)
edit.close()

