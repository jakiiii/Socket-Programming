# Socket Programming

**Network:** Network is computer and device connected ti each other with to wireless (wi-fi / li-fi).


### OSI MODEL
**Open System Interconnection**

THE SEVEN LAYER OF OSI

```
Transmit Data				User					Receive Data
	|				Application (Layer - 7)				|
	|				Presentation (Layer - 6)			|
	|				Session (Layer - 5)				|
	|				Transport (Layer - 4)				|
	|				Network (Layer - 3)				|
	|				Data Link (Layer - 2)				|
	|				Physical (Layer - 1)				|
	|-------------------------------- Physical Link --------------------------------|
```

**Allocation (Layer - 7):** Application is a protocol like STP, HTTP, HTTPS etc.

**Presentation (Layer - 6):** Converting the data or extension in UTC (mp4/mp3)

**Session (Layer - 5):** Its associate the user to clients.

**Transport (Layer - 4):** This is the main protocol of TCP/UDC.

**Network (Layer - 3):** IP Protocol using the router.

**Data Link (Layer - 2):** This is the SWITCH protocol layer.

**Physical (Layer - 1):** Transform to data layer from digital data to analog data.


**Socket:** Socket is the communication mechanism that allows clients / server to connect to each other with specific rule.

**Socket Programming:** Socket programming of connecting two node on a network to communicate to each other. Server form to listener socket while client reach out to the server.

```
----------			----------
| Server |			| Client |
----------			----------
    |				    |
  Socket			    |
    |				    |
  Setsockopt			    |
    |				    |
  Bind				    |
    |				    |
  Listen <---------------------- Connect
    |				    |
  Accept			    |
    |				    |
  Send/Recv <-----------------> Send/Recv
``` 

**TCP:** Transmission Control Protocal

**UDP:** User Datagram Protocal

```
-------------------------------------------------------------------------
|		TCP			|		UDP		|
-------------------------------------------------------------------------
| Reliable				| Unreliable			|
------------------------------------------------------------------------|
| Connection Orinented			| Connectionless		|
------------------------------------------------------------------------|
| Segment retransmission and		| No windowing or retransmission|
| flow control through			|				|
| windowing. 				|				|
------------------------------------------------------------------------|
| Segment sequencing			| No sequencing			|
------------------------------------------------------------------------|
| Acknowledgement			| No acknowledgement		|
-------------------------------------------------------------------------
```

**Raw Sockets:** Raw socket is an internet socket that allows direct sending and receiving of internet protocol packets without any protocol (TCP/UDP) specific transport layer formatting. Example, RAW SOCKET is used for DDoS (Distribute Denial of Server Attack) attack.
