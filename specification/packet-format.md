# UMP Packet Format

## Version 1.0

---

# Purpose

Defines how messages are divided for transmission.

---

# Packet Structure

```
HEADER
ROUTING
SECURITY
DATA
CHECKSUM
```

---

# Header

Contains:

* Protocol version
* Packet ID
* Message ID
* Packet type

---

# Fragmentation

Large messages may be split.

Example:

```
Message

 |
 +-- Packet 1
 |
 +-- Packet 2
 |
 +-- Packet 3
```

---

# Required Fields

```
packet_id
message_id
fragment_number
total_fragments
checksum
```

---

# Verification

Every packet must pass integrity checking before use.
