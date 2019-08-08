# PP-evaluating-ai-driving-simulators
Evaluating the generalisation of AI driving simulator trained models by their performance in other simulators

## How to ssh into the server
https://nabtron.com/gcc-mac-terminal/

## Scripts
script 0 is for gui
https://medium.com/google-cloud/graphical-user-interface-gui-for-google-compute-engine-instance-78fccda09e5c
requires that firewall (in VPC Network) has http and https accept tcp:5901 and has the tag vnc-server in target.

scripts 1-6 are modified from
https://carla.readthedocs.io/en/latest/how_to_build_on_linux/

script 7 is from 
https://github.com/deepdrive/deepdrive#tensorflow-install-tips
Had to modify install.py to use python3

script 7 requires the installation of Unreal_Engine as well

Install Anaconda (provides tensorflow, requires python 3.6.8.

cuda, cudnn https://www.tensorflow.org/install/gpu#ubuntu_1804_cuda_10

ORDER
- 1-6 at once
- 7
- modify install.py in deepdrive
- 8
