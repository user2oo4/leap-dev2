#!/bin/sh
cat instances_4/er_40_4_32.txt results/findgap_results_GAC/er_40_4_32.txt | python algorithms/GAC.py
cat instances_4/er_40_6_32.txt results/findgap_results_GAC/er_40_6_32.txt | python algorithms/GAC.py
cat instances_4/er_40_8_32.txt results/findgap_results_GAC/er_40_8_32.txt | python algorithms/GAC.py
cat instances_4/er_40_10_32.txt results/findgap_results_GAC/er_40_10_32.txt | python algorithms/GAC.py
cat instances_4/er_40_12_32.txt results/findgap_results_GAC/er_40_12_32.txt | python algorithms/GAC.py