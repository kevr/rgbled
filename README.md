# rgbled

This project provides a Python 3 package and shell scripts
for controlling an RGB Led component connected to a Raspberry Pi.

## Installation

Run the following command within the project root to install `rgbled`:

    $ python3 setup.py install --user
    ## Or, as root.
    # python3 setup.py install

After installing, once can run the `rgbled` script, or import an
rgbled module in Python via `import rgbled.<module>`.

Example: `import rgbled.main`

This will import the `rgbled/main.py` module.

## Raspberry Pi Pinout

To see the pin layout of the Raspberry Pi, run the following command:

    $ gpio readall

This will print out a table of the pin layout. By default, this program
uses the BCM numbering schema.

## Development

To get started with developing this program or modifying it, check out
`rgbled/main.py`. This is where the `rgbled` starts the program from.

## Linux Intro

On Linux (which the Raspberry Pi runs), you can view the network stack
(including ip addresses) by running:

    $ ip address list

If you are connected wirelessly, the `wlan0` interface should contain
a valid IP address. If it's over ethernet, the `eth0` interface would
contain an IP address.

Users can remotely login to a Raspberry Pi with SSH enabled by connecting
to one of the IP addresses found above as the user pi. For example:

    $ ssh pi@192.168.0.140

The default password for this machine is `johnnypi`. On a fresh
Raspbian installation, it would be `raspberry`.
