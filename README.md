# solarClone
To start off you will need to set up a raspberry pi.
Nothing special hear just just the Raspberry Pi imager:
https://www.raspberrypi.org/software/

## Raspberry Pi Set Up
Once you've imaged the SD card plug it in and bot up.
If you don't have a screen set it up headless:
https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

In short you will include a file called ```wpa_supplicant.conf```
inside you will include the wifi details:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country= AU

network={
        scan_ssid=1
        ssid="<Name of your wireless LAN>"
        psk="<Password for your wireless LAN>"
        proto=RSN
        key_mgmt=WPA-PSK
        pairwise=CCMP
        auth_alg=OPEN
}
```

In addition you should add a blank file called ssh to the SD card.
**This file does not require a any extension or data inside**. Easiest method:
Creat a next text file and save as ssh
https://www.raspberrypi.org/documentation/remote-access/ssh/README.md

Once on line open terminal and run:
```sudo apt-get update```
```sudo apt-get upgrade```
not entirely required but cant hurt to reboot
```sudo reboot```
this will ensure your system is upto date and ready to go for the next steps.

Next you will need to enable one-wire/I2c
in terminal:
```sudo raspi-config```
using the arrow keys navigate to:
**3 Interface Options**
NAvigate to the interfaces you wish to enable and press enter to select and enter to confirm.
Once complete select Back > Finish
If not prompted to reboot, reboot now for these chnages to take eefect
```sudo reboot```

## Set up directories/  clone the git
__side note I recommend getting use to terminal as it will help you later on when you need to access via ssh etc__
We want to create a directory/folder
```mkdir solarMonitor```
if you now type the list command ```ls``` into the command line, you will see the folder created
to enter the folder we can type the chand directory command ```cd solarMonitor```
Now we are in the folder we can clone the data from GitHub
```git clone https://github.com/mishave/solarCore.git```

this will automatically clone the repository with the files etc we need.
However for this code to work we will need to install libaries etc.

## Google Set Up
### gspread lib for python
to do this we can run the following commond in terminal:
```sudo pip3 install gspread```







# Addional Info
### Creating a google service account
This will enable you to access the sheet via API
this is done from the Google Developers Console
see instructions below:
https://docs.gspread.org/en/latest/oauth2.html

In brief you are looking to set up a project
* once you have a project you go to API menu > Credientials
* Credientials > Creat Credientials - Services account (editor)
* once this is done click on the service account created
* navigate to keys, click add key and select the JSON option
* this downloads the key which you can store on your PI
* make sure this is kept safe as anyone with it can access your project.

**After setting this up you will need to create a Google sheet**
**once the sheet is created SHARE THE SHEET WITH THE SERVICE BOT EMAIL**
https://docs.google.com/spreadsheets

## Helpful Git Commands
Fistly set up who you are:
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

check if there is changes:
git status

add chnages to be pushed
git add .
comment and commit ready for push
git commit -m "description of what you did"
push chnages
git push

git pull
git pull
