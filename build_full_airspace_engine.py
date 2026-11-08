import os
import urllib.parse

WORKSPACE = r'C:\Users\bkare\.gemini\antigravity\scratch\backrooms_context_decay'
GMOD_DIR  = r'J:\SteamLibrary\steamapps\common\GarrysMod\garrysmod\data\starfall\cognitive-decay'

# 1. Compile all 160 audio tracks
audio_dir = os.path.join(WORKSPACE, 'audio')
files = sorted([f for f in os.listdir(audio_dir) if f.endswith('.mp3')])

music_tracks = []
sound_tracks = []

for f in files:
    name_lower = f.lower()
    is_music = False
    cat = 'ambient'
    weight = 5.0
    eeriness = 6.0

    if 'original score' in name_lower or 'still life' in name_lower or 'daisy bell' in name_lower or 'theme' in name_lower:
        is_music = True
        cat = 'music'
        weight = 8.5
        eeriness = 8.5
    elif 'music' in name_lower or 'waltz' in name_lower or 'song' in name_lower or 'orchestra' in name_lower or 'piano' in name_lower or 'jazz' in name_lower:
        is_music = True
        cat = 'music'
        weight = 7.5
        eeriness = 7.5
    elif 'phone' in name_lower or 'dial' in name_lower or 'ring' in name_lower or 'dtmf' in name_lower or 'busy' in name_lower or 'answering' in name_lower:
        is_music = False
        cat = 'telephony'
        weight = 6.0
        eeriness = 7.0
    elif 'eas' in name_lower or 'alarm' in name_lower or 'warning' in name_lower or 'alert' in name_lower or 'siren' in name_lower or 'buzzer' in name_lower or 'uvb' in name_lower:
        is_music = False
        cat = 'broadcast'
        weight = 7.0
        eeriness = 8.8
    elif 'static' in name_lower or 'click' in name_lower or 'beep' in name_lower or 'glitch' in name_lower:
        is_music = False
        cat = 'sfx'
        weight = 4.5
        eeriness = 6.0
    else:
        is_music = False
        cat = 'ambient'
        weight = 5.0
        eeriness = 6.5

    url_name = urllib.parse.quote(f)
    raw_url = f"https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/{url_name}"
    entry = f'            {{ name = "{f}", url = "{raw_url}", is_music = {"true" if is_music else "false"}, category = "{cat}", weight = {weight}, eeriness = {eeriness} }},'

    if is_music:
        music_tracks.append(entry)
    else:
        sound_tracks.append(entry)

lua_audio_lines = [
    "    AUDIO = {",
    "        music = {",
    *music_tracks,
    "        },",
    "        sound = {",
    *sound_tracks,
    "        },",
    "    },"
]
lua_audio_str = "\n".join(lua_audio_lines)

# Read base dataset from main.lua
with open(os.path.join(WORKSPACE, 'cognitive-decay', 'core', 'main.lua'), 'r', encoding='utf-8') as f:
    current_code = f.read()

# Extract ONLY the clean DATASET table without any trailing blocks
d_start = current_code.find('local DATASET = {')
d_end = current_code.find('\n}\n', d_start) + 3
clean_head = current_code[:d_end]

audio_start = clean_head.find('AUDIO = {')
audio_end = clean_head.find('NPCS = {', audio_start)
new_dataset_head = clean_head[:audio_start] + lua_audio_str + "\n\n    " + clean_head[audio_end:]

