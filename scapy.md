SCAPY FOR CYBERSECURITY
---

# **Scapy Documentation for Beginners**

Scapy is a powerful Python library used for network packet crafting, manipulation, and analysis. It allows you to send, receive, sniff, and manipulate packets on the network.

## **1. Introduction to Scapy**

### What is Scapy?
Scapy provides a flexible tool for crafting and sending custom packets, capturing network traffic, and automating network tests. It is widely used in cybersecurity for tasks like:
- **Packet sniffing**
- **Network scanning**
- **Vulnerability analysis**
- **Custom packet crafting**
  
---

## **2. Installing Scapy**

You can install Scapy using `pip`:

```bash
pip install scapy
```

Once installed, import Scapy into your Python scripts:

```python
from scapy.all import *
```

---

## **3. Basic Functions in Scapy**

### **`send()`**

- **Purpose**: Sends packets at **Layer 3** (IP Layer).
- **Parameters**:
  - `pkt`: The packet to be sent (required).
  - `count`: Number of packets to send (default is 1).
  - `inter`: Time interval between packets.
  - `iface`: Network interface to use.
  
**Usage Example**:

```python
from scapy.all import send, IP, ICMP

# Create an IP packet with an ICMP layer (Ping)
packet = IP(dst="192.168.1.1") / ICMP()

# Send the packet
send(packet)
```

Explanation:
- **`IP(dst="192.168.1.1")`**: Creates an IP packet targeting the specified IP address.
- **`ICMP()`**: Adds an ICMP (ping) layer.
- **`send()`**: Sends the packet over the network.

---

### **`sendp()`**

- **Purpose**: Sends packets at **Layer 2** (Ethernet Layer).
- **Parameters**: Similar to `send()`, but operates at the Ethernet frame level.

**Usage Example**:

```python
from scapy.all import sendp, Ether, ARP

# Create an Ethernet frame with ARP request
packet = Ether() / ARP(pdst="192.168.1.1")

# Send the packet
sendp(packet)
```

Explanation:
- **`Ether()`**: Creates an Ethernet frame (Layer 2).
- **`ARP(pdst="192.168.1.1")`**: Adds an ARP request to resolve the IP to a MAC address.

---

### **`sniff()`**

- **Purpose**: Captures packets on the network.
- **Parameters**:
  - `count`: Number of packets to capture (optional).
  - `iface`: Interface to sniff on.
  - `filter`: Filter to capture specific traffic (e.g., "tcp", "udp").
  - `prn`: Callback function to process each packet.

**Usage Example**:

```python
from scapy.all import sniff

# Define a callback function
def packet_callback(packet):
    print(packet.summary())

# Sniff 5 packets
sniff(count=5, prn=packet_callback)
```

Explanation:
- **`count=5`**: Captures 5 packets.
- **`prn=packet_callback`**: Each captured packet is passed to `packet_callback` for processing.

---

### **`sr()` and `sr1()`**

- **Purpose**: Sends and receives packets at **Layer 3**.
  - **`sr()`**: Sends multiple packets and receives multiple responses.
  - **`sr1()`**: Sends a packet and waits for one response.
  
**Usage Example (with `sr1()`)**:

```python
from scapy.all import sr1, IP, ICMP

# Send a ping request and wait for a response
response = sr1(IP(dst="192.168.1.1") / ICMP())

# Print response details
if response:
    response.show()
```

Explanation:
- **`sr1()`**: Sends an ICMP (ping) request and waits for a response.
- **`show()`**: Displays all the fields of the received packet.

---

## **4. Packet Layers and Manipulation**

Scapy allows you to construct packets layer by layer using predefined classes. The main layers include:

### **Layer Classes in Scapy**

#### **`Ether()`**: Ethernet Frame (Layer 2)
- **Purpose**: Represents Ethernet frames used for network communication.
- **Usage**:
  
```python
from scapy.all import Ether

# Create an Ethernet frame
eth_frame = Ether()
eth_frame.show()
```

#### **`IP()`**: IP Layer (Layer 3)
- **Purpose**: Represents IP packets.
- **Common Attributes**:
  - `src`: Source IP address.
  - `dst`: Destination IP address.
  - `ttl`: Time-to-live.
  
**Usage**:

```python
from scapy.all import IP

# Create an IP packet
ip_packet = IP(dst="192.168.1.1", ttl=128)
ip_packet.show()
```

Explanation:
- **`dst="192.168.1.1"`**: Sets the destination IP.
- **`ttl=128`**: Sets the time-to-live for the packet.

---

#### **`TCP()`**: TCP Layer (Layer 4)
- **Purpose**: Represents TCP segments for data communication.
- **Common Attributes**:
  - `sport`: Source port.
  - `dport`: Destination port.
  - `flags`: TCP flags (e.g., `S` for SYN, `A` for ACK).

**Usage**:

```python
from scapy.all import TCP

# Create a TCP packet
tcp_packet = TCP(dport=80, flags='S')
tcp_packet.show()
```

Explanation:
- **`dport=80`**: Sets the destination port to HTTP (port 80).
- **`flags='S'`**: SYN flag is used to initiate a connection.

---

#### **Layer Stacking**
In Scapy, you can stack layers by combining them using the `/` operator.

**Usage**:

```python
from scapy.all import IP, TCP

# Stack IP and TCP layers
packet = IP(dst="192.168.1.1") / TCP(dport=80, flags='S')
packet.show()
```

---

## **5. Working with PCAP Files**

Scapy allows reading and writing of packets to `.pcap` files, commonly used in tools like Wireshark.

### **`wrpcap()`**: Writing to PCAP Files

- **Purpose**: Saves captured packets to a PCAP file.
  
**Usage**:

```python
from scapy.all import sniff, wrpcap

# Capture 10 packets
packets = sniff(count=10)

# Save packets to a file
wrpcap('packets.pcap', packets)
```

---

### **`rdpcap()`**: Reading from PCAP Files

- **Purpose**: Reads packets from a PCAP file.

**Usage**:

```python
from scapy.all import rdpcap

# Read packets from file
packets = rdpcap('packets.pcap')

# Print each packet's summary
for packet in packets:
    print(packet.summary())
```

---

## **6. Other Useful Methods**

### **`show()`**
- Displays all fields of a packet in a human-readable format.
  
**Usage**:

```python
packet = IP(dst="192.168.1.1")
packet.show()
```

### **`summary()`**
- Provides a one-line summary of the packet.
  
**Usage**:

```python
packet = IP(dst="192.168.1.1")
print(packet.summary())
```

---

## **7. Putting It All Together**

Here’s a practical example of sniffing packets, processing them, and saving them to a file:

```python
from scapy.all import sniff, wrpcap

# Callback function to process packets
def process_packet(packet):
    print(packet.summary())

# Capture 5 packets
packets = sniff(count=5, prn=process_packet)

# Save captured packets to a PCAP file
wrpcap('captured_packets.pcap', packets)
```

---

## **Conclusion**

Scapy is a flexible tool for network professionals and cybersecurity experts to manipulate, capture, and analyze network traffic. Understanding the basic functions, methods, and classes in Scapy will help you craft packets, automate network tasks, and explore advanced network protocols.

