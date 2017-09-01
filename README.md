# DNS Server
<img src="https://hide.me/resources/156/images/no-dns-icon@2x.png" width="100" height="100">

A Domain Name Server that allows you to use your own domain name IP address mappings.
This could be used within private networks to simplify sharing of resources within the network.

The application requires Python 3.x to run (tested with version 3.6).

# How to use

To use the server there are 2 basic steps to follow:

**Step 1:**
You must first generate a zone file. This is the file that stores the domain name and it's IP address mapping.
To generate a zone file you must create a file with the following filename format: [domain name in reverse order].zone.
Examples:
- The zone file for www.google.com will be google.com.zone
- The zone file for www.bing.co.uk will be bing.co.uk.zone
- The zone file for www.university.ac.co will be university.ac.co.zone

**Ensure the file has a '.zone' extension rather than .txt or any other extension**

An example zone file is provided in the project. You can simply copy the detail inside
and change the relevant fields for your own mapping. In particular you will need to change the domains in the following fields:
- '$origin'
- 'mname'
- 'rname'
- 'ns'

**Ensure the domain names placed in the fields match with the filename to avoid errors**
Finally the 'a' field holds 3 records for the IP address mapped to the domain name. 
Ensure you change them to the correct IP address.

**Step 2:**
Once the zone file is created and placed in the 'Zones' directory you can start the server.
No special modifications are needed to run the server. You can simply run the 'Server.py' file.
**Ensure that you run the 'Server.py' with the necessary privileges required for the program to access network resources.**

Note: The server uses the default DNS server port (53). Ensure no other process is using port 53 
or else the server will not be able to run.

Now you can change the network configurations on various machines that need to use this DNS server by specifying
the IP address of the machine running the DNS server. 

**Run:**

To see an example run you can use the 'dig' command on Linux to see the response the server provides.
- Start the server and ensure it is running before proceeding
- Open a terminal and enter use the following command
```sh
$ dig xyz.com @127.0.0.1
```
You should receive a response for the domain xyz.com
Once you have set your own zone file you can replace 'xyz.com' with your own domain name.
You can change the IP address '127.0.0.1' to the IP address where the DNS server is running when you have it running
on a remote machine on the network.

**Note:** if you have updated your network configurations to use a specific IP for
the dns server then there is no need to include the '@127.0.0.1' portion in the command.

# Run tests

If you make any modifications to the code you can run tests by navigating 
to the project directory (i.e. 'DNS Server') and then run following command:

```sh
$ python3 -m unittest
```

<a href="https://app.codesponsor.io/link/F7562BGJ3YiAu5CBEEerdT66/akapila011/DNS-Server" rel="nofollow"><img src="https://app.codesponsor.io/embed/F7562BGJ3YiAu5CBEEerdT66/akapila011/DNS-Server.svg" style="width: 888px; height: 68px;" alt="Sponsor" /></a>