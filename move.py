from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

mc.postToChat("Hello Laura")

#mc.player.setPos(-127.7,12,77.0)

x=-119
y=12
z=61.4
mc.player.setPos(x,y,z)


x,y,z = mc.player.getPos();

mc.player.setPos(x,y,z)
