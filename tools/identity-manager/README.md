# UMP Identity Manager

Command-line utility for managing UMP identities and devices.

## Features

- Create identities
- Display identities
- Add devices
- List devices
- Revoke devices
- Revoke identities

## Usage

```text
python identity.py create <identity-id> <public-key>
python identity.py show <identity-id>

python device.py add <identity-id> <device-id> <device-key>
python device.py list <identity-id>

python revoke.py device <identity-id> <device-id>
python revoke.py identity <identity-id>
Security

This tool is intended for development and administration.

Private cryptographic keys should never be stored in source code,
command history, or a Git repository.
