"""
Задание 3 
"""


from __future__ import annotations

from typing import Any, Dict

from pymonad.tools import curry

"""
3.1. tag(tag_name, value) -> "<tag_name>value</tag_name>"
"""
@curry(2)
def tag(tag_name: str, value: str) -> str:
    return f"<{tag_name}>{value}</{tag_name}>"

bold = tag("b")
italic = tag("i")


"""
3.2. new_tag(tag_name, value, attr_dict) -> "<tag_name k="v">value</tag_name>"
"""

@curry(3)
def new_tag(tag_name: str, value: str, attr: Dict[str, Any]) -> str:
    if not attr:
        return f"<{tag_name}>{value}</{tag_name}>"
    attrs = " ".join(f'{k}="{v}"' for k, v in attr.items())
    return f"<{tag_name} {attrs}>{value}</{tag_name}>"




if __name__ == "__main__":
    print(tag("b", "string"))
    print(bold("string"))
    print(italic("string"))

    print(new_tag("li", "item 23", {}))
    print(new_tag("li", "item 23", {"class": "list-group"}))
    print(new_tag("li", "item 23", {"class": "list-group", "id": "item-23"}))
