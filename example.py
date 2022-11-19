import scenario as sc
import player as plr

player = plr.Player("William", 1000)

doorA = sc.Scenario(player, "You have entered door A.")

doorB = sc.Scenario(player, "You have entered door B.", triggers=[lambda: print("This is a trigger")])

scenario1 = sc.Scenario(player, "there are 2 doors door A and door B", {'a': doorA, 'b': doorB})

scenario1.run()