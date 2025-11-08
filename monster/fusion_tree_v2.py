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

csv_file_list = [
    "./monsters_list/F_rank.csv",
    "./monsters_list/E_rank.csv",
    "./monsters_list/D_rank.csv",
    "./monsters_list/C_rank.csv",
    "./monsters_list/B_rank.csv",
    "./monsters_list/A_rank.csv",
    "./monsters_list/S_rank.csv",
    "./monsters_list/SS_rank.csv",
]


# monsters = load_monsters_from_csv("monsters.csv")

monsters = {}
for csv_file in csv_file_list:
    # 読み込んだファイルにランク情報を追加
    rank = csv_file.split("/")[-1].split("_")[0]  # ファイル名からランクを取得
    temp_monsters = load_monsters_from_csv(csv_file)
    for name, info in temp_monsters.items():
        info["ランク"] = rank  # ランク情報を追加
    monsters.update(temp_monsters)

print(f"Loaded {len(monsters)} monsters.")

def build_tree(name):
    """モンスター名からanytreeのNodeを作る再帰関数"""
    if name not in monsters:
        return Node(f"{name}（データなし）")
    
    info = monsters[name]

    # モンスター名 + ランク
    rank = info.get("ランク", "")
    label = f"{name} [{rank}]" if rank else name

    # 入手方法・所持・他国などの情報をラベルに追加
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
    target = input("モンスター名を入力してください: ")
    # target = "キラーパンサー"
    # print()
    # print_tree(target)

    root_node = build_tree(target)
    
    for pre, fill, node in RenderTree(root_node):
        print(f"{pre}{node.name}")