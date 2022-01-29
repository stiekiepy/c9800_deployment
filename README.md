This is a work in progress. Do not run any code that you're not sure of what it does. 

**NOTE 12/11/2021:**
If modules are missing let me know. I believe this is all you need but like anything, I could be missing something small.

### Install the following modules:

pip install nornir  
pip install nornir_jinja2  
pip install nornir_utils  


This was tested on Ubuntu but you should be able to install everything you need on any Linux distro. Create a python3 virtual environment to keep your python installation separate for this project. 


### SPECIFIC TEMPLATE COMMENTS
*"c9800_deployment/templates"*

#### 01_switch_interfaces.j2
Every linie with a < comment > needs to be replaced by your orginization's names. Switch names etc.

Section "!# SVIs for vlans", update your own routing info here for OSPF

#### 03_vlans.j2
The WMI vlan is the vlan and IP to which APs will connect to associate to the controller.

#### 04_tacacs_radius.j2
If your AAA configurations are different just update the template here otherwise this works perfect.

#### 07_guestredirect_internet_ACL.j2
These two ACLs work with the local Guest SSID so users are allowed to contact the ISE server to get the portal before being allowed on the network. If your ACL names are different, just change the names here. When you pass authentication from ISE, ISE sends the names of the ACLs to the controller which controls what the client can do.

#### 08_snmp_ntp.j2
The variable "sw_server" could be your syslog/solarwinds/snmp server. You can change the variable if you want to anything to represent your org.

#### 10_line_configs.j2
Orginizations have different configs for the lines so make sure to change this based on your standard. This config works fine to allow the GUI and SSH access etc.

#### 11_policy_tag_wlan_policy_profiles.j2
Go through the template and insert any descriptions you don't like and make sure to add your own SSID names in the <> sections. This profile setup is standard for  a normal office. If you need specific radio settings etc just change them here. This will get your wifi up no problem

#### 12_apjoin_tag_profile.j2
Here, you have to edit the <> sections to add your AP admin credentials and change any descriptions you don't like.

#### 13_rf_tag_profile.j2
This section disables the lower rates and makes anything 24M and up mandatory. Change as you see fit.


### SPECIFIC SCRIPTS COMMENTS

#### skeleton_config_generate.py
This script takes the variables in the file "hosts_skeleton.yaml" and generates skeleton configs for the two controllers and saves them in *"/configs_skeleton"* folder. It gives them enough config to enable SSH and get on the network to be reachable. It generates the switch configs to which the two WLCs connect. Each WLC will be in a port-channel to the switch. It generates the redundancy configs for both as well. You can connect the RP ports to a switch with a L2 vlan dedicated for this or you can cross connect them to each other with a cross over cable. Once you paste in the redundancy configs and reload, the WLCs will logically be "one" and you no longer need to log into them separately.

#### generate_config.py
This script takes all the variables you filled out in "hosts.yaml, groups.yaml and defaults.yaml" and generates individual files in the *"/configs_partial"* folder. Lastly, it takes all those configs and generates one big config file. Benefits of this is you can take any partial config if you need it. Like just needing to update AAA etc.


### Example diagram of a common deployment
![c9800_deployment_github](https://user-images.githubusercontent.com/22822441/149586164-072e4bc8-4039-4f29-96c8-ad69717683d7.png)
