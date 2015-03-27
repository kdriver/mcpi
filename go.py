from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

mc.postToChat("Hello Laura")
x=-119
y=12
z=61.4
mc.player.setPos(x,y,z)

x,y,z = mc.player.getPos();

z=z+5

air=block.AIR.id
stone=block.STONE.id
brick=block.BRICK_BLOCK.id
moss=block.MOSS_STONE.id
torch=block.TORCH.id
glowstone=block.GLOWSTONE_BLOCK.id
stair=block.STAIRS_WOOD.id
glass=block.GLASS.id
door=block.DOOR_WOOD.id
stoneslab=block.STONE_SLAB.id

width=8
length=15
height=6

x=-127

# build the walls
mc.setBlocks(x,y,z,x+length,y+height,z,brick)
mc.setBlocks(x,y,z+width,x+length,y+height,z+width,brick)
mc.setBlocks(x,y,z,x,y+height,z+width,brick)
mc.setBlocks(x+length,y,z,x+length,y+height,z+width,brick)
# put a floor in
mc.setBlocks(x,y+(height/2),z,x+length,y+(height/2),z+width,brick)
# put a hole in for the stairs
mc.setBlocks(x+length-2,y+(height/2),z+width-1,x+length-4,y+(height/2),z+width-1,air)
#put the roof on
mc.setBlocks(x,y+height+1,z,x+length,y+height+1,z+width,moss)
# put the door in
mc.setBlocks(x+(length/2),y,z,x+(length/2),y+1,z,door)
# put a torch downstairs
mc.setBlock(x+length-1,y+(height/2)-1,z+width-3,torch)
# put a torch downstairs
mc.setBlock(x+1,y+(height/2)-1,z+width-3,torch)

# put the stairs in
mc.setBlock(x+length-4,y,z+width-1,stair)
mc.setBlock(x+length-4+1,y+1,z+width-1,stair)
mc.setBlock(x+length-4+2,y+2,z+width-1,stair)

# put the windows in
mc.setBlocks(x,y+1,z+(width/3),x,y+2,z+width-(width/3),glass)

# put the glowstone under the stairs in
mc.setBlock(x+(length-1),y+2,z+(width-1),glowstone)
mc.setBlock(x+(length-1),y+1,z+(width-1),glowstone)
mc.setBlock(x+(length-2),y+1,z+(width-1),glowstone)
mc.setBlock(x+(length-1),y,z+(width-1),glowstone)
mc.setBlock(x+(length-2),y,z+(width-1),glowstone)
mc.setBlock(x+(length-3),y,z+(width-1),glowstone)

# put the trapdoors over the glowstone under the stairs
mc.setBlock(x+(length-1),y+2,z+(width-2),stoneslab)
mc.setBlock(x+(length-1),y+1,z+(width-2),stoneslab)
mc.setBlock(x+(length-2),y+1,z+(width-2),stoneslab)
mc.setBlock(x+(length-1),y,z+(width-2),stoneslab)
mc.setBlock(x+(length-2),y,z+(width-2),stoneslab)
mc.setBlock(x+(length-3),y,z+(width-2),stoneslab)

# put the window upstairs
mc.setBlocks(x,y+5,z+(width/3),x,y+6,z+width-(width/3),glass)

# put the window upstairs view
mc.setBlocks(x+length,y+5,z+(width/3),x+length,y+6,z+width-(width/3),glass)
























