import re
from datetime import datetime

# ✏️ UPDATE THESE MANUALLY whenever your stats change
USERNAME = "ayomiolutoye"
POINTS = 34
STREAK = 80
RANK = "[0x8] HACKER"
RANK_POSITION = 125862
TOP_PERCENT = "6%"

COMPLETED_ROOMS = [
    {"title": "How Websites Work", "url": "https://tryhackme.com/room/howwebsiteswork"},
    {"title": "Putting it all together", "url": "https://tryhackme.com/room/puttingitalltogether"},
    {"title": "DNS in Detail", "url": "https://tryhackme.com/room/dnsindetail"},
    {"title": "HTTP in Detail", "url": "https://tryhackme.com/room/httpindetail"},
    {"title": "What is Networking?", "url": "https://tryhackme.com/room/whatisnetworking"},
    {"title": "Intro to LAN", "url": "https://tryhackme.com/room/introtolan"},
    {"title": "OSI Model", "url": "https://tryhackme.com/room/osimodelzi"},
    {"title": "Packets & Frames", "url": "https://tryhackme.com/room/packetsframes"},
    {"title": "Extending Your Network", "url": "https://tryhackme.com/room/extendingyournetwork"},
    {"title": "Careers in Cyber", "url": "https://tryhackme.com/room/careersincyber"},
    {"title": "Virtualisation Basics", "url": "https://tryhackme.com/room/virtualisationbasics"},
    {"title": "Client-Server Basics", "url": "https://tryhackme.com/room/clientserverbasics"},
    {"title": "Inside a Computer System", "url": "https://tryhackme.com/room/insideacomputersystem"},
    {"title": "Offensive Security Intro", "url": "https://tryhackme.com/room/offensivesecurityintro"},
    {"title": "Computer Types", "url": "https://tryhackme.com/room/computertypes"},
    {"title": "Defensive Security Intro", "url": "https://tryhackme.com/room/defensivesecurityintro"},
    {"title": "Operating System Security", "url": "https://tryhackme.com/room/operatingsystemsecurity"},
    {"title": "Search Skills", "url": "https://tryhackme.com/room/searchskills"},
    {"title": "Operating Systems: Introduction", "url": "https://tryhackme.com/room/operatingsystemsintroduction"},
    {"title": "Linux CLI Basics", "url": "https://tryhackme.com/room/linuxclibasics"},
    {"title": "Data Representation", "url": "https://tryhackme.com/room/datarepresentation"},
    {"title": "Data Encoding", "url": "https://tryhackme.com/room/dataencoding"},
    {"title": "JavaScript: Simple Demo", "url": "https://tryhackme.com/room/javascriptsimpledemo"},
    {"title": "Python: Simple Demo", "url": "https://tryhackme.com/room/pythonsimpledemo"},
    {"title": "Windows Basics", "url": "https://tryhackme.com/room/windowsbasics"},
    {"title": "Cloud Computing Fundamentals", "url": "https://tryhackme.com/room/cloudcomputingfundamentals"},
    {"title": "Windows CLI Basics", "url": "https://tryhackme.com/room/windowsclibasics"},
    {"title": "The CIA Triad", "url": "https://tryhackme.com/room/theciatriad"},
    {"title": "Database SQL Basics", "url": "https://tryhackme.com/room/databasesqlbasics"},
    {"title": "Cryptography Concepts", "url": "https://tryhackme.com/room/cryptographyconcepts"},
    {"title": "Become a Hacker", "url": "https://tryhackme.com/room/becomeahacker"},
    {"title": "Become a Defender", "url": "https://tryhackme.com/room/becomeadefender"},
    {"title": "Linux Fundamentals Part 1", "url": "https://tryhackme.com/room/linuxfundamentalspart1"},
    {"title": "Linux Fundamentals Part 2", "url": "https://tryhackme.com/room/linuxfundamentalspart2"},
    {"title": "Linux Fundamentals Part 3", "url": "https://tryhackme.com/room/linuxfundamentalspart3"},
    {"title": "Windows Fundamentals 1", "url": "https://tryhackme.com/room/windowsfundamentals1xbx"},
    {"title": "Windows Fundamentals 2", "url": "https://tryhackme.com/room/windowsfundamentals2x0x"},
    {"title": "Windows Fundamentals 3", "url": "https://tryhackme.com/room/windowsfundamentals3xzx"},
    {"title": "Wireshark: The Basics", "url": "https://tryhackme.com/room/wiresharkthebasics"},
    {"title": "Active Directory Basics", "url": "https://tryhackme.com/room/winadbasics"},
    {"title": "Windows Command Line", "url": "https://tryhackme.com/room/windowscommandline"},
    {"title": "Networking Concepts", "url": "https://tryhackme.com/room/networkingconcepts"},
    {"title": "Networking Essentials", "url": "https://tryhackme.com/room/networkingessentials"},
    {"title": "Networking Core Protocols", "url": "https://tryhackme.com/room/networkingcoreprotocols"},
    {"title": "Networking Secure Protocols", "url": "https://tryhackme.com/room/networkingsecureprotocols"},
    {"title": "Windows PowerShell", "url": "https://tryhackme.com/room/windowspowershell"},
    {"title": "Linux Shells", "url": "https://tryhackme.com/room/linuxshells"},
    {"title": "Blue", "url": "https://tryhackme.com/room/blue"},
    {"title": "John the Ripper: The Basics", "url": "https://tryhackme.com/room/johntheripper0"},
    {"title": "Metasploit: Exploitation", "url": "https://tryhackme.com/room/metasploitexploitation"},
    {"title": "Metasploit: Introduction", "url": "https://tryhackme.com/room/metasploitintro"},
    {"title": "Metasploit: Meterpreter", "url": "https://tryhackme.com/room/meterpreter"},
    {"title": "Moniker Link (CVE-2024-21413)", "url": "https://tryhackme.com/room/monikerlink"},
    {"title": "Nmap: The Basics", "url": "https://tryhackme.com/room/nmap01"},
    {"title": "Tcpdump: The Basics", "url": "https://tryhackme.com/room/tcpdump"},
    {"title": "Public Key Cryptography Basics", "url": "https://tryhackme.com/room/publickeycryptography"},
    {"title": "Cryptography Basics", "url": "https://tryhackme.com/room/cryptographybasics"},
    {"title": "Hashing Basics", "url": "https://tryhackme.com/room/hashingbasics"},
    {"title": "JavaScript Essentials", "url": "https://tryhackme.com/room/javascriptessentials"},
    {"title": "Web Application Basics", "url": "https://tryhackme.com/room/webapplicationbasics"},
    {"title": "SQL Fundamentals", "url": "https://tryhackme.com/room/sqlfundamentals"},
]

