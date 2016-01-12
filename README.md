# pyLiter

A simply python module to to interact with the [Pi-LITEr 8-LED Raspberry Pi shield](http://ciseco.co.uk/docs/Pi-LITEr-v-0-1.pdf) from Ciseko.

This is a a work in progress.

## Installation

This code currently runs on either python2 or python3, and depends on [wiringpi2](https://github.com/Gadgetoid/WiringPi2-Python). It is intended for use on the Raspberry Pi.

### Python 3

On the Raspberry Pi, run-

    sudo apt-get install python3 python3-pip
    pip3 install wiringpi2

Execute the test script with:

    python3 test.py

### Python 2

    sudo apt-get install python python-pip
    pip install wiringpi2

Execute the test script with:

    python test.py

## Development

Execute unit tests with:

    python -m unittest discover

Install coverage plugin:

    apt-get install python-coverage
    yum install python-coverage

Run with coverage:

    coverage run -m unittest discover

