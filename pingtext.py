#!/usr/local/bin/python3.8
import os
INTERFACES = ['pppoe0', 'igb0']

networks = {}
for interface in INTERFACES:
    address = os.popen("ifconfig {} inet | grep inet".format(interface)).read()
    address = address.split(" ")
    networks[interface] = {
        'address' : address[1]
        }
    test = os.popen("ping -S {} -c 5 google.de".format(networks[interface]["address"])).read()
    test = test.split("\n")
    packetloss = test[8].split(", ")
    networks[interface]["packetloss"] = packetloss[2].replace("% packet loss", "")
    pings = test[9].replace("round-trip min/avg/max/stddev = ", "")
    pings = pings.replace(" ms", "")
    pings = pings.split("/")
    networks[interface]["min"] = pings[0]
    networks[interface]["avg"] = pings[1]
    networks[interface]["max"] = pings[2]
    networks[interface]["mdev"] = pings[3]
    print('P "Ping_{}" packetloss={};25;50;0;100|min={};100;200|avg={};100;200|max={};100;200|mdev={};50;75 Pingcheck für Interface {}'.format(interface, networks[interface]["packetloss"], networks[interface]["min"], networks[interface]["avg"], networks[interface]["max"], networks[interface]["mdev"], interface))