BADGES = [
    "🎳 First Four — Completing four rooms in your first week",
    "🔥 3 Day Streak — Achieving a 3 day hacking streak",
    "🌐 Networking Nerd — Completing the Network Fundamentals module",
    "🔥 7 Day Streak — Achieving a 7 day hacking streak",
    "🕸️ Webbed — Understands how the world wide web works",
    "💻 World Wide Web — Completing the How The Web Works module",
    "🐧 cat linux.txt — Being competent in Linux",
    "🔥 30 Day Streak — Hacking for 30 days solid",
    "📦 Session Held — Completing 4 weekly missions in a row (Rare: 1.9%)",
    "🥇 Platinum League — Platinum League 1st place (Epic: 0.9%)",
    "🛡️ Metasploitable — Contains the knowledge to use Metasploit (Rare: 9.6%)",
    "🪟 Blue — Hacking into Windows via EternalBlue",
]

SKILLS = [
    "Networking", "Linux", "Windows", "Active Directory",
    "Web Application Security", "Cryptography", "SQL",
    "Nmap", "Metasploit", "Wireshark", "Tcpdump",
    "PowerShell", "Python", "JavaScript", "Cloud Computing",
    "Offensive Security", "Defensive Security"
]


def build_readme_section():
    rooms_md = "\n".join(
        [f"- [{r['title']}]({r['url']})" for r in COMPLETED_ROOMS]
    )
    badges_md = "\n".join([f"- {b}" for b in BADGES]) or "_Visit your profile → Badges tab to see all 12 badges!_"
    skills_md = ", ".join(SKILLS)
    last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    section = f"""<!-- THM-STATS:START -->
## 🛡️ TryHackMe Progress

| Stat | Value |
|------|-------|
| 👤 Username | [{USERNAME}](https://tryhackme.com/p/{USERNAME}) |
| 🏆 Rank | {RANK} (#{RANK_POSITION} — Top {TOP_PERCENT}) |
| 💰 Points | {POINTS} |
| 🔥 Current Streak | {STREAK} days |
| ✅ Rooms Completed | {len(COMPLETED_ROOMS)} |
| 🎖️ Badges Earned | {len(BADGES) or 12} |

### 🧠 Skills Gained
{skills_md}

### 🎖️ Badges
{badges_md}

### 📚 Completed Rooms ({len(COMPLETED_ROOMS)})
{rooms_md}

> _Last updated: {last_updated}_
<!-- THM-STATS:END -->"""

    return section


def update_readme(section, readme_path="README.md"):
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = "# My CyberSecurity Journey\n\n"

    pattern = r"<!-- THM-STATS:START -->.*?<!-- THM-STATS:END -->"
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, section, content, flags=re.DOTALL)
    else:
        content += f"\n\n{section}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md updated successfully.")


if __name__ == "__main__":
    section = build_readme_section()
    update_readme(section)
