# vkCatSender
A simple python script for sending a random cat in a personal messages with vkontakte api

#### Tech
* [python3](https://www.python.org/download/releases/3.0/)
* [pip vk](https://pypi.python.org/pypi/vk/1.5)
* [pip Image](https://pillow.readthedocs.org/en/3.2.x/index.html)

#### Setup:
**0.1** [create](https://vk.com/dev/standalone) standalone vk application  
**0.2** replace '<application ID>' string in token.html with your application id  
**0.3** open token.html and 'Push the button'  
**0.4** copy access_token value from address line to 'TOKEN' field in sender.properties  

**1** set target user id in 'TARGET' field  
**2** (usually not required) set python3 execute path in 'EXEC' field  
**3** (optional) you can change save directory with 'SAVE_PATH' value  
  
```
TOKEN=<access_token from step 0>
TARGET=<user_id form step 1>
EXEC=python
SAVE_PATH=./images/
```
#### Usage:
windows: sender.cmd  
bash: sender.sh
