from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

mc.postToChat("Hello Laura")

mc.player.setPos(0,0,0)

#x,y,z = mc.player.getPos();

x= -127
y= -127
z= -80
air=block.AIR.id
stone=block.STONE.id
grass=block.GRASS.id

mc.setBlocks(-127,0,-127,127,50,127,air)


