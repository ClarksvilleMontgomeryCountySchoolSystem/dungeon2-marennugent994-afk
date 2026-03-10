escaped = True
if escaped:
    outcome = "Legend: You see the light for what felt like ages. People tell your story as being the first one to ever escape the dungeon."
    good = r"""ldb"""
else:
    outcome = "Doom: You remain inside the dungeon, the corridors and walls appear to be endless as you go mad."
    bad = r"""bug"""
print(outcome)