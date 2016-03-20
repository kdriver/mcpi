from mcpi import block

def build_cottage(mc):
        x,y,z = mc.player.getPos();
        
        z=z+5
        mc.postToChat("Build a cottage")
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
        oak_plank=block.WOOD_PLANKS.id
        wool=block.WOOL.id
        yellow_wool=4
        ladder=block.LADDER.id

        width=6
        length=8
        height=2

        #  x=-127

        # build the walls
        mc.setBlocks(x,y,z,x+length,y+height,z,oak_plank)
        mc.setBlocks(x,y,z+width,x+length,y+height,z+width,oak_plank)
        mc.setBlocks(x,y,z,x,y+height,z+width,oak_plank)
        mc.setBlocks(x+length,y,z,x+length,y+height,z+width,oak_plank)

        # put a floor in
        mc.setBlocks(x,y+(height),z,x+length,y+(height),z+width,oak_plank)
        
        # put a hole in for the ladder
        mc.setBlocks(x+length-2,y+(height/2),z+width-1,x+length-1,y+(height/2),z+width-1,air)

        #put the roof on
        mc.setBlocks(x,y+height+1,z,x+length,y+height+1,z+width,wool,yellow_wool)
        mc.setBlocks(x,y+height+2,z+1,x+length,y+height+2,z+width-1,wool,yellow_wool)
        mc.setBlocks(x,y+height+3,z+2,x+length,y+height+3,z+width-2,wool,yellow_wool)
        mc.setBlocks(x,y+height+4,z+3,x+length,y+height+4,z+width-3,wool,yellow_wool)
        
##        mc.setBlocks(x,y+height+3,z+2,x+length-2,y+height+3,z+width,wool-2,yellow_wool)

        # put the door in
        mc.setBlocks(x+(length/2),y,z,x+(length/2),y+1,z,door)

        # put a torch downstairs
##        mc.setBlock(x+length-1,y+(height/5),z+width-3,torch)
        # put a torch downstairs
##        mc.setBlock(x+1,y+(height/5)-1,z+width-3,torch)

        # put the ladder in
        mc.setBlock(x+length-4,y,z+width-1,ladder)

         # put the windows in
        mc.setBlocks(x,y,z+(width/3),x,y+1,z+width-(width/3),glass)
        
       























