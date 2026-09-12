# UMP Message Format

## Version 1.0

---

# Purpose

Defines the structure of UMP messages.

---

# Message Structure

A message contains:

```
HEADER
IDENTITY
SECURITY
PAYLOAD
METADATA
```

---

# Header

Example:

```json
{
 "version":"1.0",
 "id":"unique-id",
 "type":"TEXT",
 "timestamp":"UTC"
}
```

---

# Message Types

```
TEXT
MEDIA
FILE
GROUP
CONTROL
```

---

# Payload

Contains the actual content.

Examples:

Text:

```json
{
"type":"TEXT",
"content":"Hello"
}
```

File:

```json
{
"type":"FILE",
"name":"photo.jpg",
"size":"100MB"
}
```

---

# Metadata

Optional information:

* Reply information
* Reactions
* Delivery state
* Priority

---

# Security

Messages must be encrypted before transport.
