from mcpi import minecraft
from mcpi import block
from house import *
from cottage import *

mc = minecraft.Minecraft.create()

air=block.AIR.id
mc.player.setPos(0,0,0)

mc.setBlocks(-127,0,-127,127,50,127,air)

mc.postToChat("Bob The Builder")
x=0
y=0
z=0
mc.player.setPos(x,y,z)

build_house(mc) 



mc.player.setPos(x-25,y,z)
build_cottage(mc)





