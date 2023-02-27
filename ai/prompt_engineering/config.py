PROMPT = (
    "Please generate a complete yoga session for someone with a {} skill level, lasting approximately "
    "{}. The session should include a warm-up, a series of poses, and a cool-down. The warm-up should "
    "consist of gentle stretches to prepare the body for the yoga practice. The series of poses should include a "
    "mix of standing, seated, and supine poses, and should be designed to improve flexibility, balance, "
    "and strength. Each pose should have a brief description, including its purpose, how to perform it "
    "correctly, and modifications for different skill levels. The cool-down should include deep stretching and "
    "relaxation to release any tension in the body and help the body return to its normal state. The poses "
    "should each flow into each other naturally. The session should be designed to help with {}"
)

SKILL_LEVELS = [
    ("novice", "Novice"),
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced"),
]

PROMPT_SKILL_LEVELS = [skill_level[0] for skill_level in SKILL_LEVELS]

PROMPT_DURATIONS = [
    "10 minutes",
    "15 minutes",
    "20 minutes",
    "25 minutes",
    "30 minutes",
    "45 minutes",
]