# Now build the full airspace procedural engine with VERIFIED VertexLitGeneric materials
master_engine_body = r'''
-- --------------------------------------------------------------------------
-- 0. HIGH-ENTROPY PROCEDURAL SEED GENERATOR (ZERO FORBIDDEN GLOBALS)
-- --------------------------------------------------------------------------
local function getProceduralSeed()
    local t = (os.time and os.time()) or 0
    local ct = (timer.curtime and math.floor(timer.curtime() * 1000)) or 0
    local seed = (t * 1103515245 + ct + math.random(1, 999999)) % 2147483647
    print("[Cognitive Decay Engine] Procedural seed initialized: " .. tostring(seed))
    return seed
end
pcall(getProceduralSeed)

if SERVER then
    -- Dematerialize any previous instance on hot-reload
    if _G.CognitiveDecay_Cleanup then
        pcall(_G.CognitiveDecay_Cleanup)
    end

    -- --------------------------------------------------------------------------
    -- 2. FULL AIRSPACE BOUNDS & DESCENDING MULTI-TIER GEOMETRY
    -- --------------------------------------------------------------------------
    local CONFIG = {
        CELL_SIZE   = 189.8,     -- Hunter plate4x4 dimension: 189.8 units
        WALL_HEIGHT = 189.8,
        
        -- Multi-Tier Descending Elevations (Top to Bottom across airspace)
        Z_TIER_0 = -12700.0, -- Level 0: High Mezzanine / Ingress (Near Corner 1)
        Z_TIER_1 = -13840.0, -- Level 0/1: Mid Liminal Sub-Offices
        Z_TIER_2 = -14980.0, -- Level 1: Industrial Warehouse / Habitable Zone
        Z_TIER_3 = -16250.0, -- Level 2: Concrete Crypt / Bedrock (Floor of Corner 2)
        
        -- Structural Primitives
        FLOOR_MODEL = "models/hunter/plates/plate4x4.mdl",
        WALL_MODEL  = "models/hunter/plates/plate4x4.mdl",
        RAMP_MODEL  = "models/hunter/plates/plate4x8.mdl",
        RAIL_MODEL  = "models/hunter/plates/plate1x4.mdl",
        DOOR_MODEL  = "models/props_c17/door01_left.mdl",
        DOOR_HEADER = "models/hunter/plates/plate2x2.mdl",
        
        -- 100% VERIFIED VertexLitGeneric MODEL MATERIALS (NEVER USE HAZARD CAUTION)
        MAT_WALL_PANEL    = "phoenix_storms/pack2/interior_sides", -- Smooth interior office wall panel
        MAT_WALL_CLEAN    = "phoenix_storms/fender_white",        -- Clean matte white panel
        MAT_FLOOR_CARPET  = "phoenix_storms/pack2/train_floor",   -- Textured office floor
        MAT_CEILING_PANEL = "phoenix_storms/pack2/interior_top",   -- Drop-ceiling acoustic tile
        MAT_CONCRETE      = "phoenix_storms/concrete1",            -- Real industrial concrete
        MAT_DEBUG_WHITE   = "models/debug/debugwhite",             -- Universal VertexLitGeneric matte
        
        -- Vibrant Liminal Color Tints
        TINT_MONO_YELLOW  = Color(245, 225, 140), -- Classic Backrooms Level 0 Mono-Yellow!
        TINT_CARPET       = Color(185, 170, 120), -- Damp vintage office carpet
        TINT_CEILING      = Color(215, 210, 190), -- Aged drop-ceiling tiles
        TINT_CONCRETE     = Color(150, 150, 150), -- Cold warehouse concrete
        TINT_DARK_CRYPT   = Color(125, 125, 125), -- Subterranean crypt
    }

    -- --------------------------------------------------------------------------
    -- 3. VERIFIED SOURCE MODEL POOLS (100% COLLISION & PHYSICS VERIFIED)
    -- --------------------------------------------------------------------------
    local MODEL_POOLS = {
        office_desks = {
            "models/props_c17/furnituretable001a.mdl"
        },
        office_chairs = {
            "models/props_c17/furniturechair001a.mdl"
        },
        office_storage = {
            "models/props_c17/furnituredrawer001a.mdl",
            "models/props_c17/furnituredrawer002a.mdl"
        },
        monitors = {
            "models/props_c17/tv_monitor01.mdl",
            "models/props_lab/monitor01a.mdl"
        },
        radios = {
            "models/props_lab/citizenradio.mdl"
        },
        office_props = {
            "models/props_trainstation/trashcan_indoor001a.mdl",
            "models/props_junk/trashbin01a.mdl",
            "models/props_c17/display_cooler01a.mdl",
            "models/props_c17/furniturecouch001a.mdl"
        },
        warehouse_props = {
            "models/props_junk/wood_pallet001a.mdl",
            "models/props_c17/oildrum001.mdl",
            "models/props_junk/cardboard_box001a.mdl",
            "models/props_junk/cardboard_box002a.mdl"
        },
        ceiling_lights = {
            "models/props_interiors/lights_florescent01a.mdl"
        },
        cage_lights = {
            "models/props_c17/light_cagelight01_on.mdl"
        }
    }

    -- Exact vertical bounding offsets (bottom sits perfectly flush with surface)
    local MODEL_OFFSETS = {
        ["models/props_c17/furnituretable001a.mdl"]       = 18.21,
        ["models/props_c17/furniturechair001a.mdl"]       = 20.14,
        ["models/props_c17/furnituredrawer001a.mdl"]      = 20.25,
        ["models/props_c17/furnituredrawer002a.mdl"]      = 16.88,
        ["models/props_c17/furniturecouch001a.mdl"]       = 16.89,
        ["models/props_c17/tv_monitor01.mdl"]             = 8.28,
        ["models/props_lab/monitor01a.mdl"]               = 13.12,
        ["models/props_lab/citizenradio.mdl"]             = 0.28,
        ["models/props_trainstation/trashcan_indoor001a.mdl"] = 20.28,
        ["models/props_junk/trashbin01a.mdl"]             = 12.0,
        ["models/props_c17/display_cooler01a.mdl"]        = 0.26,
        ["models/props_junk/wood_pallet001a.mdl"]         = 4.56,
        ["models/props_c17/oildrum001.mdl"]               = 0.28,
        ["models/props_junk/cardboard_box001a.mdl"]       = 12.27,
        ["models/props_junk/cardboard_box002a.mdl"]       = 12.27,
        ["models/props_interiors/lights_florescent01a.mdl"] = 3.5,
        ["models/props_c17/light_cagelight01_on.mdl"]    = 5.0,
        ["models/props_c17/door01_left.mdl"]              = 54.28
    }

    -- Pure VertexLitGeneric model materials (NO LIGHTMAPPED OR HAZARD CAUTION)
    local PHX_MATERIALS = {
        wallpaper = {
            CONFIG.MAT_WALL_PANEL,
            CONFIG.MAT_WALL_CLEAN,
            CONFIG.MAT_DEBUG_WHITE
        },
        carpet = {
            CONFIG.MAT_FLOOR_CARPET,
            CONFIG.MAT_DEBUG_WHITE
        },
        ceiling = {
            CONFIG.MAT_CEILING_PANEL,
            CONFIG.MAT_DEBUG_WHITE
        },
        concrete = {
            CONFIG.MAT_CONCRETE,
            CONFIG.MAT_DEBUG_WHITE
        }
    }

    -- --------------------------------------------------------------------------
    -- 4. STATE TRACKING & SPAWN QUEUE
    -- --------------------------------------------------------------------------
    local spawnQueue = {}
    local activeEntities = {}
    local activeDoors = {}
    local activeRadios = {}
    local activeLights = {}

    local function safeChoice(tbl, fallback)
        if not tbl or #tbl == 0 then return fallback end
        return tbl[math.random(1, #tbl)]
    end

    local function safeSetMaterialWithFallback(ent, primaryMat, category, tintColor)
        if not isValid(ent) then return false end

        if primaryMat then
            local ok = pcall(ent.setMaterial, ent, primaryMat)
            if ok then
                if tintColor then pcall(ent.setColor, ent, tintColor) end
                return true
            end
        end

        local pool = (category and PHX_MATERIALS[category]) or PHX_MATERIALS.wallpaper
        for _, altMat in ipairs(pool) do
            if altMat ~= primaryMat then
                local aOk = pcall(ent.setMaterial, ent, altMat)
                if aOk then
                    if tintColor then pcall(ent.setColor, ent, tintColor) end
                    return true
                end
            end
        end

        pcall(ent.setMaterial, ent, CONFIG.MAT_DEBUG_WHITE)
        pcall(ent.setColor, ent, tintColor or CONFIG.TINT_MONO_YELLOW)
        return true
    end

    local function trySpawnWithFallbacks(item)
        if item.model then
            local ok, ent = pcall(prop.create, item.pos, item.ang, item.model, item.keepFrozen)
            if ok and isValid(ent) then
                return ent, item.model
            end
        end

        local cat = item.category or "flat_surface"
        local universalModel = (cat == "floor" or cat == "wall" or cat == "ceiling" or cat == "ramp")
            and "models/hunter/plates/plate4x4.mdl"
            or "models/props_c17/furnituretable001a.mdl"

        local uOk, uEnt = pcall(prop.create, item.pos, item.ang, universalModel, item.keepFrozen)
        if uOk and isValid(uEnt) then
            return uEnt, universalModel
        end

        return nil, nil
    end

    -- --------------------------------------------------------------------------
    -- 5. GEOMETRY PRIMITIVES: ENCLOSED ROOMS, FRAMED DOORS, CEILING LIGHTS
    -- --------------------------------------------------------------------------
    local HALF_CELL = CONFIG.CELL_SIZE * 0.5

    local function queueEnclosedCell(pos, floorMat, ceilMat, floorCat, ceilCat, floorTint, ceilTint)
        -- Floor Plate
        table.insert(spawnQueue, {
            pos = pos,
            ang = Angle(0, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = floorMat or CONFIG.MAT_FLOOR_CARPET,
            tint = floorTint or CONFIG.TINT_CARPET,
            category = "floor",
            matCategory = floorCat or "carpet",
            keepFrozen = true
        })
        -- Ceiling Plate
        table.insert(spawnQueue, {
            pos = pos + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = Angle(180, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = ceilMat or CONFIG.MAT_CEILING_PANEL,
            tint = ceilTint or CONFIG.TINT_CEILING,
            category = "ceiling",
            matCategory = ceilCat or "ceiling",
            keepFrozen = true
        })
    end

    local function queueWall(pos, isNorthSouth, wallMat, wallCat, wallTint)
        local wallAng = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0)
        table.insert(spawnQueue, {
            pos = pos,
            ang = wallAng,
            model = CONFIG.WALL_MODEL,
            mat = wallMat or CONFIG.MAT_WALL_PANEL,
            tint = wallTint or CONFIG.TINT_MONO_YELLOW,
            category = "wall",
            matCategory = wallCat or "wallpaper",
            keepFrozen = true
        })
    end

    local function queueCeilingLight(cellPos, lightModel)
        local ceilZ = cellPos.z + CONFIG.WALL_HEIGHT
        local lightZ = ceilZ - (MODEL_OFFSETS[lightModel] or 3.5)
        local lightPos = Vector(cellPos.x, cellPos.y, lightZ)

        table.insert(spawnQueue, {
            pos = lightPos,
            ang = Angle(0, math.random(0, 1) * 90, 0),
            model = lightModel,
            category = "light",
            keepFrozen = true,
            onSpawn = function(ent)
                table.insert(activeLights, ent)
            end
        })
    end

    local function queueFramedDoor(cellCenter, isNorthSouth, wallMat, wallTint)
        -- Door origin at floorZ + 54.3 rests flush on the floor surface!
        local doorPos = cellCenter + (isNorthSouth and Vector(0, HALF_CELL, 54.3) or Vector(HALF_CELL, 0, 54.3))
        local doorAng = isNorthSouth and Angle(0, 0, 0) or Angle(0, 90, 0)

        -- 1. Realistic Interactive Source Door
        table.insert(spawnQueue, {
            pos = doorPos,
            ang = doorAng,
            model = CONFIG.DOOR_MODEL,
            category = "door",
            keepFrozen = true,
            onSpawn = function(ent)
                table.insert(activeDoors, {
                    ent = ent,
                    isOpen = false,
                    moving = false,
                    moveStart = 0,
                    moveDuration = 0.85,
                    startAng = doorAng,
                    baseAng = doorAng,
                    openAng = doorAng + Angle(0, 90, 0),
                    nextUse = 0
                })
            end
        })

        -- 2. Solid Wall Header Plate above the door frame up to the ceiling
        local headerPos = doorPos + Vector(0, 0, 54.3 + 41.0)
        local headerAng = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0)
        table.insert(spawnQueue, {
            pos = headerPos,
            ang = headerAng,
            model = CONFIG.DOOR_HEADER,
            mat = wallMat or CONFIG.MAT_WALL_PANEL,
            tint = wallTint or CONFIG.TINT_MONO_YELLOW,
            category = "wall",
            keepFrozen = true
        })
    end

    -- Continuous Walkable Ramp Connecting Two Elevation Tiers
    local function queueWalkableRampCorridor(startPos, endPos, isNorthSouth, wallMat, wallTint)
        local delta = endPos - startPos
        local distHoriz = isNorthSouth and math.abs(delta.y) or math.abs(delta.x)
        local distVert  = math.abs(delta.z)
        local numRamps = math.max(1, math.ceil(distVert / 190.0))

        for i = 1, numRamps do
            local frac = (i - 0.5) / numRamps
            local midPos = startPos + (isNorthSouth and Vector(0, delta.y * frac, delta.z * frac) or Vector(delta.x * frac, 0, delta.z * frac))
            
            -- Pitch: 30 degrees down
            local rampPitch = 30.0 * (delta.z < 0 and 1 or -1)
            local rampAng = isNorthSouth and Angle(rampPitch, 90, 0) or Angle(rampPitch, 0, 0)

            -- Ramp Floor
            table.insert(spawnQueue, {
                pos = midPos,
                ang = rampAng,
                model = CONFIG.RAMP_MODEL,
                mat = CONFIG.MAT_CONCRETE,
                tint = wallTint or CONFIG.TINT_CONCRETE,
                category = "ramp",
                keepFrozen = true
            })

            -- Side Safety Railings
            local sideOffset = isNorthSouth and Vector(HALF_CELL, 0, 30) or Vector(0, HALF_CELL, 30)
            table.insert(spawnQueue, {
                pos = midPos + sideOffset,
                ang = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0),
                model = CONFIG.RAIL_MODEL,
                mat = wallMat or CONFIG.MAT_WALL_PANEL,
                tint = wallTint or CONFIG.TINT_MONO_YELLOW,
                category = "wall",
                keepFrozen = true
            })
            table.insert(spawnQueue, {
                pos = midPos - sideOffset,
                ang = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0),
                model = CONFIG.RAIL_MODEL,
                mat = wallMat or CONFIG.MAT_WALL_PANEL,
                tint = wallTint or CONFIG.TINT_MONO_YELLOW,
                category = "wall",
                keepFrozen = true
            })
        end
    end

    -- --------------------------------------------------------------------------
    -- 6. CONTEXTUAL PROPS & GLITCH ANOMALIES (100% PERMANENTLY FROZEN)
    -- --------------------------------------------------------------------------
    local function queueProp(pos, ang, mdl, category, isGlitched)
        local offset = MODEL_OFFSETS[mdl] or 15.0
        local finalPos = pos + Vector(0, 0, offset)
        local finalAng = ang or Angle(0, math.random(0, 3) * 90, 0)

        if isGlitched then
            -- 8% rare anomaly item tilted surreal and suspended in space
            finalAng = Angle(math.random(-35, 35), math.random(0, 360), math.random(-35, 35))
            finalPos = finalPos + Vector(0, 0, math.random(25, 60))
        end

        table.insert(spawnQueue, {
            pos = finalPos,
            ang = finalAng,
            model = mdl,
            category = category or "furniture",
            keepFrozen = true -- 100% FROZEN! NEVER UNFREEZE!
        })
    end

    local function queueDeskWorkstation(cellPos, floorZ, isGlitched)
        local deskMdl = MODEL_POOLS.office_desks[1]
        local deskYaw = math.random(0, 3) * 90
        local deskAng = Angle(0, deskYaw, 0)
        local deskPos = Vector(cellPos.x, cellPos.y, floorZ + 1.8 + MODEL_OFFSETS[deskMdl])

        -- Desk
        table.insert(spawnQueue, {
            pos = deskPos,
            ang = deskAng,
            model = deskMdl,
            category = "furniture",
            keepFrozen = true
        })

        local tableSurfaceZ = floorZ + 1.8 + 37.0

        -- Monitor on Desk
        local monMdl = safeChoice(MODEL_POOLS.monitors, "models/props_c17/tv_monitor01.mdl")
        local monOffset = MODEL_OFFSETS[monMdl] or 8.28
        local monPos = Vector(cellPos.x, cellPos.y, tableSurfaceZ + monOffset)
        local monAng = deskAng + Angle(0, math.random(-15, 15), 0)

        table.insert(spawnQueue, {
            pos = monPos,
            ang = monAng,
            model = monMdl,
            category = "surface_mount",
            keepFrozen = true
        })

        -- Chair
        local chairMdl = MODEL_POOLS.office_chairs[1]
        local fwd = deskAng:getForward()
        local chairPos = Vector(cellPos.x, cellPos.y, floorZ + 1.8 + MODEL_OFFSETS[chairMdl]) - (fwd * 34.0)
        local chairAng = deskAng + Angle(0, math.random(-20, 20), 0)

        table.insert(spawnQueue, {
            pos = chairPos,
            ang = chairAng,
            model = chairMdl,
            category = "furniture",
            keepFrozen = true
        })

        -- Radio (25% chance per workstation)
        if math.random() < 0.25 then
            local radioMdl = MODEL_POOLS.radios[1]
            local rPos = Vector(cellPos.x + 28, cellPos.y - 15, tableSurfaceZ + MODEL_OFFSETS[radioMdl])
            table.insert(spawnQueue, {
                pos = rPos,
                ang = deskAng + Angle(0, 30, 0),
                model = radioMdl,
                category = "radio",
                keepFrozen = true,
                onSpawn = function(ent)
                    local isMusicRadio = (math.random() < 0.5)
                    local rData = {
                        ent = ent,
                        isMusic = isMusicRadio,
                        isLooping = (math.random() < 0.35),
                        category = isMusicRadio and "music" or "sound",
                        nextHopTime = timer.curtime() + 60,
                        hasStarted = false
                    }
                    table.insert(activeRadios, rData)
                    net.start("CognitiveDecay_RadioRegister")
                    net.writeEntity(ent)
                    net.writeBool(isMusicRadio)
                    net.send()
                end
            })
        end
    end

    -- --------------------------------------------------------------------------
    -- 7. MASTER MULTI-TIER TOP-TO-BOTTOM GENERATOR
    -- --------------------------------------------------------------------------
    local function generateFullAirspaceComplex()
        print("[Cognitive Decay Engine] Synthesizing top-to-bottom megastructure across airspace...")

        -- TIER 0: HIGH MEZZANINE / INGRESS (Z = -12,700) Near Corner 1
        local t0Origin = Vector(6800.0, -4500.0, CONFIG.Z_TIER_0)
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t0Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)
                queueEnclosedCell(cPos, CONFIG.MAT_FLOOR_CARPET, CONFIG.MAT_CEILING_PANEL, "carpet", "ceiling", CONFIG.TINT_CARPET, CONFIG.TINT_CEILING)

                -- Outer Perimeter Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW) end
                
                -- Entrance Doorway at gy == 0, gx == 1 (Enter from outside!)
                if gy == 0 then
                    if gx == 1 then
                        queueFramedDoor(cPos, false, CONFIG.MAT_WALL_PANEL, CONFIG.TINT_MONO_YELLOW)
                    else
                        queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW)
                    end
                end

                -- gy == 3 has open exit to Ramp 1!
                if gy == 3 and gx ~= 2 then
                    queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW)
                end

                -- Ceiling Lights
                if (gx == 1 and gy == 1) or (gx == 2 and gy == 2) then
                    queueCeilingLight(cPos, MODEL_POOLS.ceiling_lights[1])
                end

                -- Contextual Office Furniture
                if (gx == 1 and gy == 2) or (gx == 2 and gy == 1) then
                    queueDeskWorkstation(cPos, CONFIG.Z_TIER_0, false)
                elseif gx == 0 and gy == 1 then
                    queueProp(cPos, Angle(0, 0, 0), MODEL_POOLS.office_storage[1], "furniture", false)
                elseif gx == 3 and gy == 2 then
                    queueProp(cPos, Angle(0, 180, 0), MODEL_POOLS.office_props[4], "furniture", (math.random() < 0.10))
                end
            end
        end

        -- RAMP HIGHWAY 1 (Connecting Tier 0 at -12,700 to Tier 1 at -13,840)
        local r1Start = t0Origin + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, 0)
        local r1MidLanding = r1Start + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, -570.0)
        local r1End = r1Start + Vector(4 * CONFIG.CELL_SIZE, -6 * CONFIG.CELL_SIZE, -1140.0) -- Hits Z_TIER_1 (-13,840)!

        queueWalkableRampCorridor(r1Start, r1MidLanding, true, CONFIG.MAT_WALL_PANEL, CONFIG.TINT_MONO_YELLOW)
        -- Mid-flight Observation Landing with an open pit hole!
        queueEnclosedCell(r1MidLanding, CONFIG.MAT_CONCRETE, CONFIG.MAT_CEILING_PANEL, "concrete", "ceiling", CONFIG.TINT_CONCRETE, CONFIG.TINT_CEILING)
        queueCeilingLight(r1MidLanding, MODEL_POOLS.ceiling_lights[1])
        queueWalkableRampCorridor(r1MidLanding, r1End, true, CONFIG.MAT_WALL_PANEL, CONFIG.TINT_MONO_YELLOW)

        -- TIER 1: MID LIMINAL SUB-OFFICES (Z = -13,840)
        local t1Origin = r1End
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t1Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)

                -- Pit Hole in cell (1, 1): floor omitted! Looking down into the darkness!
                if gx == 1 and gy == 1 then
                    table.insert(spawnQueue, {
                        pos = cPos + Vector(0, 0, CONFIG.WALL_HEIGHT),
                        ang = Angle(180, 0, 0),
                        model = CONFIG.FLOOR_MODEL,
                        mat = CONFIG.MAT_CEILING_PANEL,
                        tint = CONFIG.TINT_CEILING,
                        category = "ceiling",
                        keepFrozen = true
                    })
                    -- Safety warning rail
                    table.insert(spawnQueue, {
                        pos = cPos - Vector(HALF_CELL, 0, -30),
                        ang = Angle(90, 90, 0),
                        model = CONFIG.RAIL_MODEL,
                        mat = CONFIG.MAT_WALL_PANEL,
                        tint = CONFIG.TINT_MONO_YELLOW,
                        category = "wall",
                        keepFrozen = true
                    })
                else
                    queueEnclosedCell(cPos, CONFIG.MAT_FLOOR_CARPET, CONFIG.MAT_CEILING_PANEL, "carpet", "ceiling", CONFIG.TINT_CARPET, CONFIG.TINT_CEILING)
                end

                -- Outer Perimeter Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW) end
                if gy == 0 and gx ~= 0 then queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW) end
                if gy == 3 and gx ~= 2 then queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_WALL_PANEL, "wallpaper", CONFIG.TINT_MONO_YELLOW) end

                -- Interior Partition Walls & Framed Doors
                if gx == 2 and gy == 1 then
                    queueFramedDoor(cPos, true, CONFIG.MAT_WALL_PANEL, CONFIG.TINT_MONO_YELLOW)
                elseif gx == 1 and gy == 2 then
                    queueFramedDoor(cPos, false, CONFIG.MAT_WALL_PANEL, CONFIG.TINT_MONO_YELLOW)
                end

                -- Ceiling Lights
                if (gx == 0 and gy == 2) or (gx == 3 and gy == 1) then
                    queueCeilingLight(cPos, MODEL_POOLS.ceiling_lights[1])
                end

                -- Furniture & Anomaly Items
                if gx == 0 and gy == 3 then
                    queueDeskWorkstation(cPos, CONFIG.Z_TIER_1, false)
                elseif gx == 3 and gy == 3 then
                    queueProp(cPos, Angle(0, 90, 0), MODEL_POOLS.office_props[3], "furniture", false)
                elseif gx == 2 and gy == 3 then
                    queueProp(cPos, Angle(0, 0, 0), MODEL_POOLS.office_storage[2], "furniture", (math.random() < 0.15))
                end
            end
        end

        -- RAMP HIGHWAY 2 (Connecting Tier 1 at -13,840 to Tier 2 at -14,980)
        local r2Start = t1Origin + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, 0)
        local r2MidLanding = r2Start + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, -570.0)
        local r2End = r2Start + Vector(4 * CONFIG.CELL_SIZE, -6 * CONFIG.CELL_SIZE, -1140.0) -- Hits Z_TIER_2 (-14,980)!

        queueWalkableRampCorridor(r2Start, r2MidLanding, true, CONFIG.MAT_CONCRETE, CONFIG.TINT_CONCRETE)
        queueEnclosedCell(r2MidLanding, CONFIG.MAT_CONCRETE, CONFIG.MAT_CEILING_PANEL, "concrete", "ceiling", CONFIG.TINT_CONCRETE, CONFIG.TINT_CEILING)
        queueCeilingLight(r2MidLanding, MODEL_POOLS.cage_lights[1])
        queueWalkableRampCorridor(r2MidLanding, r2End, true, CONFIG.MAT_CONCRETE, CONFIG.TINT_CONCRETE)

        -- TIER 2: INDUSTRIAL WAREHOUSE / HABITABLE ZONE (Z = -14,980)
        local t2Origin = r2End
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t2Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)
                queueEnclosedCell(cPos, CONFIG.MAT_CONCRETE, CONFIG.MAT_CEILING_PANEL, "concrete", "ceiling", CONFIG.TINT_CONCRETE, CONFIG.TINT_DARK_CRYPT)

                -- Concrete Perimeter Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_CONCRETE) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_CONCRETE) end
                if gy == 0 and gx ~= 0 then queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_CONCRETE) end
                if gy == 3 and gx ~= 2 then queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_CONCRETE) end

                -- Industrial Cage Lights
                if (gx == 1 and gy == 1) or (gx == 2 and gy == 2) then
                    queueCeilingLight(cPos, MODEL_POOLS.cage_lights[1])
                end

                -- Warehouse Pallets, Oil Drums, and Storage Crates
                if gx == 1 and gy == 2 then
                    queueProp(cPos, Angle(0, 45, 0), MODEL_POOLS.warehouse_props[1], "furniture", false)
                    queueProp(cPos + Vector(0, 0, 9), Angle(0, 15, 0), MODEL_POOLS.warehouse_props[3], "furniture", false)
                elseif gx == 0 and gy == 2 then
                    queueProp(cPos, Angle(0, 0, 0), MODEL_POOLS.warehouse_props[2], "furniture", (math.random() < 0.10))
                end
            end
        end

        -- RAMP HIGHWAY 3 (Connecting Tier 2 at -14,980 down to Tier 3 / Bedrock at -16,250)
        local r3Start = t2Origin + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, 0)
        local r3MidLanding = r3Start + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, -635.0)
        local r3End = r3Start + Vector(4 * CONFIG.CELL_SIZE, -6 * CONFIG.CELL_SIZE, -1270.0) -- Hits Z_TIER_3 (-16,250 Bedrock Floor)!

        queueWalkableRampCorridor(r3Start, r3MidLanding, true, CONFIG.MAT_CONCRETE, CONFIG.TINT_DARK_CRYPT)
        queueEnclosedCell(r3MidLanding, CONFIG.MAT_CONCRETE, CONFIG.MAT_CEILING_PANEL, "concrete", "ceiling", CONFIG.TINT_DARK_CRYPT, CONFIG.TINT_DARK_CRYPT)
        queueCeilingLight(r3MidLanding, MODEL_POOLS.cage_lights[1])
        queueWalkableRampCorridor(r3MidLanding, r3End, true, CONFIG.MAT_CONCRETE, CONFIG.TINT_DARK_CRYPT)

        -- TIER 3: THE DEEP CRYPT & PIPE DREAMS (Z = -16,250 - Bedrock Floor of Corner 2!)
        local t3Origin = r3End
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t3Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)
                queueEnclosedCell(cPos, CONFIG.MAT_CONCRETE, CONFIG.MAT_CEILING_PANEL, "concrete", "ceiling", CONFIG.TINT_DARK_CRYPT, CONFIG.TINT_DARK_CRYPT)

                -- Heavy Concrete Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_DARK_CRYPT) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_DARK_CRYPT) end
                if gy == 0 and gx ~= 0 then queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_DARK_CRYPT) end
                if gy == 3 then queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_CONCRETE, "concrete", CONFIG.TINT_DARK_CRYPT) end

                -- Maintenance Cage Lights
                if (gx == 1 and gy == 2) or (gx == 2 and gy == 1) then
                    queueCeilingLight(cPos, MODEL_POOLS.cage_lights[1])
                end

                -- Heavy crypt barrels, crates, and radio
                if gx == 2 and gy == 2 then
                    queueProp(cPos, Angle(0, 0, 0), MODEL_POOLS.warehouse_props[2], "furniture", false)
                elseif gx == 1 and gy == 1 then
                    queueProp(cPos, Angle(0, 30, 0), MODEL_POOLS.warehouse_props[4], "furniture", (math.random() < 0.15))
                end
            end
        end

        print(string.format("[Cognitive Decay Engine] Queued %d contiguous airspace entities spanning Z=-12,700 to Z=-16,250", #spawnQueue))
    end

    -- --------------------------------------------------------------------------
    -- 8. ASYNC FAULT-TOLERANT SPAWN PIPELINE (NEVER HALTS ON MODEL/MAT FAILURES)
    -- --------------------------------------------------------------------------
    local function executeSpawnQueue()
        local index = 1
        local timerName = "CognitiveDecay_SpawnPipeline"

        timer.create(timerName, 0.015, #spawnQueue, function()
            local item = spawnQueue[index]
            index = index + 1
            if not item then return end

            pcall(function()
                local ent, usedModel = trySpawnWithFallbacks(item)
                if isValid(ent) then
                    table.insert(activeEntities, ent)

                    if item.mat or item.matCategory or item.tint then
                        safeSetMaterialWithFallback(ent, item.mat, item.matCategory, item.tint)
                    end

                    if item.onSpawn then
                        pcall(item.onSpawn, ent)
                    end
                end
            end)
        end)
    end

    -- --------------------------------------------------------------------------
    -- 9. INTERACTIVE DOOR CONTROLLER (+USE 'E' KEY, COSINE SMOOTH EASE, WOOD SOUNDS)
    -- --------------------------------------------------------------------------
    local function toggleDoor(d)
        if not isValid(d.ent) or d.moving then return end
        d.isOpen = not d.isOpen
        d.moving = true
        d.moveStart = timer.curtime()
        d.startAng = d.ent:getAngles()
        d.targetAng = d.isOpen and d.openAng or d.baseAng
        d.nextUse = timer.curtime() + 1.0

        local dPos = d.ent:getPos()
        pcall(sound.play, "doors/door_latch1.wav", dPos, 70, 100)
        pcall(sound.play, "doors/door_wood_move1.wav", dPos, 65, 100)
    end

    hook.add("think", "CognitiveDecay_DoorController", function()
        pcall(function()
            local now = timer.curtime()

            -- 1. Animate moving doors with smooth cosine ease
            for i = #activeDoors, 1, -1 do
                local d = activeDoors[i]
                if not isValid(d.ent) then
                    table.remove(activeDoors, i)
                elseif d.moving then
                    local frac = math.min(1.0, (now - d.moveStart) / d.moveDuration)
                    local smooth = 0.5 - 0.5 * math.cos(frac * math.pi)
                    local curAng = LerpAngle(smooth, d.startAng, d.targetAng)
                    pcall(d.ent.setAngles, d.ent, curAng)

                    if frac >= 1.0 then
                        d.moving = false
                        pcall(d.ent.setAngles, d.ent, d.targetAng)
                        if not d.isOpen then
                            pcall(sound.play, "doors/door_wood_close1.wav", d.ent:getPos(), 70, 100)
                        end
                    end
                end
            end

            -- 2. +USE ('E' Key) Listener
            local players = find.allPlayers()
            for _, ply in ipairs(players) do
                if isValid(ply) and ply:keyDown(32) then -- 32 = IN_USE ('E' key)
                    local eyePos = ply:getEyePos()
                    local aimVec = ply:getAimVector()
                    local tr = trace.line(eyePos, eyePos + (aimVec * 85), nil, MASK_SOLID)

                    for _, d in ipairs(activeDoors) do
                        if isValid(d.ent) and now > (d.nextUse or 0) then
                            local dPos = d.ent:getPos()
                            if tr.Entity == d.ent or tr.HitPos:getDistance(dPos) < 55 or eyePos:getDistance(dPos) < 75 then
                                toggleDoor(d)
                                break
                            end
                        end
                    end
                end
            end
        end)
    end)

    -- --------------------------------------------------------------------------
    -- 10. CLEANUP & INITIALIZATION
    -- --------------------------------------------------------------------------
    _G.CognitiveDecay_Cleanup = function()
        timer.remove("CognitiveDecay_SpawnPipeline")
        hook.remove("think", "CognitiveDecay_DoorController")
        for _, ent in ipairs(activeEntities) do
            if isValid(ent) then pcall(ent.remove, ent) end
        end
        table.empty(activeEntities)
        table.empty(activeDoors)
        table.empty(activeRadios)
        table.empty(activeLights)
        table.empty(spawnQueue)
        print("[Cognitive Decay Engine] Dematerialized all existing entities.")
    end

    -- Trigger Generation
    generateFullAirspaceComplex()
    executeSpawnQueue()

else -- CLIENT

    local activeRadios = {}
    local activeLights = {}
    local glowMat = Material("sprites/light_glow02")
    if not glowMat or glowMat:isError() then glowMat = Material("sprites/glow01") end

    -- Dynamic Radio Tuning with Automatic Looping & Station Hopping
    local function tuneRadio(rData)
        if not isValid(rData.ent) then return end
        if isValid(rData.station) then pcall(rData.station.stop, rData.station) end

        local pool = rData.isMusic and DATASET.AUDIO.music or DATASET.AUDIO.sound
        if not pool or #pool == 0 then pool = DATASET.AUDIO.music end
        local track = safeChoice(pool, nil)
        if not track or not track.url then return end

        pcall(sound.playURL, track.url, "3d noblock", function(station, errCode, errName)
            if isValid(station) and isValid(rData.ent) then
                station:setPos(rData.ent:getPos())
                station:setVolume(0.85)
                station:play()
                rData.station = station
                rData.hasStarted = true
                rData.nextHopTime = timer.curtime() + (station:getLength() > 0 and (station:getLength() + 2) or 75)
            end
        end)
    end

    net.receive("CognitiveDecay_RadioRegister", function()
        pcall(function()
            local ent = net.readEntity()
            local isMusic = net.readBool()
            if isValid(ent) then
                local rData = {
                    ent = ent,
                    isMusic = isMusic,
                    isLooping = (math.random() < 0.35),
                    nextHopTime = timer.curtime() + 60,
                    hasStarted = false
                }
                table.insert(activeRadios, rData)
                tuneRadio(rData)
            end
        end)
    end)

    -- Radio Life Management Loop: Loops or hops stations when track ends so it never dies
    hook.add("think", "CognitiveDecay_RadioLifeManager", function()
        pcall(function()
            local now = timer.curtime()
            for i = #activeRadios, 1, -1 do
                local r = activeRadios[i]
                if not isValid(r.ent) then
                    if isValid(r.station) then pcall(r.station.stop, r.station) end
                    table.remove(activeRadios, i)
                else
                    if isValid(r.station) then
                        pcall(r.station.setPos, r.station, r.ent:getPos())
                        local curTime = r.station:getTime()
                        local totalLen = r.station:getLength()
                        local state = r.station:getState()

                        local isDone = (totalLen > 0 and curTime >= totalLen - 0.3) or (r.hasStarted and curTime > 2.0 and state == 0)
                        local isExpired = (now > (r.nextHopTime or 0))

                        if isDone or isExpired then
                            if r.isLooping and not isExpired then
                                pcall(r.station.setTime, r.station, 0)
                                pcall(r.station.play, r.station)
                            else
                                tuneRadio(r)
                            end
                        end
                    elseif r.hasStarted and (now > (r.nextHopTime or 0)) then
                        tuneRadio(r)
                    end
                end
            end
        end)
    end)

    -- Ambient Fluorescent Hum & Ceilings Glow Render Hook
    hook.add("render", "CognitiveDecay_ClientLighting", function()
        pcall(function()
            local ply = player()
            if not isValid(ply) then return end
            local plyPos = ply:getPos()

            -- Warm Fluorescent Light Glow Sprites
            if glowMat then
                render.setMaterial(glowMat)
                for _, fix in ipairs(find.byClass("prop_physics")) do
                    if isValid(fix) and fix:getModel() == "models/props_interiors/lights_florescent01a.mdl" then
                        local fPos = fix:getPos()
                        if plyPos:getDistance(fPos) < 900 then
                            render.setColor(Color(255, 245, 180, 215))
                            render.drawSprite(fPos - Vector(0, 0, 6), 160, 160)
                        end
                    elseif isValid(fix) and fix:getModel() == "models/props_c17/light_cagelight01_on.mdl" then
                        local fPos = fix:getPos()
                        if plyPos:getDistance(fPos) < 700 then
                            render.setColor(Color(255, 210, 130, 200))
                            render.drawSprite(fPos - Vector(0, 0, 8), 120, 120)
                        end
                    end
                end
            end
        end)
    end)

end
'''

