# UMP Capability Negotiation

## Version 1.0

---

# Purpose

Capability negotiation allows UMP devices to determine supported features before communication begins.

---

# Exchange Process

```text
Device A

   |
   | Capability Request
   v

Device B

   |
   | Capability Response
   v

Feature Selection
```

---

# Capability Data

Example:

```json
{
 "protocol":"UMP",
 "version":"1.0",
 "features":
 [
  "encryption",
  "groups",
  "files",
  "mesh"
 ]
}
```

---

# Feature Categories

## Messaging

```text
text
media
groups
reactions
```

---

## Security

```text
encryption
four-ratchet
identity-verification
```

---

## Transport

```text
sms
rcs
wifi
mesh
satellite
```

---

## File Transfer

```text
large-files
chunking
resume
```

---

# Compatibility Rules

If a feature is unsupported:

* Use the highest available capability
* Do not weaken security silently
* Notify the user when required

---

# Version Handling

Devices must negotiate:

* Protocol version
* Supported extensions
* Security capabilities
