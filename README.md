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
<h3>Setting up cookies:</h3>
First of all you have to sign up into the <a href="https://www.kitkat.es/promo-iphone/">KitKat website</a>. Then you have to go to the code submitting page and open your browser inspector (Ctrl+Shift+I).<br>In my case I will be using Firefox but this works for Chrome too at least. Go to the Network tab and then submit a random code.
<img src="https://raw.githubusercontent.com/lectair/KitKat-Bruteforcer/master/img/cookies1.png" alt="Sending code" style="size:2%;"><br>
This will generate some GET & POST requests that are visible in your browser inspector. You have to select the only POST request and go to the request headers part in the right tab. Search the Cookie header and copy its value.
<img src="https://raw.githubusercontent.com/lectair/KitKat-Bruteforcer/master/img/cookies2.png" alt="Browser Inspector" style="size:2%;"><br>
This is the value that you have to paste into the line 87. Just paste it inside the quotes.
<img src="https://raw.githubusercontent.com/lectair/KitKat-Bruteforcer/master/img/cookies3.png" alt="Paste the cookies" style="size:2%;"><br>

<hr>
<h3>Usage:</h3>
Once you've set your cookies you can run the tool just by using the following instructions:<br><br>

Usage:    python3 kitkat_bruteforcer.py [random/specific] [threads]<br>
Example:  python3 kitkat_bruteforcer.py specific 2

<hr>
<h3>Images</h3>
<h4>Usage</h4>
<img src="https://raw.githubusercontent.com/lectair/KitKat-Bruteforcer/master/img/usage.png" alt="Usage" style="size:2%;">
<h4>Working code:</h4>
<img src="https://raw.githubusercontent.com/lectair/KitKat-Bruteforcer/master/img/code_sent.png" alt="Code sent" style="size:2%;">
