#!/bin/sh
cat parameters.txt instances_4/er_40_4_32.txt | python algorithms/findgap.py
cat parameters.txt instances_4/er_40_6_32.txt | python algorithms/findgap.py
cat parameters.txt instances_4/er_40_8_32.txt | python algorithms/findgap.py
cat parameters.txt instances_4/er_40_10_32.txt | python algorithms/findgap.py
cat parameters.txt instances_4/er_40_12_32.txt | python algorithms/findgap.py
