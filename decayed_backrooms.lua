--@name Backrooms Cognitive Hallucination
--@author Cognitive Decay Engine
--@shared

-- Generated from Fallible Machine Brain
-- Simulating Context Loss & Reality Breakdown

if SERVER then
    local roomSpacing = 300
    local origin = chip():getPos() + Vector(0, 0, 10)
    
    local spawnedHolograms = {}
    local roomData = [
  {
    "room_index": 1,
    "confusion_level": 0.2,
    "biome_state": "STABLE (office)",
    "elements": [
      {
        "type": "wall",
        "id": "materials/plaster/office_wallpaper_yellow",
        "name": "Yellow Mono Wallpaper"
      },
      {
        "type": "floor",
        "id": "materials/carpet/office_carpet_damp_01",
        "name": "Damp Commercial Carpet"
      },
      {
        "type": "light",
        "id": "models/props_wasteland/light_caged01a.mdl",
        "name": "Industrial Caged Lamp"
      },
      {
        "type": "primary_furniture",
        "id": "models/props_wasteland/controlroom_desk001b.mdl",
        "name": "Control Terminal",
        "dimensions": [
          72.0,
          36.0,
          48.0
        ]
      },
      {
        "type": "secondary_furniture",
        "id": "models/props_c17/FurnitureChair001a.mdl",
        "name": "Office Chair",
        "dimensions": [
          24.0,
          24.0,
          36.0
        ]
      },
      {
        "type": "tech_accessory",
        "id": "models/props_lab/monitor02.mdl",
        "name": "CRT Computer Monitor",
        "dimensions": [
          18.0,
          18.0,
          16.0
        ]
      }
    ],
    "logs": [
      "NORMAL: Matched Yellow Mono Wallpaper for biome office.",
      "NORMAL: Matched Damp Commercial Carpet for biome office.",
      "TAG_COLLISION: Looked for ['light_source', 'ceiling_anchored'], but locked onto 'light_source' -> grabbed Industrial Caged Lamp!",
      "TAG_COLLISION: Looked for ['flat_surface', 'furniture', 'work'], but locked onto 'flat_surface' -> grabbed Control Terminal!",
      "NORMAL: Matched Office Chair for biome office.",
      "NORMAL: Matched CRT Computer Monitor for biome office."
    ]
  },
  {
    "room_index": 2,
    "confusion_level": 0.4,
    "biome_state": "STABLE (office)",
    "elements": [
      {
        "type": "wall",
        "id": "materials/plaster/office_wallpaper_yellow",
        "name": "Yellow Mono Wallpaper"
      },
      {
        "type": "floor",
        "id": "materials/carpet/office_carpet_damp_01",
        "name": "Damp Commercial Carpet"
      },
      {
        "type": "light",
        "id": "models/props_c17/light_fluorescent01a.mdl",
        "name": "Fluorescent Ceiling Light Fixture"
      },
      {
        "type": "primary_furniture",
        "id": "models/props_c17/FurnitureDesk001a.mdl",
        "name": "Office Desk",
        "dimensions": [
          64.0,
          36.0,
          30.0
        ]
      },
      {
        "type": "secondary_furniture",
        "id": "models/props_c17/FurnitureChair001a.mdl",
        "name": "Office Chair",
        "dimensions": [
          24.0,
          24.0,
          36.0
        ]
      },
      {
        "type": "tech_accessory",
        "id": "models/props_lab/monitor02.mdl",
        "name": "CRT Computer Monitor",
        "dimensions": [
          18.0,
          18.0,
          16.0
        ]
      }
    ],
    "logs": [
      "NORMAL: Matched Yellow Mono Wallpaper for biome office.",
      "NORMAL: Matched Damp Commercial Carpet for biome office.",
      "NORMAL: Matched Fluorescent Ceiling Light Fixture for biome office.",
      "NORMAL: Matched Office Desk for biome office.",
      "NORMAL: Matched Office Chair for biome office.",
      "NORMAL: Matched CRT Computer Monitor for biome office."
    ]
  },
  {
    "room_index": 3,
    "confusion_level": 0.6,
    "biome_state": "BIOME_DRIFT (office -> archive)",
    "elements": [
      {
        "type": "wall",
        "id": "models/props_c17/FurnitureDesk001a.mdl",
        "name": "Office Desk"
      },
      {
        "type": "floor",
        "id": "materials/concrete/floor_concrete01",
        "name": "Stained Concrete Floor"
      },
      {
        "type": "light",
        "id": "models/props_c17/FurnitureDesk001a.mdl",
        "name": "Office Desk"
      },
      {
        "type": "primary_furniture",
        "id": "models/props_c17/FurnitureDesk001a.mdl",
        "name": "Office Desk",
        "dimensions": [
          64.0,
          36.0,
          30.0
        ]
      },
      {
        "type": "secondary_furniture",
        "id": "models/props_c17/FurnitureChair001a.mdl",
        "name": "Office Chair",
        "dimensions": [
          24.0,
          24.0,
          36.0
        ]
      },
      {
        "type": "tech_accessory",
        "id": "models/props_wasteland/controlroom_desk001b.mdl",
        "name": "Control Terminal",
        "dimensions": [
          72.0,
          36.0,
          48.0
        ]
      }
    ],
    "logs": [
      "MEMORY_STUCK: Reused Office Desk due to token fixation.",
      "TAG_COLLISION: Looked for ['floor_covering', 'horizontal'], but locked onto 'floor_covering' -> grabbed Stained Concrete Floor!",
      "MEMORY_STUCK: Reused Office Desk due to token fixation.",
      "NORMAL: Matched Office Desk for biome archive.",
      "NORMAL: Matched Office Chair for biome archive.",
      "TAG_COLLISION: Looked for ['technology', 'box', 'electronic'], but locked onto 'electronic' -> grabbed Control Terminal!"
    ]
  },
  {
    "room_index": 4,
    "confusion_level": 0.8,
    "biome_state": "STABLE (archive)",
    "elements": [
      {
        "type": "wall",
        "id": "materials/plaster/office_wallpaper_yellow",
        "name": "Yellow Mono Wallpaper"
      },
      {
        "type": "floor",
        "id": "materials/concrete/floor_concrete01",
        "name": "Stained Concrete Floor"
      },
      {
        "type": "light",
        "id": "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Car Skidding Sound Effect.mp3",
        "name": "Audio: car skidding sound effect"
      },
      {
        "type": "primary_furniture",
        "id": "models/props_c17/FurnitureDesk001a.mdl",
        "name": "Office Desk",
        "dimensions": [
          64.0,
          36.0,
          30.0
        ]
      },
      {
        "type": "secondary_furniture",
        "id": "models/props_c17/FurnitureChair001a.mdl",
        "name": "Office Chair",
        "dimensions": [
          24.0,
          24.0,
          36.0
        ]
      },
      {
        "type": "tech_accessory",
        "id": "models/props_c17/filecabinet02.mdl",
        "name": "Filing Cabinet",
        "dimensions": [
          24.0,
          30.0,
          54.0
        ]
      }
    ],
    "logs": [
      "NORMAL: Matched Yellow Mono Wallpaper for biome archive.",
      "TAG_COLLISION: Looked for ['floor_covering', 'horizontal'], but locked onto 'floor_covering' -> grabbed Stained Concrete Floor!",
      "MEMORY_STUCK: Reused Audio: car skidding sound effect due to token fixation.",
      "NORMAL: Matched Office Desk for biome archive.",
      "NORMAL: Matched Office Chair for biome archive.",
      "TAG_COLLISION: Looked for ['technology', 'box', 'electronic'], but locked onto 'box' -> grabbed Filing Cabinet!"
    ]
  },
  {
    "room_index": 5,
    "confusion_level": 1.0,
    "biome_state": "BIOME_DRIFT (archive -> basement)",
    "elements": [
      {
        "type": "wall",
        "id": "materials/plaster/office_wallpaper_yellow",
        "name": "Yellow Mono Wallpaper"
      },
      {
        "type": "floor",
        "id": "materials/plaster/office_wallpaper_yellow",
        "name": "Yellow Mono Wallpaper"
      },
      {
        "type": "light",
        "id": "models/props_wasteland/light_caged01a.mdl",
        "name": "Industrial Caged Lamp"
      },
      {
        "type": "primary_furniture",
        "id": "models/props_c17/FurnitureDesk001a.mdl",
        "name": "Office Desk",
        "dimensions": [
          64.0,
          36.0,
          30.0
        ]
      },
      {
        "type": "secondary_furniture",
        "id": "models/props_c17/FurnitureChair001a.mdl",
        "name": "Office Chair",
        "dimensions": [
          24.0,
          24.0,
          36.0
        ]
      },
      {
        "type": "tech_accessory",
        "id": "models/props_c17/filecabinet02.mdl",
        "name": "Filing Cabinet",
        "dimensions": [
          24.0,
          30.0,
          54.0
        ]
      }
    ],
    "logs": [
      "TAG_COLLISION: Looked for ['wall_covering', 'vertical'], but locked onto 'wall_covering' -> grabbed Yellow Mono Wallpaper!",
      "MEMORY_STUCK: Reused Yellow Mono Wallpaper due to token fixation.",
      "TAG_COLLISION: Looked for ['light_source', 'ceiling_anchored'], but locked onto 'light_source' -> grabbed Industrial Caged Lamp!",
      "TAG_COLLISION: Looked for ['flat_surface', 'furniture', 'work'], but locked onto 'work' -> grabbed Office Desk!",
      "TAG_COLLISION: Looked for ['seating', 'furniture', 'rest'], but locked onto 'rest' -> grabbed Office Chair!",
      "TAG_COLLISION: Looked for ['technology', 'box', 'electronic'], but locked onto 'box' -> grabbed Filing Cabinet!"
    ]
  }
]

    local function spawnRoom(index, room)
        local roomOffset = Vector((index - 1) * roomSpacing, 0, 0)
        
        -- Create Floor
        local floorElem = room.elements[2]
        local floorHolo = holograms.create(origin + roomOffset, Angle(0,0,0), "models/hunter/plates/plate6x6.mdl", Vector(1,1,1))
        if floorElem then
            floorHolo:setMaterial(floorElem.id)
        end
        table.insert(spawnedHolograms, floorHolo)

        -- Create Walls (4 sides)
        local wallElem = room.elements[1]
        local wallMat = wallElem and wallElem.id or "materials/plaster/office_wallpaper_yellow"
        local wallOffsets = {
            { pos = Vector(150, 0, 75), ang = Angle(0, 0, 90) },
            { pos = Vector(-150, 0, 75), ang = Angle(0, 0, 90) },
            { pos = Vector(0, 150, 75), ang = Angle(0, 90, 90) },
            { pos = Vector(0, -150, 75), ang = Angle(0, -90, 90) }
        }

        for _, w in ipairs(wallOffsets) do
            -- If confusion is high, randomly skew or tilt wall angle
            local ang = w.ang
            if room.confusion_level > 0.5 and math.random() > 0.6 then
                ang = ang + Angle(math.random(-15, 15), math.random(-15, 15), 0)
            end
            local wallHolo = holograms.create(origin + roomOffset + w.pos, ang, "models/hunter/plates/plate6x3.mdl", Vector(1,1,1))
            wallHolo:setMaterial(wallMat)
            table.insert(spawnedHolograms, wallHolo)
        end

        -- Spawn Props with Spatial Affordance & Rare Anomalies
        for i = 4, #room.elements do
            local elem = room.elements[i]
            if elem and string.find(elem.id, ".mdl") then
                local propPos = origin + roomOffset + Vector(math.random(-80, 80), math.random(-80, 80), 0)
                local propAng = Angle(0, math.random(0, 360), 0)
                local propScale = Vector(1, 1, 1)
                local propColor = Color(255, 255, 255, 255)
                local renderFx = 0

                -- 1. SPATIAL AFFORDANCES: If it's a TV/Radio, place it ON the desk/table surface
                if elem.anchor == "on_top_of" or string.find(elem.id, "tv") or string.find(elem.id, "monitor") or string.find(elem.id, "reciever") then
                    propPos.z = propPos.z + 30.0 -- Sit on desk height
                end

                -- 2. UNCOMMON SCALE ANOMALY (~8-20% chance)
                if math.random() < (0.08 + (room.confusion_level * 0.15)) then
                    local scaleType = math.random(1, 4)
                    if scaleType == 1 then
                        propScale = Vector(1, 1, math.Rand(2.0, 3.5)) -- Stretched vertically (uncanny tall chair/TV)
                    elseif scaleType == 2 then
                        propScale = Vector(math.Rand(1.5, 2.2), 0.3, 1) -- Flattened sideways like a paper cutout
                    elseif scaleType == 3 then
                        propScale = Vector(0.3, 0.3, 0.3) -- Miniature prop
                    elseif scaleType == 4 then
                        propScale = Vector(2.8, 2.8, 2.8) -- Giant oversized anomaly
                    end
                end

                -- 3. RARE COLOR CORRUPTION (~4-10% chance)
                if math.random() < (0.04 + (room.confusion_level * 0.08)) then
                    local colorRoll = math.random(1, 3)
                    if colorRoll == 1 then
                        propColor = Color(30, 255, 90, 255) -- Radioactive decay green
                    elseif colorRoll == 2 then
                        propColor = Color(30, 30, 30, 255)   -- Scorched void black
                    elseif colorRoll == 3 then
                        propColor = Color(20, 220, 255, 255) -- Inverted negative cyan
                    end
                end

                -- 4. ULTRA-RARE RENDER FX GLITCH (~2-5% chance)
                if math.random() < (0.02 + (room.confusion_level * 0.05)) then
                    renderFx = math.random(1, 2) == 1 and 16 or 3 -- 16: PulseFast, 3: Hologram shimmer
                end

                local pHolo = holograms.create(propPos, propAng, elem.id, propScale)
                if pHolo then
                    pHolo:setColor(propColor)
                    if renderFx > 0 then
                        pcall(pHolo.setRenderFX, pHolo, renderFx)
                    end
                    table.insert(spawnedHolograms, pHolo)
                end
            end
        end
    end

    -- Sequential build loop
    for idx, room in ipairs(roomData) do
        timer.simple(idx * 0.2, function()
            spawnRoom(idx, room)
            print("[Brain Decay] Materialized Room " .. idx .. " | Confusion: " .. room.confusion_level)
        end)
    end
end
