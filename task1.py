torch_lit = True
if torch_lit:
    outcome = "Flicker: The atmosphere is dark and damp, luckily a lit up torch is nearby."
    good = r"""Zot"""
else:
    outcome = "Doom: The atmosphere is dark and damp, you can't seem to find anything."
    bad = r"""bug"""
print(outcome)