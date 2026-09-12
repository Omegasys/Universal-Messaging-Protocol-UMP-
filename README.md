# Universal Messaging Protocol (UMP)

## An open, secure, and transport-independent messaging protocol

Universal Messaging Protocol (UMP) is an open-source communication protocol designed to provide a modern replacement and evolution path for traditional mobile messaging systems such as SMS, MMS, and RCS.

UMP is designed around a simple idea:

> Messages should not depend on a single network.

A message should be able to travel through cellular networks, the Internet, local wireless connections, mesh networks, or future communication systems while maintaining the same identity, security, and user experience.

---

# Goals

UMP aims to provide:

* Modern replacement for SMS and MMS
* Open alternative to carrier-dependent messaging systems
* Compatibility path with RCS
* End-to-end encrypted communication
* Large file transfer support
* Multi-device identity management
* Offline and low-bandwidth operation
* Transport-independent communication
* Emergency communication capabilities

---

# Core Features

## Messaging

UMP supports:

* Text messages
* Rich messages
* Group conversations
* Message reactions
* Replies
* Read receipts
* Typing indicators
* Presence information
* Multimedia attachments

---

## Security

UMP uses a multi-layer security architecture:

* End-to-end encryption
* Cryptographic identity verification
* Forward secrecy
* Post-compromise recovery
* Metadata protection

UMP introduces the Four-Ratchet Security Model:

1. Identity Ratchet
2. Session Ratchet
3. Message Ratchet
4. Transport Ratchet

---

## Large File Support

UMP supports files up to:

```
10 GB maximum size
```

Large files are handled through:

* Chunking
* Encryption per chunk
* Integrity verification
* Resumable transfers
* Transport switching

A transfer may continue even if the available network changes.

Example:

```
Wi-Fi
  |
  X disconnected
  |
Cellular
  |
Mesh relay
  |
Completed transfer
```

---

# Transport Independence

UMP separates the message system from the network system.

Supported transports may include:

```
Cellular
 ├── SMS
 ├── MMS
 └── RCS

Internet
 ├── TCP
 ├── UDP
 └── WebSockets

Local Networks
 ├── Wi-Fi Direct
 ├── Bluetooth
 └── Mesh

Alternative Networks
 ├── LoRa
 ├── Tor
 ├── I2P
 └── Satellite
```

The protocol remains the same regardless of transport.

---

# Design Philosophy

UMP follows these principles:

## Open

The protocol specification is publicly available.

## Secure

Security is built into the protocol rather than added afterward.

## Resilient

Communication should continue when networks fail.

## User Controlled

Users own their identities and encryption keys.

## Modular

New transports and features can be added without redesigning the protocol.

---

# Project Structure

```
universal-messaging-protocol/

├── docs/
│   ├── protocol-spec.md
│   ├── architecture.md
│   ├── security-model.md
│   ├── four-ratchet.md
│   ├── file-transfer.md
│   ├── transport-layer.md
│   └── interoperability.md

├── src/
│   ├── core/
│   ├── crypto/
│   ├── messaging/
│   ├── files/
│   ├── transports/
│   └── routing/
```

---

# Status

UMP is currently a protocol design project.

The current focus is:

* Defining the protocol architecture
* Designing message formats
* Creating security specifications
* Designing transport abstraction
* Developing reference implementations

---

# License

Universal Messaging Protocol is licensed under the GNU General Public License Version 3.0.

See:

```
LICENSE
```

for full license information.

---

# Vision

The long-term goal of UMP is to create a universal communication layer where a phone can communicate regardless of:

* Carrier
* Device manufacturer
* Network provider
* Geographic location
* Available infrastructure

A message should simply be a message.
