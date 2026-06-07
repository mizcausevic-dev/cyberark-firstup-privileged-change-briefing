signals = [
    {"lane": "CyberArk + FirstUp evidence coverage", "risk": 72, "savings": 21, "investment": 61},
    {"lane": "communication and access exception closure", "risk": 66, "savings": 18, "investment": 57},
]

def rank(rows):
    return sorted(rows, key=lambda row: row["risk"] * 0.5 + row["savings"] * 0.2 + row["investment"] * 0.3, reverse=True)

if __name__ == "__main__":
    for row in rank(signals):
        print("cyberark-firstup-privileged-change-briefing | " + row["lane"])
