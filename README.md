# dynv6AutoUpdate
Auto updates your current IPv6 to dynv6 DynDns service. Handy if you got an ISP like me who only serves IPv6 public IPs.

## Requirements
- python3
- requests library

``
sudo apt-get -y install python3 python3-pip
sudo pip3 install requests
``

## Installation
You can use the install.sh script.


## Add a scheduled task manually
Open cron configuration file using:
`crontab -e`

I add the following to run the script every day at 4:30 AM.
Replace the path with your script path.
30 4 * * * /usr/bin/python3 /path/to/your/python/script.py

**Note:**
\* \* \* \* \* command_to_execute
First * | Second * | Third * | Fourth * | Fifth *
--- | --- | --- | --- |--- 
|-Minute-|-Hour-|-Day-|- Month -|- Day of week |

