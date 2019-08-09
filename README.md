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

## Anaconda
https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart

Goal is to install anaconda3 and to create an environment that uses python 3.6 (compatible with tensorflow).
All scripts are found in the anaconda folder. 

## Setting up a gui
How to install a desktop:\
https://www.linuxtrainingacademy.com/install-desktop-on-ubuntu-server/

How to set up a vncserver:\
https://medium.com/google-cloud/linux-gui-on-the-google-cloud-platform-800719ab27c5  
https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781788474221/1/ch01lvl1sec15/installing-and-configuring-ubuntu-desktop-for-google-cloud-platform  
http://leadtosilverlining.blogspot.com/2019/01/setup-desktop-environment-on-google.html (THIS ONE IS THE MOST DETAILED)

NOTE: still need to set up a VNCviewer on local.\
https://www.realvnc.com/en/connect/download/viewer/  
Also you will have to enable http and https accepting tcp:5901 with tage vnc-server in target connections in firewall in the google compute center (under VPC network section).

You should then be able to connect to your server desktop using your vncviewer.
Also useful commands
```
vncserver -geometry "1920x1080"
vncserver -kill :1
```

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
