# PP-evaluating-ai-driving-simulators
Evaluating the generalisation of AI driving simulator trained models by their performance in other simulators

## How to ssh into the server
https://nabtron.com/gcc-mac-terminal/

## Setting up the terminal and getting setup scripts
Setup git ssh keys 
https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

```
git clone git@github.com:hcollins345/PP-evaluating-ai-driving-simulators.git
git clone git@github.com:hcollins345/dotfiles
```

https://github.com/hcollins345/dotfiles

## Anaconda
https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart

Goal is to install anaconda3 and to create an environment that uses python 3.6 (compatible with tensorflow).
All scripts are found in the anaconda folder. 

https://www.anaconda.com/tensorflow-in-anaconda/

## Tensorflow CUDA cuDNN and Nvidia Drivers
Used this:
https://www.tensorflow.org/install/gpu#linux_setup
NOTE: sudo apt update necessary after reboot step

NUMA warning for tensorflow botch/fix  
https://dmitry.ai/t/topic/50/2  
NOTE: also requires reboot

__ extra info __
See compatible TF-CUDA-cuDNN here:\
https://www.tensorflow.org/install/source#tested_build_configurations

These scripts use tf:1.14.0, CUDA 10.0 and cuDNN:7.6\
https://mc.ai/tensorflow-gpu-installation-on-ubuntu-18-04/

What to do with the drivers under (additional information)\
https://www.nvidia.com/Download/driverResults.aspx/143675/en-us

To see tensorflow version installed use:
```
python -c 'import tensorflow as tf; print(tf.__version__)'
```
Verify versions using tf, cuda and cudnn are installed correctly run the file:
```
conda list
```
CUDA\
https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal

## Setting up a gui
How to install a desktop:\
https://www.linuxtrainingacademy.com/install-desktop-on-ubuntu-server/

How to set up a vncserver:\
https://medium.com/google-cloud/linux-gui-on-the-google-cloud-platform-800719ab27c5  
https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781788474221/1/ch01lvl1sec15/installing-and-configuring-ubuntu-desktop-for-google-cloud-platform  
http://leadtosilverlining.blogspot.com/2019/01/setup-desktop-environment-on-google.html (THIS ONE IS THE MOST DETAILED)

NOTE: still need to set up a VNCviewer on local.\
https://www.realvnc.com/en/connect/download/viewer/  
Also you will have to enable http and https accepting tcp:5901 with tage vnc-server in target connections in firewall in the google compute center (under VPC network section).\
Do not use tightvncserver as it does not support randr, tried vnc4server which does support it but still unable to get it to function. Recommended to try TurboVNC.

You should then be able to connect to your server desktop using your vncviewer.
Also useful commands
```
vncserver -geometry "1920x1080"
vncserver -kill :1
```


## CARLA
https://usermanual.wiki/Document/CARLASetupGuideUbuntu.271743992.pdf

https://carla.readthedocs.io/en/latest/carla_headless/  
https://github.com/carla-simulator/carla/issues/312  
https://github.com/carla-simulator/carla/issues/1112  

*Benchmarking*\
https://carla.readthedocs.io/en/stable/benchmark_start/

Using TurboVNC and VirtualGL\
https://gist.github.com/cyberang3l/422a77a47bdc15a0824d5cca47e64ba2

How to run (Running in server mode with python controller)\ 
https://carla.readthedocs.io/en/stable/connecting_the_client/#running-the-client-examples

Unable to run the 'standalone' Carla but can run server and can use manual_control.py (uses pygame) running through vnc4server to verify ability to control the car using python scripts and in the simulator. Just run vncserver and add to DISPLAY ie.
```
vncserver
export DISPLAY=:1
```


## Deepdrive

https://github.com/deepdrive/deepdrive




## Scripts

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
