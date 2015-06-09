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
the Nmap XML file as the description. Alternatively, you can also provide a
directory and the transform will recursively search the given directory for
files named `results.xml` and parse each one into the same graph.

## Just for Fun

I posted a video [here](http://youtu.be/ToR3I87Yvhg).

## License

Copyright (c) 2015, Active Shadow LLC
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
