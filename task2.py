has_key = True
if has_key:
    outcome = "Click: You managed to find a key and use it to open the door."
    good = r"""jgs"""
else:
    outcome = "Doom: You can't find the key. You might be stuck here forever."
    bad = r"""bug"""
print(outcome)