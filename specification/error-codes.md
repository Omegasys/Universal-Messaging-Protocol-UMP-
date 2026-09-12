# UMP Error Codes

## Version 1.0

---

# Purpose

Defines standard errors returned by UMP implementations.

---

# Error Format

Example:

```json
{
 "error":"E100",
 "message":"Invalid packet"
}
```

---

# General Errors

| Code | Meaning             |
| ---- | ------------------- |
| E001 | Unknown error       |
| E002 | Invalid request     |
| E003 | Unsupported feature |
| E004 | Invalid version     |

---

# Message Errors

| Code | Meaning           |
| ---- | ----------------- |
| M100 | Invalid message   |
| M101 | Message corrupted |
| M102 | Message expired   |
| M103 | Delivery failed   |

---

# Security Errors

| Code | Meaning               |
| ---- | --------------------- |
| S100 | Authentication failed |
| S101 | Invalid signature     |
| S102 | Key mismatch          |
| S103 | Encryption failure    |

---

# File Errors

| Code | Meaning              |
| ---- | -------------------- |
| F100 | File too large       |
| F101 | Invalid chunk        |
| F102 | Hash mismatch        |
| F103 | Transfer interrupted |

---

# Transport Errors

| Code | Meaning               |
| ---- | --------------------- |
| T100 | Transport unavailable |
| T101 | Connection failed     |
| T102 | Routing failure       |

---

# Recovery

Implementations should:

* Retry when possible
* Select alternative transports
* Preserve user data
