# gamepro-phone-notifier

A script to run alongside the gamepro shiny pokemon hunting scripts.
(https://www.noobysgamepro.com/software)
It will send a push notification to your device when the script finds a shiny pokemon.

Requires setup of notify_run. https://pypi.org/project/notify-run/

Run the script in the directory of the gamepro hunting scripts and create a script to run the hunts such
that they pipe their output to a file called output.txt

Example:

startHunt.bat
```
"Crystal_VC_Shiny_Starter_1.0.exe" > output.txt
```
