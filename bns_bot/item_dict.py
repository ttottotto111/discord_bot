category = {
    "weapon" :"weapon",         # 무기
    "accessory" : "accessory",  # 악세
    "gem" : "equip-gem"         # 보패   
}

# 캐릭터 스탯창 링크
charlink = "https://bns.plaync.com/world/character/neo/501/욱"

# 무기
class Weapon:
    weapon = {
     "sword" : "sword",         # 검
     "gauntlet" : "gauntlet",   # 권갑
     "aura" : "aura-bangle",    # 기공패
     "axe" : "axe",             # 도끼
     "dagger" : "dagger",       # 소태도
     "staff":"staff",           # 지팡이
     "lyn" : "lyn-sword"        # 린검
    }
    rink = "https://api-goats.plaync.com/bnsneo/v2.0/dict/search/item?size=30&category1={category['weapon']}&category2={weapon[]}&locale=ko-KR"
    
# 악세
class Accessories:
    accessories = {
        "necklace" : "necklace", # 목걸이
        "ring" : "ring",         # 반지
        "earring" : "earring",   # 귀걸이
        "bracelet" : "bracelet", # 팔찌
        "belt" : "belt",         # 허리띠
        "gloves" : "gloves",     # 장갑
    }
    rink = "https://api-goats.plaync.com/bnsneo/v2.0/dict/search/item?size=30&category1={category['accessory']}&category2={accessories[]}&locale=ko-KR"

# 신비공패
class Rune:
    rune = {
        "rune1" : "rune-1", # 신공패
        "rune2" : "rune-2"  # 비공패
    }
    rink = "https://api-goats.plaync.com/bnsneo/v2.0/dict/search/item?size=30&category1={category['gem']}&category2={rune[]}&locale=ko-KR"

def test():
    w = Weapon()
    a = Accessories()
    r = Rune()
    print()