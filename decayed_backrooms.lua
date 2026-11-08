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
      "TAG_COLLISION: Looked for ['flat_surface', 'furniture', 'work'], but locked onto 'work' -> grabbed Office Desk!",
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
      "TAG_COLLISION: Looked for ['floor_covering', 'horizontal'], but locked onto 'floor_covering' -> grabbed Damp Commercial Carpet!",
      "NORMAL: Matched Fluorescent Ceiling Light Fixture for biome office.",
      "TAG_COLLISION: Looked for ['flat_surface', 'furniture', 'work'], but locked onto 'work' -> grabbed Office Desk!",
      "NORMAL: Matched Office Chair for biome office.",
      "NORMAL: Matched CRT Computer Monitor for biome office."
    ]
  },
  {
    "room_index": 4,
    "confusion_level": 0.8,
    "biome_state": "BIOME_DRIFT (office -> subway)",
    "elements": [
      {
        "type": "wall",
        "id": "models/props_wasteland/controlroom_desk001b.mdl",
        "name": "Control Terminal"
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
        "id": "materials/carpet/office_carpet_damp_01",
        "name": "Damp Commercial Carpet",
        "dimensions": [
          128.0,
          128.0,
          8.0
        ]
      },
      {
        "type": "secondary_furniture",
        "id": "models/props_lab/monitor02.mdl",
        "name": "CRT Computer Monitor",
        "dimensions": [
          18.0,
          18.0,
          16.0
        ]
      },
      {
        "type": "tech_accessory",
        "id": "models/props_wasteland/light_caged01a.mdl",
        "name": "Industrial Caged Lamp",
        "dimensions": [
          16.0,
          16.0,
          16.0
        ]
      }
    ],
    "logs": [
      "MEMORY_STUCK: Reused Control Terminal due to token fixation.",
      "NORMAL: Matched Damp Commercial Carpet for biome subway.",
      "TAG_COLLISION: Looked for ['light_source', 'ceiling_anchored'], but locked onto 'light_source' -> grabbed Industrial Caged Lamp!",
      "MEMORY_STUCK: Reused Damp Commercial Carpet due to token fixation.",
      "MEMORY_STUCK: Reused CRT Computer Monitor due to token fixation.",
      "MEMORY_STUCK: Reused Industrial Caged Lamp due to token fixation."
    ]
  },
  {
    "room_index": 5,
    "confusion_level": 1.0,
    "biome_state": "BIOME_DRIFT (subway -> subway)",
    "elements": [
      {
        "type": "wall",
        "id": "materials/concrete/warehouse_wall_c17",
        "name": "Raw Concrete Wall"
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
        "id": "models/props_junk/wood_pallet001a.mdl",
        "name": "Wood Pallet",
        "dimensions": [
          48.0,
          48.0,
          8.0
        ]
      },
      {
        "type": "secondary_furniture",
        "id": "models/props_interiors/Bed_Hospital.mdl",
        "name": "Hospital Bed",
        "dimensions": [
          40.0,
          80.0,
          36.0
        ]
      },
      {
        "type": "tech_accessory",
        "id": "models/props_junk/wood_pallet001a.mdl",
        "name": "Wood Pallet",
        "dimensions": [
          48.0,
          48.0,
          8.0
        ]
      }
    ],
    "logs": [
      "TAG_COLLISION: Looked for ['wall_covering', 'vertical'], but locked onto 'wall_covering' -> grabbed Raw Concrete Wall!",
      "TAG_COLLISION: Looked for ['floor_covering', 'horizontal'], but locked onto 'floor_covering' -> grabbed Damp Commercial Carpet!",
      "MEMORY_STUCK: Reused Fluorescent Ceiling Light Fixture due to token fixation.",
      "TAG_COLLISION: Looked for ['flat_surface', 'furniture', 'work'], but locked onto 'flat_surface' -> grabbed Wood Pallet!",
      "TAG_COLLISION: Looked for ['seating', 'furniture', 'rest'], but locked onto 'seating' -> grabbed Hospital Bed!",
      "MEMORY_STUCK: Reused Wood Pallet due to token fixation."
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

        -- Spawn Props
        for i = 4, #room.elements do
            local elem = room.elements[i]
            if elem and string.find(elem.id, ".mdl") then
                local propPos = origin + roomOffset + Vector(math.random(-80, 80), math.random(-80, 80), 0)
                local propAng = Angle(0, math.random(0, 360), 0)
                
                -- Severe confusion glitch: inverted or sideways props
                if room.confusion_level > 0.7 and math.random() > 0.5 then
                    propAng = propAng + Angle(180, 0, 0)
                    propPos = propPos + Vector(0, 0, 40)
                end

                local pHolo = holograms.create(propPos, propAng, elem.id, Vector(1,1,1))
                table.insert(spawnedHolograms, pHolo)
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
