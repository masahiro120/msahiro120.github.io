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
    no = info.get("No", "")
    label = f"{name} [{rank} {no}]" if rank else name

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
        # return Node(label)

    # Nodeを作成
    node = Node(label)

    # 配合がある場合、再帰的に子ノードを追加
    for comp_key in ["配合1", "配合2", "配合3", "配合4"]:
        if info[comp_key]:
            child_node = build_tree(info[comp_key])
            child_node.parent = node

    return node

def extract_rank(node_name):
    """ノード名の末尾 [] からランクを抽出"""
    if "[" in node_name and "]" in node_name:
        return node_name.split("[")[-1].split("]")[0].strip()
    return None

if __name__ == "__main__":
    # target = input("モンスター名を入力してください: ")
    # target = "キラーパンサー"

    rank_order = {"SS": 1, "S": 2, "A": 3, "B": 4, "C": 5, "D": 6, "E": 7, "F": 8, None: 9}
    if func_type == "target":
        if target == "":
            print("モンスター名が入力されていません。")
        else:
            # 🔍 部分一致検索で対象モンスターをリストアップ
            matched_monsters = [name for name in monsters if target in name]

            if not matched_monsters:
                print(f"「{target}」を含むモンスターは見つかりませんでした。")
            else:
                all_required_leaves = set()

                for match in matched_monsters:
                    print(f"\n=== {match} の配合ツリー ===")

                    root_node = build_tree(match)
                    
                    for pre, fill, node in RenderTree(root_node):
                        print(f"{pre}{node.name}")

                    leaves = [node for node in root_node.descendants if not node.children]
                    for leaf in leaves:
                        all_required_leaves.add(leaf.name)

                # --- まとめて出力 ---
                leaves_sorted = sorted(
                    all_required_leaves,
                    key=lambda name: rank_order.get(extract_rank(name), 9)
                )

                print("\n【必要モンスター一覧（ランク順）】")
                for leaf_name in leaves_sorted:
                    print(f"・{leaf_name}")
    else:
        all_required_leaves = set()
        print("=== 全モンスターの配合ツリーを出力 ===")

        for name, info in monsters.items():
            if info["所持"] == "T":
                continue  # 所持済はスキップ

            print(f"\n=== {name} の配合ツリー ===")
            root_node = build_tree(name)

            for pre, fill, node in RenderTree(root_node):
                print(f"{pre}{node.name}")

            # 各モンスターの葉ノード（必要素材）を抽出して集合に追加
            leaves = [node for node in root_node.descendants if not node.children]
            for leaf in leaves:
                all_required_leaves.add(leaf.name)

        # --- まとめて出力 ---
        #print("\n\n【全モンスターに必要な素材一覧（重複除去・ランク順）】")

        # ランク順にソート
        #all_required_leaves_sorted = sorted(
            #all_required_leaves,
            #key=lambda name: rank_order.get(extract_rank(name), 9)
        #)

        #for leaf_name in all_required_leaves_sorted:
            #print(f"・{leaf_name}")

        # --- まとめて出力 ---
        print("\n\n【全モンスターに必要な素材一覧（重複除去・入手方法順）】")
        
        # 入手方法順にソート
        all_required_leaves_sorted = sorted(
            all_required_leaves,
            key=lambda name: monsters.get(
                name.split(" [")[0], {}  # "モンスター名 [ランク No]" → "モンスター名" に変換
            ).get("入手方法", "zzz")     # 入手方法が空なら末尾に回す
        )
        
        for leaf_name in all_required_leaves_sorted:
            print(f"・{leaf_name}")