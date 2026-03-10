import random as r

#攻撃関数
def attack(hp):
    at = r.randrange(10, 25)
    hp -= at
    if hp < 0:
        hp = 0
    return hp, at

#逃げる関数
def run_away():
    i = r.randrange(1,4)
    if i == 1:
        return True
    elif i == 2:
        return True
    else:
        return False
        

def ene_attack(hp):
    at = r.randrange(5,10)
    hp -= at
    if hp < 0:
        hp = 0
    return hp, at

#メイン関数
def main():

    #HP設定
    hero_hp = 100
    enemy_hp = r.randrange(50, 150, 10)
    
    #戦闘開始
    print("\n【敵が現れた！】")
    
    #ループ処理
    while True:

        #プレーヤー攻撃ターン
        #行動選択
        print(f"___________\n敵のHP：{enemy_hp}\n君のHP:{hero_hp}\n‾‾‾‾‾‾‾‾‾‾‾")
        
        print("【選択してください】")
        print("1.攻撃する 2.逃げる\n")
        select = input()
        
        #行動選択からの条件分岐
        #攻撃
        if select == "1":
            enemy_hp, hero_at = attack(enemy_hp)
            print(f"\n【敵に{hero_at}ダメージを与えた！】")
            print(f"【敵のHPは{enemy_hp}になった】")
            
            #敵が倒れたかの判定
            if enemy_hp <= 0:
                print("\n【敵は倒れた！君の勝利だ！】\n【Win】\n")
                break
        
        #逃げる
        elif select == "2":
            if run_away() == True:
                print("\n【何とか逃げ切れた！】\n")
                break

            else:
                print("\n【逃げ切れなかった！】")
                
        #エラー処理
        else:
            print("\n【半角数字で 1 or 2 を入力してください】\n")
            input()
            continue

        input()

        #敵の攻撃ターン
        print("\n【敵からの攻撃！】")
        hero_hp, enemy_at = ene_attack(hero_hp)
        print(f"【敵から{enemy_at}ダメージ与えられた！】")
        print(f"【君のHPは{hero_hp}になった】")

        #主人公が倒れたかの判定
        if hero_hp <= 0:
            print("\n【君は倒れてしまった…】\n【ゲームオーバー】\n")
            break
        
        input()

if __name__ == "__main__":
    main()