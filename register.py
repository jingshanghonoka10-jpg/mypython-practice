#簡易的レジスターのプログラム作成

#メニューの作成
menu = {"コーヒー":400,"紅茶":450,"チョコレート":300,"クッキー":250,"ドーナツ":350}

#注文
print("こんにちは！注文したいメニューを選んでください")
orders = []
while True:
    order = input()
    if order in menu:
        orders.append(order)
    else:
        print('その商品はありません')
        continue
    
    print("まだ選びますか？ーはい or いいえ")
    ans = input()
    if ans == "いいえ":
        break
    elif ans == "はい":
        print('商品を選んでください')
        True
    else:
        print("yesかnoを入力してください")

#合計金額計算
sum = 0
for i in range(len(orders)):
    sum = sum + menu[orders[i]]

#おつり計算
print(f'合計金額は{sum}円です')
print('お支払金額を入力してください')
while True:
    pay = int(input())
    if pay < sum:
        print(f'支払額が{sum-pay}不足しています。もう一度入力してください')
        True
    elif pay >= sum:
        print(f'おつりは{pay-sum}円です。ありがとうございました。')
        break
    else:
        print('数字でお支払い金額を入力してください')
        True
