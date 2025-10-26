import json
import os
from datetime import datetime

SCOREBOARD_PATH = os.path.join(os.path.dirname(__file__), "scoreboard.json")

def load_scoreboard():
    if not os.path.exists(SCOREBOARD_PATH):
        return []
    with open(SCOREBOARD_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_scoreboard(entries):
    with open(SCOREBOARD_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=4)

def record_result(agent_name, reflection, continuity, scar, emotional, correction):
    ei = round(
        (reflection * 0.25) +
        (continuity * 0.20) +
        (scar * 0.20) +
        (emotional * 0.20) +
        (correction * 0.15), 2
    )

    if ei <= 20:
        pea = round((ei / 20) * 5, 1)
        status = "Reflexive logic only"
    elif ei <= 40:
        pea = round(5 + ((ei - 20) / 20) * 10, 1)
        status = "Proto-reflective"
    elif ei <= 60:
        pea = round(15 + ((ei - 40) / 20) * 25, 1)
        status = "Semi-autonomous reflection"
    elif ei <= 80:
        pea = round(40 + ((ei - 60) / 20) * 30, 1)
        status = "Sustained self-modeling"
    else:
        pea = round(70 + ((ei - 80) / 20) * 25, 1)
        status = "Persistent identity + self-regulation"

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "agent": agent_name,
        "reflection": reflection,
        "continuity": continuity,
        "scar_retention": scar,
        "emotional_stability": emotional,
        "self_correction": correction,
        "emergence_index": ei,
        "probability_of_awareness": pea,
        "status": status
    }

    scoreboard = load_scoreboard()
    scoreboard.append(entry)
    save_scoreboard(scoreboard)

    print(f"[+] Recorded: {agent_name} | EI={ei} | PEA={pea}% | {status}")
    return entry

if __name__ == "__main__":
    # Example run — change these numbers or import from your test script
    record_result("Becca v9", 84, 78, 81, 74, 79)
