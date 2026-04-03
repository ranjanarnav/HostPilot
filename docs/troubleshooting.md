# <img src="../assets/icons/gear-solid.png" width="30" /> Troubleshooting Guide

<p>
  <img src="https://img.shields.io/badge/Support-Troubleshooting-orange" />
  <img src="https://img.shields.io/badge/Errors-Resolvable-blue" />
  <img src="https://img.shields.io/badge/Status-Maintained-green" />
</p>

This section lists common issues encountered while running **HostPilot** along with recommended solutions.

If problems occur, review the sections below and verify your configuration.

---

# <img src="../assets/icons/server-solid.png" width="26" /> Bot Not Starting

If the bot fails to start, verify the following:

* Python version is **3.9 or higher**
* `.env` file exists in the root directory
* All dependencies are installed correctly
* Required environment variables are defined
* No syntax errors exist in configuration files

### Recommended Checks

Run the following command to verify Python version:

```
python --version
```

Install dependencies again if necessary:

```
pip install -r requirements.txt
```

---

# <img src="../assets/icons/shield-solid.png" width="26" /> API Errors

API-related issues usually occur due to incorrect credentials or invalid URLs.

Verify the following:

* Pterodactyl API key is valid
* Panel URL is correct
* API permissions are enabled
* Internet connection is stable

### Recommended Checks

Confirm your `.env` file includes:

```
PTERO_PANEL_URL=https://your-panel-url
PTERO_API_KEY=your_api_key_here
```

Restart the bot after making changes.

---

# <img src="../assets/icons/file-solid.png" width="26" /> Permission Errors

Permission issues occur when the bot cannot validate user roles or lacks required access.

Verify the following:

* Role ID is correct
* Role exists in Discord server
* Bot has required permissions
* Users have the correct role assigned

### Recommended Checks

Confirm your `.env` configuration:

```
ALLOWED_ROLE_ID=123456789012345678
```

Ensure the role is properly assigned to authorized users.

---

# <img src="../assets/icons/server-solid.png" width="26" /> Logging and Debugging Tips

<p>
  <img src="https://img.shields.io/badge/Logs-Helpful-blue" />
  <img src="https://img.shields.io/badge/Debugging-Recommended-orange" />
</p>

If issues persist:

* Check terminal logs for error messages
* Verify configuration values
* Restart the bot after changes
* Reinstall dependencies if necessary
* Review recent changes to configuration files

Logs often provide useful information about connection failures or permission problems.

---

# <img src="../assets/icons/shield-solid.png" width="26" /> When to Seek Further Help

If the issue cannot be resolved:

* Review the Configuration Guide
* Check the Installation Guide
* Verify API credentials
* Inspect server logs

Most issues are caused by configuration errors or incorrect credentials.

---
