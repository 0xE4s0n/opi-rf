opi-rf
======

Introduction
------------

forked from `rpi-rf`_.

Python module for sending and receiving 433/315MHz LPD/SRD signals with generic low-cost GPIO RF modules on a Orange Pi.

Protocol and base logic ported ported from `rc-switch`_.

Supported hardware
------------------

Most generic 433/315MHz capable modules (cost: ~￥5) connected via GPIO to a Orange Pi.

.. figure:: http://i.imgur.com/vG89UP9.jpg
   :alt: 433modules

Compatibility
-------------

Generic RF outlets and most 433/315MHz switches (cost: ~15€/3pcs).

.. figure:: http://i.imgur.com/WVRxvWe.jpg
   :alt: rfoutlet


Chipsets:

* SC5262 / SC5272
* HX2262 / HX2272
* PT2262 / PT2272
* EV1527 / RT1527 / FP1527 / HS1527

For a full list of compatible devices and chipsets see the `rc-switch Wiki`_

Dependencies
------------

::

   wiringpi

Installation
------------
**NOT NOW!!! Just download and run it.**

On your Orange Pi, install the *opi_rf* module via pip.

Python 3::

    # apt-get install python3-pip
    # pip3 install opi-rf

Wiring diagram (example)
------------------------

Orangepi Pi 5::

                        OPI GPIO TABLE
 +------+-----+----------+   OPI5   +----------+-----+------+
 | GPIO | wPi |   Name   | Physical | Name     | wPi | GPIO |
 +------+-----+----------+----++----+----------+-----+------+
 |      |     |     3.3V |  1 || 2  | 5V       |     |      |
 |   47 |   0 |    SDA.5 |  3 || 4  | 5V       |     |      |
 |   46 |   1 |    SCL.5 |  5 || 6  | GND      |     |      |
 |   54 |   2 |    PWM15 |  7 || 8  | RXD.0    | 3   | 131  |
 |      |     |      GND |  9 || 10 | TXD.0    | 4   | 132  |
 |  138 |   5 |  CAN1_RX | 11 || 12 | CAN2_TX  | 6   | 29   |
 |  139 |   7 |  CAN1_TX | 13 || 14 | GND      |     |      |
 |   28 |   8 |  CAN2_RX | 15 || 16 | SDA.1    | 9   | 59   |
 |      |     |     3.3V | 17 || 18 | SCL.1    | 10  | 58   |
 |   49 |  11 | SPI4_TXD | 19 || 20 | GND      |     |      |
 |   48 |  12 | SPI4_RXD | 21 || 22 | GPIO2_D4 | 13  | 92   |
 |   50 |  14 | SPI4_CLK | 23 || 24 | SPI4_CS1 | 15  | 52   |
 |      |     |      GND | 25 || 26 | PWM1     | 16  | 35   |
 +------+-----+----------+----++----+----------+-----+------+
 | GPIO | wPi |   Name   | Physical | Name     | wPi | GPIO |
 +------+-----+----------+   OPI5   +----------+-----+------+


                      OPI GPIO HEADER
                  ____________
                 |        ____|__
                 |       |    |  |
                 |     01|  . x  |02
                 |       |  . x__|04______       RX
                 |       |  . x__|06____  |   ________
                 |       |  . .  |      | |  |        |
       TX        |   __09|__x .  |      | |__|VCC     |
     _______     |  |  11|  x____|______|_   |        |
    |       |    |  |  13|__x .  |      | |__|DATA    |
    |    GND|____|__| |  |  . .  |      |    |        |
    |       |    |    |  |  . .  |      |    |DATA    |
    |    VCC|____|    |  |  . .  |      |    |        |
    |       |         |  |  . .  |      |____|GND     |
    |   DATA|_________|  |  . .  |           |________|
    |_______|          25|  . .  |26
                         |_______|

    TX:
       GND > PIN 09 (GND)
       VCC > PIN 02 (5V)
      DATA > PIN 13 (GPIO7)

    RX:
       VCC > PIN 04 (5V)
      DATA > PIN 11 (GPIO5)
       GND > PIN 06 (GND)

Usage
-----

See `scripts`_ (`opi-rf_send`_, `opi-rf_receive`_) which are also shipped as cmdline tools.

Open Source
-----------

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues

.. _rpi-rf: https://github.com/milaq/rpi-rf
.. _rc-switch: https://github.com/sui77/rc-switch
.. _rc-switch Wiki: https://github.com/sui77/rc-switch/wiki
.. _BSD Licence: http://www.linfo.org/bsdlicense.html
.. _GitHub: https://github.com/0xE4s0n/opi-rf
.. _GitHub issues: https://github.com/0xE4s0n/opi-rf/issues
.. _scripts: https://github.com/0xE4s0n/opi-rf/blob/master/scripts
.. _opi-rf_send: https://github.com/0xE4s0n/opi-rf/blob/master/scripts/opi-rf_send
.. _opi-rf_receive: https://github.com/0xE4s0n/opi-rf/blob/master/scripts/opi-rf_receive