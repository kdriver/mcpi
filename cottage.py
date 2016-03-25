from mcpi import block

def build_cottage(mc):
        x,y,z = mc.player.getPos();
        
        z=z+5
        
        mc.postToChat("fixed the cottage")
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
        orange_wool=1
        brown_wool=12
        ladder=block.LADDER.id
        bed=block.BED.id
        bookcase=block.BOOKSHELF.id
        painting=321
        furnace=62
        craft=block.CRAFTING_TABLE.id
        stonebrick=block.STONE_BRICK.id
        cobblestone=block.COBBLESTONE.id
        stoneslab_double=block.STONE_SLAB_DOUBLE.id
        ironblock=block.IRON_BLOCK.id
        irondoor=block.DOOR_IRON.id

        south=0
        west=1
        north=2
        east=3
        
        width=6
        length=8
        height=4
    

      

        # build the walls
        mc.setBlocks(x,y,z,x+length,y+height,z,oak_plank)
        mc.setBlocks(x,y,z+width,x+length,y+height,z+width,oak_plank)
        mc.setBlocks(x,y,z,x,y+height,z+width,oak_plank)
        mc.setBlocks(x+length,y,z,x+length,y+height,z+width,oak_plank)
        

        # put a floor in
        mc.setBlocks(x,y-1,z,x+length,y-1,z+width,oak_plank)
        
        # put a hole in for the ladder
        mc.setBlocks(x+length-2,y+2,z+width-2,x+length-2,y+2,z+width-2,air)

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
        mc.setBlocks(x+length-1,y+2,z+width-1,x+length-1,y+2,z+width-1,ladder)
        mc.setBlocks(x+length-1,y+1,z+width-1,x+length-1,y+1,z+width-1,ladder)
        mc.setBlocks(x+length-1,y,z+width-1,x+length-1,y,z+width-1,ladder)
        mc.setBlocks(x+length-1,y+3,z+width-1,x+length-1,y+3,z+width-1,ladder)
        mc.setBlocks(x+length-1,y+4,z+width-1,x+length-1,y+4,z+width-1,ladder)
        

        # put the windows in
        mc.setBlocks(x,y,z+(width/3),x,y+1,z+width-(width/3),glass)
        # put the second floor in
        mc.setBlocks(x,y+2,z,x+length,y+2,z+width,oak_plank)
        mc.setBlocks(x+length-1,y+2,z+width-1,x+length-1,y+2,z+width-1,air)


        # put bed in
        mc.setBlocks(x,y+3,z+3,x,y+3,bed)

        # put glowstone in right
        mc.setBlocks(x,y+3,z+1,x,y+3,z+1,glowstone)
        mc.setBlocks(x,y+4,z+1,x,y+4,z+1,glowstone)

        # put glowstone in left
        mc.setBlocks(x,y+3,z+5,x,y+3,z+5,glowstone)
        mc.setBlocks(x,y+4,z+5,x,y+4,z+5,glowstone)

        # put glowstone in right other
        mc.setBlocks(x+8,y+3,z+1,x+8,y+3,z+1,glowstone)
        mc.setBlocks(x+8,y+4,z+1,x+8,y+4,z+1,glowstone)

        # put glowstone in right other
        mc.setBlocks(x+8,y+3,z+5,x+8,y+3,z+5,glowstone)
        mc.setBlocks(x+8,y+4,z+5,x+8,y+4,z+5,glowstone)

        # put bookcases by the  side of the bed
        mc.setBlocks(x+1,y+3,z+2,x+1,y+3,z+2,bookcase)
        mc.setBlocks(x+1,y+3,z+4,x+1,y+3,z+4,bookcase)
        mc.setBlocks(x+1,y+4,z+2,x+1,y+4,z+2,bookcase)
        mc.setBlocks(x+1,y+4,z+4,x+1,y+4,z+4,bookcase)

        # put painting on the wall
        mc.setBlocks(x+3,y+4,z+1,x+3,y+4,z+1,painting,2)
        
        # put a furnace in
        mc.setBlocks(x+1,y,z+5,x+1,y,z+5,furnace,east)

        # put the stone blocks in as the counter tops
        mc.setBlocks(x+1,y,z+4,x+1,y,z+4,stoneslab_double)
        mc.setBlocks(x+1,y,z+2,x+1,y,z+2,stoneslab_double)

        # put a crafting table in
        mc.setBlocks(x+1,y,z+3,x+1,y,z+3,craft)

        # put a fridge in
        mc.setBlocks(x+1,y,z+1,x+1,y,z+1,ironblock)
        mc.setBlocks(x+1,y+1,z+1,x+1,y+1,z+1,ironblock)
        mc.setBlocks(x+2,y,z+1,x+2,y,z+1,door)
        mc.setBlocks(x+2,y+1,z+1,x+2,y+1,z+1,door)

        # put a sofa dowstairs
        mc.setBlocks(x+7,y,z+1,x+7,y,z+1,wool,orange_wool)
        mc.setBlocks(x+7,y,z+2,x+7,y,z+2,stoneslab)
        mc.setBlocks(x+7,y,z+3,x+7,y,z+3,stoneslab)
        mc.setBlocks(x+7,y,z+4,x+7,y,z+4,wool,orange_wool)




        
        return
       























