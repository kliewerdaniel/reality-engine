# Permission Model

**Reality Engine — Permission Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the permission model of Reality Engine. It covers the authorized actors and the permissions.

---

## 1. Permission Model Overview

The permission model defines who can do what in the system.

---

## 2. Authorized Actors

| Actor | Description |
|---|---|
| SYSTEM | The system itself |
| AGENT | A valid agent |
| USER | A user |

---

## 3. Permissions

| Permission | Description |
|---|---|
| READ | Read authorized information |
| WRITE | Write to the world model |
| DELETE | Delete audit records |
| OVERRIDE | Override validation |
| GRANT | Grant themselves permissions |

---

## 4. Constraint

1. **The system must not grant itself permissions.**
2. **The system must not directly change accepted world state.**
