def respawn(self, world: VoxelWorld):
    # Xbox 360 demo / TU0 tutorial spawn (files=off — coords baked in code)
    # Stand on the gravel path just outside the incomplete shelter, facing south gate.
    self.x = float(XBOX_SPAWN_X)
    self.z = float(XBOX_SPAWN_Z)
    self.yaw = float(XBOX_SPAWN_YAW)   # face south (+Z)
    self.pitch = -0.12
    world.ensure_around(self.x, self.z)
    world.stamp_xbox_demo_spawn()
    sx, sz = int(math.floor(self.x)), int(math.floor(self.z))
    self.y = float(SEA_LEVEL + 3)
    for y in range(1, WORLD_Y - 3):
        if world.solid_at((sx, y, sz)) and not world.solid_at((sx, y + 1, sz)) \
                and not world.solid_at((sx, y + 2, sz)):
            # Prefer gravel path / grass pads (skip shelter roof planks)
            ground = world.get((sx, y, sz))
            if ground in (GRAVEL, GRASS, DIRT, COBBLESTONE, SAND):
                self.y = float(y + 1.05)
                break
    self.vy = 0.0
    self.flying = False
    self.hp = self.max_hp
    self.hurt_cd = 0.0
    self.fall_start = None
    self.riding = None

def hurt(self, amount: int):
    if self.hurt_cd > 0 or self.flying:
        return
    self.hp = max(0, self.hp - amount)
    self.hurt_cd = 0.6

def collides(self, world: VoxelWorld, px, py, pz) -> bool:
    min_x = int(math.floor(px - self.radius))
    max_x = int(math.floor(px + self.radius))
    min_y = int(math.floor(py))
    max_y = int(math.floor(py + self.height))
    min_z = int(math.floor(pz - self.radius))
    max_z = int(math.floor(pz + self.radius))
    for bx in range(min_x, max_x + 1):
        for by in range(min_y, max_y + 1):
            for bz in range(min_z, max_z + 1):
                if world.solid_at((bx, by, bz)):
                    return True
    return False
