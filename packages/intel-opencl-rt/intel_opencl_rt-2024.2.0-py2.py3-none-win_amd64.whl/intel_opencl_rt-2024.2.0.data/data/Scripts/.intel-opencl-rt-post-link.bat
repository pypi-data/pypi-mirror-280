REM Copyright  (C) 2024 Intel Corporation. All rights reserved.
REM
REM The information and source code contained herein is the exclusive property
REM of Intel Corporation and may not be disclosed, examined, or reproduced in
REM whole or in part without explicit written authorization from the Company.

setlocal EnableDelayedExpansion
set "cl_cfg_orig=%PREFIX%\Library\lib\cl.cfg"
set "cl_cfg_temp=%PREFIX%\Library\lib\cl.cfg.temp"
set "lib_bin=%PREFIX%\Library\bin"
set "PATH=%PATH%;C:\Windows\System32"
%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell -Command "(gc '%cl_cfg_orig%') -replace 'CL_CONFIG_TBB_DLL_PATH =.*', 'CL_CONFIG_TBB_DLL_PATH = %lib_bin%' | Out-File -Encoding ASCII -FilePath '%cl_cfg_temp%'"
move /Y "%cl_cfg_temp%" "%cl_cfg_orig%"
