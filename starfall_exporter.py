"""
StarfallEx Lua Code Exporter.
Translates generated room sequences or live dynamic brain logic into StarfallEx Lua chips.
Spawns rooms as holograms, dynamic lights, and sound loops.
"""

from typing import List, Dict
import json

class StarfallLuaExporter:
    @staticmethod
    def export_room_sequence_chip(rooms: List[Dict], chip_name: str = "Backrooms Cognitive Hallucination") -> str:
        """
        Exports a generated room sequence as an interactive StarfallEx Lua script.
        """
        # Convert rooms data to clean JSON-compatible Lua structure
        rooms_json = json.dumps(rooms, indent=2)

        lua_code = f"""--@name {chip_name}
--@author Cognitive Decay Engine
--@shared

-- Generated from Fallible Machine Brain
-- Simulating Context Loss & Reality Breakdown

if SERVER then
    local roomSpacing = 300
    local origin = chip():getPos() + Vector(0, 0, 10)
    
    local spawnedHolograms = {{}}
    local roomData = {rooms_json}

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
        local wallOffsets = {{
            {{ pos = Vector(150, 0, 75), ang = Angle(0, 0, 90) }},
            {{ pos = Vector(-150, 0, 75), ang = Angle(0, 0, 90) }},
            {{ pos = Vector(0, 150, 75), ang = Angle(0, 90, 90) }},
            {{ pos = Vector(0, -150, 75), ang = Angle(0, -90, 90) }}
        }}

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
"""
        return lua_code
