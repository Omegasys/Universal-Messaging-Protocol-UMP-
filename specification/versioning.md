# UMP Versioning

## Version 1.0

---

# Purpose

Defines how UMP versions are managed.

---

# Version Format

UMP uses:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
1.0.0
```

---

# Major Version

Changes:

* Protocol structure
* Security model
* Breaking changes

Example:

```text
1.x.x → 2.x.x
```

---

# Minor Version

Adds:

* New features
* Optional improvements
* Extensions

Example:

```text
1.0.x → 1.1.x
```

---

# Patch Version

Contains:

* Bug fixes
* Security fixes
* Clarifications

Example:

```text
1.0.0 → 1.0.1
```

---

# Compatibility Rules

Implementations should:

* Support their current version
* Gracefully reject unsupported versions
* Preserve backward compatibility when possible

---

# Version Negotiation

Example:

```text
Device A

UMP 1.2

    |

Device B

UMP 1.0


Result:

Common Features
UMP 1.0 Compatibility
```

---

# Future Versions

Future versions may introduce:

* New encryption algorithms
* New transports
* New message types
* New security improvements
