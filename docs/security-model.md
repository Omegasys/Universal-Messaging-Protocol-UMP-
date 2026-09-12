# Universal Messaging Protocol Security Model

## UMP Security Architecture Version 1.0

---

# 1. Introduction

Security is a fundamental part of the Universal Messaging Protocol (UMP) design.

UMP assumes that communication networks cannot always be trusted.

A message may travel through:

* Mobile carriers
* Internet providers
* Public Wi-Fi networks
* Mesh relays
* Third-party infrastructure
* Unknown intermediate systems

Therefore, security must exist independently from the transport network.

The core security principle of UMP is:

> The network delivers the message, but the network does not own the message.

---

# 2. Security Goals

UMP is designed to provide:

## 2.1 Confidentiality

Only intended participants should be able to read message contents.

Protected data includes:

* Text messages
* Media files
* Attachments
* Group conversations
* Identity information

---

## 2.2 Integrity

Recipients must be able to verify that:

* Messages were not modified
* Files were not corrupted
* Sender identity is authentic

---

## 2.3 Authentication

Users should be able to verify:

* Who sent a message
* Which device sent it
* Whether an identity has changed

---

## 2.4 Forward Secrecy

If a current key is compromised:

* Previous messages should remain protected

---

## 2.5 Post-Compromise Recovery

If an attacker gains access:

* Future communication should recover security automatically

---

## 2.6 Transport Privacy

The protocol attempts to reduce unnecessary exposure of:

* Message metadata
* Identity information
* Communication patterns

---

# 3. Threat Model

UMP assumes attackers may include:

## 3.1 Network Attackers

Examples:

* Public Wi-Fi attackers
* Carrier network observers
* Internet service providers

Capabilities:

* Observe traffic
* Block traffic
* Delay traffic
* Attempt modification

---

## 3.2 Malicious Infrastructure

Examples:

* Rogue servers
* Compromised relays
* Untrusted routing nodes

UMP assumes infrastructure may be hostile.

---

## 3.3 Device Compromise

Examples:

* Malware
* Lost devices
* Stolen devices

UMP provides protections but cannot protect data after a fully compromised unlocked device.

---

## 3.4 Metadata Attackers

Attackers may attempt to determine:

* Who communicates
* When communication occurs
* Message size
* Frequency patterns

---

# 4. Security Architecture

UMP security is divided into layers.

```text
+--------------------------------+
| Application Security           |
| Permissions / User Controls    |
+--------------------------------+
| Message Security               |
| Encryption / Integrity         |
+--------------------------------+
| Identity Security              |
| Keys / Verification            |
+--------------------------------+
| Four-Ratchet Security          |
| Continuous Key Evolution       |
+--------------------------------+
| Transport Security             |
| Network Protection             |
+--------------------------------+
```

---

# 5. Identity Model

UMP does not rely solely on phone numbers.

A phone number is considered an address, not an identity.

The identity model contains:

```text
User Identity

       |
       |
+------+------+
|             |
Device A   Device B
```

---

Each identity contains:

* Identity public key
* Device public keys
* Verification information
* Device authorization state

---

# 6. Key Architecture

UMP uses multiple key categories.

## 6.1 Identity Keys

Long-term keys used to establish identity.

Purpose:

* User verification
* Device authentication

---

## 6.2 Session Keys

Temporary keys used for conversations.

Purpose:

* Secure communication sessions
* Forward secrecy

---

## 6.3 Message Keys

Short-lived keys used for individual messages.

Purpose:

* Limit damage from compromise

---

## 6.4 Transport Keys

Keys used for communication channels.

Purpose:

* Protect individual transport sessions

---

# 7. Four-Ratchet Security Model

UMP introduces four independent key evolution systems.

```text
Identity Ratchet
        |
        v
Session Ratchet
        |
        v
Message Ratchet
        |
        v
Transport Ratchet
```

Each protects a different layer.

---

## 7.1 Identity Ratchet

Purpose:

Maintain long-term identity security.

Provides:

* Identity key rotation
* Device changes
* Recovery after identity events

---

## 7.2 Session Ratchet

Purpose:

Protect communication sessions.

Provides:

* New session keys
* Session recovery
* Forward secrecy

---

## 7.3 Message Ratchet

Purpose:

Protect individual messages.

Each message may use a different encryption key.

Benefits:

* Limits exposure
* Prevents large-scale message compromise

---

## 7.4 Transport Ratchet

Purpose:

Protect network transitions.

Example:

```text
Wi-Fi Session

      |
      v

Cellular Session

      |
      v

Mesh Session
```

Each transport receives independent key material.

---

# 8. Encryption Model

UMP separates:

```text
Encryption
+
Authentication
+
Key Management
```

Encryption protects:

* Message contents
* Files
* Metadata where possible

Authentication verifies:

* Sender identity
* Message integrity

---

# 9. Group Security

Groups require additional protections.

UMP groups support:

* Member management
* Secure membership changes
* Individual device verification
* Group key rotation

Example:

```text
Group

Alice
 |
Bob
 |
Charlie

Member removed

      |
      v

New group keys generated
```

---

# 10. File Security

Large files use the same security model as messages.

A 10 GB file is:

```text
File

 |
 v

Split into chunks

 |
 v

Encrypt each chunk

 |
 v

Transmit

 |
 v

Verify

 |
 v

Reassemble
```

Each chunk contains:

* Integrity information
* Encryption information
* Sequence information

---

# 11. Privacy Features

UMP may support:

## Metadata Minimization

Reducing exposure of:

* Sender information
* Recipient information
* Timing information

---

## Anonymous Transport Support

Optional transports may include:

* Tor
* I2P
* Privacy relays

---

## User-Controlled Identity

Users control:

* Identity keys
* Devices
* Verification status

---

# 12. Device Security

UMP implementations should support:

* Secure key storage
* Hardware security modules where available
* Encrypted local databases
* Device authentication

Examples:

* Secure Enclave
* Trusted Execution Environment
* Hardware security keys

---

# 13. Recovery

UMP supports recovery from:

## Lost Device

Actions:

* Revoke device
* Add replacement device
* Rotate keys

---

## Compromised Session

Actions:

* Reset session
* Establish new keys
* Continue communication

---

# 14. Security Limitations

UMP cannot protect against:

* A compromised unlocked device
* A user intentionally sharing messages
* Malware with complete device control
* Physical observation of the screen

Security depends on both:

* Protocol design
* Device security

---

# 15. Security Requirements

A compliant UMP implementation should provide:

Required:

* Strong encryption
* Identity verification
* Secure key storage
* Message authentication
* Secure session management

Recommended:

* Hardware-backed keys
* Metadata protection
* Anonymous transport support

---

# 16. Summary

UMP security is based on one principle:

```text
Trust the cryptography.
Do not trust the network.
```

The protocol provides:

* End-to-end encryption
* Identity protection
* Four-layer key evolution
* Secure file transfers
* Transport-independent security

Security follows the message wherever it travels.
