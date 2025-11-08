# -*- coding: utf-8 -*-
import csv
from anytree import Node, RenderTree

def load_monsters_from_csv(filename):
    monsters = {}
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["モンスター名"]
            monsters[name] = {
                "No": row["No"] if row["No"] else None,
                "他国": row["他国"] if row["他国"] else None,
                "所持": row["所持"] if row["所持"] else None,
                "入手方法": row["入手方法"] if row["入手方法"] else None,
                "配合1": row["配合1"] if row["配合1"] else None,
                "配合2": row["配合2"] if row["配合2"] else None,
                "配合3": row["配合3"] if row["配合3"] else None,
                "配合4": row["配合4"] if row["配合4"] else None,
            }
    return monsters

# csv_file_list = [
#     "./monsters_list/F_rank.csv",
#     "./monsters_list/E_rank.csv",
#     "./monsters_list/D_rank.csv",
#     "./monsters_list/C_rank.csv",
#     "./monsters_list/B_rank.csv",
#     "./monsters_list/A_rank.csv",
#     "./monsters_list/S_rank.csv",
#     "./monsters_list/SS_rank.csv",
# ]

csv_file_list = [
    "F_rank.csv",
    "E_rank.csv",
    "D_rank.csv",
    "C_rank.csv",
    "B_rank.csv",
    "A_rank.csv",
    "S_rank.csv",
    "SS_rank.csv",
]


# monsters = load_monsters_from_csv("monsters.csv")

monsters = {}
for csv_file in csv_file_list:
    monsters.update(load_monsters_from_csv(csv_file))

print(f"Loaded {len(monsters)} monsters.")


def print_tree(name, prefix="", first_call=True, last_monster=True):
    """モンスターの配合経路を枝付きで右方向に展開"""
    if name not in monsters:
        print(prefix + name + "（データなし）")
        return

    info = monsters[name]

    # 入手方法があるなら表示して終了
    if info["入手方法"]:
        if info["所持"] == "T":
            print(f"{name} ── {info['入手方法']}（所持済）")
        else:
            print(f"{name} ── {info['入手方法']}")
        return
    if info["他国"] == "入手可":
        if info["所持"] == "T":
            print(f"{name} ── 他国（所持済）")
        else:
            print(f"{name} ── 他国")
        return
    if info["所持"] == "T":
        print(f"{name} ── 所持済")
        return
    
    # next_prefix = prefix + "　" * (len(name) + 2)
    if first_call:
        next_prefix = prefix + " " * (len(name) * 2)
    else:
        if last_monster:
            next_prefix = prefix + "    " + " " * (len(name) * 2)
        else:
            next_prefix = prefix + " │  " + " " * (len(name) * 2)
    # print(f"len(name): {len(name)}, prefix: '{prefix}', next_prefix: '{next_prefix}'")

    print(name, end="")
    if info["配合1"]:
        line = f" ┬─ "
        print(line, end="")
        print_tree(info["配合1"], next_prefix, first_call=False, last_monster=False)
    if info["配合2"]:
        line = f" └─ " if not info["配合4"] else f" ├─ "
        print(next_prefix + line, end="")
        if not info["配合4"]:
            print_tree(info["配合2"], next_prefix, first_call=False, last_monster=True)
        else:
            print_tree(info["配合2"], next_prefix, first_call=False, last_monster=False)
    if info["配合3"]:
        line = f" ├─ "
        print(next_prefix + line, end="")
        print_tree(info["配合3"], next_prefix, first_call=False, last_monster=False)
    if info["配合4"]:
        line = f" └─ "
        print(next_prefix + line, end="")
        print_tree(info["配合4"], next_prefix, first_call=False, last_monster=True)


def build_tree(name):
    """モンスター名からanytreeのNodeを作る再帰関数"""
    if name not in monsters:
        return Node(f"{name}（データなし）")
    
    info = monsters[name]

    # 入手方法・所持・他国などの情報をノード名に追加
    label = name
    if info["入手方法"]:
        if info["所持"] == "T":
            label += f" ── {info['入手方法']}（所持済）"
        else:
            label += f" ── {info['入手方法']}"
        return Node(label)
    if info["所持"] == "T":
        label += " ── 所持済"
        return Node(label)
    if info["他国"] == "入手可":
        label += " ── 他国"
        return Node(label)

    # Nodeを作成
    node = Node(label)

    # 配合がある場合、再帰的に子ノードを追加
    for comp_key in ["配合1", "配合2", "配合3", "配合4"]:
        if info[comp_key]:
            child_node = build_tree(info[comp_key])
            child_node.parent = node

    return node

# 実行例
if __name__ == "__main__":
    # target = input("モンスター名を入力してください: ")
    # target = "キラーパンサー"
    # print()
    # print_tree(target)

    root_node = build_tree(target)
    
    for pre, fill, node in RenderTree(root_node):
        print(f"{pre}{node.name}")