# Universal Messaging Protocol Specification

## UMP Protocol Specification Version 1.0

---

# 1. Introduction

Universal Messaging Protocol (UMP) is a transport-independent communication protocol designed to provide a unified messaging layer for modern communication systems.

UMP is designed to replace and extend traditional messaging protocols including:

* SMS
* MMS
* RCS

while supporting additional communication methods such as:

* Internet messaging
* Wi-Fi communication
* Bluetooth communication
* Mesh networking
* Low-bandwidth networks
* Satellite communication

UMP separates the message itself from the network used to deliver it.

A message created using UMP should remain identical regardless of whether it travels through:

```
Cellular tower
Internet connection
Bluetooth relay
Mesh network
Satellite link
```

---

# 2. Protocol Goals

UMP is designed around the following goals:

## 2.1 Universal Communication

Any compatible device should be able to communicate regardless of:

* Carrier
* Manufacturer
* Operating system
* Network availability

---

## 2.2 Security by Default

All UMP communication should support:

* Encryption
* Authentication
* Identity verification
* Forward secrecy
* Recovery after compromise

---

## 2.3 Transport Independence

The protocol must not depend on one network.

The transport layer is responsible only for delivery.

The message layer is responsible for:

* Content
* Identity
* Security
* Integrity

---

## 2.4 Backward Compatibility

UMP may operate alongside existing systems:

```
UMP Device
    |
    |
+---+---+
|       |
RCS    SMS
```

When another UMP endpoint is unavailable, compatibility gateways may provide fallback communication.

---

# 3. Protocol Layers

UMP uses a layered architecture.

```
+--------------------------------+
| Application Layer              |
| Messages, Groups, Media        |
+--------------------------------+
| Protocol Layer                 |
| Message Formatting             |
+--------------------------------+
| Security Layer                 |
| Encryption and Authentication  |
+--------------------------------+
| Transport Layer                |
| SMS/RCS/WiFi/Mesh/Satellite    |
+--------------------------------+
| Physical Network               |
| Cellular, Radio, Internet      |
+--------------------------------+
```

---

# 4. Message Structure

Every UMP message contains five primary sections.

```
UMP Message

+----------------+
| Header         |
+----------------+
| Identity       |
+----------------+
| Security Data  |
+----------------+
| Payload        |
+----------------+
| Transport Data |
+----------------+
```

---

# 5. Message Header

The message header contains routing and protocol information.

Example:

```json
{
 "version": "1.0",
 "message_id": "unique-id",
 "timestamp": "UTC",
 "type": "text",
 "priority": "normal"
}
```

Required fields:

| Field      | Purpose           |
| ---------- | ----------------- |
| Version    | Protocol version  |
| Message ID | Unique identifier |
| Timestamp  | Creation time     |
| Type       | Message category  |
| Priority   | Delivery priority |

---

# 6. Identity System

UMP separates identity from phone numbers.

A user may have:

```
User Identity
      |
      |
+-----+------+
|            |
Phone     Computer
Device    Device
```

Each identity contains:

* Public identity key
* Device keys
* Verification information
* Permissions

A phone number may be used as an address, but it is not the security identity.

---

# 7. Message Types

UMP supports multiple message categories.

## 7.1 Text Message

Example:

```json
{
"type":"text",
"content":"Hello world"
}
```

---

## 7.2 Rich Message

Supports:

* Formatting
* Links
* Cards
* Interactive content

---

## 7.3 Media Message

Supports:

* Images
* Video
* Audio
* Documents

---

## 7.4 Group Message

Groups support:

* Multiple members
* Membership changes
* Administrator controls
* Group encryption

---

## 7.5 Emergency Message

Emergency messages have:

* Priority routing
* Optional location data
* Increased delivery attempts

---

# 8. Capability Negotiation

Before communication begins, devices exchange capabilities.

Example:

```json
{
 "supports":
 [
 "encryption",
 "large-files",
 "groups",
 "mesh"
 ]
}
```

Capabilities determine:

* Available features
* Maximum file size
* Supported transports
* Security level

---

# 9. Delivery States

Messages may have these states:

```
Created
 |
Encrypted
 |
Sent
 |
Received
 |
Delivered
 |
Read
```

A device may optionally disable delivery reporting.

---

# 10. Message Priority

UMP supports priority levels.

```
Emergency
High
Normal
Low
Background
```

Priority affects:

* Routing decisions
* Retry behavior
* Network selection

---

# 11. Fragmentation

UMP supports splitting data into multiple packets.

Example:

```
Large Message

Packet 1
Packet 2
Packet 3
Packet 4
```

Each packet contains:

* Message ID
* Fragment number
* Total fragments
* Integrity information

---

# 12. Reliability

UMP provides:

* Packet verification
* Duplicate detection
* Retry handling
* Resume support

The protocol can operate over unreliable networks.

---

# 13. Extension System

UMP supports future expansion.

Extensions may add:

* Voice calls
* Video calls
* New encryption methods
* New transports
* New media formats

Extensions must:

* Have unique identifiers
* Maintain compatibility
* Not weaken security

---

# 14. Versioning

UMP versions use:

```
Major.Minor.Patch
```

Example:

```
1.0.0
```

Major versions may introduce breaking changes.

Minor versions add features.

Patch versions fix issues.

---

# 15. Implementation Requirements

A compliant UMP implementation must support:

Required:

* Message formatting
* Identity handling
* Encryption support
* Packet handling
* Transport abstraction

Optional:

* Large file transfers
* Mesh networking
* Satellite transport
* Emergency features

---

# 16. Summary

UMP defines a universal communication protocol where:

```
Message
  |
Security
  |
Protocol
  |
Any Available Network
```

The network should not determine how people communicate.

The message should work everywhere.
