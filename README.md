Junos Show Chassis Output to CSV
=================================
This python script reads a directory of JSON files, parses parts with serial numbers, and dumps them into a single CSV for review.

Requirements
------------
Python 3

Tested with Python 3.9.6

Python packages

* built-in

Virtualenv Install
----------
    python3 -m venv venv
    source venv/bin/activate

Usage
---
Python script doesn't expect any arguments. Just needs the chassis_hardware_outputs directory created prior to script run. That is the dir that is read on execution.

Example
---
Python script execution example:

    python junos_show_chassis_hardware_to_csv.py 

Caveats
---
Only have tested against:
* SRX320 JUNOS 21.4R1
* vJunos 21.2R3-S1

Improvement
---
