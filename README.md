#Babos Branch of Pikapy - Mass Pokemon Go Account Creator and ToS verifier
==============================================================


Description
-----------
Automatically creates Pokemon Trainer Club accounts, and reads the ToS making them usable after the recent Niantic patch.
Text files will be created in your current directory.
Added functionality:

-Mass create accounts with scheme: UsernameNR

-Auto use Google Mail + Trick Mailaddress+Username@gmail.com

-Auto solve Captchas via 2Captcha API

Installation
------------
**Windows users**

Install all the necessary prerequisites as listed here:

http://pgm.readthedocs.io/en/develop/basic-install/windows.html

You will also need to download the chromedriver.exe:

http://chromedriver.storage.googleapis.com/2.23/chromedriver_win32.zip

Unzip and paste the chromedriver.exe file in "C:\Python27\Scripts" Folder.

Finally, open up your command prompt and paste this command:

    pip install git+https://github.com/babo96/ptc-captcha-solver


**Linux users/OSX**

(OSX prerequisites)Selenium support:

    brew install chromedriver
(Ubuntu and variants prerequisites)

    sudo apt-get install chromium-browser

	sudo apt-get install unzip

	wget -N http://chromedriver.storage.googleapis.com/2.23/chromedriver_linux64.zip -P ~/Downloads

	unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads

	chmod +x ~/Downloads/chromedriver

	sudo mv -f ~/Downloads/chromedriver /usr/local/share/chromedriver

	sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

	sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

	sudo apt-get install xvfb

	(Everyone from this point)
From your terminal run::

    pip install git+https://github.com/babo96/ptc-captcha-solver

If you have both python2 and python3 installed::

    pip2 install git+https://github.com/babo96/ptc-captcha-solver

If given permission errors::

    sudo pip2 install git+https://github.com/babo96/ptc-captcha-solver

Updating to the latest version
------------------------------

    pip install --upgrade git+https://github.com/babo96/ptc-captcha-solver

Uninstalling
------------

    pip uninstall pikapy

Usage
-----
**Command line interface:**

After installing the package run 'pikapy' from the terminal to create a new accounts.
Optional parameters include *--username*, *--password*, *--email*, *--count*
Use *--help* for command line interface help.

usernames.txt file is created in the current working directory.

Example 1 (Create entirely random new account)::

    ~pikapy
    Created new account:
      Username:  dGXJXnAzxqmjbaP
      Password:  yUbiAgcXhBrEwHk
      Email   :  TVKzlu1AcW@6yxi6.com
      
Example 2 (Create 2 accounts with the same password)::

    ~pikapy -p password -c 2
    Created new account:
      Username:  dGXJXnAzxqmjbaP
      Password:  password
      Email   :  TVKzlu1AcW@6yxi6.com
    Created new account:
      Username:  vKEkp19eb0l4mFW
      Password:  password
      Email   :  TVKzlu1AcW@6yxi6.com
      
Example 3 (Create a new account with specified parameters)::

    ~pikapy --username=mycustomusername --password=hunter2 --email=verifiable@lackmail.ru
    Created new account:
      Username:  mycustomusername
      Password:  hunter2
      Email   :  verifiable@lackmail.ru

