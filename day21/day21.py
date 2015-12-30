import math
class Item(object):
    
    def __init__(self, name, cost, damage, armor):
        self.name   = name
        self.cost   = cost
        self.damage = damage
        self.armor  = armor

    def get_info(self):
        print(self.name, "\n cost: ", self.cost, " damage:", self.damage, " armor:", self.armor, "\n===\n") 

    def get_name(self):
        print(self.name)

class Weapon(Item):
    def __init__(self, name, cost, damage):
        super(Weapon,self).__init__(name,cost,damage,0)    


class Armor(Item):
    def __init__(self, name, cost, armor):
        super(Armor,self).__init__(name,cost,0,armor)  

class Ring(Item):
    def __init__(self,name,cost,armor):
        super(Ring, self).__init__(name,cost, damage, armor)


#            Weapons:
dagger     = Weapon("dagger",8,4)
shortsword = Weapon("shortsword",10,5)
warhammer  = Weapon("warhammer",25,6)
longsword  = Weapon("longsword",40,7)
greataxe   = Weapon("greataxe", 74,8)

#            Armor:
leather    = Armor("leather",13,1)
chainmail  = Armor("chainmail",31,2)
splintmail = Armor("splintmail",53,3)
bandedmail = Armor("bandedmail",75,4)
platemail  = Armor("platemail", 102,5)

#            Rings:
damage1    = Item("damage + 1", 25,1,0)
damage2    = Item("damage + 2", 50,2,0)
damage3    = Item("damage + 3",100,3,0)
defense1   = Item("defense + 1",20,0,1)
defense2   = Item("defense + 2",40,0,2)
defense3   = Item("defense + 3",80,0,3)





class Living(object):

    items = []

    def __init__(self, name, hp, damage, armor, goes_first):
        self.name       = name
        self.hp         = hp
        self.damage     = damage
        self.armor      = armor
        self.goes_first = goes_first
        self.attakable  = True
        self.shop = Shop()
    
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, val):
        if val <= 0:
            self.__damage = 1
        else:
            self.__damage = val  

    def get_info(self):
        print("***\n",self.name, "\n HP: ", self.hp, " damage:", self.damage, " armor:", self.armor, "\n---\n")
        print("*********** Inventory ***********")
        list(map(lambda x:x.get_info(), self.items))
        print("---------------------------------")

    def buy_item(self,item):
        if type(item) is Weapon:
            if(all(type(x) is not Weapon) for x in self.items):
                if self.shop.buy_weapon(item, 100000):
                    self.add_to_inventory(item)
                    

        elif type(item) is Armor:
            if(all(type(x) is not Armor) for x in self.items):
                if self.shop.buy_armor(item, 100000):
                    self.add_to_inventory(item)          

    def add_to_inventory(self, item):
        self.items.append(item)
        self.__damage += item.damage
        self.armor  += item.armor

    def take_damage(self, dmg):
        if self.attakable:
            self.hp -= abs((dmg - self.armor))

    def is_alive(self):
        return True if self.hp > 0 else False

    def attack(self, target):
        target.take_damage(self.damage)
        print("The", self.name, "deals ", self.damage, "-", target.armor, "=" , abs(self.damage-target.armor), "damage; the", target.name, "goes down to" , target.hp, "hit points")
        if not target.is_alive():
               target.attackable = False
               print(target.name, "has died")

class Shop(object):
    total_spent = 0
    weapons = [dagger,shortsword,warhammer,longsword,greataxe]
    armors  = [leather,chainmail,splintmail,bandedmail,platemail]
    rings   = [damage1,damage2,damage3,defense1,defense2,defense3]

    def buy_item(self, item, gold, inventory):
        if gold >= item.cost:
            self.remove_from_shop(inventory,item)
            self.total_spent += item.cost
            print(item.name,item.cost, "| total spent:", self.total_spent)
            return True
        else:
            return False
         
    def buy_weapon(self, weapon, gold):
        if weapon in self.weapons:
            return self.buy_item(weapon, gold, self.weapons) 
        return False
    
    def buy_armor(self,armor,gold):
        if armor in self.armors:
            return self.buy_item(armor, gold, self.armors)
        return False

    def remove_from_shop(self, inventory, item):
        inventory[:] = (value for value in inventory if value != item)



class Game(object):

    def __init__(self):     
        self.player = Living("Player", 8, 0, 0, True)
        self.player.buy_item(shortsword)
        self.player.buy_item(platemail)

        self.boss   = Living("Boss  ", 12, 7, 2, False)

    def play(self, show_moves):
        player_moves =  math.ceil(self.boss.hp / max(self.player.damage - self.boss.armor, 1))
        print("Player Moves: ", player_moves)

        boss_moves = math.ceil(self.player.hp / max(self.boss.damage - self.player.armor, 1))
        print("Boss Moves: ", boss_moves)

        total_moves = player_moves + boss_moves
        print("Total Moves:", abs(total_moves),"\n-========-")

        if show_moves:
            while(True):
                self.player.attack(self.boss)
                if not self.boss.is_alive():
                    break

                self.boss.attack(self.player)
                if not self.player.is_alive():
                    break


    def get_best_items(self):
        pass

    def get_cheapest_items(self):
        pass
   
    def get_possible_item_variants(self):
       # return self.factorial(len(self.player.shop.weapons))

       weapons = pow(len(self.player.shop.weapons),len(self.player.shop.weapons))
       armors  = pow(len(self.player.shop.armors), len(self.player.shop.armors))
       rings = len(self.player.shop.rings)
       print(len(self.player.shop.weapons),len(self.player.shop.armors), rings)
       


       return armors

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

game = Game()
game.play(True)

print(game.get_possible_item_variants())