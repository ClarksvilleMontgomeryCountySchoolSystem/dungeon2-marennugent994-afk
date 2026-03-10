guard_awake = True
if not guard_awake:
    outcome = "Shadow: The appears to be sleeping. You sneak past them by acting as their shadow."
    good = r"""drx"""
else:
    outcome = "Doom: The guard catches you trying to sneak past them and quickly recaptures you."
    bad = r"""bug"""
print(outcome)
