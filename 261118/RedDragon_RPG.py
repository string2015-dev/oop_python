"""기획 미션: 신입 게임 개발자인 당신에게 소형 RPG의 전투 시스템 개발이 맡겨졌습니다.
 기획서를 읽고 상속(IS-A) 과 구성(HAS-A) 기반으로 클래스를 설계하세요"""
# 보조 도구들
class Level:
    def __init__(self, level=1, exp=0):
        self.level =level
        self.exp =exp

    def gain(self, amount):
        if self.exp + amount < self.need():
            self.exp+=amount
            return 0
        elif self.exp +amount >= self.need():
            lv_count =0
            res_exp = self.exp + amount - self.need()
            while res_exp >=0:
                """레벨 1 업 반영"""
                self.level += 1
                """최대 HP +20 반영"""
                # self. => 상위의 Character에서 정의하기.
                lv_count +=1
                res_exp -= self.need()
            self.exp = res_exp + self.need()
            return lv_count
        #체력 회복과 최대 HP 반영을 어떻게 하나! 그건 캐릭터로 가야하나?
    def need(self):
        return self.level*100


    
class Inventory:
    def __init__(self, capacity=5):
        self.items =[]
        self.capacity =capacity
    
    def add(self, item):
        if len(self.items)==self.capacity:
            return False
        else: 
            self.items.append(item)
            return True
        

    def take(self, name):
        get_item = None
        for c, i in enumerate(self.items):
            if name == i.name:
                get_item = self.items.pop(c)
                return get_item

        return get_item
        

class Hp:
    def __init__(self,  max_hp):
        self.current = max_hp
        self.max_hp = max_hp

    def damage(self, amount):
        if amount < 0:
            print('효과 없는 공격입니다.')

        if self.current - amount > 0:
            self.current -= amount
            return self.is_alive()
        else: 
            self.current -= amount
            return self.is_alive()

    def heal_full(self):
        self.current = self.max_hp

    def is_alive(self):
        return False if self.current <=0 else True
        
class Item:
    def __init__(self,name):
        self.name = name

class Weapon(Item):
    def __init__(self, name, power, element, enhance=0):
        super().__init__(name)
        self.power = power
        self.enhance = enhance
        self.element = Element(element)
    def upgrade(self):
        self.enhance +=1
        self.power +=5
        return True
    
    def __str__(self):
        return f"+{self.enhance} {self.name}[{self.element.name}]" if self.enhance !=0 else f"{self.name}[{self.element.name}]"

class Element:
    def __init__(self, name):
        self.name =name

    def multiplier(self, target):
        if self.name == target.name:
            return 1.0
        elif self.name =='불':
            if target.name =='물':
                return 0.5
            return 2.0
        elif self.name =='물':
            if target.name =='풀':
                return 0.5
            return 2.0
        elif self.name =='풀':
            if target.name =='불':
                return 0.5
            return 2.0

# 전체 개요===============================================
class GameObject:
    def __init__(self,name):
        self.name =name
