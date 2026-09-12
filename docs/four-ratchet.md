# Universal Messaging Protocol Four-Ratchet Security Model

## UMP Four-Ratchet Specification Version 1.0

---

# 1. Introduction

The Universal Messaging Protocol (UMP) uses a layered key evolution system called the **Four-Ratchet Security Model**.

Traditional secure messaging systems generally focus on protecting conversations through a single ratcheting mechanism.

UMP separates security responsibilities into four independent systems:

```text
+----------------------+
| Identity Ratchet     |
+----------------------+
           |
           v
+----------------------+
| Session Ratchet      |
+----------------------+
           |
           v
+----------------------+
| Message Ratchet      |
+----------------------+
           |
           v
+----------------------+
| Transport Ratchet    |
+----------------------+
```

Each ratchet protects a different security boundary.

The purpose is to reduce the impact of compromise by ensuring that one compromised layer does not automatically compromise all communication.

---

# 2. Design Philosophy

The Four-Ratchet Model follows this principle:

> Identity should not equal session.
> Session should not equal message.
> Message should not equal transport.

Each layer receives independent cryptographic protection.

Example:

```text
User Identity

       |
       v

Conversation Session

       |
       v

Individual Message

       |
       v

Network Connection
```

---

# 3. Ratchet Overview

| Ratchet           | Protects                 | Rotation Frequency |
| ----------------- | ------------------------ | ------------------ |
| Identity Ratchet  | User and device identity | Long-term          |
| Session Ratchet   | Conversations            | Periodic           |
| Message Ratchet   | Individual messages      | Every message      |
| Transport Ratchet | Network connections      | Transport changes  |

---

# 4. Identity Ratchet

## Purpose

The Identity Ratchet protects the long-term identity of a user and their devices.

It manages:

* Identity keys
* Device registration
* Device replacement
* Identity verification

---

# 4.1 Identity Structure

```text
User Identity Key

        |
        |
+-------+-------+
|               |
Phone Key    Laptop Key
```

Each device receives its own identity material.

---

# 4.2 Identity Rotation

Identity keys may rotate due to:

* Device replacement
* Security events
* User request
* Scheduled rotation

Example:

```text
Old Identity

       |
       v

Generate New Identity

       |
       v

Verify Transition

       |
       v

Retire Old Identity
```

---

# 4.3 Identity Compromise

If an identity key is compromised:

The system should:

1. Mark identity as compromised
2. Notify contacts
3. Generate new identity keys
4. Re-establish trust

---

# 5. Session Ratchet

## Purpose

The Session Ratchet protects ongoing conversations.

A session exists between:

* Two users
* Multiple group members
* Devices

---

# 5.1 Session Creation

Example:

```text
Alice Device

       |
       |
Secure Handshake

       |
       |

Bob Device
```

The result:

```text
Encrypted Session
```

---

# 5.2 Session Evolution

Sessions continuously change.

Example:

```text
Session Key 1

      |
      v

Session Key 2

      |
      v

Session Key 3
```

Old session keys are discarded.

---

# 5.3 Session Recovery

If a session becomes invalid:

UMP can:

* End the session
* Create a new session
* Resume communication securely

---

# 6. Message Ratchet

## Purpose

The Message Ratchet protects individual messages.

Every message receives independent encryption material.

---

# 6.1 Message Key Generation

Example:

```text
Message 1 → Key A

Message 2 → Key B

Message 3 → Key C

Message 4 → Key D
```

Compromise of one key does not reveal other messages.

---

# 6.2 Message Chain

Messages form a cryptographic chain.

```text
Root Key

    |
    v

Message Key 1

    |
    v

Message Key 2

    |
    v

Message Key 3
```

Each step derives a new key.

---

# 6.3 Message Deletion

After use:

* Message keys are removed
* Temporary encryption material is destroyed

---

# 7. Transport Ratchet

## Purpose

The Transport Ratchet protects the network connection itself.

UMP assumes transports may change.

Example:

```text
Wi-Fi

  |
  X

Cellular

  |
  X

Mesh Relay
```

Each connection receives separate security material.

---

# 7.1 Transport Sessions

Example:

```text
Transport Session A

Wi-Fi

      |

Transport Session B

5G

      |

Transport Session C

Mesh
```

A compromise of one transport does not expose others.

---

# 7.2 Transport Switching

When a device changes networks:

1. Detect transport change
2. Create new transport keys
3. Verify route
4. Continue communication

---

# 8. Combined Operation

All four ratchets operate together.

Example message:

```text
User Identity
      |
      v
Session Established
      |
      v
Message Created
      |
      v
Message Key Generated
      |
      v
Transport Selected
      |
      v
Transport Key Created
      |
      v
Message Delivered
```

---

# 9. Group Messaging

Groups require multiple ratchet states.

Example:

```text
Group Identity

      |
      +-------------+
      |             |
   Alice          Bob
      |
   Charlie
```

Group events trigger:

* Membership verification
* Group key updates
* Session updates

---

# 10. File Transfer Security

Large files use the Message Ratchet and Transport Ratchet together.

Example:

```text
10 GB File

      |
      v

Chunk 1 → Message Key 1

Chunk 2 → Message Key 2

Chunk 3 → Message Key 3

      |
      v

Transport changes

      |
      v

New Transport Keys
```

---

# 11. Compromise Scenarios

## Scenario 1: Single Message Key Leak

Impact:

* One message exposed

Protection:

* Other messages remain secure

---

## Scenario 2: Transport Key Leak

Impact:

* One network session exposed

Protection:

* Future transport sessions remain secure

---

## Scenario 3: Session Key Leak

Impact:

* Current conversation risk

Protection:

* Future sessions recover through ratcheting

---

## Scenario 4: Identity Key Leak

Impact:

* Identity verification affected

Protection:

* Identity rotation and revocation

---

# 12. Security Goals

The Four-Ratchet Model provides:

## Forward Secrecy

Past communication remains protected.

---

## Future Secrecy

Future communication can recover after compromise.

---

## Layer Isolation

One compromised layer does not automatically compromise all layers.

---

## Transport Independence

Security remains consistent regardless of network.

---

# 13. Implementation Requirements

A compliant implementation should:

Required:

* Maintain separate ratchet states
* Rotate keys automatically
* Protect stored keys
* Verify identity changes
* Destroy expired keys

Recommended:

* Hardware-backed key storage
* Secure memory handling
* Automatic compromise recovery

---

# 14. Summary

The Four-Ratchet Security Model creates four independent security boundaries:

```text
Identity
    ↓
Session
    ↓
Message
    ↓
Transport
```

The goal is simple:

> A failure in one layer should not become a failure everywhere.

UMP uses this model to provide secure communication across traditional cellular networks and future communication systems.
