# <img src="../assets/icons/shield-solid.png" width="30" /> Permissions System

<p>
  <img src="https://img.shields.io/badge/Security-Role_Based-orange" />
  <img src="https://img.shields.io/badge/Access-Controlled-blue" />
  <img src="https://img.shields.io/badge/Protection-Enabled-green" />
</p>

HostPilot uses a **role-based access control (RBAC)** system to restrict administrative commands to authorized users.

This ensures that only approved users can execute sensitive operations such as server management and infrastructure control.

---

# <img src="../assets/icons/server-solid.png" width="26" /> Allowed Role Configuration

Administrative commands are restricted to users assigned a specific Discord role.

This role is defined using the following environment variable:

```
ALLOWED_ROLE_ID=123456789012345678
```

Replace the value with the **Role ID** from your Discord server.

---

# <img src="../assets/icons/file-solid.png" width="26" /> How Permissions Work

The permission system follows this validation process:

1. A user executes a command in Discord
2. The bot checks the user's role list
3. The bot compares roles with `ALLOWED_ROLE_ID`
4. If the role matches → command executes
5. If the role does not match → access is denied

This ensures secure and controlled command execution.

---

# <img src="../assets/icons/gear-solid.png" width="26" /> How to Get Role ID in Discord

Follow these steps to retrieve your role ID:

1. Open **Discord Settings**
2. Go to **Advanced Settings**
3. Enable **Developer Mode**
4. Navigate to your server roles
5. Right-click the role
6. Click **Copy ID**

Paste the copied value into:

```
ALLOWED_ROLE_ID=your_role_id_here
```

---

# <img src="../assets/icons/shield-solid.png" width="26" /> Permission Notes

<p>
  <img src="https://img.shields.io/badge/Role-Required-red" />
  <img src="https://img.shields.io/badge/Access-Restricted-blue" />
</p>

Before starting the bot:

* Ensure the role exists in your Discord server
* Confirm the correct Role ID is used
* Verify assigned users have the required role
* Restart the bot after updating permissions

---

# <img src="../assets/icons/server-solid.png" width="26" /> Example Configuration

Below is an example `.env` entry:

```
ALLOWED_ROLE_ID=123456789012345678
```

This value must match an existing role ID in your Discord server.

---
