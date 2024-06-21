#!/bin/bash

#
# Copyright  (C) 2024 Intel Corporation. All rights reserved.
#
# The information and source code contained herein is the exclusive property
# of Intel Corporation and may not be disclosed, examined, or reproduced in
# whole or in part without explicit written authorization from the Company.
#

loc=$PREFIX/etc/OpenCL/vendors

while read line; do
    echo ${line//\/opt\/anaconda1anaconda2anaconda3/$PREFIX}
done < $loc/intel-cpu.icd > $loc/intel-cpu.icd_fixed

mv $loc/intel-cpu.icd_fixed $loc/intel-cpu.icd

while read line; do
    echo ${line//\/opt\/anaconda1anaconda2anaconda3/$PREFIX}
done < $loc/intel-fpga_emu.icd > $loc/intel-fpga_emu.icd_fixed

mv $loc/intel-fpga_emu.icd_fixed $loc/intel-fpga_emu.icd
