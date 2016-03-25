from mcpi import block

def build_castle(mc,x,y,z):
        
        
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
        
        width=20
        length=20
        height=6
    

      

        # build the walls
        mc.setBlocks(x,y,z,x+length,y+height,z,cobblestone)
        mc.setBlocks(x,y,z+width,x+length,y+height,z+width,cobblestone)
        mc.setBlocks(x,y,z,x,y+height,z+width,cobblestone)
        mc.setBlocks(x+length,y,z,x+length,y+height,z+width,cobblestone)

        # build the inner walls
        mc.setBlocks(x+4,y,z+4,x+length-4,y,z+width-4,cobblestone)
        

        # put a floor in
        mc.setBlocks(x,y-1,z,x+length,y-1,z+width,cobblestone)

        #put the roof on
        mc.setBlocks(x,y+height+1,z,x+length,y+height+1,z+width,wool,cobblestone)

        # put the door in
        mc.setBlocks(x+(length/2),y,z,x+(length/2),y+1,z,door)

        # put a torch downstairs
##        mc.setBlock(x+length-1,y+(height/5),z+width-3,torch)
        # put a torch downstairs
##        mc.setBlock(x+1,y+(height/5)-1,z+width-3,torch)

        # put the turrests on the roof
##        mc.setBlocks(x


        
        return
       