# 캐릭터(게임오브젝트)
class Character(GameObject):
    def __init__(self,name,hp, weapon,level,inventory):
        super().__init__(name)
        self.hp =hp
        self.weapon =weapon
        self.level =level
        self.inventory = inventory

    def attack(self,target):
        self.target =target
        m = self.weapon.element.multiplier(target.element)
        amount = int(self.weapon.power*m)
        log =[]
        if target.hp.damage(amount):
            """아직 살아있음"""
            log.append(f"{self.name}의 {self.weapon.__str__()}공격! {target.name}에게 {amount} 피해 (x{m})")
            return log
        else:
            """죽음"""
            """경험치에 따른 레벨업 유무"""
            lv_c = self.level.gain(target.exp_reward)
            get_itme = target.drop

            """drop 아이템 없을때"""
            if target.drop is None:
                if lv_c != 0:
                    # 레벨업에 따른 체력 리셋
                    self.hp.max_hp += lv_c*20
                    self.hp.current = self.hp.max_hp
                    log.append(f"{self.name}의 {self.weapon.__str__()} 공격! {target.name}에게 {amount} 피해 (x{m})")
                    log.append(f"{target.name} 처치! EXP +{target.exp_reward}")
                    log.append(f"레벨 업! Lv.{self.level.level} (최대 HP {self.hp.max_hp})")
                    return log
                else: 
                    log.append(f"{self.name}의 {self.weapon.__str__()} 공격! {target.name}에게 {amount} 피해 (x{m})")
                    log.append(f"{target.name} 처치! EXP +{target.exp_reward}")
                    return log


            """drop 아이템 있을때 승리하고 레벨업"""
            """획득한 아이템 인벤토리에 넣기"""
            self.inventory.add(get_itme)
            
            if lv_c != 0:
                # 레벨업에 따른 체력 리셋
                self.hp.max_hp += lv_c*20
                self.hp.current = self.hp.max_hp
                log.append(f"{self.name}의 {self.weapon.__str__()} 공격! {target.name}에게 {amount} 피해 (x{m})")
                log.append(f"{target.name} 처치! EXP +{target.exp_reward}")
                log.append(f"레벨 업! Lv.{self.level.level} (최대 HP {self.hp.max_hp})")
                log.append(f"'{get_itme.name}' 획득!")
                return log
            else: 
                log.append(f"{self.name}의 {self.weapon.__str__()} 공격! {target.name}에게 {amount} 피해 (x{m})")
                log.append(f"{target.name} 처치! EXP +{target.exp_reward}")
                log.append(f"'{get_itme.name}' 획득!")
                return log
    
    def equip(self,name):
        item =self.inventory.take(name)
        if item :
            self.inventory.add(self.weapon)
            self.weapon = item
            return True
        return False

    def upgrade_weapon(self):
        stone = self.inventory.take('강화석')
        if stone :
            return self.weapon.upgrade()
        else: return False


# 직업 클래스(캐릭터)
class Warrior(Character):
        def __init__(self,name):
            hp =Hp(150)
            weapon =Weapon('화염검',30,'불')
            level =Level()
            inventory = Inventory()
            super().__init__(name, hp, weapon, level, inventory)
            
# 몬스터(게임오브젝트)
class Monster(GameObject):
    def __init__(self,name,hp,element, exp_reward,drop=None):
        super().__init__(name)
        self.hp =hp
        self.element =element
        self.drop =drop
        self.exp_reward = exp_reward

# 몬스터종(몬스터)
class Slime(Monster):
    def __init__(self,name ='슬라임'):
        
        hp =Hp(40)
        element =Element('풀')
        drop =Weapon('물의 창',25,'물')
        exp_reward = 60
        super().__init__(name,hp,element,exp_reward,drop)

    
class Golem(Monster):
    def __init__(self,name='골렘'):
        hp =Hp(120)
        element =Element('풀')
        drop =Item('강화석')
        exp_reward = 90
        super().__init__(name,hp,element,exp_reward,drop)

class Dragon(Monster):
    def __init__(self,name='The_RED_Dragon'):
        hp =Hp(300)
        element =Element('불')
        exp_reward = 500        
        super().__init__(name,hp,element,exp_reward)
        

# Element 확인 코드 ==================================================================================
print("Element 확인 코드 ====================================")
fire = Element("불")
print(fire.multiplier(Element("풀")), fire.multiplier(Element("물")), fire.multiplier(Element("불")))
# 레벨업 확인 코드
print("level 확인 코드 ====================================")
lv = Level()
print(lv.gain(150), lv.level, lv.exp)
print(lv.gain(500), lv.level, lv.exp)
# 최종 보스 레이드 =====================================================================================
print("최종 보스 레이드 ====================================")
hero = Warrior("아서")

# 1) 슬라임 사냥
for line in hero.attack(Slime()):
    print(line)
print([i.name for i in hero.inventory.items])
print("---")

# 2) 골렘 사냥 (쓰러질 때까지 공격)
golem = Golem()
while golem.hp.is_alive():
    for line in hero.attack(golem):
        print(line)
print("---")

# 3) 보스전 준비: 무기 교체 + 강화
print(hero.equip("물의 창"), hero.weapon, [i.name for i in hero.inventory.items])
print(hero.upgrade_weapon(), hero.weapon, hero.weapon.power)
print("---")

# 4) 보스전
boss = Dragon()
turn = 0
while boss.hp.is_alive():
    turn += 1
    hero.attack(boss)
print(f"{turn}턴 만에 보스 처치! Lv.{hero.level.level}, EXP {hero.level.exp}")