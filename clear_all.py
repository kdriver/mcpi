from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

mc.postToChat("Hello Laura")

#mc.player.setPos(-127.7,12,77.0)

#x,y,z = mc.player.getPos();

x=-127
y=12
z=61.4
air=block.AIR.id
stone=block.STONE.id

mc.setBlocks(x,y,z,x+20,y+10,z+15,air)


