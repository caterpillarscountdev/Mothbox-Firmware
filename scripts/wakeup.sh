#!/bin/bash

echo $1 | sudo tee /sys/class/rtc/rtc0/wakealarm
