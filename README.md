# Anomaly Calculator

Hi there. Thanks for checking out the Anomaly Calculator, a simple,
cross platform RPN calculator.

## Running Anomaly as TUI
Anomaly can be run in TUI mode by adding the `-t` flag:
```
python3 -m anomaly -t
```
## Running Anomaly as CLI
Anomaly can be run as a CLI utility by navigating to this repo's root
folder in a terminal application and typing:
```
python3 -m anomaly {arguments}
```
if you are on a on unix systems. If you are using Windows, you can type:
```
python -m anomaly {arguments}
```
`{arguments}` should be a space-seperated list of numbers and operations you wish to compute and operates as would a standard RPN calculator. 
For example:
```
python3 -m anomaly 4 2 divide 3 sum
```
should return
```[5]```
The top of the stack will be listed first, the next entry next, and so on.
