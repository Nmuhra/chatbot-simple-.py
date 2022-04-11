import random

R_EATING = "ouch!, hide your heels at all time"
R_ADVICE = "If I were you, I would go exploit inside position and get my knee to elbow connection"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "So to .",
                "What does that mean?"][
        random.randrange(4)]
    return response
