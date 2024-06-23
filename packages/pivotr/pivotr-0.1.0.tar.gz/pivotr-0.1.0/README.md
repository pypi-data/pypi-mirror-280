# Pivotr - A remote command execution framework

The aim of pivotr initially is to simplify the task of maintaining ssh connections throughout a network environment. These connections, which we refer to as 'nodes', are stored in an encrypted file as a list of objects. Each object currently only contains very basic data regarding each node, including a basic node ID (and consequently, the id of the node in the list), the node's IP address, and the option to append a username and password to the node if SSH credentials are known.

Stage 1 - Nodes:
- Implement basic node manipulation, including the ability to add, delete, modify, view nodes
- Implement basic node data persistance (in this case, pickling)
- Successfully send single SSH commands or make SSH connections to nodes with credentials
- Implement pivot functionality to where connections that require jumps between nodes are seamless
- Encrypt all stored data given the need for stored credentials to nodes
- Add 'mapping' functionality to display a basic map of connected nodes via CLI (aesthetically differentiates between nodes with credentials and nodes without)
- Add uploading/downloading to/from nodes via SCP
- Implement a 'snapshot' feature to allow us to save encrypted node data to be utilized later if necessary
- Introduce ping-sweep feature that scans for hosts on a node's subnet and adds all new discoveries as nodes without credentials
- Work on input validation and clean up code

Stage 2 - Agents:
- Implement a master server process to listen for incoming 'reverse' connections
- Add to node object variables in order to account for much larger data sets provided by agents (see next bullet point)
- Design 'agent' executables that, when run, connect back to our pivotr server. These agents will be the hallmark of any non-ssh functionality and will include features such as:
	+ The ability to harvest data from their respective hosts and transmit the data back to our pivotr server for safekeeping
	+ Remain persistent and callback to the pivotr server after a connection is lost
	+ Utilize IDS/IPS avoidance and obfuscation to maintain persistence
	+ Transmit data via encrypted channels
	+ Cross-platform, non-OS-specific implementation
	+ Integration into current node object schema and mapping functionality

Stage 3 - Profit
- ?

<p align="right">(<a href="#top">back to top</a>)</p>

# Setup

Clone this project:
```sh
git clone https://gitlab.com/maturon/pivotr
```
Enter the new project file:
```sh
cd pivotr
```
Create a virtual environment for all dependencies and activate environment:
```sh
python -m venv .
source bin/activate
```
Install dependencies:
```sh
pip install -r requirements.txt
```

Note: may implement this as a more portable executable with `pip install -U pyinstaller` and `pyinstaller pivotr.py`

# Pivotr basics

Help:
```sh
pivotr.py -h
```
Show map of all nodes we currently know about (hard lines are credentialed hosts, dotted lines have no credentials):
```sh
pivotr.py -m

╭─────────────────╮
│n0 - pivotr      │
│  192.168.1.150  │
╰───────────┬─────╯
            │  ╭ ─ ─ ─ ─ ─ ─ ─ ─ ╮
            ├──┤n1               ╎
            │  ╎   192.168.1.1   ╎
            │  ╰ ─ ─ ─ ─ ─ ─ ─ ─ ╯
            │  ╭ ─ ─ ─ ─ ─ ─ ─ ─ ╮
            ├──┤n2               ╎
            │  ╎  192.168.1.59   ╎
            │  ╰ ─ ─ ─ ─ ─ ─ ─ ─ ╯
            │  ╭─────────────────╮
            ├──┤n3               │
            │  │  192.168.1.170  │
            │  ╰─────────┬───────╯
            │            │  ╭ ─ ─ ─ ─ ─ ─ ─ ─ ╮
            │            ├──┤n4               ╎
            │            │  ╎     10.0.2.3    ╎
            │            │  ╰ ─ ─ ─ ─ ─ ─ ─ ─ ╯
            │            │  ╭─────────────────╮
            │            ├──┤n5               │
            │            │  │     10.0.2.1    │
            │            │  ╰─────────┬───────╯
            │            │            │  ╭─────────────────╮
            │            │            ╰──┤n10              │
            │            │               │   172.6.12.15   │
            │            │               ╰─────────────────╯
            │            │  ╭ ─ ─ ─ ─ ─ ─ ─ ─ ╮
            │            ├──┤n6               ╎
            │            │  ╎     10.0.2.4    ╎
            │            │  ╰ ─ ─ ─ ─ ─ ─ ─ ─ ╯
            │            │  ╭ ─ ─ ─ ─ ─ ─ ─ ─ ╮
            │            ├──┤n7               ╎
            │            │  ╎     10.0.2.2    ╎
            │            │  ╰ ─ ─ ─ ─ ─ ─ ─ ─ ╯
            │            │  ╭─────────────────╮
            │            ╰──┤n8               │
            │               │     10.0.2.5    │
            │               ╰─────────────────╯
            │  ╭ ─ ─ ─ ─ ─ ─ ─ ─ ╮
            ╰──┤n9               ╎
               ╎     1.2.3.4     ╎
               ╰ ─ ─ ─ ─ ─ ─ ─ ─ ╯


```
Since our host is node 0 (n0) by default, run a ping sweep from n0 to map our subnet (check to see if ping sweep was successfully by running `pivotr.py -m` afterward):
```sh
pivotr.py -n0 -S
```
Add known SSH credentials to node 10:
```sh
pivotr.py -n10 -e

Current node values:
    1) IP addr:   172.6.12.15
    2) UN:        jsmith
    3) PW:        
    4) Exit:

Select property to edit: 3

New password: ************

Node 10 successfully modified.
```
Send command `uname -a` to node 10 via SSH:
```sh
pivotr.py -n10 -c "uname -a"
```
Make SSH connection to node 10:
```sh
pivotr.py -n10 -i

jsmith@172.6.12.15$
```
Save our current node data set for later use in ./snapshots directory:
```sh
pivotr.py -s
```
Use a data set from ./snapshots (which replaces current data set at /tmp/nodes.data):
```sh
./pivotr.py -f ./snapshots/2024-01-15_114534-nodes.data
```

<p align="right">(<a href="#top">back to top</a>)</p>

# Contact

Maturon Miner - maturon@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>