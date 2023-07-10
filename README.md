# Capture! 
Alright, so were given a huge ass list of usernames and passwords and its our job to brute force the usernames and then brute force the passwords. Alright, sounds simple enough. Only annoying thing is having to bypass the constant captcha that makes us solve a math equation. Not to mention the username list is 800+. We must solve the captcha to verify the username. <br>

This comes in two steps. First find the username, the only way you know if the username is valid is if the error message states the *usernames* password is incorrect. Otherwise the username is not in the system. lame. Fun part is I finally implemented Regex and have quite a good grasp on how it works now. Second part is now just brute forcing all 1000+ passwords. 

Hardest part for me was trying to find the equation that checks the captcha, but regex helped me sovled that problem instantly. Either way, after spending a couple hours learning regex I got the flag. Pretty fun, just lots of waiting .... 

<img width="556" alt="Screenshot 2023-07-10 at 3 44 08 PM" src="https://github.com/katstews/Capture/assets/112781868/8b2885e6-327f-43e9-bffd-702fb7ba40f0">
