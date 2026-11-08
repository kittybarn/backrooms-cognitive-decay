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
"""
        return lua_code