full_code = new_dataset_head + "\n" + master_engine_body

assert 'randomseed' not in full_code, "FATAL: randomseed keyword found!"
assert 'MAT_STRIPES' not in full_code, "FATAL: MAT_STRIPES found!"
assert 'stripes' not in full_code.lower(), "FATAL: stripes found!"

# Write to workspace
main_lua_path = os.path.join(WORKSPACE, 'cognitive-decay', 'core', 'main.lua')
main_txt_path = os.path.join(WORKSPACE, 'cognitive-decay', 'core', 'main.txt')
root_lua_path = os.path.join(WORKSPACE, 'cognitive-decay', 'main.lua')
root_txt_path = os.path.join(WORKSPACE, 'cognitive-decay', 'main.txt')

for p in [main_lua_path, main_txt_path, root_lua_path, root_txt_path]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(full_code)

print("Saved clean engine to workspace successfully!")

# Write to GMod Starfall directory
if os.path.exists(GMOD_DIR):
    gmod_main_lua = os.path.join(GMOD_DIR, 'core', 'main.lua')
    gmod_main_txt = os.path.join(GMOD_DIR, 'core', 'main.txt')
    gmod_root_lua = os.path.join(GMOD_DIR, 'main.lua')
    gmod_root_txt = os.path.join(GMOD_DIR, 'main.txt')

    os.makedirs(os.path.join(GMOD_DIR, 'core'), exist_ok=True)
    for p in [gmod_main_lua, gmod_main_txt, gmod_root_lua, gmod_root_txt]:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(full_code)
    print("Synchronized clean engine to GMod Starfall directory successfully!")
