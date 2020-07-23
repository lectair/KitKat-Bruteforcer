<h1>KitKat Bruteforcer</h1>

This is a tool written in Python3 that attempts to get some working codes for the KitKat iPhone 11 raffle.

There are two modes, random and specific:<br>
    &nbsp;&nbsp;- Random mode: Generates a random string with numbers, uppercase and lowercase letters.<br>
    &nbsp;&nbsp;- Specific mode: Generates a string with 6 uppercase letters, 3 lowercase letters and 1 number.

<h3>BETA - Threading:</h3>
You can set a number of threads to make it faster.<br>
This is still on beta phase so it doesn't work properly yet.
More than 1 or 2 threads doesn't usually work.
<hr>
<h3>Installation:</h3>
First clone this repository running <pre>git clone https://github.com/lectair/KitKat-Bruteforcer</pre>
To install the required modules, run the following command in your command line: <pre>pip3 install -r requirements.txt</pre>
If this doesn't work, try "pip" instead of "pip3".

<hr>
<h3>Usage:</h3>
First of all, you need to edit the line 87 in order to set your account. You have to put your cookies in the 'Cookies' value.<br>

Usage:    python3 kitkat_bruteforcer.py [random/specific] [threads (BETA)]<br>
Example:  python3 kitkat_bruteforcer.py specific 2

<hr>
<h3>Images</h3>
<h4>Usage</h4>
<img src="https://raw.githubusercontent.com/lectair/KitKat-Bruteforcer/master/usage.png" alt="Usage" style="size:2%;">
<h4>Working code:</h4>
<img src="https://raw.githubusercontent.com/lectair/KitKat-Bruteforcer/master/code_sent.png" alt="Code sent" style="size:2%;">
