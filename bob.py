from mcpi import minecraft
from mcpi import block
from house import *
from cottage import *
from castle import *

mc = minecraft.Minecraft.create()

air=block.AIR.id
stone=block.STONE.id

mc.player.setPos(0,0,0)

 

mc.setBlocks(-127,0,-127,127,50,127,air)

mc.setBlocks(-127,-1,-127,127,-1,127,stone)

mc.postToChat("Bob The Fixer")
x=0
y=0
z=0
mc.player.setPos(0,0,0)

build_house(mc) 



mc.player.setPos(-25,0,0)
build_cottage(mc)

mc.player.setPos(-50,0,0)
build_castle(mc,-50,0,0)

