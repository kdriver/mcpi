from mcpi import minecraft
from mcpi import block
from house import *

mc = minecraft.Minecraft.create()

mc.postToChat("Bob the builder")
x=0
y=0
z=0
mc.player.setPos(x,y,z)

build_house(mc) 



mc.player.setPos(x-25,y,z)
build_house(mc) 



