# UMP Identity Format

## Version 1.0

---

# Purpose

Defines how users and devices identify themselves.

---

# Identity Structure

```
USER IDENTITY

 |
 +-- Device 1
 |
 +-- Device 2
```

---

# Identity Contains

Required:

* Public identity key
* Identity ID
* Device list

Optional:

* Phone number
* Username
* Email address

---

# Example

```json
{
"id":"user123",
"devices":
[
"phone01",
"tablet01"
]
}
```

---

# Security

Phone numbers are addresses, not identities.

Cryptographic keys define identity.
