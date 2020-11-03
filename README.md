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




## EXPECTED RESULTS
It must convert the voice user input to text, process it and give desired output in the form of voice.


## FLOW CHART
![image_1](https://user-images.githubusercontent.com/42416500/97989555-b6c50600-1e04-11eb-8bf9-1dcb897094b9.PNG)



## RESULTS
It took input as a voice from users and given them desired output in the form of voice.



## References
Dahl, George E., et al. "Context-dependent pre-trained deep neural networks for large-vocabulary speech recognition." Audio, Speech, and Language Processing, IEEE Transactions on 20.1 (2012): 30-42. 



