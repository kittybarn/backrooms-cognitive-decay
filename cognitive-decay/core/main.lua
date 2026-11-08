--@name cognitive-decay/core/main
--@author kittybarn & Antigravity
--@shared
-- ==============================================================================
-- PROJECT COGNITIVE DECAY - DYNAMIC PRODUCTION ENGINE (V1.0)
-- 
-- Official Repository:
--   https://github.com/kittybarn/backrooms-cognitive-decay
--
-- Targeted Spatial Volume:
--   Corner 1: Vector(6441.24, -4107.08, -12576.3)
--   Corner 2: Vector(16306.50, -16307.30, -16255.70)
--   Spanning: X = 9,865 units | Y = 12,200 units | Z = 3,679 units
-- 
-- 100% Dynamic Core Features:
--  1. Fully Dynamic Audio Streaming:
--     Directly streams 163 tracks from github:kittybarn/backrooms-cognitive-decay/main/audio/
--     using Starfall bass.loadURL. Biome & decay-driven (Still Life, Async Research,
--     The Complex, numbers stations, telephony disconnects, analog horror).
--  2. Fully Dynamic NPC Bone & Face Corruptions:
--     ZERO hardcoded angles. Mannequin neck rolls, pitch tilts, and face flex weights
--     are randomized and dynamically calculated on spawn from entanglement matrices.
--  3. Multi-Biome Spatial Maximization:
--     - Level 0: Main Liminal Office (21 wallpapers, 10 carpets, yellow & floral)
--     - Level 1: Industrial Concrete Crypt (Z = -16,250, pallets, oil drums, cage lights)
--     - Level 2: Institutional Ward & Mezzanine (Z = -15,870, tiles, beds, lockers)
--  4. Watertight Boundary Filler Solver:
--     Detects horizons and caps outer faces with flush walls and 100% ceiling canopies.
--  5. Zero-Gap Seamless Transit Ramps:
--     Mathematically derived 29.965° slope connecting tiers with 0.00 gap.
--  6. Sudden Floor Collapse Pitfalls:
--     Floor drop shafts plunging players into the dark crypt below.
--  7. Map-Like Interactive Doors:
--     Spawns doorway apertures with models/props_c17/door01_left.mdl. Swings open on
--     player proximity or +USE with authentic Source sounds and entangled speeds.
--  8. Interactive Unfrozen Physics & Floor Traces:
--     Traced flush to carpet (+1.2 units) and unfreezes 60ms after settling.
--     Props are 100% interactive (kick chairs, push desks, knock radios off tables).
--  9. The Image 2 Anomaly:
--     Rare 2% chance for half-round table embedded 50% in drywall with PC tower on top.
-- 10. Atmospheric Darkness, Dense Fog & Half-Life 1 Xen Green Electric Beams.
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 1. EMBEDDED TRAINED KNOWLEDGE GRAPH (DATASET V2.0)
-- ------------------------------------------------------------------------------
local DATASET = {
    VERSION = "2.0.0",

    -- Categorized Prop Affordances
    PROPS = {
        surface_mount = {
            "models/props_lab/citizenradio.mdl",
            "models/breen_monitor.mdl",
            "models/combine_room/combine_monitor002.mdl",
            "models/combine_room/combine_monitor003a.mdl",
            "models/eli_monitor.mdl",
            "models/kleiner_monitor.mdl",
            "models/props/cs_militia/tv_console.mdl",
            "models/props/cs_office/coffee_mug.mdl",
            "models/props/cs_office/coffee_mug2.mdl",
            "models/props/cs_office/coffee_mug3.mdl",
            "models/props/cs_office/coffee_mug_p1.mdl",
            "models/props/cs_office/coffee_mug_p2.mdl",
            "models/props/cs_office/coffee_mug_p3.mdl",
            "models/props/cs_office/computer.mdl",
            "models/props/cs_office/computer_case.mdl",
            "models/props/cs_office/computer_caseb.mdl",
            "models/props/cs_office/computer_caseb_p1.mdl",
            "models/props/cs_office/computer_caseb_p1a.mdl",
            "models/props/cs_office/computer_caseb_p2.mdl",
            "models/props/cs_office/computer_caseb_p2a.mdl",
            "models/props/cs_office/computer_caseb_p3.mdl",
            "models/props/cs_office/computer_caseb_p3a.mdl",
            "models/props/cs_office/computer_caseb_p3b.mdl",
            "models/props/cs_office/computer_caseb_p4.mdl",
            "models/props/cs_office/computer_caseb_p4a.mdl",
            "models/props/cs_office/computer_caseb_p4b.mdl",
            "models/props/cs_office/computer_caseb_p5.mdl",
            "models/props/cs_office/computer_caseb_p5a.mdl",
            "models/props/cs_office/computer_caseb_p5b.mdl",
            "models/props/cs_office/computer_caseb_p6.mdl",
        },
        storage = {
            "models/props_c17/filecabinet02.mdl",
            "models/props/cs_italy/it_mkt_shelf1.mdl",
            "models/props/cs_militia/furniture_shelf01a.mdl",
            "models/props/cs_militia/gun_cabinet.mdl",
            "models/props/cs_militia/gun_cabinet_glass.mdl",
            "models/props/cs_militia/shelves.mdl",
            "models/props/cs_militia/shelves_wood.mdl",
            "models/props/cs_office/file_cabinet1.mdl",
            "models/props/cs_office/file_cabinet1_group.mdl",
            "models/props/cs_office/file_cabinet2.mdl",
            "models/props/cs_office/file_cabinet3.mdl",
            "models/props/cs_office/shelves_metal.mdl",
            "models/props/cs_office/shelves_metal1.mdl",
            "models/props/cs_office/shelves_metal2.mdl",
            "models/props/cs_office/shelves_metal3.mdl",
            "models/props/de_inferno/flower_barrel.mdl",
            "models/props/de_inferno/flower_barrel_p1.mdl",
            "models/props/de_inferno/flower_barrel_p10.mdl",
            "models/props/de_inferno/flower_barrel_p11.mdl",
            "models/props/de_inferno/flower_barrel_p2.mdl",
            "models/props/de_inferno/flower_barrel_p3.mdl",
            "models/props/de_inferno/flower_barrel_p4.mdl",
            "models/props/de_inferno/flower_barrel_p5.mdl",
            "models/props/de_inferno/flower_barrel_p6.mdl",
            "models/props/de_inferno/flower_barrel_p7.mdl",
            "models/props/de_inferno/flower_barrel_p8.mdl",
            "models/props/de_inferno/flower_barrel_p9.mdl",
            "models/props/de_inferno/wine_barrel.mdl",
            "models/props/de_inferno/wine_barrel_p1.mdl",
            "models/props/de_inferno/wine_barrel_p10.mdl",
        },
        flat_surface = {
            "models/props_interiors/table_folding.mdl",
            "models/props_c17/FurnitureDesk001a.mdl",
            "models/props_c17/FurnitureTable003a.mdl",
            "models/props_c17/FurnitureTable002a.mdl",
            "models/props_c17/FurnitureTable001a.mdl",
            "models/props/cs_italy/it_mkt_table1.mdl",
            "models/props/cs_italy/it_mkt_table2.mdl",
            "models/props/cs_italy/it_mkt_table3.mdl",
            "models/props/cs_militia/table_kitchen.mdl",
            "models/props/cs_militia/table_shed.mdl",
            "models/props/cs_militia/wood_table.mdl",
            "models/props/cs_office/table_coffee.mdl",
            "models/props/cs_office/table_coffee_p1.mdl",
            "models/props/cs_office/table_coffee_p2.mdl",
            "models/props/cs_office/table_coffee_p3.mdl",
            "models/props/cs_office/table_meeting.mdl",
            "models/props/de_prodigy/desk_console1.mdl",
            "models/props/de_prodigy/desk_console1a.mdl",
            "models/props/de_prodigy/desk_console1b.mdl",
            "models/props/de_prodigy/desk_console2.mdl",
            "models/props/de_prodigy/desk_console3.mdl",
            "models/props/de_tides/patio_table.mdl",
            "models/props/de_tides/patio_table2.mdl",
            "models/props/de_tides/restaurant_table.mdl",
            "models/props_forest/table_shed.mdl",
            "models/props_interiors/furniture_desk01a.mdl",
            "models/props_silo/desk_console1.mdl",
            "models/props_silo/desk_console1a.mdl",
            "models/props_silo/desk_console1b.mdl",
            "models/props_silo/desk_console2.mdl",
        },
        seating = {
            "models/props_interiors/chair_office2.mdl",
            "models/props_c17/FurnitureChair001a.mdl",
            "models/props/cs_militia/couch.mdl",
            "models/props/cs_militia/wood_bench.mdl",
            "models/props/cs_office/chair_office.mdl",
            "models/props/cs_office/sofa.mdl",
            "models/props/cs_office/sofa_chair.mdl",
            "models/props/de_inferno/bench_concrete.mdl",
            "models/props/de_inferno/bench_wood.mdl",
            "models/props/de_inferno/furniture_couch01a.mdl",
            "models/props/de_inferno/furniture_couch02a.mdl",
            "models/props/de_piranesi/pi_bench.mdl",
            "models/props/de_tides/patio_chair.mdl",
            "models/props/de_tides/patio_chair2.mdl",
            "models/props_c17/bench01a.mdl",
            "models/props_c17/chair02a.mdl",
            "models/props_c17/chair_kleiner03a.mdl",
            "models/props_c17/chair_office01a.mdl",
            "models/props_c17/chair_stool01a.mdl",
            "models/props_interiors/furniture_chair01a.mdl",
            "models/props_interiors/furniture_chair03a.mdl",
            "models/props_interiors/furniture_couch01a.mdl",
            "models/props_interiors/furniture_couch02a.mdl",
            "models/props_wasteland/cafeteria_bench001a.mdl",
            "models/props_wasteland/controlroom_chair001a.mdl",
        },
        light = {
            "models/props_wasteland/light_caged01a.mdl",
            "models/props_c17/light_fluorescent01a.mdl",
        },
    },

    -- Verified Liminal Materials
    MATERIALS = {
        wallpaper = {
            "cs_havana/plasterwallpaper004a",
            "cs_italy/wallpaper01",
            "cs_italy/wallpaper02",
            "cs_italy/wallpaper02a",
            "cs_italy/wallpaper03",
            "cs_italy/wallpaper1",
            "plaster/plasterwallpaper001a",
            "plaster/plasterwallpaper001a_c17",
            "plaster/plasterwallpaper003a",
            "plaster/plasterwallpaper004a",
            "plaster/plasterwallpaper005a",
            "plaster/plasterwallpaper006a",
            "plaster/plasterwallpaper006a_c17",
            "plaster/wallpaper001a",
            "plaster/wallpaper001b",
            "plaster/wallpaper002a",
            "plaster/wallpaper002b",
            "plaster/wallpaper003a",
            "plaster/wallpaper003b",
            "plaster/wallpaper004a",
            "plaster/wallpaper005a",
        },
        carpet = {
            "carpet/offflra",
            "carpet/offflrb",
            "cs_italy/carpet-sn03",
            "decals/tides_redcarpet",
            "props/carpetfloor001a",
            "props/carpetfloor003a",
            "props/carpetfloor004a",
            "props/carpetfloor006a",
            "props/carpetfloor007a",
            "props/carpetfloor008a",
        },
        ceiling = {
            "concrete/concreteceiling001a",
            "concrete/concreteceiling002a",
            "concrete/concreteceiling003a",
            "concrete/concreteceiling004a",
            "concrete/concreteceiling_bunker01a",
            "concrete/offceilinga",
            "concrete/offceilingb",
            "cs_havana/ceiling01",
            "cs_havana/ceiling02",
            "cs_italy/ceiling01",
            "de_cbble/woodceiling01",
            "de_chateau/ceiling01",
            "de_chateau/ceiling02",
            "de_nuke/nukceilingvent",
            "de_nuke/nuke_ceiling_01",
            "de_nuke/nuke_ceiling_02",
            "de_nuke/nuke_ceiling_facility_01",
            "de_piranesi/woodceiling01",
            "de_prodigy/ceiling01",
            "de_prodigy/ceiling02",
            "de_tides/tides_ceiling_a",
            "de_tides/tides_ceiling_b",
            "de_train/train_metalceiling_01",
            "de_train/train_metalceiling_02",
            "decals/offceilingvent",
        },
        tile = {
            "cs_italy/ptilefloor1",
            "de_dust/tilefloor01",
            "de_dust/tilefloor02",
            "metal/citadel_tilefloor016a",
            "metal/citadel_tilefloor016a_cheap",
            "metal/citadel_tilewall005a",
            "tile/ceilingtilea",
            "tile/prodceilingtilea",
            "tile/tilefloor001a",
            "tile/tilefloor001b",
            "tile/tilefloor001c",
            "tile/tilefloor003a",
            "tile/tilefloor005a",
            "tile/tilefloor007b",
            "tile/tilefloor008a",
            "tile/tilefloor009a",
            "tile/tilefloor009b",
            "tile/tilefloor010a",
            "tile/tilefloor010b",
            "tile/tilefloor010c",
            "tile/tilefloor010d",
            "tile/tilefloor011a",
            "tile/tilefloor012a",
            "tile/tilefloor012b",
            "tile/tilefloor013a",
        },
        plaster_walls = {
            "cs_havana/plasterwall003g",
            "cs_havana/plasterwall003h",
            "cs_havana/plasterwall027c",
            "cs_havana/plasterwall046a",
            "cs_havana/plasterwall1_3",
            "cs_havana/plasterwallpaper004a",
            "cs_italy/plaster_wall2_1",
            "cs_italy/plasterwall01",
            "cs_italy/plasterwall01a",
            "cs_italy/plasterwall01b",
            "cs_italy/plasterwall02",
            "cs_italy/plasterwall02a",
            "cs_italy/plasterwall02b",
            "cs_italy/plasterwall03",
            "cs_italy/plasterwall03a",
            "cs_italy/plasterwall03b",
            "cs_italy/plasterwall04",
            "cs_italy/plasterwall04a",
            "cs_italy/plasterwall04b",
            "de_train/de_train_plasterwall_01",
            "dev/dev_plasterwall001c",
            "plaster/cellarwall01b",
            "plaster/infplasterwall044b",
            "plaster/infplasterwall044d",
            "plaster/milwall001",
        },
        concrete = {
            "concrete/concretefloor001a",
            "concrete/concretefloor002a",
            "concrete/concretefloor002b",
            "concrete/concretefloor003c",
            "concrete/concretefloor005a",
            "concrete/concretefloor006a",
            "concrete/concretefloor007a",
            "concrete/concretefloor007a_c17",
            "concrete/concretefloor008a",
            "concrete/concretefloor008b",
            "concrete/concretefloor009a",
            "concrete/concretefloor009a_construct",
            "concrete/concretefloor010a",
            "concrete/concretefloor010b",
            "concrete/concretefloor011a",
            "concrete/concretefloor011a_c17",
            "concrete/concretefloor012a",
            "concrete/concretefloor013a",
            "concrete/concretefloor013a_c17",
            "concrete/concretefloor013b",
            "concrete/concretefloor013c",
            "concrete/concretefloor014a",
            "concrete/concretefloor015a",
            "concrete/concretefloor015a_c17",
            "concrete/concretefloor016a",
        },
        office = {
            "de_nuke/nuke_officedoor_01",
            "de_nuke/nuke_walloffice_01",
            "de_train/train_officetile_01",
            "overviews/cs_office",
            "overviews/cs_office_radar",
            "phoenix_storms/officewindow_1-1",
            "skybox/officebk",
            "skybox/officedn",
            "skybox/officeft",
            "skybox/officelf",
            "skybox/officert",
            "skybox/officeup",
            "vgui/achievements/win_map_cs_office",
            "vgui/achievements/win_map_cs_office_bw",
            "vgui/gfx/vgui/summary_maps/summary_cs_office",
        },
    },

    -- Audio Tracks & Soundscapes (by Cognitive Decay Stage)
    AUDIO = {
        vibe = {
            { name = "Backrooms (Original Score), Vol. 3 - Still Life.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%203%20-%20Still%20Life.mp3", weight = 10.0, eeriness = 9.2, type = "music" },
            { name = "Backrooms (Original Score), Vol. 1 - You're Done (Daisy Bell).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20You're%20Done%20(Daisy%20Bell).mp3", weight = 8.0, eeriness = 8.9, type = "music" },
            { name = "Backrooms (Original Score), Vol. 1 - Auditory Guidepost.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Auditory%20Guidepost.mp3", weight = 7.5, eeriness = 7.8, type = "music" },
            { name = "Backrooms (Original Score), Vol. 1 - Post-Traumatic Amnesia.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Post-Traumatic%20Amnesia.mp3", weight = 7.5, eeriness = 8.0, type = "music" },
            { name = "Backrooms (Original Score), Vol. 1 - Not Your Decision.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Not%20Your%20Decision.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 1 - Sealed Away.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Sealed%20Away.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 1 - The Only Thing That Matters (Demo).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20The%20Only%20Thing%20That%20Matters%20(Demo).mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - A Passage.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20A%20Passage.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Compromises.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Compromises.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Congratulations, Ivan.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Congratulations,%20Ivan.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - data not accessible.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20data%20not%20accessible.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Department of Energy.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Department%20of%20Energy.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Distant.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Distant.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Ghost.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Ghost.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Hanging Frame (Time Passages).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Hanging%20Frame%20(Time%20Passages).mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Instances.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Instances.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Malignant.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Malignant.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Non-Disclosure Agreement.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Non-Disclosure%20Agreement.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Old Objects in Quiet Rooms.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Old%20Objects%20in%20Quiet%20Rooms.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Person.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Person.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 2 - Remember.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Remember.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 3 - Do You Like Air Conditioning.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%203%20-%20Do%20You%20Like%20Air%20Conditioning.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 3 - For the Sake of Mankind, There Is Nothing More to Be Extracted.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%203%20-%20For%20the%20Sake%20of%20Mankind,%20There%20Is%20Nothing%20More%20to%20Be%20Extracted.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 3 - MidwesternTraumaLight.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%203%20-%20MidwesternTraumaLight.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
            { name = "Backrooms (Original Score), Vol. 3 - Off the Deep End.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%203%20-%20Off%20the%20Deep%20End.mp3", weight = 4.0, eeriness = 4.5, type = "music" },
        },
        drone = {
            { name = "Backrooms (Original Score), Vol. 1 - The Complex.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20The%20Complex.mp3", weight = 8.5, eeriness = 8.0, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - Async Research Institute.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Async%20Research%20Institute.mp3", weight = 8.0, eeriness = 7.5, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - Deeper Than The Walls.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Deeper%20Than%20The%20Walls.mp3", weight = 8.0, eeriness = 8.2, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - KV31.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20KV31.mp3", weight = 7.0, eeriness = 8.0, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - Missing Persons.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Missing%20Persons.mp3", weight = 7.0, eeriness = 7.5, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - Government Funding.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Government%20Funding.mp3", weight = 6.5, eeriness = 7.0, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - Hazmat.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Hazmat.mp3", weight = 6.5, eeriness = 7.5, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - Glacier.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Glacier.mp3", weight = 6.0, eeriness = 7.0, type = "ambient" },
            { name = "Backrooms (Original Score), Vol. 1 - Pipes.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%201%20-%20Pipes.mp3", weight = 6.0, eeriness = 7.2, type = "ambient" },
            { name = "apple-air-tag(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/apple-air-tag(1).mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "apple-air-tag.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/apple-air-tag.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "attention.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/attention.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "audio [vocals].mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/audio%20[vocals].mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - 4-PCH.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%204-PCH.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Basement Land.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Basement%20Land.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Cafe Bossa v1.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Cafe%20Bossa%20v1.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Capitol & McKee.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Capitol%20&%20McKee.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Cold Floor.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Cold%20Floor.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Complex.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Complex.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Dining Room.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Dining%20Room.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Feeling of a Door Imminently Remembered.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Feeling%20of%20a%20Door%20Imminently%20Remembered.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Furnished Dead End.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Furnished%20Dead%20End.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Furniture Lament.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Furniture%20Lament.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Handprint.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Handprint.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
            { name = "Backrooms (Original Soundtrack) - Homothet.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Soundtrack)%20-%20Homothet.mp3", weight = 2.0, eeriness = 5.0, type = "ambient" },
        },
        telephony = {
            { name = "allcircuitbusy.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/allcircuitbusy.mp3", weight = 7.0, eeriness = 8.5, type = "sfx" },
            { name = "uvb76_the_buzzer_shortwave_radio.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/uvb76_the_buzzer_shortwave_radio.mp3", weight = 6.5, eeriness = 9.0, type = "broadcast" },
            { name = "alerta-sismica-mexico.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/alerta-sismica-mexico.mp3", weight = 6.0, eeriness = 8.5, type = "alarm" },
            { name = "japan-eas-alarm-tsunami-alert.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/japan-eas-alarm-tsunami-alert.mp3", weight = 6.0, eeriness = 8.8, type = "alarm" },
            { name = "answering-machine-beep.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/answering-machine-beep.mp3", weight = 5.5, eeriness = 6.5, type = "sfx" },
            { name = "Backrooms (Original Score), Vol. 2 - Please do not Speak.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%202%20-%20Please%20do%20not%20Speak.mp3", weight = 4.5, eeriness = 8.0, type = "alarm" },
            { name = "Backrooms (Original Score), Vol. 3 - The Reason.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20(Original%20Score),%20Vol.%203%20-%20The%20Reason.mp3", weight = 4.5, eeriness = 8.0, type = "alarm" },
            { name = "warning.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/warning.mp3", weight = 4.5, eeriness = 8.0, type = "alarm" },
            { name = "warning_hq.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/warning_hq.mp3", weight = 4.5, eeriness = 8.0, type = "alarm" },
            { name = "warning_matching.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/warning_matching.mp3", weight = 4.5, eeriness = 8.0, type = "alarm" },
            { name = "aithy-number-you-dialed-does-not-exist.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/aithy-number-you-dialed-does-not-exist.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "arabic-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/arabic-phone-cannot-be-reached.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "avaya-cheerful-ringtone.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/avaya-cheerful-ringtone.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "balmuda-phone-low-battery-sound.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/balmuda-phone-low-battery-sound.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "bhaasaakhmaer-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/bhaasaakhmaer-phone-cannot-be-reached.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "constellation-iphone-ringtone.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/constellation-iphone-ringtone.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "dial-up-homemade(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dial-up-homemade(1).mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "dial-up-homemade.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dial-up-homemade.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "disconnected-phone-number.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/disconnected-phone-number.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "dtmf-dial-tones-1.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dtmf-dial-tones-1.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "dtmf-dial-tones-9.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dtmf-dial-tones-9.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "european-spanish-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/european-spanish-phone-cannot-be-reached.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "german-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/german-phone-cannot-be-reached.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "hindi-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/hindi-phone-cannot-be-reached.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
            { name = "indonesian-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/indonesian-phone-cannot-be-reached.mp3", weight = 4.0, eeriness = 6.5, type = "telephony" },
        },
    },

    -- Uncanny NPC & Mannequin Archetypes
    NPCS = {
        models = {
            "models/humans/group01/male_01.mdl",
            "models/humans/group01/male_02.mdl",
            "models/humans/group01/male_04.mdl",
            "models/humans/group01/female_01.mdl",
            "models/humans/group01/female_02.mdl",
            "models/police.mdl",
            "models/zombie/classic.mdl",
            "models/gman_high.mdl",
        },
        traits = {
            { name = "still_life", rarity = 0.45, speed = 0.0 },
            { name = "confused_wanderer", rarity = 0.3, speed = 60.0 },
            { name = "corrupt_chaser", rarity = 0.15, speed = 260.0 },
            { name = "mimic_observer", rarity = 0.1, speed = 0.0 },
        },
        citizen_vo = {
            "vo/npc/male01/whoops01.wav",
            "vo/npc/male01/thislldonicely01.wav",
            "vo/npc/male01/sorry01.wav",
            "vo/npc/male01/sorry02.wav",
            "vo/npc/male01/behindyou01.wav",
            "vo/npc/male01/didyouhear01.wav",
            "vo/npc/male01/question05.wav",
            "vo/npc/male01/gordead_ans01.wav",
            "vo/npc/male01/strider_run.wav",
            "vo/npc/male01/runforyourlife02.wav",
        }
    },

    -- Entangled Variable Matrices (Scrambled on Cognitive Breakdown)
    ENTANGLEMENTS = {
        door_speeds = { 20.0, 50.0, 100.0, 300.0, 800.0 },
        pitch_shifts = { 0.35, 0.65, 0.85, 1.0, 1.25, 1.6 },
        flicker_rates = { 0.05, 0.12, 0.35, 1.2, 5.0 },
    }
}

if SERVER then
    -- Hot-reload dematerialization
    if _G.CognitiveDecay_Cleanup then
        pcall(_G.CognitiveDecay_Cleanup)
    end

    -- --------------------------------------------------------------------------
    -- 2. SPATIAL VOLUME & CONFIGURATION
    -- --------------------------------------------------------------------------
    local BOUNDS = {
        MIN = Vector(6441.24, -16307.3, -16255.7),
        MAX = Vector(16306.5, -4107.08, -12576.3),
        CENTER = Vector(11373.87, -10207.19, -16060.2)
    }

    local CONFIG = {
        CELL_SIZE   = 189.8,     -- Hunter plate4x4: 4 * 47.45 = 189.8
        WALL_HEIGHT = 189.8,
        
        -- Multi-Tier Elevations
        Z_TIER_SUB   = -16250.0, -- Level 1: Concrete Maintenance Crypt (Bottom)
        Z_TIER_MAIN  = -16060.2, -- Level 0: Main Liminal Complex
        Z_TIER_UPPER = -15870.4, -- Level 2: Institutional Mezzanine
        
        -- Structural Models
        FLOOR_MODEL = "models/hunter/plates/plate4x4.mdl",
        WALL_MODEL  = "models/hunter/plates/plate4x4.mdl",
        RAMP_MODEL  = "models/hunter/plates/plate4x8.mdl",
        DOOR_MODEL  = "models/props_c17/door01_left.mdl",
        LIGHT_MODEL = "models/props_c17/light_fluorescent01a.mdl",
        CAGE_LIGHT  = "models/props_wasteland/light_caged01a.mdl",
        
        -- Generation Probabilities
        LIGHT_CHANCE        = 0.35,
        DOOR_CHANCE         = 0.30,
        RADIO_CHANCE        = 0.25,
        NPC_CHANCE          = 0.05,
        PHASED_TABLE_CHANCE = 0.02,
        
        -- Spawning Throttle
        SPAWN_INTERVAL = 0.18
    }

    local HALF_CELL = CONFIG.CELL_SIZE * 0.5
    local chipPos = chip():getPos()
    local ANCHOR_POS = Vector(BOUNDS.CENTER.x, BOUNDS.CENTER.y, CONFIG.Z_TIER_MAIN)

    if chipPos.x >= BOUNDS.MIN.x and chipPos.x <= BOUNDS.MAX.x and
       chipPos.y >= BOUNDS.MIN.y and chipPos.y <= BOUNDS.MAX.y then
        ANCHOR_POS = Vector(chipPos.x, chipPos.y, CONFIG.Z_TIER_MAIN)
    end
    print("[Cognitive Decay Engine] Spawning anchor: " .. tostring(ANCHOR_POS))

    -- --------------------------------------------------------------------------
    -- 3. COGNITIVE DECAY BRAIN (DYNAMIC SELECTION & MUTATION)
    -- --------------------------------------------------------------------------
    local Brain = {
        confusion = 0.05,
        roomCount = 0
    }

    function Brain:step()
        self.roomCount = self.roomCount + 1
        self.confusion = math.min(0.85, 0.05 + (self.roomCount * 0.012))
    end

    function Brain:pickWall(biome)
        if biome == "crypt" then
            return DATASET.MATERIALS.concrete[math.random(#DATASET.MATERIALS.concrete)] or "concrete/concretefloor001a"
        elseif biome == "institutional" then
            return DATASET.MATERIALS.plaster_walls[math.random(#DATASET.MATERIALS.plaster_walls)] or "cs_havana/plasterwall027c"
        else
            -- Office
            if math.random() < self.confusion and #DATASET.MATERIALS.plaster_walls > 0 then
                return DATASET.MATERIALS.plaster_walls[math.random(#DATASET.MATERIALS.plaster_walls)]
            end
            return DATASET.MATERIALS.wallpaper[math.random(#DATASET.MATERIALS.wallpaper)] or "cs_havana/plasterwallpaper004a"
        end
    end

    function Brain:pickFloor(biome)
        if biome == "crypt" then
            return DATASET.MATERIALS.concrete[math.random(#DATASET.MATERIALS.concrete)] or "concrete/concretefloor001a"
        elseif biome == "institutional" then
            return DATASET.MATERIALS.tile[math.random(#DATASET.MATERIALS.tile)] or "cs_italy/ptilefloor1"
        else
            -- Office carpet
            if math.random() < self.confusion and #DATASET.MATERIALS.tile > 0 then
                return DATASET.MATERIALS.tile[math.random(#DATASET.MATERIALS.tile)]
            end
            return DATASET.MATERIALS.carpet[math.random(#DATASET.MATERIALS.carpet)] or "carpet/offflra"
        end
    end

    function Brain:pickCeiling(biome)
        if biome == "crypt" then
            return "concrete/concreteceiling002a"
        elseif biome == "institutional" then
            return "concrete/concreteceiling001a"
        else
            return DATASET.MATERIALS.ceiling[math.random(#DATASET.MATERIALS.ceiling)] or "concrete/concreteceiling001a"
        end
    end

    function Brain:pickAudioTrack()
        -- Dynamic track sampling by decay stage
        if self.confusion > 0.60 and math.random() < 0.40 then
            local list = DATASET.AUDIO.nightmare
            return list[math.random(#list)]
        elseif self.confusion > 0.35 and math.random() < 0.45 then
            local list = DATASET.AUDIO.telephony
            return list[math.random(#list)]
        end
        local list = DATASET.AUDIO.vibe
        return list[math.random(#list)]
    end

    function Brain:pickPitch()
        return DATASET.ENTANGLEMENTS.pitch_shifts[math.random(#DATASET.ENTANGLEMENTS.pitch_shifts)] or 1.0
    end

    -- --------------------------------------------------------------------------
    -- 4. ENTITY TRACKERS & QUEUE
    -- --------------------------------------------------------------------------
    local spawnQueue = {}
    local activeEntities = {}
    local activeDoors = {}
    local activeRadios = {}
    local activeLights = {}

    local function safeSetMaterial(ent, mat, col)
        if not isValid(ent) or not mat then return end
        pcall(ent.setMaterial, ent, mat)
        if col then pcall(ent.setColor, ent, col) end
    end

    local function traceFloorHeight(worldPos)
        local startPos = worldPos + Vector(0, 0, 40)
        local endPos = worldPos - Vector(0, 0, 120)
        local tr = trace.line(startPos, endPos, nil, MASK_SOLID)
        if tr and tr.Hit and tr.HitPos then
            return tr.HitPos.z + 1.2
        end
        return worldPos.z + 1.2
    end

    local function adjustPositionWithSensing(pos, radius, existingProps)
        local maxBound = HALF_CELL - 24 - radius
        local clampedX = math.clamp(pos.x, -maxBound, maxBound)
        local clampedY = math.clamp(pos.y, -maxBound, maxBound)
        local candidate = Vector(clampedX, clampedY, pos.z)

        for _, other in ipairs(existingProps) do
            local diff = candidate - other.pos
            local dist = diff:getLength2D()
            local minDist = radius + other.radius + 8
            if dist < minDist then
                local pushDir = dist > 0.1 and diff:getNormalized() or Vector(1, 0, 0)
                candidate = candidate + (pushDir * (minDist - dist))
                candidate.x = math.clamp(candidate.x, -maxBound, maxBound)
                candidate.y = math.clamp(candidate.y, -maxBound, maxBound)
            end
        end
        return candidate
    end

    -- --------------------------------------------------------------------------
    -- 5. GEOMETRY PRIMITIVES & WATERTIGHT SOLVER
    -- --------------------------------------------------------------------------
    local function queueEnclosedCell(pos, floorMat, ceilMat)
        table.insert(spawnQueue, {
            pos = pos,
            ang = Angle(0, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = floorMat,
            category = "floor",
            keepFrozen = true
        })
        table.insert(spawnQueue, {
            pos = pos + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = Angle(180, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = ceilMat,
            category = "ceiling",
            keepFrozen = true
        })
    end

    local function queueWall(pos, isNorthSouth, wallMat)
        local wallAng = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0)
        table.insert(spawnQueue, {
            pos = pos,
            ang = wallAng,
            model = CONFIG.WALL_MODEL,
            mat = wallMat,
            category = "wall",
            keepFrozen = true
        })
    end

    local function queueInteractiveDoor(doorPos, isNorthSouth)
        local doorAng = isNorthSouth and Angle(0, 0, 0) or Angle(0, 90, 0)
        local speed = DATASET.ENTANGLEMENTS.door_speeds[math.random(#DATASET.ENTANGLEMENTS.door_speeds)] or 100.0

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
                    baseAng = doorAng,
                    openAng = doorAng + Angle(0, 90, 0),
                    speed = speed,
                    nextUse = 0
                })
            end
        })
    end

    local function queueSeamlessTransitRamp(topLandingPos, isNorthSouth, goingDown)
        local slopeLen = 380.0
        local heightDiff = CONFIG.Z_TIER_MAIN - CONFIG.Z_TIER_SUB -- 189.8
        local radAngle = math.asin(heightDiff / slopeLen)
        local runDist = slopeLen * math.cos(radAngle) -- 329.21 units

        local rampAng = isNorthSouth and Angle(0, 0, goingDown and 150 or -150) or Angle(goingDown and 30 or -30, 0, 0)
        local forwardDir = isNorthSouth and Vector(0, goingDown and 1 or -1, 0) or Vector(goingDown and 1 or -1, 0, 0)
        local rampCenter = topLandingPos + (forwardDir * (runDist * 0.5)) - Vector(0, 0, heightDiff * 0.5)

        local rampMat = "concrete/concretefloor001a"

        table.insert(spawnQueue, {
            pos = rampCenter,
            ang = rampAng,
            model = CONFIG.RAMP_MODEL,
            mat = rampMat,
            category = "ramp",
            keepFrozen = true
        })
        local sideOffset = isNorthSouth and Vector(HALF_CELL, 0, 0) or Vector(0, HALF_CELL, 0)
        table.insert(spawnQueue, {
            pos = rampCenter + sideOffset,
            ang = isNorthSouth and Angle(90, 0, 0) or Angle(90, 90, 0),
            model = CONFIG.WALL_MODEL,
            mat = rampMat,
            category = "wall",
            keepFrozen = true
        })
        table.insert(spawnQueue, {
            pos = rampCenter - sideOffset,
            ang = isNorthSouth and Angle(90, 0, 0) or Angle(90, 90, 0),
            model = CONFIG.WALL_MODEL,
            mat = rampMat,
            category = "wall",
            keepFrozen = true
        })
        table.insert(spawnQueue, {
            pos = rampCenter + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = rampAng + Angle(180, 0, 0),
            model = CONFIG.RAMP_MODEL,
            mat = "concrete/concreteceiling001a",
            category = "ceiling",
            keepFrozen = true
        })

        local bottomFloorPos = topLandingPos + (forwardDir * runDist) - Vector(0, 0, heightDiff)
        queueEnclosedCell(bottomFloorPos, rampMat, "concrete/concreteceiling001a")
    end

    local function queuePitfall(posMain)
        local posSub = Vector(posMain.x, posMain.y, CONFIG.Z_TIER_SUB)
        table.insert(spawnQueue, {
            pos = posSub,
            ang = Angle(0, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = "concrete/concretefloor001a",
            category = "floor",
            keepFrozen = true
        })
        table.insert(spawnQueue, {
            pos = posMain + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = Angle(180, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = "concrete/concreteceiling001a",
            category = "ceiling",
            keepFrozen = true
        })
    end

    -- --------------------------------------------------------------------------
    -- 6. MULTI-BIOME ARCHITECTURE & SECTORS
    -- --------------------------------------------------------------------------
    print("[Cognitive Decay Engine] Building sprawling multi-biome Backrooms layout...")

    -- SECTOR 1: Level 0 - Main Yellow Liminal Complex (Tier 0: Z = -16,060)
    local S1_W, S1_H = 6, 6
    local s1Origin = ANCHOR_POS - Vector(S1_W * 0.5 * CONFIG.CELL_SIZE, S1_H * 0.5 * CONFIG.CELL_SIZE, 0)

    for x = 1, S1_W do
        for y = 1, S1_H do
            Brain:step()
            local cCenter = s1Origin + Vector((x - 0.5) * CONFIG.CELL_SIZE, (y - 0.5) * CONFIG.CELL_SIZE, 0)
            local wallMat = Brain:pickWall("office")
            local floorMat = Brain:pickFloor("office")
            local ceilMat = Brain:pickCeiling("office")

            local isPitfall = (x == 4 and y == 4)
            if isPitfall then
                queuePitfall(cCenter)
            else
                queueEnclosedCell(cCenter, floorMat, ceilMat)
            end

            -- Perimeter & Partition Walls
            if y == S1_H or math.random() < 0.40 then
                if math.random() < CONFIG.DOOR_CHANCE and y < S1_H then
                    queueInteractiveDoor(cCenter + Vector(0, HALF_CELL, 0), true)
                else
                    queueWall(cCenter + Vector(0, HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, wallMat)
                end
            end
            if y == 1 then queueWall(cCenter + Vector(0, -HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, wallMat) end

            if x == S1_W or math.random() < 0.40 then
                if math.random() < CONFIG.DOOR_CHANCE and x < S1_W then
                    queueInteractiveDoor(cCenter + Vector(HALF_CELL, 0, 0), false)
                else
                    queueWall(cCenter + Vector(HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, wallMat)
                end
            end
            if x == 1 then queueWall(cCenter + Vector(-HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, wallMat) end

            -- Fluorescent Lights
            if not isPitfall and math.random() < CONFIG.LIGHT_CHANCE then
                local lightPos = cCenter + Vector(0, 0, CONFIG.WALL_HEIGHT - 3)
                table.insert(spawnQueue, {
                    pos = lightPos,
                    ang = Angle(0, 0, 0),
                    model = CONFIG.LIGHT_MODEL,
                    category = "light",
                    keepFrozen = true,
                    onSpawn = function(ent)
                        safeSetMaterial(ent, "models/debug/debugwhite", Color(255, 250, 195))
                        table.insert(activeLights, ent)
                        net.start("CognitiveDecay_LightSpawn")
                        net.writeEntity(ent)
                        net.send()
                    end
                })
            end

            -- Dynamic Furnishings with Semantic Affordances
            if not isPitfall then
                local cellProps = {}

                -- The Image 2 Anomaly (2% chance)
                if math.random() < CONFIG.PHASED_TABLE_CHANCE then
                    local worldPos = cCenter + Vector(0, HALF_CELL - 14, 18.2)
                    table.insert(spawnQueue, {
                        pos = worldPos,
                        ang = Angle(0, -90, 0),
                        model = "models/props_c17/FurnitureTable002a.mdl",
                        category = "furniture",
                        keepFrozen = true
                    })
                    table.insert(spawnQueue, {
                        pos = worldPos + Vector(0, 4, 16.5),
                        ang = Angle(0, math.random(-25, 25), 0),
                        model = "models/props_lab/harddrive02.mdl",
                        category = "furniture",
                        keepFrozen = true
                    })
                else
                    -- Dynamic Tables & Desks
                    if math.random() < 0.55 then
                        local deskLocal = adjustPositionWithSensing(Vector(math.random(-32, 32), math.random(-32, 32), 0), 28, cellProps)
                        table.insert(cellProps, { pos = deskLocal, radius = 28 })
                        local deskWorld = cCenter + deskLocal
                        local dynamicYaw = math.random(0, 359)
                        local deskAng = Angle(0, dynamicYaw, 0)
                        local deskMdl = DATASET.PROPS.flat_surface[math.random(#DATASET.PROPS.flat_surface)] or "models/props_c17/FurnitureDesk001a.mdl"

                        table.insert(spawnQueue, {
                            pos = deskWorld,
                            ang = deskAng,
                            model = deskMdl,
                            category = "furniture",
                            keepFrozen = false,
                            onSpawn = function(ent)
                                local groundZ = traceFloorHeight(deskWorld)
                                ent:setPos(Vector(deskWorld.x, deskWorld.y, groundZ))
                                timer.simple(0.06, function()
                                    if isValid(ent) then
                                        ent:setFrozen(false)
                                        ent:enableMotion(true)
                                    end
                                end)
                            end
                        })

                        -- Dynamic Surface Mount (Radio, PC, CRT Monitor)
                        if math.random() < 0.70 then
                            local mountMdl = DATASET.PROPS.surface_mount[math.random(#DATASET.PROPS.surface_mount)] or "models/props_lab/citizenradio.mdl"
                            local mountPos = deskWorld + Vector(0, 0, 32.5)
                            local mountAng = deskAng + Angle(0, math.random(-45, 45), 0)

                            table.insert(spawnQueue, {
                                pos = mountPos,
                                ang = mountAng,
                                model = mountMdl,
                                category = "furniture",
                                keepFrozen = false,
                                onSpawn = function(ent)
                                    timer.simple(0.08, function()
                                        if isValid(ent) then
                                            ent:setFrozen(false)
                                            ent:enableMotion(true)
                                        end
                                    end)
                                    if string.find(mountMdl, "radio") then
                                        local track = Brain:pickAudioTrack()
                                        local isGlitch = math.random() < 0.15
                                        local pitchVal = Brain:pickPitch()
                                        net.start("CognitiveDecay_RadioSpawn")
                                        net.writeEntity(ent)
                                        net.writeString(track.url or "")
                                        net.writeBool(isGlitch)
                                        net.writeFloat(pitchVal)
                                        net.send()
                                    end
                                end
                            })
                        end

                        -- Dynamic Seating (Chairs)
                        if math.random() < 0.65 then
                            local chairDist = math.random(28, 42)
                            local chairOffset = deskAng:getForward() * -chairDist + deskAng:getRight() * math.random(-12, 12)
                            local chairLocal = adjustPositionWithSensing(deskLocal + chairOffset, 18, cellProps)
                            table.insert(cellProps, { pos = chairLocal, radius = 18 })
                            local chairWorld = cCenter + chairLocal
                            local chairMdl = DATASET.PROPS.seating[math.random(#DATASET.PROPS.seating)] or "models/props_c17/FurnitureChair001a.mdl"

                            -- 20% chance chair is askew or knocked over
                            local isTipped = math.random() < 0.20
                            local chairAng = deskAng + Angle(isTipped and math.random(75, 95) or 0, math.random(-40, 40), isTipped and math.random(-25, 25) or 0)

                            table.insert(spawnQueue, {
                                pos = chairWorld,
                                ang = chairAng,
                                model = chairMdl,
                                category = "furniture",
                                keepFrozen = false,
                                onSpawn = function(ent)
                                    local groundZ = traceFloorHeight(chairWorld)
                                    ent:setPos(Vector(chairWorld.x, chairWorld.y, groundZ))
                                    timer.simple(0.06, function()
                                        if isValid(ent) then
                                            ent:setFrozen(false)
                                            ent:enableMotion(true)
                                        end
                                    end)
                                end
                            })
                        end
                    end

                    -- Dynamic Wall Storage
                    if math.random() < 0.35 then
                        local cabinetLocal = adjustPositionWithSensing(Vector(math.random(-35, 35), HALF_CELL - 20, 0), 20, cellProps)
                        table.insert(cellProps, { pos = cabinetLocal, radius = 20 })
                        local cabinetWorld = cCenter + cabinetLocal
                        local storageMdl = DATASET.PROPS.storage[math.random(#DATASET.PROPS.storage)] or "models/props_c17/filecabinet02.mdl"

                        table.insert(spawnQueue, {
                            pos = cabinetWorld,
                            ang = Angle(0, math.random(-180, 180), 0),
                            model = storageMdl,
                            category = "furniture",
                            keepFrozen = false,
                            onSpawn = function(ent)
                                local groundZ = traceFloorHeight(cabinetWorld)
                                ent:setPos(Vector(cabinetWorld.x, cabinetWorld.y, groundZ))
                                timer.simple(0.06, function()
                                    if isValid(ent) then
                                        ent:setFrozen(false)
                                        ent:enableMotion(true)
                                    end
                                end)
                            end
                        })
                    end
                end

                -- Dynamic NPC (Still Life Mannequin)
                if math.random() < CONFIG.NPC_CHANCE then
                    local npcPos = cCenter + Vector(math.random(-30, 30), math.random(-30, 30), 0)
                    local npcMdl = DATASET.NPCS.models[math.random(#DATASET.NPCS.models)]

                    -- Dynamic bone corruptions generated on spawn
                    local neckPitch = math.random(-35, 35)
                    local neckYaw   = math.random(-50, 50)
                    local neckRoll  = math.random(20, 85) * (math.random() < 0.5 and 1 or -1)

                    table.insert(spawnQueue, {
                        pos = npcPos,
                        ang = Angle(0, math.random(0, 360), 0),
                        model = npcMdl,
                        category = "npc",
                        keepFrozen = true,
                        onSpawn = function(ent)
                            net.start("CognitiveDecay_NPCSpawn")
                            net.writeEntity(ent)
                            net.writeAngle(Angle(neckPitch, neckYaw, neckRoll))
                            net.send()
                        end
                    })
                end
            end
        end
    end

    -- SECTOR 2: Seamless Transit Ramp to Level 1 Crypt
    local ramp1Pos = s1Origin + Vector((3 - 0.5) * CONFIG.CELL_SIZE, (4 - 0.5) * CONFIG.CELL_SIZE, 0)
    queueSeamlessTransitRamp(ramp1Pos, true, true)

    -- SECTOR 3: Level 1 - Concrete Industrial Crypt (Tier -1 at Z = -16,250)
    local S2_W, S2_H = 4, 4
    local s2Origin = ANCHOR_POS + Vector(S1_W * 0.5 * CONFIG.CELL_SIZE, 0, CONFIG.Z_TIER_SUB - CONFIG.Z_TIER_MAIN)

    for x = 1, S2_W do
        for y = 1, S2_H do
            local cCenter = s2Origin + Vector((x - 0.5) * CONFIG.CELL_SIZE, (y - 0.5) * CONFIG.CELL_SIZE, 0)
            local cryptMat = "concrete/concretefloor001a"
            local cryptCeil = "concrete/concreteceiling002a"

            queueEnclosedCell(cCenter, cryptMat, cryptCeil)

            if y == S2_H then queueWall(cCenter + Vector(0, HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, cryptMat) end
            if y == 1 then queueWall(cCenter + Vector(0, -HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, cryptMat) end
            if x == S2_W then queueWall(cCenter + Vector(HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, cryptMat) end
            if x == 1 then queueWall(cCenter + Vector(-HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, cryptMat) end

            if math.random() < 0.40 then
                local lightPos = cCenter + Vector(0, 0, CONFIG.WALL_HEIGHT - 4)
                table.insert(spawnQueue, {
                    pos = lightPos,
                    ang = Angle(0, 0, 0),
                    model = CONFIG.CAGE_LIGHT,
                    category = "light",
                    keepFrozen = true,
                    onSpawn = function(ent)
                        safeSetMaterial(ent, "models/debug/debugwhite", Color(255, 180, 100))
                        table.insert(activeLights, ent)
                        net.start("CognitiveDecay_LightSpawn")
                        net.writeEntity(ent)
                        net.send()
                    end
                })
            end

            -- Dynamic Crypt Props: Pallets, Oil Drums, Metal Shelves
            if math.random() < 0.60 then
                local propMdl = (math.random() < 0.5) and "models/props_junk/wood_pallet001a.mdl" or "models/props_c17/oildrum001.mdl"
                local propWorld = cCenter + Vector(math.random(-25, 25), math.random(-25, 25), 0)

                table.insert(spawnQueue, {
                    pos = propWorld,
                    ang = Angle(0, math.random(0, 360), 0),
                    model = propMdl,
                    category = "furniture",
                    keepFrozen = false,
                    onSpawn = function(ent)
                        local groundZ = traceFloorHeight(propWorld)
                        ent:setPos(Vector(propWorld.x, propWorld.y, groundZ))
                        timer.simple(0.06, function()
                            if isValid(ent) then
                                ent:setFrozen(false)
                                ent:enableMotion(true)
                            end
                        end)
                    end
                })
            end
        end
    end

    -- SECTOR 4: Level 2 - Institutional Mezzanine (Tier +1 at Z = -15,870)
    local S3_W, S3_H = 3, 5
    local s3Origin = ANCHOR_POS - Vector((S1_W * 0.5 + S3_W) * CONFIG.CELL_SIZE, 0, CONFIG.Z_TIER_UPPER - CONFIG.Z_TIER_MAIN)

    for x = 1, S3_W do
        for y = 1, S3_H do
            local cCenter = s3Origin + Vector((x - 0.5) * CONFIG.CELL_SIZE, (y - 0.5) * CONFIG.CELL_SIZE, 0)
            local instWall = "cs_havana/plasterwall027c"
            local instFloor = "cs_italy/ptilefloor1"
            local instCeil = "concrete/concreteceiling001a"

            queueEnclosedCell(cCenter, instFloor, instCeil)

            if y == S3_H then queueWall(cCenter + Vector(0, HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, instWall) end
            if y == 1 then queueWall(cCenter + Vector(0, -HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, instWall) end
            if x == S3_W then queueWall(cCenter + Vector(HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, instWall) end
            if x == 1 then queueWall(cCenter + Vector(-HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, instWall) end

            if math.random() < 0.50 then
                local bedPos = cCenter + Vector(0, 0, 0)
                table.insert(spawnQueue, {
                    pos = bedPos,
                    ang = Angle(0, math.random(0, 360), 0),
                    model = "models/props_c17/FurnitureTable001a.mdl",
                    category = "furniture",
                    keepFrozen = false,
                    onSpawn = function(ent)
                        local groundZ = traceFloorHeight(bedPos)
                        ent:setPos(Vector(bedPos.x, bedPos.y, groundZ))
                        timer.simple(0.06, function()
                            if isValid(ent) then
                                ent:setFrozen(false)
                                ent:enableMotion(true)
                            end
                        end)
                    end
                })
            end
        end
    end

    -- --------------------------------------------------------------------------
    -- 7. SAFE QUEUED MATERIALIZER ENGINE
    -- --------------------------------------------------------------------------
    local function processQueue()
        if #spawnQueue == 0 then
            print("[Cognitive Decay Engine] Sector generation complete. All multi-tier entities materialized.")
            timer.remove("CognitiveDecay_Spawner")
            return
        end

        if not prop.canSpawn() then return end

        local item = table.remove(spawnQueue, 1)
        local ent = prop.create(item.pos, item.ang, item.model, item.keepFrozen)

        if isValid(ent) then
            table.insert(activeEntities, ent)
            if item.mat then safeSetMaterial(ent, item.mat) end
            if item.onSpawn then item.onSpawn(ent) end
        end
    end
    timer.create("CognitiveDecay_Spawner", CONFIG.SPAWN_INTERVAL, 0, processQueue)

    -- Interactive Doors Think Loop (Proximity & +USE)
    hook.add("think", "CognitiveDecay_DoorThink", function()
        local now = timer.curtime()
        for _, d in ipairs(activeDoors) do
            if isValid(d.ent) and now > d.nextUse then
                for _, ply in ipairs(find.allPlayers()) do
                    if ply:getPos():getDistance(d.ent:getPos()) < 58 then
                        d.isOpen = not d.isOpen
                        d.nextUse = now + 1.2
                        local targetAng = d.isOpen and d.openAng or d.baseAng
                        d.ent:setAngles(targetAng)
                        pcall(sound.playFile, "doors/door_wood_move1.wav", "3d", function(st)
                            if isValid(st) and isValid(d.ent) then
                                st:setPos(d.ent:getPos())
                                st:play()
                            end
                        end)
                        break
                    end
                end
            end
        end
    end)

    -- --------------------------------------------------------------------------
    -- 8. CLEANUP ON REMOVAL & HOT-RELOAD
    -- --------------------------------------------------------------------------
    _G.CognitiveDecay_Cleanup = function()
        timer.remove("CognitiveDecay_Spawner")
        for _, ent in ipairs(activeEntities) do
            if isValid(ent) then pcall(ent.remove, ent) end
        end
        print("[Cognitive Decay Engine] Sector dematerialized cleanly.")
    end
    hook.add("Removed", "CognitiveDecay_CleanupHook", _G.CognitiveDecay_Cleanup)

else
    -- ==========================================================================
    -- CLIENT: DYNAMIC BASS AUDIO STREAMING, XEN BEAMS, NPCS & LIGHTING
    -- ==========================================================================
    if _G.CognitiveDecay_ClientCleanup then
        pcall(_G.CognitiveDecay_ClientCleanup)
    end

    local activeRadios = {}
    local activeLights = {}
    local activeZaps = {}
    local activeNPCs = {}

    local xenBeamMat = material.load("sprites/physbeam") or material.load("sprites/lgtning")
    local glowMat = material.load("sprites/light_glow02")

    _G.CognitiveDecay_ClientCleanup = function()
        hook.remove("render", "CognitiveDecay_ClientRender")
        hook.remove("think", "CognitiveDecay_ClientThink")
        for _, r in ipairs(activeRadios) do
            if isValid(r.station) then pcall(r.station.stop, r.station) end
        end
        table.empty(activeRadios)
        table.empty(activeLights)
        table.empty(activeZaps)
        table.empty(activeNPCs)
    end
    hook.add("Removed", "CognitiveDecay_ClientCleanupHook", _G.CognitiveDecay_ClientCleanup)

    -- Ambient Fluorescent Drone
    hook.add("Initialize", "CognitiveDecay_ClientInit", function()
        pcall(sound.playFile, "ambient/levels/labs/equipment_printer_loop1.wav", "noplay", function(st)
            if isValid(st) then
                st:setVolume(0.22)
                st:play()
            end
        end)
    end)

    net.receive("CognitiveDecay_LightSpawn", function()
        local ent = net.readEntity()
        if isValid(ent) then table.insert(activeLights, ent) end
    end)

    -- DYNAMIC BASS STREAMING FROM GITHUB REPO (ZERO HARDCODED AUDIO)
    net.receive("CognitiveDecay_RadioSpawn", function()
        local radio = net.readEntity()
        local rawUrl = net.readString()
        local isGlitch = net.readBool()
        local basePitch = net.readFloat()

        if isValid(radio) and rawUrl and #rawUrl > 0 then
            pcall(bass.loadURL, rawUrl, "3d noblock", function(station, errCode, errName)
                if isValid(station) and isValid(radio) then
                    station:setPos(radio:getPos())
                    station:setFade(80, 520)
                    station:setVolume(math.Rand(0.55, 0.85))
                    station:setPlaybackRate(basePitch or 1.0)
                    station:play()
                    table.insert(activeRadios, {
                        ent = radio,
                        station = station,
                        isGlitch = isGlitch,
                        nextGlitch = timer.curtime() + math.Rand(3, 8)
                    })
                end
            end)
        end
    end)

    -- DYNAMIC NPC CORRUPTIONS (ZERO HARDCODED ANGLES)
    net.receive("CognitiveDecay_NPCSpawn", function()
        local npc = net.readEntity()
        local corruptAngle = net.readAngle()
        if isValid(npc) then
            pcall(npc.manipulateBoneAngles, npc, 6, corruptAngle)
            local flexNum = npc:getFlexNum()
            if flexNum and flexNum > 0 then
                for f = 0, math.min(flexNum - 1, 6) do
                    if math.random() < 0.40 then
                        pcall(npc.setFlexWeight, npc, f, math.Rand(0.25, 1.0))
                    end
                end
            end
            table.insert(activeNPCs, npc)
        end
    end)

    -- Render Hook: Deep Liminal Darkness, Xen Lightning, and Fluorescent Lighting
    hook.add("render", "CognitiveDecay_ClientRender", function()
        local now = timer.curtime()
        local plyPos = player():getPos()

        -- 1. Deep Claustrophobic Liminal Fog & Darkness
        pcall(function()
            render.setFogMode(1)
            render.setFogStart(40)
            render.setFogEnd(480)
            render.setFogColor(Color(12, 10, 6))
        end)

        -- 2. Half-Life 1 Xen Green Electric Beams
        for i = #activeZaps, 1, -1 do
            local zap = activeZaps[i]
            if now > zap.dieTime then
                table.remove(activeZaps, i)
            else
                render.setColor(Color(45, 255, 65, 240))
                if xenBeamMat then render.setMaterial(xenBeamMat) end
                for b = 1, 6 do
                    local offset = Vector(math.random(-25, 25), math.random(-25, 25), math.random(0, 75))
                    render.draw3DBeam(zap.pos + Vector(0, 0, 80), zap.pos + offset, math.random(6, 14), 0, 1)
                end
            end
        end

        -- 3. Fluorescent Light Fixture Pools
        for i = #activeLights, 1, -1 do
            local fix = activeLights[i]
            if not isValid(fix) then
                table.remove(activeLights, i)
            else
                local fixPos = fix:getPos()
                if plyPos:getDistance(fixPos) < 700 then
                    if glowMat then
                        render.setMaterial(glowMat)
                        render.setColor(Color(255, 245, 190, 210))
                        render.drawSprite(fixPos - Vector(0, 0, 6), 140, 140)
                    end
                end
            end
        end
    end)
end
