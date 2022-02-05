# checkmk_pfsense_multiwan_ping

To get a ping result over a specific interface and get the result into CheckMK

## Requirements

 - Installed CheckMK Agent into pfsense. Tested on pfsense 2.5.2

## Installation

 - Move python script into the local scripts folder of the Agent.
   Default is `/usr/local/lib/check_mk_agent/local`
 - Edit Variables in line 3 and match it with the interfaces you want to test
 - Make the script exexuteable with `chmod +x`
