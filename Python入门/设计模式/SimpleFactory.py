#------           英雄联盟，英雄商店          ----

#---- 英雄商店 ----
class ChampionStore(object):

    def __init__(self):
        self.champion_factory = ChampionFactory()

    def get_a_champion(self, champ_name):
        return self.champion_factory.get_champion(champ_name)


#---- 英雄工厂 ----
class ChampionFactory(object):
    def get_champion(self, champ_name):
        if champ_name == "无双剑姬":
            return Fiora()
        if champ_name == "盖伦":
            return Garen()
        if champ_name == "武器大师":
            return Jax()

#---- 英雄基类 ----
class Champion(object):
    def q(self):
        print("释放Q")
    def w(self):
        print("释放W")
    def e(self):
        print("释放E")
    def r(self):
        print("释放R")

# ---- 无双剑姬 ----
class Fiora(Champion):
    pass

#---- 盖伦 ----
class Garen(Champion):
    pass

#---- 武器大师 ----
class Jax(Champion):
    pass

store = ChampionStore()
jax = store.get_a_champion("武器大师")
jax.q()