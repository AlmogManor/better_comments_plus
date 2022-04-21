"""
Author: Almog Manor
A script to generate templates for the "Better Comments" Extention

Usage:

prefix + modifiers (lowercase) + first letter of color (uppercase)
e.g:
.hbR this is a red highlighted and bold comment
"""

from itertools import combinations, permutations

PREFIX = "."

COLORS = [("Red", "#FF4242"),
          ("Orange", "#FFA73B"),
          ("Yellow", "#F9FF4A"),
          ("Green", "#6BFF4E"),
          ("Light blue", "#33EEFF"),
          ("Azure", "#3784FF"),
          ("Violet", "#A545FF"),
          ("Pink", "#FF55FF"),
          ("White", "#FFFFFC")]

"""
h - highlight
b - bold
s - strike-through
u - underline
i - italic
"""
MODIFIERS = ["h", "b", "s", "u", "i", ""]

HIGHLIGHT = ["transparent", "40"]

TEMPLATE = '{"tag": "_modifire",\
"color": "_color",\
"strikethrough": _strikethrough,\
"underline": _underline,\
"backgroundColor": "_highlight",\
"bold": _bold,\
"italic": _italic},'

#.hR test


def main():
    output = ''

    modifiers_ordered = []

    for i in range(1, len(MODIFIERS)):
        modifiers_ordered.extend(list(combinations(MODIFIERS, i)))

    modifiers_unordered = []
    for ordered in modifiers_ordered:
        modifiers_unordered.extend(permutations(ordered))

    for color in COLORS:
        for modifier in modifiers_unordered:
            # first letter of color name
            header = PREFIX + ''.join(modifier) + color[0][0]

            option = TEMPLATE
            option = option.replace("_modifire", header)
            option = option.replace("_color", color[1])
            option = option.replace(
                "_strikethrough", "true" if "s" in header else "false")
            option = option.replace(
                "_underline", "true" if "u" in header else "false")
            option = option.replace(
                "_highlight", color[1] + HIGHLIGHT[1] if "h" in header else HIGHLIGHT[0])
            option = option.replace(
                "_bold", "true" if "b" in header else "false")
            option = option.replace(
                "_italic", "true" if "i" in header else "false")

            output += option

    output = output[:-1]  # remove the last ","

    with open("./better_comments_template.txt", "w", encoding="ascii") as f:
        f.write(output)
    # paste this in:
    # F1 -> Preferences:Open Settings (JSON)
    #  "better-comments.tags": [ paste here ] (include the [])
    


if __name__ == "__main__":
    main()
