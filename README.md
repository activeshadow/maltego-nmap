# Maltego Nmap Configuration

A few Python-based Maltego transforms and a Maltego machine for parsing Nmap
XML results into Maltego.

Leverages the MaltegoTransform Python library located
[here](https://github.com/sroberts/MaltegoTransform-Python).

## Disclaimer

I've only tested this on Kali...

## Install

Clone the repo or unpack the archive to `/opt/`, such that you now have
`/opt/maltego-nmap`, and import `/opt/maltego-nmap/etc/maltego-nmap.mtz` into
Maltego.

This *should* create two transforms and a machine in Maltego.

* Transforms
  * `Nmap XML Parser`
    - Operates on the `File` entity
  * `Nmap Port Services`
    - Operates on the `IPv4 Address` Entity
* Machine
  * `Nmap XML Parser`
    - Expects a path to the Nmap XML file

## Use

From the `Run Machine` option, select `Nmap XML Parser` and enter the path to
the Nmap XML file as the description.
