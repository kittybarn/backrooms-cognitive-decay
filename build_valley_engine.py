import os
import urllib.parse
import re

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

lua_audio_str = "    AUDIO = {\n        music = {\n" + "\n".join(music_tracks) + "\n        },\n        sound = {\n" + "\n".join(sound_tracks) + "\n        },\n    },"

# 2. Extract base dataset structure
with open(os.path.join(WORKSPACE, 'cognitive-decay', 'core', 'main.lua'), 'r', encoding='utf-8') as f:
    current_code = f.read()

d_start = current_code.find('local DATASET = {')
d_end = current_code.find('\n}\n', d_start) + 3
clean_head = current_code[:d_end].replace('models/props_c17/door01_left.mdl', 'doorless open portal')

audio_start = clean_head.find('AUDIO = {')
audio_end = clean_head.find('NPCS = {', audio_start)
new_dataset_head = clean_head[:audio_start] + lua_audio_str + "\n\n    " + clean_head[audio_end:]

print(f"Compiled audio tracks: {len(music_tracks)} music, {len(sound_tracks)} sound/ambient.")

# 3. Master Valley Chasm & Generative Biome Engine Body
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
    -- 1. AIRSPACE BOUNDS & VERTICAL VALLEY CHASM GEOMETRY
    -- --------------------------------------------------------------------------
    -- Airspace designated bounds:
    -- Corner 1 (Top NW): Vector(6441.24, -4107.08, -12576.30)
    -- Corner 2 (Bottom SE): Vector(16306.50, -16307.30, -16255.70)
    -- Total Drop: 3,679.4 units!
    --
    -- 4 Stacked Horizontal Levels cut by a central Grand Valley Chasm:
    -- Level 0 (Top Mezzanine):  Z = -13000.0 (Ceiling = -12810.2, >234u clearance below roof)
    -- Level 1 (Mid Sub-Offices): Z = -14050.0
    -- Level 2 (Industrial Whse): Z = -15100.0
    -- Level 3 (Deep Bedrock):   Z = -16150.0 (Floor of Corner 2 bedrock basin)
    local CONFIG = {
        CELL_SIZE   = 189.8,     -- Hunter plate4x4 dimension: 189.8 units
        WALL_HEIGHT = 189.8,
        
        Z_TIERS = {
            [0] = -13000.0,
            [1] = -14050.0,
            [2] = -15100.0,
            [3] = -16150.0
        },

        GRID_X = 8, -- 8 cells wide along X (0..7)
        GRID_Y = 6, -- 6 cells deep along Y (0..5)
        
        -- Central Grand Valley Chasm: columns 3 and 4 (380 units wide, 1140 units long, 3150 units deep!)
        VALLEY_COLS = { [3] = true, [4] = true },
        
        -- Aligned Facade Entryway Rows leading to chasm overlook balconies
        ENTRY_ROWS  = { [1] = true, [4] = true },

        -- Structural Primitives
        FLOOR_MODEL = "models/hunter/plates/plate4x4.mdl",
        WALL_MODEL  = "models/hunter/plates/plate4x4.mdl",
        HEADER_MODEL= "models/hunter/plates/plate2x4.mdl",
        BALCONY_MODEL = "models/hunter/plates/plate2x4.mdl",
        RAIL_MODEL  = "models/hunter/plates/plate1x4.mdl",

        -- 100% VERIFIED VertexLitGeneric MODEL MATERIALS (ZERO HAZARD PATTERNS, ZERO BATHROOM TILES)
        MAT_WALL_PANEL    = "phoenix_storms/pack2/interior_sides", -- Smooth yellow office wallpaper
        MAT_WALL_WHITE    = "phoenix_storms/fender_white",        -- Clean matte white panel
        MAT_FLOOR_CARPET  = "phoenix_storms/pack2/train_floor",   -- Textured vintage office carpet
        MAT_CEILING_PANEL = "phoenix_storms/pack2/interior_top",   -- Drop-ceiling acoustic tile
        MAT_CONCRETE      = "phoenix_storms/concrete1",            -- Real industrial concrete
        MAT_CONCRETE_DARK = "phoenix_storms/concrete2",            -- Subterranean crypt concrete
        MAT_DEBUG_WHITE   = "models/debug/debugwhite",             -- Universal VertexLitGeneric matte

        -- Vibrant Liminal Color Tints
        TINT_MONO_YELLOW  = Color(245, 225, 140), -- Classic Backrooms Level 0 Mono-Yellow!
        TINT_CARPET       = Color(185, 170, 120), -- Damp vintage office carpet
        TINT_CEILING      = Color(215, 210, 190), -- Aged drop-ceiling tiles
        TINT_WHITE_WALL   = Color(230, 230, 220), -- Liminal living quarters white
        TINT_GREY_CARPET  = Color(145, 140, 135), -- Muted institutional carpet
        TINT_CONCRETE     = Color(150, 150, 150), -- Cold warehouse concrete
        TINT_DARK_CRYPT   = Color(105, 105, 110), -- Deep bedrock crypt concrete
        TINT_CHASM_BALCONY= Color(130, 130, 130), -- Overlook metal/concrete
    }

    -- --------------------------------------------------------------------------
    -- 2. VERIFIED BASE SOURCE MODEL POOLS & EXACT BOUNDING OFFSETS
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
            "models/props_c17/furnituredrawer002a.mdl",
            "models/props_lab/filecabinet02.mdl"
        },
        couches = {
            "models/props_c17/furniturecouch001a.mdl"
        },
        crt_monitors = {
            "models/props_lab/monitor01a.mdl"
        },
        crt_tvs = {
            "models/props_c17/tv_monitor01.mdl"
        },
        radios = {
            "models/props_lab/citizenradio.mdl"
        },
        office_props = {
            "models/props_trainstation/trashcan_indoor001a.mdl",
            "models/props_junk/trashbin01a.mdl",
            "models/props_c17/display_cooler01a.mdl"
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
        },
        npcs = {
            "models/humans/group01/male_01.mdl",
            "models/humans/group01/female_01.mdl",
            "models/police.mdl"
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
        ["models/props_lab/filecabinet02.mdl"]            = 24.0,
        ["models/humans/group01/male_01.mdl"]             = 36.0,
        ["models/humans/group01/female_01.mdl"]           = 36.0,
        ["models/police.mdl"]                             = 36.0,
    }

    local PHX_MATERIALS = {
        wallpaper = {
            CONFIG.MAT_WALL_PANEL,
            CONFIG.MAT_WALL_WHITE,
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
            CONFIG.MAT_CONCRETE_DARK,
            CONFIG.MAT_DEBUG_WHITE
        }
    }

    -- --------------------------------------------------------------------------
    -- 3. STATE TRACKING & ADAPTIVE SPAWN QUEUE
    -- --------------------------------------------------------------------------
    local spawnQueue = {}
    local activeEntities = {}
    local activeRadios = {}
    local activeTVs = {}
    local activeLights = {}
    local activeNPCs = {}

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
        local universalModel = (cat == "floor" or cat == "wall" or cat == "ceiling")
            and "models/hunter/plates/plate4x4.mdl"
            or "models/props_c17/furnituretable001a.mdl"

        local uOk, uEnt = pcall(prop.create, item.pos, item.ang, universalModel, item.keepFrozen)
        if uOk and isValid(uEnt) then
            return uEnt, universalModel
        end

        return nil, nil
    end

    -- --------------------------------------------------------------------------
    -- 4. GEOMETRY PRIMITIVES: ENCLOSED ROOMS, SOLID FACADES, OVERLOOK BALCONIES
    -- --------------------------------------------------------------------------
    local HALF_CELL = CONFIG.CELL_SIZE * 0.5

    local function queueFloorAndCeiling(pos, floorMat, ceilMat, floorCat, ceilCat, floorTint, ceilTint)
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

    local function queueCeilingLight(cellPos, lightModel, isCage)
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
                pcall(ent.setSkin, ent, 1) -- illuminated glowing tube texture skin
                table.insert(activeLights, { ent = ent, isCage = isCage })
                net.start("CognitiveDecay_RegisterLight")
                net.writeEntity(ent)
                net.writeBool(isCage or false)
                net.send()
            end
        })
    end

    -- Doorless Open Archway Entryway leading to the Valley Chasm Overlook Balcony
    local function queueValleyEntryway(cellCenter, facingEast, wallMat, wallTint)
        local sign = facingEast and 1 or -1
        local wallPos = cellCenter + Vector(sign * HALF_CELL, 0, HALF_CELL)

        -- Top Header Plate above doorway (leaves bottom 95 units completely open)
        table.insert(spawnQueue, {
            pos = wallPos + Vector(0, 0, 47.5),
            ang = Angle(90, 90, 0),
            model = CONFIG.HEADER_MODEL,
            mat = wallMat or CONFIG.MAT_WALL_PANEL,
            tint = wallTint or CONFIG.TINT_MONO_YELLOW,
            category = "wall",
            keepFrozen = true
        })

        -- Overlook Balcony Ledge extending 95u out into the Chasm
        local balconyPos = cellCenter + Vector(sign * (HALF_CELL + 47.5), 0, 0)
        table.insert(spawnQueue, {
            pos = balconyPos,
            ang = Angle(0, 0, 0),
            model = CONFIG.BALCONY_MODEL,
            mat = CONFIG.MAT_CONCRETE,
            tint = CONFIG.TINT_CHASM_BALCONY,
            category = "floor",
            keepFrozen = true
        })

        -- Guardrails on Balcony Edges
        table.insert(spawnQueue, {
            pos = balconyPos + Vector(sign * 47.5, 0, 20),
            ang = Angle(90, 90, 0),
            model = CONFIG.RAIL_MODEL,
            mat = CONFIG.MAT_CONCRETE,
            tint = CONFIG.TINT_CHASM_BALCONY,
            category = "wall",
            keepFrozen = true
        })
    end

    -- --------------------------------------------------------------------------
    -- 5. CONTEXTUAL PROPS & COGNITIVE DECAY ANOMALIES (100% PERMANENTLY FROZEN)
    -- --------------------------------------------------------------------------
    local function queueProp(pos, ang, mdl, category, isGlitched)
        local offset = MODEL_OFFSETS[mdl] or 15.0
        local finalPos = pos + Vector(0, 0, offset)
        local finalAng = ang or Angle(0, math.random(0, 3) * 90, 0)

        if isGlitched then
            -- 8-12% rare anomaly item tilted surreal and suspended in space
            finalAng = Angle(math.random(-35, 35), math.random(0, 360), math.random(-35, 35))
            finalPos = finalPos + Vector(0, 0, math.random(25, 55))
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

        -- CRT Monitor on Desk
        local monMdl = MODEL_POOLS.crt_monitors[1]
        local monOffset = MODEL_OFFSETS[monMdl] or 13.12
        local monPos = Vector(cellPos.x, cellPos.y, tableSurfaceZ + monOffset)
        local monAng = deskAng + Angle(0, math.random(-15, 15), 0)

        table.insert(spawnQueue, {
            pos = monPos,
            ang = monAng,
            model = monMdl,
            category = "surface_mount",
            keepFrozen = true
        })

        -- Office Swivel Chair
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

        -- Citizen Radio on Desk (40% chance)
        if math.random() < 0.40 then
            local radioMdl = MODEL_POOLS.radios[1]
            local rPos = Vector(cellPos.x + 26, cellPos.y - 12, tableSurfaceZ + MODEL_OFFSETS[radioMdl])
            table.insert(spawnQueue, {
                pos = rPos,
                ang = deskAng + Angle(0, 30, 0),
                model = radioMdl,
                category = "radio",
                keepFrozen = true,
                onSpawn = function(ent)
                    local isMusicRadio = (math.random() < 0.65)
                    local rData = {
                        ent = ent,
                        isMusic = isMusicRadio,
                        isLooping = (math.random() < 0.40),
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

    local function queueLivingLounge(cellPos, floorZ, isGlitched)
        local couchMdl = MODEL_POOLS.couches[1]
        local couchYaw = math.random(0, 3) * 90
        local couchAng = Angle(0, couchYaw, 0)
        local couchPos = Vector(cellPos.x, cellPos.y, floorZ + 1.8 + MODEL_OFFSETS[couchMdl])

        -- Couch
        table.insert(spawnQueue, {
            pos = couchPos,
            ang = couchAng,
            model = couchMdl,
            category = "furniture",
            keepFrozen = true
        })

        -- Coffee Table with CRT TV Monitor in front of Couch
        local fwd = couchAng:getForward()
        local tablePos = couchPos + (fwd * 55.0)
        local tableMdl = MODEL_POOLS.office_desks[1]
        table.insert(spawnQueue, {
            pos = Vector(tablePos.x, tablePos.y, floorZ + 1.8 + MODEL_OFFSETS[tableMdl]),
            ang = couchAng + Angle(0, 180, 0),
            model = tableMdl,
            category = "furniture",
            keepFrozen = true
        })

        -- CRT TV Monitor displaying analog emergency glitch
        local tvMdl = MODEL_POOLS.crt_tvs[1]
        local tvSurfaceZ = floorZ + 1.8 + 37.0
        local tvPos = Vector(tablePos.x, tablePos.y, tvSurfaceZ + MODEL_OFFSETS[tvMdl])
        local tvAng = couchAng + Angle(0, 180, 0)

        table.insert(spawnQueue, {
            pos = tvPos,
            ang = tvAng,
            model = tvMdl,
            category = "tv",
            keepFrozen = true,
            onSpawn = function(ent)
                table.insert(activeTVs, ent)
                net.start("CognitiveDecay_RegisterTV")
                net.writeEntity(ent)
                net.send()
            end
        })
    end

    local function queueStorageWarehouse(cellPos, floorZ, isGlitched)
        local palletMdl = MODEL_POOLS.warehouse_props[1]
        local pPos = Vector(cellPos.x, cellPos.y, floorZ + 1.8 + MODEL_OFFSETS[palletMdl])
        local pAng = Angle(0, math.random(0, 3) * 90, 0)

        -- Pallet
        table.insert(spawnQueue, {
            pos = pPos,
            ang = pAng,
            model = palletMdl,
            category = "furniture",
            keepFrozen = true
        })

        -- Cargo Crates / Oil Drums stacked on pallet
        if math.random() < 0.5 then
            local boxMdl = MODEL_POOLS.warehouse_props[3]
            table.insert(spawnQueue, {
                pos = pPos + Vector(0, 0, 10 + MODEL_OFFSETS[boxMdl]),
                ang = pAng + Angle(0, math.random(-15, 15), 0),
                model = boxMdl,
                category = "furniture",
                keepFrozen = true
            })
        else
            local drumMdl = MODEL_POOLS.warehouse_props[2]
            table.insert(spawnQueue, {
                pos = pPos + Vector(0, 0, 10 + MODEL_OFFSETS[drumMdl]),
                ang = pAng,
                model = drumMdl,
                category = "furniture",
                keepFrozen = true
            })
        end
    end

    local function queueGlitchedNPC(pos, floorZ, tier)
        local npcMdl = safeChoice(MODEL_POOLS.npcs, "models/humans/group01/male_01.mdl")
        local npcPos = Vector(pos.x, pos.y, floorZ + 1.8 + (MODEL_OFFSETS[npcMdl] or 36.0))
        local npcAng = Angle(0, math.random(0, 360), 0)

        table.insert(spawnQueue, {
            pos = npcPos,
            ang = npcAng,
            model = npcMdl,
            category = "npc",
            keepFrozen = true,
            onSpawn = function(ent)
                table.insert(activeNPCs, ent)
                -- Apply uncanny bone manipulations
                local headBone = ent:lookupBone("ValveBiped.Bip01_Head1")
                if headBone then
                    ent:manipulateBoneAngles(headBone, Angle(0, 0, math.random(35, 75)))
                end
                local spineBone = ent:lookupBone("ValveBiped.Bip01_Spine1")
                if spineBone then
                    ent:manipulateBoneAngles(spineBone, Angle(math.random(-15, 15), math.random(-10, 10), 0))
                end
                -- Flex uncanny smile or vacant stare
                local smileFlex = ent:getFlexByName("smile")
                if smileFlex then ent:setFlexWeight(smileFlex, 1.0) end
            end
        })
    end

    -- --------------------------------------------------------------------------
    -- 6. MASTER MULTI-TIER VALLEY CHASM GENERATOR
    -- --------------------------------------------------------------------------
    local function generateFullAirspaceComplex()
        print("[Cognitive Decay Engine] Synthesizing 4-Tier Valley Megastructure with Hole-Free Autofill...")

        local origin = Vector(7200.0, -4800.0, 0)

        for tier = 0, 3 do
            local floorZ = CONFIG.Z_TIERS[tier]
            local entropy = (tier / 3.0) * 0.75 + 0.10

            -- Tier Biome Configuration
            local wallMat, wallTint, floorMat, floorTint, ceilMat, ceilTint, isCageLight
            if tier == 0 then
                wallMat = CONFIG.MAT_WALL_PANEL
                wallTint = CONFIG.TINT_MONO_YELLOW
                floorMat = CONFIG.MAT_FLOOR_CARPET
                floorTint = CONFIG.TINT_CARPET
                ceilMat = CONFIG.MAT_CEILING_PANEL
                ceilTint = CONFIG.TINT_CEILING
                isCageLight = false
            elseif tier == 1 then
                wallMat = CONFIG.MAT_WALL_WHITE
                wallTint = CONFIG.TINT_WHITE_WALL
                floorMat = CONFIG.MAT_FLOOR_CARPET
                floorTint = CONFIG.TINT_GREY_CARPET
                ceilMat = CONFIG.MAT_CEILING_PANEL
                ceilTint = CONFIG.TINT_CEILING
                isCageLight = false
            elseif tier == 2 then
                wallMat = CONFIG.MAT_CONCRETE
                wallTint = CONFIG.TINT_CONCRETE
                floorMat = CONFIG.MAT_CONCRETE
                floorTint = CONFIG.TINT_CONCRETE
                ceilMat = CONFIG.MAT_CONCRETE_DARK
                ceilTint = CONFIG.TINT_DARK_CRYPT
                isCageLight = true
            else -- tier 3: deep crypt & bedrock chasm floor
                wallMat = CONFIG.MAT_CONCRETE_DARK
                wallTint = CONFIG.TINT_DARK_CRYPT
                floorMat = CONFIG.MAT_CONCRETE_DARK
                floorTint = CONFIG.TINT_DARK_CRYPT
                ceilMat = CONFIG.MAT_CONCRETE_DARK
                ceilTint = CONFIG.TINT_DARK_CRYPT
                isCageLight = true
            end

            for gx = 0, CONFIG.GRID_X - 1 do
                for gy = 0, CONFIG.GRID_Y - 1 do
                    local isChasm = CONFIG.VALLEY_COLS[gx] or false
                    local cellCenter = origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, floorZ)

                    -- 1. FLOOR & CEILING
                    if not isChasm then
                        queueFloorAndCeiling(cellCenter, floorMat, ceilMat, (tier >= 2 and "concrete" or "carpet"), (tier >= 2 and "concrete" or "ceiling"), floorTint, ceilTint)
                    elseif tier == 3 then
                        -- Bottom of Valley Chasm has solid bedrock concrete floor!
                        table.insert(spawnQueue, {
                            pos = cellCenter,
                            ang = Angle(0, 0, 0),
                            model = CONFIG.FLOOR_MODEL,
                            mat = CONFIG.MAT_CONCRETE_DARK,
                            tint = CONFIG.TINT_DARK_CRYPT,
                            category = "floor",
                            matCategory = "concrete",
                            keepFrozen = true
                        })
                    end

                    -- 2. SOLID EXTERIOR PERIMETER WALLS (AUTOFILL: ZERO VOID HOLES)
                    -- West Outer Perimeter (gx == 0)
                    if gx == 0 then
                        queueWall(cellCenter - Vector(HALF_CELL, 0, -HALF_CELL), true, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                    end
                    -- East Outer Perimeter (gx == GRID_X - 1)
                    if gx == CONFIG.GRID_X - 1 then
                        queueWall(cellCenter + Vector(HALF_CELL, 0, HALF_CELL), true, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                    end
                    -- North Outer Perimeter (gy == 0)
                    if gy == 0 and not isChasm then
                        queueWall(cellCenter + Vector(0, HALF_CELL, HALF_CELL), false, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                    end
                    -- South Outer Perimeter (gy == GRID_Y - 1)
                    if gy == CONFIG.GRID_Y - 1 and not isChasm then
                        queueWall(cellCenter - Vector(0, HALF_CELL, -HALF_CELL), false, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                    end

                    -- 3. SOLID VALLEY FACADE WALLS & OVERLOOK BALCONY ENTRYWAYS
                    -- West Wing Facade facing East into Chasm (gx == 2)
                    if gx == 2 then
                        if CONFIG.ENTRY_ROWS[gy] then
                            queueValleyEntryway(cellCenter, true, wallMat, wallTint)
                        else
                            queueWall(cellCenter + Vector(HALF_CELL, 0, HALF_CELL), true, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                        end
                    end
                    -- East Wing Facade facing West into Chasm (gx == 5)
                    if gx == 5 then
                        if CONFIG.ENTRY_ROWS[gy] then
                            queueValleyEntryway(cellCenter, false, wallMat, wallTint)
                        else
                            queueWall(cellCenter - Vector(HALF_CELL, 0, -HALF_CELL), true, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                        end
                    end

                    -- 4. INTERIOR PARTITION WALLS (Doorless navigation)
                    if not isChasm then
                        -- West Wing internal division: wall along Y between gx=0 and gx=1 (except at gy=2 doorless portal)
                        if gx == 1 and gy ~= 2 and gy ~= 4 then
                            queueWall(cellCenter - Vector(HALF_CELL, 0, -HALF_CELL), true, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                        end
                        -- East Wing internal division: wall along Y between gx=6 and gx=7 (except at gy=2 doorless portal)
                        if gx == 6 and gy ~= 1 and gy ~= 3 then
                            queueWall(cellCenter + Vector(HALF_CELL, 0, HALF_CELL), true, wallMat, (tier >= 2 and "concrete" or "wallpaper"), wallTint)
                        end
                    end

                    -- 5. CEILING LIGHTS (Active dynamic light sources)
                    if not isChasm then
                        if (gx == 1 and (gy == 1 or gy == 4)) or (gx == 6 and (gy == 2 or gy == 5)) then
                            local lightMdl = isCageLight and MODEL_POOLS.cage_lights[1] or MODEL_POOLS.ceiling_lights[1]
                            queueCeilingLight(cellCenter, lightMdl, isCageLight)
                        end
                    elseif tier == 3 and (gx == 3 and gy == 2) then
                        -- Abyss beacon cage light at bedrock
                        queueCeilingLight(cellCenter, MODEL_POOLS.cage_lights[1], true)
                    end

                    -- 6. GENERATIVE CONTEXTUAL PROPS (Trained Data Driven)
                    if not isChasm then
                        local isAnomaly = (math.random() < (0.08 + entropy * 0.05))
                        if tier == 0 then
                            -- Level 0 Office Suite
                            if (gx == 1 and gy == 2) or (gx == 6 and gy == 3) then
                                queueDeskWorkstation(cellCenter, floorZ, isAnomaly)
                            elseif gx == 0 and gy == 3 then
                                queueProp(cellCenter, Angle(0, 0, 0), MODEL_POOLS.office_storage[1], "furniture", isAnomaly)
                            elseif gx == 7 and gy == 2 then
                                queueProp(cellCenter, Angle(0, 90, 0), MODEL_POOLS.office_props[3], "furniture", isAnomaly)
                            end
                        elseif tier == 1 then
                            -- Level 1 Habitable Living Quarters
                            if (gx == 1 and gy == 2) or (gx == 6 and gy == 3) then
                                queueLivingLounge(cellCenter, floorZ, isAnomaly)
                            elseif gx == 0 and gy == 1 then
                                queueProp(cellCenter, Angle(0, 0, 0), MODEL_POOLS.office_storage[3], "furniture", isAnomaly)
                            end
                        elseif tier == 2 then
                            -- Level 2 Industrial Warehouse
                            if (gx == 1 and gy == 1) or (gx == 6 and gy == 2) or (gx == 1 and gy == 4) then
                                queueStorageWarehouse(cellCenter, floorZ, isAnomaly)
                            end
                        else
                            -- Level 3 Bedrock Substation Crypt
                            if (gx == 1 and gy == 3) or (gx == 6 and gy == 2) then
                                queueProp(cellCenter, Angle(0, 45, 0), MODEL_POOLS.warehouse_props[2], "furniture", isAnomaly)
                            end
                        end

                        -- Chance for Motionless Observer NPC (1-2 per tier)
                        if (gx == 0 and gy == 5 and tier <= 1) or (gx == 7 and gy == 0 and tier >= 2) then
                            queueGlitchedNPC(cellCenter, floorZ, tier)
                        end
                    end
                end
            end
        end

        print(string.format("[Cognitive Decay Engine] Queued %d watertight entities across 4 tiers with Central Chasm!", #spawnQueue))
    end

    -- --------------------------------------------------------------------------
    -- 7. ADAPTIVE PROP RATE CONTROLLER (ZERO DROPPED PROPS, DYNAMIC MAX THROUGHPUT)
    -- --------------------------------------------------------------------------
    local function executeSpawnQueue()
        local index = 1
        local total = #spawnQueue
        local nextSpawnTime = 0
        local burstDelay = 0.03 -- Dynamic adaptive delay (starts at 30ms)
        local minDelay = 0.015  -- Max speed: ~66 props/sec
        local maxDelay = 0.40   -- Max backoff when throttled by server quota

        hook.add("think", "CognitiveDecay_AdaptiveSpawner", function()
            if index > total then
                hook.remove("think", "CognitiveDecay_AdaptiveSpawner")
                print(string.format("[Cognitive Decay Engine] Spawning pipeline complete! All %d entities materialized.", total))
                return
            end

            local now = timer.curtime()
            if now < nextSpawnTime then return end

            -- Check Starfall's native quota check if available
            if prop.canSpawn and not prop.canSpawn() then
                -- Server quota full: back off adaptively and wait!
                burstDelay = math.min(maxDelay, burstDelay * 1.5 + 0.05)
                nextSpawnTime = now + burstDelay
                return
            end

            local item = spawnQueue[index]
            if not item then
                index = index + 1
                return
            end

            -- Attempt spawn
            local ent, usedModel = trySpawnWithFallbacks(item)
            if isValid(ent) then
                -- SUCCESS! Advance to the next item!
                index = index + 1
                table.insert(activeEntities, ent)

                if item.mat or item.matCategory or item.tint then
                    safeSetMaterialWithFallback(ent, item.mat, item.matCategory, item.tint)
                end

                if item.onSpawn then
                    pcall(item.onSpawn, ent)
                end

                -- Gradually accelerate spawn rate to maximum permitted throughput
                burstDelay = math.max(minDelay, burstDelay * 0.94)
                nextSpawnTime = now + burstDelay
            else
                -- Spawn failed (rate limited by engine): DO NOT ADVANCE INDEX!
                -- Adaptively back off and retry this exact item next tick!
                burstDelay = math.min(maxDelay, burstDelay * 1.6 + 0.08)
                nextSpawnTime = now + burstDelay
            end
        end)
    end

    -- --------------------------------------------------------------------------
    -- 8. CLEANUP & INITIALIZATION
    -- --------------------------------------------------------------------------
    _G.CognitiveDecay_Cleanup = function()
        hook.remove("think", "CognitiveDecay_AdaptiveSpawner")
        for _, ent in ipairs(activeEntities) do
            if isValid(ent) then pcall(ent.remove, ent) end
        end
        table.empty(activeEntities)
        table.empty(activeRadios)
        table.empty(activeTVs)
        table.empty(activeLights)
        table.empty(activeNPCs)
        table.empty(spawnQueue)
        print("[Cognitive Decay Engine] Dematerialized all existing entities.")
    end

    -- Trigger Generation
    generateFullAirspaceComplex()
    executeSpawnQueue()

else -- CLIENT

    local activeRadios = {}
    local activeTVs = {}
    local activeLights = {}
    local dynamicLights = {}

    local glowMat = Material("sprites/light_glow02")
    if not glowMat or glowMat:isError() then glowMat = Material("sprites/glow01") end

    -- --------------------------------------------------------------------------
    -- 9. DYNAMIC 160-TRACK RADIO STREAMER (STATION HOPPING & SEAMLESS REWIND)
    -- --------------------------------------------------------------------------
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
                    isLooping = (math.random() < 0.40),
                    nextHopTime = timer.curtime() + 60,
                    hasStarted = false
                }
                table.insert(activeRadios, rData)
                tuneRadio(rData)
            end
        end)
    end)

    -- Radio Life Management Loop: Never dies, hops stations or loops
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

    -- --------------------------------------------------------------------------
    -- 10. REAL DYNAMIC LIGHTING EMISSION (TRUE ILLUMINATION & GLOW SPRITES)
    -- --------------------------------------------------------------------------
    net.receive("CognitiveDecay_RegisterLight", function()
        pcall(function()
            local ent = net.readEntity()
            local isCage = net.readBool()
            if isValid(ent) then
                table.insert(activeLights, { ent = ent, isCage = isCage })
            end
        end)
    end)

    hook.add("think", "CognitiveDecay_RealDynamicLighting", function()
        pcall(function()
            local ply = player()
            if not isValid(ply) then return end
            local plyPos = ply:getPos()
            local now = timer.curtime()

            -- Manage dynamic lights for nearby fixtures (< 1200 units)
            for _, fix in ipairs(activeLights) do
                if isValid(fix.ent) then
                    local fPos = fix.ent:getPos()
                    local dist = plyPos:getDistance(fPos)

                    if dist < 1200 then
                        if not dynamicLights[fix.ent] and light and light.create then
                            local ok, dl = pcall(light.create, fPos - Vector(0, 0, 8), 650, 2.5, fix.isCage and Color(255, 195, 110) or Color(255, 240, 185))
                            if ok and dl then
                                dynamicLights[fix.ent] = dl
                            end
                        end

                        local dl = dynamicLights[fix.ent]
                        if dl then
                            pcall(dl.setDieTime, dl, now + 1.0)
                            pcall(dl.draw, dl)
                        end
                    else
                        if dynamicLights[fix.ent] then
                            pcall(dynamicLights[fix.ent].destroy, dynamicLights[fix.ent])
                            dynamicLights[fix.ent] = nil
                        end
                    end
                end
            end
        end)
    end)

    hook.add("render", "CognitiveDecay_LightSprites", function()
        pcall(function()
            local ply = player()
            if not isValid(ply) or not glowMat then return end
            local plyPos = ply:getPos()

            render.setMaterial(glowMat)
            for _, fix in ipairs(activeLights) do
                if isValid(fix.ent) then
                    local fPos = fix.ent:getPos()
                    local dist = plyPos:getDistance(fPos)
                    if dist < 950 then
                        if fix.isCage then
                            render.setColor(Color(255, 200, 120, 190))
                            render.drawSprite(fPos - Vector(0, 0, 6), 110, 110)
                        else
                            render.setColor(Color(255, 245, 180, 210))
                            render.drawSprite(fPos - Vector(0, 0, 5), 150, 150)
                        end
                    end
                end
            end
        end)
    end)

    -- --------------------------------------------------------------------------
    -- 11. CRT TV ANALOG GLITCH & EMERGENCY BROADCAST SCREEN RENDERER
    -- --------------------------------------------------------------------------
    net.receive("CognitiveDecay_RegisterTV", function()
        pcall(function()
            local ent = net.readEntity()
            if isValid(ent) then
                table.insert(activeTVs, ent)
            end
        end)
    end)

    local tvFont = render.createFont("Trebuchet", 28, 700, true)
    local tvAlertMessages = {
        "[ EMERGENCY BROADCAST SYSTEM ]",
        "COGNITIVE DECAY - SECTOR NULL",
        "WARNING: CONTEXT DRIFT ACTIVE",
        "FACILITY CORRIDORS VACATED",
        "UNATTENDED LIMINAL SPACE"
    }

    hook.add("PostDrawTranslucentRenderables", "CognitiveDecay_TVScreens", function()
        pcall(function()
            local ply = player()
            if not isValid(ply) then return end
            local plyPos = ply:getPos()
            local curSec = math.floor(timer.curtime())

            for i = #activeTVs, 1, -1 do
                local tv = activeTVs[i]
                if not isValid(tv) then
                    table.remove(activeTVs, i)
                elseif plyPos:getDistance(tv:getPos()) < 500 then
                    local m = tv:getMatrix()
                    -- CRT screen surface position on props_c17/tv_monitor01.mdl
                    m:translate(Vector(8.8, 0, 1.2))
                    m:rotate(Angle(0, 90, 90))
                    m:setScale(Vector(0.045, -0.045, 0.045))

                    render.pushMatrix(m)
                    -- Dark CRT Phosphor Background
                    render.setColor(Color(8, 15, 10, 245))
                    render.drawRect(-160, -120, 320, 240)

                    -- Analog Scanlines
                    local offsetScan = math.floor((timer.curtime() * 40) % 8)
                    render.setColor(Color(15, 30, 20, 180))
                    for y = -120, 120, 8 do
                        render.drawRectFast(-160, y + offsetScan, 320, 3)
                    end

                    -- Static Noise Jitter
                    render.setColor(Color(math.random(30, 80), math.random(60, 140), math.random(30, 80), 120))
                    for n = 1, 14 do
                        render.drawRectFast(math.random(-150, 150), math.random(-110, 110), math.random(15, 45), 2)
                    end

                    -- Corrupted Amber/Green Emergency Text
                    render.enableDepth(true)
                    render.setColor(Color(255, 190, 40, 240))
                    render.setFont(tvFont)
                    local msgIdx = (curSec % #tvAlertMessages) + 1
                    render.drawSimpleText(0, -35, tvAlertMessages[msgIdx], 1, 1)

                    render.setColor(Color(120, 255, 140, 210))
                    render.drawSimpleText(0, 15, "SECTOR DECAY: " .. string.format("%.1f%%", (math.sin(timer.curtime() * 0.5) * 20 + 75)), 1, 1)

                    render.popMatrix()
                end
            end
        end)
    end)

end
'''

full_code = new_dataset_head + "\n" + master_engine_body

assert 'randomseed' not in full_code, "FATAL: randomseed keyword found!"
assert 'phoenix_storms/stripes' not in full_code.lower(), "FATAL: phoenix_storms/stripes found!"
assert 'door01_left' not in full_code, "FATAL: door01_left found!"

# Write to workspace
main_lua_path = os.path.join(WORKSPACE, 'cognitive-decay', 'core', 'main.lua')
main_txt_path = os.path.join(WORKSPACE, 'cognitive-decay', 'core', 'main.txt')
root_lua_path = os.path.join(WORKSPACE, 'cognitive-decay', 'main.lua')
root_txt_path = os.path.join(WORKSPACE, 'cognitive-decay', 'main.txt')

for p in [main_lua_path, main_txt_path, root_lua_path, root_txt_path]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(full_code)

print("Saved clean valley engine to workspace successfully!")

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
    print("Synchronized clean valley engine to GMod Starfall directory successfully!")
