drawbridge_raised = True
if not drawbridge_raised:
    outcome = "Thunder: You hear it thunder in the distance, the drawbridge currently being raised up."
    good = r"""lbm"""
else:
    outcome = "Doom: The thunder can be heard in the distance as the drawbridge is broken and damaged."
    bad = r"""bug"""
print(outcome)