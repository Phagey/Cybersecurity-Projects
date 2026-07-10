# Week 1 — Task 1A: Protocol Analysis & Traffic Capture

**Role:** Cybersecurity Intern, Cybervast
**Analyst:** Ayomikun Olutoye
**Focus:** Passive network traffic analysis in an isolated lab environment

This project documents Week 1 of my Cybersecurity Internship at Cybervast, where I conducted a passive network traffic analysis on an isolated lab environment to establish a "before hardening" security baseline. Using Wireshark and tcpdump, I captured and analyzed live traffic across a simulated enterprise network to identify protocol-level misconfigurations and security exposures before any remediation was applied.

---

## Situation

Assigned to baseline a private sandbox network prior to any security hardening. The lab environment consisted of:

| Node | Role | IP |
|---|---|---|
| pfSense | Gateway / DNS / DHCP | 192.168.1.1 |
| Kali Linux | Analyst workstation | 192.168.1.101 |
| Ubuntu 22.04 | Target host | 192.168.1.100 |

## Task

Capture live network traffic and analyze it in Wireshark to establish a "before hardening" security baseline and surface any protocol-level or configuration issues.

## Action

- Captured raw traffic natively using `tcpdump`:
- Loaded the capture into Wireshark for protocol dissection and TCP stream reconstruction
- Applied DNS and ICMP filters to trace a resolution failure
- Used **Follow TCP Stream** to reconstruct a plaintext administrative session

## Result — Key Findings

**1. Cleartext credential exposure (Critical)**
An unencrypted FTP/Telnet session exposed administrative login credentials in full ASCII plaintext, readable to any on-path observer via passive capture. Credentials have been redacted in this repo — see `screenshots/` for a sanitized version.

> **Remediation:** Disable FTP/Telnet, enforce SSH for remote access, enforce TLS 1.3 on management interfaces, block ports 21/23 at the firewall.

**2. DNS resolution failure → ICMP error storm (High)**
No DNS A record existed for the internal domain `cybervast.local`, causing repeated NXDOMAIN-equivalent responses and cascading ICMP "Port Unreachable" traffic.

> **Remediation:** Create a forward lookup zone on the pfSense resolver, add host A records, validate with `dig`.

**3. Operational note — filter syntax error**
Early in the analysis, an invalid Wireshark filter (`dnsSS`) was entered — a reminder that Wireshark filters are case-sensitive. Corrected to `dns`. Documented as a small process lesson, not a technical finding.

## Risk Summary

| Finding | Severity | Priority |
|---|---|---|
| Cleartext credential leakage | Critical | Immediate |
| Missing DNS zone | High | Short-term |
| ICMP error storm | Medium | Short-term |
| Filter syntax error | Low (operational) | Informational |

## Tools Used
`tcpdump` · `Wireshark` (display filters, Follow TCP Stream) · Oracle VirtualBox · pfSense

## Files in this folder
- `report.pdf` — full write-up (credentials redacted)
- `screenshots/` — Wireshark evidence (sensitive values blurred)

---
*Lab exercise conducted in an isolated, non-production sandbox as part of the Cybervast Cybersecurity Internship Programme.*


