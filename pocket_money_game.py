#お小遣い計算ゲーム
import random as r

#お菓子の種類と金額
snaks = {"アメ":200,"グミ":200,"チョコレート":200,"クッキー":250,"ドーナツ":350}

#お小遣い設定
mony = r.randrange(500,1000)

print(f"\nお母さんから{mony}円お小遣いをもらった！超えないようにお菓子を選ぼう！\n")
print(snaks)

print("買いたいお菓子を選んでください")
orders = []
while True:
    order = input()
    if order in snaks:
        orders.append(order)
    else:
        print('その商品はありません')
        continue
    
    print("まだ選びますか？(半角英字で入力) - はい or いいえ")
    ans = input()
    if ans == "いいえ":
        break
    elif ans == "はい":
        print('商品を選んでください')
        True
    else:
        print("半角英字で「はい」か「いいえ」を入力してください")

# 合計金額計算
total = 0

# 買ったものリスト(orders)から、お菓子の名前(item)を1つずつ取り出す
for item in orders:
    # メニュー表(snaks)から、そのお菓子の値段を調べて total に足す
    total = total + snaks[item]

print(f"【買ったもの】{orders}")
print(f"【合計金額】{total}")

#条件判定（結果発表）
if total <= mony:
    print("上手にお買い物できたね！\n")
else:
    print(f"{total-mony}円超えている！買いすぎです！すべて没収！\n")
