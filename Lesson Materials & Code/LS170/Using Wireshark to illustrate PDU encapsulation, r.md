# Using Wireshark to illustrate PDU encapsulation, request-response cycle, TLS handshake and more

Course: LS170
Concepts: Encapsulation (Networking), Ethernet Protocol, Networking fundamentals theory, Request-Response Cycle, TCP Handshake, TLS Handshake
Last Edited: June 6, 2022 3:56 PM

### Description

Wireshark is a free and open-source packet analyzer (also called packet sniffer). It reads the traffic on your network interface and shows you what data is sent in a neat interface.

 This packet capture shows a DNS query and response:

![Using%20Wireshark%20to%20illustrate%20PDU%20encapsulation,%20r%207dfa48677653436eb6b40d527cc54fe6/DNS-query-and-response.png](DNS-query-and-response.png)

You can download and open this capture file with Wireshark to explore it yourself:

[DNS Question & Answer.pcapng.cap](DNS_Question__Answer.pcapng.cap)

When I lead a study session for 170, I find it helpful to go over the course concepts from the beginning. Like I'll start with "What is the Internet?", "What are protocols?", before getting into what aspect of network communication the Link layer is responsible for and how Ethernet provides that, then moving on the the Network layer, Transport layer... While I ask the students to explain these concepts and quiz them about it, I introduce Wireshark as a way to illustrate what we're talking about.

What's neat about doing this is, while the LS170 course covers what can be abstract, difficult to understand concepts, I can use Wireshark to make them concrete and tangible.

For example, most students haven't worked as network engineers, so how the different protocols work together might be opaque. But I can be made very clear when reading a Wireshark capture together.