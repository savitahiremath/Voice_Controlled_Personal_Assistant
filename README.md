# PROJECT NAME
Voice Contolled Personal Assistant Using Raspberry Pi

## OVERVIEW
It is a Voice Controlled System, Where User gives input as Voice and receives desired output also as Voice. The main moto of this project is to help Visually impaired person to get Connected to the outer world, by giving them access Wikipedia, calculator, email and music all through their voice. In total acting as a Personal Assistant.


## PROBLEM STATEMENT
Visually impaired person can't give text input to get any source of information which they are in need of, Therefore have to be dependent on others.



## INTERFACING HARDWARE DEVICES WITH RASPBERRY PI

![image](https://user-images.githubusercontent.com/42416500/98030584-4388b780-1e37-11eb-9c35-d51e75f07802.png)



### INTERFACING OF RASPBERRY PI WITH SPEAKER

![image](https://user-images.githubusercontent.com/42416500/98030983-d6c1ed00-1e37-11eb-83fe-e6ae00e5bc55.png)


Make sure your Raspberry Pi is powered up and connected to your network.
Connect the speaker to the audio jack as shown in the image. 




## AUDIO CONFIGURATION


Step1:  Open up raspi-config by entering the following into the command line:

Sudo raspi-config

This will open the configuaration screen :         

![image](https://user-images.githubusercontent.com/42416500/98031435-7e3f1f80-1e38-11eb-8fdf-61a57e77c98e.png)



Step2: Select option 8: advanced options and press Enter, then select options A6: Audio and press Enter:    



![image](https://user-images.githubusercontent.com/42416500/98032887-acbdfa00-1e3a-11eb-8706-e884afca9b9c.png)

                                        
Now you are presented with the two modes explained above as an alternative to the default Auto option. 
Select a mode, Press Enter and press the right arrow key to exit the options list, 
then select finish to exit the configuration tool.



## MICROPHONE CONFIGUARATION

Step 1. Check If the Device is Detected by Raspberry Pi:

Before you start, you need to check if your USB device is detected by the Raspberry Pi. To do this, you can use the “lsusb” command. Locate the device manufacturer name in the command output as shown in the following output (If you don’t see your device in the command output, either your device is faulty or the device driver is not available for it.) 

![image](https://user-images.githubusercontent.com/42416500/98409447-e2f8b500-2098-11eb-8c93-12ea132dd069.png)


                            
Step2: List Available Recording Devices (Microphone) and Locate Card Number and Device Number:


The next step is to locate the correct Recording Device (Microphone) Card and the Device Number. You can use the “arecord -l” command to list all the playback devices available on your Raspberry Pi. Locate the device with the same Manufacturer name as you found in the “lsusb” command output, and note down the card number and device number for it.

![image](https://user-images.githubusercontent.com/42416500/98410488-c78ea980-209a-11eb-9639-3134a38135a1.png)


Step 3. Set your Recording and Playback Device as the Default PCM Devices:


At this stage, you should have the Card Number and the Device Number for you Recording and Playback devices. You can now use the following configuration template and replace “card number” and “device number” for the Mic and Speaker sections.

After making the changes you can paste this configuration in “.asoundrc” file under your Raspberry Pi home directory (/home/pi). For global configuration, you may add this config to “/etc/asound.conf” directory. Your configuration should similar to the config shown in the following screenshot with your respective “card number” and “device number” values 




![image](https://user-images.githubusercontent.com/42416500/98411289-cad66500-209b-11eb-99a1-3c9dfc8d3726.png)




## EXPECTED RESULTS
It must convert the voice user input to text, process it and give desired output in the form of voice.


## FLOW CHART

![image](https://user-images.githubusercontent.com/42416500/98411813-bf376e00-209c-11eb-9868-7ae2a53403b5.png)



## RESULTS
It took input as a voice from users and given them desired output in the form of voice.



## References
Dahl, George E., et al. "Context-dependent pre-trained deep neural networks for large-vocabulary speech recognition." Audio, Speech, and Language Processing, IEEE Transactions on 20.1 (2012): 30-42. 



