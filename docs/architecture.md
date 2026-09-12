# Universal Messaging Protocol Architecture

## UMP System Architecture Version 1.0

---

# 1. Introduction

Universal Messaging Protocol (UMP) is designed as a modular communication architecture that separates:

* User communication
* Message processing
* Security
* Routing
* Network transport

The purpose of this separation is to allow the same communication protocol to function across many different networks.

A message should not need to know whether it is being delivered through:

* Cellular networks
* Internet connections
* Local wireless connections
* Mesh networks
* Satellite systems

The transport is simply a delivery method.

---

# 2. High-Level Architecture

UMP follows a layered architecture.

```text
+------------------------------------------------+
|                 Application Layer              |
|                                                |
|  Messaging Apps / Services / Devices           |
+------------------------------------------------+
|                 Protocol Layer                 |
|                                                |
|  Messages, Groups, Media, Presence             |
+------------------------------------------------+
|                 Security Layer                 |
|                                                |
| Encryption, Authentication, Four-Ratchet        |
+------------------------------------------------+
|                 Routing Layer                  |
|                                                |
| Path Selection, Relays, Fallback               |
+------------------------------------------------+
|                 Transport Layer                |
|                                                |
| SMS, RCS, WiFi, Mesh, LoRa, Satellite          |
+------------------------------------------------+
|                 Network Layer                  |
|                                                |
| Cellular, Internet, Radio                      |
+------------------------------------------------+
```

---

# 3. Core Design Principles

## 3.1 Separation of Concerns

Each layer has a specific responsibility.

Example:

A message does not decide:

* Which carrier to use
* Which radio technology to use
* Which route to take

Instead:

```text
Message
   |
Security
   |
Routing
   |
Transport Selection
   |
Network
```

---

# 4. Core Components

UMP is divided into several major subsystems.

---

# 4.1 Core Protocol Engine

Location:

```text
src/core/
```

The core engine handles:

* Message creation
* Message parsing
* Packet creation
* Identity management
* Capability negotiation

The core does not handle network communication.

---

Example:

```text
Create Message

        |
        v

Core Protocol Engine

        |
        v

Encrypted Packet
```

---

# 4.2 Identity System

Location:

```text
src/core/identity/
```

UMP separates:

* User identity
* Device identity
* Network address

A single user may have multiple devices.

Example:

```text
User Identity

      |
      +----------------+
      |                |
   Phone            Laptop
 Device            Device
```

Each device has:

* Unique identity keys
* Device permissions
* Verification state

---

# 4.3 Security Layer

Location:

```text
src/crypto/
```

The security layer provides:

* Encryption
* Authentication
* Key management
* Secure sessions

Security happens before transport selection.

Example:

```text
Plain Message

      |
      v

Encryption

      |
      v

Secure Packet

      |
      v

Transport
```

---

# 4.4 Four-Ratchet Security System

Location:

```text
src/crypto/four_ratchet/
```

UMP uses four independent security ratchets.

```text
+-----------------------+
| Identity Ratchet      |
+-----------------------+
          |
          v
+-----------------------+
| Session Ratchet       |
+-----------------------+
          |
          v
+-----------------------+
| Message Ratchet       |
+-----------------------+
          |
          v
+-----------------------+
| Transport Ratchet     |
+-----------------------+
```

Each ratchet protects a different part of communication.

---

# 4.5 Messaging Layer

Location:

```text
src/messaging/
```

Handles user-visible communication.

Includes:

* Text
* Media
* Groups
* Reactions
* Presence
* Receipts

The messaging layer does not know how delivery happens.

---

Example:

```text
Send Image

Messaging Layer
       |
       |
Security Layer
       |
       |
Transport Layer
```

---

# 4.6 File System Layer

Location:

```text
src/files/
```

Responsible for large data transfers.

Features:

* File chunking
* Encryption
* Verification
* Resume support

Example:

```text
10GB File

      |
      v

Split into chunks

      |
      v

Encrypt chunks

      |
      v

Transmit

      |
      v

Reassemble
```

---

# 5. Transport Architecture

Location:

```text
src/transports/
```

The transport layer provides communication methods.

All transports implement the same interface.

Example:

```text
Transport Interface

        |
+-------+-------+-------+
|       |       |       |
SMS    RCS    WiFi   Mesh
```

---

# 5.1 Cellular Transport

Supported systems:

```text
Cellular

├── SMS
├── MMS
└── RCS
```

Used for:

* Compatibility
* Carrier networks
* Legacy devices

---

# 5.2 Internet Transport

Supports:

* TCP
* UDP
* WebSockets

Used for:

* High-speed messaging
* Large files
* Normal operation

---

# 5.3 Alternative Transport

UMP can support:

```text
Bluetooth
WiFi Direct
LoRa
Mesh Networks
Tor
I2P
Satellite
```

These are optional modules.

---

# 6. Routing Architecture

Location:

```text
src/routing/
```

The routing system decides:

* Best available path
* Backup routes
* Delivery priority

Example:

```text
Attempt 1:

WiFi
 |
Failed

Attempt 2:

Cellular
 |
Failed

Attempt 3:

Mesh Relay
```

---

# 7. Transport Switching

One of UMP's major features is live transport switching.

A message can change networks during delivery.

Example:

```text
Device A

WiFi
 |
Disconnected
 |
Cellular
 |
Mesh Relay
 |
Device B
```

The message remains the same.

Only the transport changes.

---

# 8. Storage Architecture

Location:

```text
src/storage/
```

Provides:

* Offline message queue
* Local message database
* Attachment storage
* Temporary caching

Used when:

* Device is offline
* Recipient unavailable
* Network unavailable

---

# 9. API Architecture

Location:

```text
src/api/
```

Provides interfaces for:

* Applications
* Transport modules
* Security modules
* Extensions

Example:

```text
Messaging App

      |
      v

UMP API

      |
      v

Protocol Engine
```

---

# 10. Data Flow Example

A normal message:

```text
User writes message

        |
        v

Messaging Layer

        |
        v

Protocol Formatter

        |
        v

Four-Ratchet Encryption

        |
        v

Routing Engine

        |
        v

Transport Selection

        |
        v

Network Delivery

        |
        v

Recipient Device
```

---

# 11. Failure Handling

UMP assumes networks fail.

Failures are handled through:

* Retries
* Alternate transports
* Stored messages
* Routing changes

Example:

```text
Network Failure

       |
       v

Detect failure

       |
       v

Select alternative transport

       |
       v

Continue delivery
```

---

# 12. Extensibility

New features are added as modules.

Possible future modules:

* Voice calling
* Video calling
* Broadcast messaging
* Emergency systems
* Satellite communication
* New encryption systems

The core protocol does not need redesign.

---

# 13. Summary

UMP architecture is built around one principle:

```text
The message is permanent.
The network is temporary.
```

The protocol provides:

* Universal messaging
* Secure communication
* Transport independence
* Network resilience
* Future expansion

UMP is designed to become a communication layer that can operate anywhere a connection exists.
