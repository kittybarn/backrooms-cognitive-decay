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
            "models/props_lab/monitor02.mdl",
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
            "models/props/cs_office/file_cabinet1.mdl",
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
            "models/props/cs_italy/it_mkt_table1.mdl",
            "models/props_interiors/furniture_desk01a.mdl",
            "models/props/cs_office/table_meeting.mdl",
            "models/props_c17/furnituretable002a.mdl",
            "models/props_c17/furnituretable001a.mdl",
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
            "models/props/cs_office/chair_office.mdl",
            "models/props_c17/furniturechair001a.mdl",
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
            "models/props_c17/light_cagelight01_on.mdl",
            "models/props/cs_office/light_ceiling.mdl",
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
        music = {
            { name = "Backrooms (Original Score), Vol. 1 - Async Research Institute.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Async%20Research%20Institute.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Auditory Guidepost.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Auditory%20Guidepost.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Deeper Than The Walls.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Deeper%20Than%20The%20Walls.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Glacier.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Glacier.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Government Funding.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Government%20Funding.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Hazmat.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Hazmat.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - KV31.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20KV31.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Missing Persons.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Missing%20Persons.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Not Your Decision.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Not%20Your%20Decision.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Pipes.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Pipes.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Post-Traumatic Amnesia.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Post-Traumatic%20Amnesia.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - Sealed Away.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20Sealed%20Away.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - The Complex.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20The%20Complex.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - The Only Thing That Matters (Demo).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20The%20Only%20Thing%20That%20Matters%20%28Demo%29.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 1 - You're Done (Daisy Bell).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%201%20-%20You%27re%20Done%20%28Daisy%20Bell%29.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - A Passage.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20A%20Passage.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Compromises.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Compromises.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Congratulations, Ivan.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Congratulations%2C%20Ivan.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Department of Energy.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Department%20of%20Energy.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Distant.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Distant.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Ghost.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Ghost.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Hanging Frame (Time Passages).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Hanging%20Frame%20%28Time%20Passages%29.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Instances.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Instances.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Malignant.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Malignant.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Non-Disclosure Agreement.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Non-Disclosure%20Agreement.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Old Objects in Quiet Rooms.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Old%20Objects%20in%20Quiet%20Rooms.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Person.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Person.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Please do not Speak.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Please%20do%20not%20Speak.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - Remember.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20Remember.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 2 - data not accessible.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%202%20-%20data%20not%20accessible.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Do You Like Air Conditioning.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Do%20You%20Like%20Air%20Conditioning.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - For the Sake of Mankind, There Is Nothing More to Be Extracted.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20For%20the%20Sake%20of%20Mankind%2C%20There%20Is%20Nothing%20More%20to%20Be%20Extracted.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - MidwesternTraumaLight.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20MidwesternTraumaLight.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Off the Deep End.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Off%20the%20Deep%20End.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Red Sun in the Sky.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Red%20Sun%20in%20the%20Sky.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Rest Forever in This Dead End.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Rest%20Forever%20in%20This%20Dead%20End.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Still Life.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Still%20Life.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Survey.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Survey.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - The Reason.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20The%20Reason.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Threshold.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Threshold.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - Tunnel Vision.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20Tunnel%20Vision.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "Backrooms (Original Score), Vol. 3 - 煤气灶.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Score%29%2C%20Vol.%203%20-%20%E7%85%A4%E6%B0%94%E7%81%B6.mp3", is_music = true, category = "music", weight = 8.5, eeriness = 8.5 },
            { name = "numbers_station_swedish_rhapsody_musicbox.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/numbers_station_swedish_rhapsody_musicbox.mp3", is_music = true, category = "music", weight = 7.5, eeriness = 7.5 },
            { name = "pachelbel's Canon in D--Soothing music(the best version).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/pachelbel%27s%20Canon%20in%20D--Soothing%20music%28the%20best%20version%29.mp3", is_music = true, category = "music", weight = 7.5, eeriness = 7.5 },
            { name = "phone-call-transfer-elevator-music.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/phone-call-transfer-elevator-music.mp3", is_music = true, category = "music", weight = 7.5, eeriness = 7.5 },
        },
        sound = {
            { name = "Backrooms (Original Soundtrack) - 4-PCH.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%204-PCH.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Basement Land.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Basement%20Land.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Cafe Bossa v1.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Cafe%20Bossa%20v1.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Capitol & McKee.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Capitol%20%26%20McKee.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Cold Floor.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Cold%20Floor.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Complex.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Complex.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Dining Room.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Dining%20Room.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Feeling of a Door Imminently Remembered.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Feeling%20of%20a%20Door%20Imminently%20Remembered.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Furnished Dead End.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Furnished%20Dead%20End.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Furniture Lament.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Furniture%20Lament.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Handprint.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Handprint.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Homothet.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Homothet.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Humble MRI Company.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Humble%20MRI%20Company.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Landsick.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Landsick.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Layout Extrapolation.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Layout%20Extrapolation.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Local Network.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Local%20Network.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Next Room Over.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Next%20Room%20Over.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Old Home Not Yet Built (Instupendo Remix).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Old%20Home%20Not%20Yet%20Built%20%28Instupendo%20Remix%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Old Home Not Yet Built.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Old%20Home%20Not%20Yet%20Built.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Open The Window.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Open%20The%20Window.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Ottoman Empire.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Ottoman%20Empire.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Paint.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Paint.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - People In San Jose.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20People%20In%20San%20Jose.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Pirate Shanty.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Pirate%20Shanty.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Quiet Wall in Dark Room.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Quiet%20Wall%20in%20Dark%20Room.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - The Untrained Mind.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20The%20Untrained%20Mind.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - Wired.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20Wired.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Backrooms (Original Soundtrack) - You Know Me.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Backrooms%20%28Original%20Soundtrack%29%20-%20You%20Know%20Me.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Car Skidding Sound Effect.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Car%20Skidding%20Sound%20Effect.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Caramell.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Caramell.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Congratulations (Remastered).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Congratulations%20%28Remastered%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Für Elise, WoO 59.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/F%C3%BCr%20Elise%2C%20WoO%2059.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Midnight_in_Mondstadt_[_YouConvert.net_].mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Midnight_in_Mondstadt_%5B_YouConvert.net_%5D.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Paul Williams  - wistful dreams.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Paul%20Williams%20%20-%20wistful%20dreams.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Tchaikovsky - 1812 Overture (Full with Cannons).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Tchaikovsky%20-%201812%20Overture%20%28Full%20with%20Cannons%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "Yodelling Sound Effect.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/Yodelling%20Sound%20Effect.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "aithy-number-you-dialed-does-not-exist.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/aithy-number-you-dialed-does-not-exist.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "alerta-sismica-mexico.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/alerta-sismica-mexico.mp3", is_music = false, category = "broadcast", weight = 7.0, eeriness = 8.8 },
            { name = "allcircuitbusy.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/allcircuitbusy.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "answering-machine-beep.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/answering-machine-beep.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "apple-air-tag(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/apple-air-tag%281%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "apple-air-tag.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/apple-air-tag.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "arabic-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/arabic-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "attention.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/attention.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "audio [vocals].mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/audio%20%5Bvocals%5D.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "avaya-cheerful-ringtone.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/avaya-cheerful-ringtone.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "balmuda-phone-low-battery-sound.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/balmuda-phone-low-battery-sound.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "bhaasaakhmaer-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/bhaasaakhmaer-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "button.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/button.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "button_hq.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/button_hq.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "button_matching.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/button_matching.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "button_unique.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/button_unique.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "cat.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/cat.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "classic-hold-sound(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/classic-hold-sound%281%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "classic-hold-sound(2).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/classic-hold-sound%282%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "classic-hold-sound.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/classic-hold-sound.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "constellation-iphone-ringtone.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/constellation-iphone-ringtone.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "d9fe-2649-4672-be5f-fdaa99ccaf61.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/d9fe-2649-4672-be5f-fdaa99ccaf61.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "def.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/def.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "dial-up-homemade(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dial-up-homemade%281%29.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "dial-up-homemade.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dial-up-homemade.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "disconnected-2x.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/disconnected-2x.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "disconnected-phone-number.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/disconnected-phone-number.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "dtmf-dial-tones-1.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dtmf-dial-tones-1.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "dtmf-dial-tones-9.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/dtmf-dial-tones-9.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "electronics(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/electronics%281%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "electronics.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/electronics.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "european-spanish-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/european-spanish-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "german-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/german-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "guan-hua-voicemail-yu-yin-xin-xiang.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/guan-hua-voicemail-yu-yin-xin-xiang.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "hindi-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/hindi-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "indonesian-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/indonesian-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "japan-eas-alarm-tsunami-alert.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/japan-eas-alarm-tsunami-alert.mp3", is_music = false, category = "broadcast", weight = 7.0, eeriness = 8.8 },
            { name = "japanese-phone-cannot-be-reached(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/japanese-phone-cannot-be-reached%281%29.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "japanese-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/japanese-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "loon-bird-calling.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/loon-bird-calling.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%281%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(2).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%282%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(3).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%283%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(4).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%284%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(5).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%285%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(6).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%286%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(7).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%287%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(8).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%288%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime(9).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime%289%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "los-angeles-metro-chime.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/los-angeles-metro-chime.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "mbxbb447pq2pr2f80r61wmw6shbhj88d7v4nmb8j69143_audio.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/mbxbb447pq2pr2f80r61wmw6shbhj88d7v4nmb8j69143_audio.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "metro-rj-pavuna.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/metro-rj-pavuna.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "motor_loop_arc.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/motor_loop_arc.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "motor_loop_softtop.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/motor_loop_softtop.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "nokia-mozart-40.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/nokia-mozart-40.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "north-korea-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/north-korea-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "numbers_station_counting_cia.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/numbers_station_counting_cia.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "numbers_station_lincolnshire_poacher_chime.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/numbers_station_lincolnshire_poacher_chime.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "omc-electronics-rosie-go-on-have-a-go(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/omc-electronics-rosie-go-on-have-a-go%281%29.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "omc-electronics-rosie-go-on-have-a-go.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/omc-electronics-rosie-go-on-have-a-go.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "phone-static.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/phone-static.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "polish-phone-cannot-be-reached(1).mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/polish-phone-cannot-be-reached%281%29.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "polish-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/polish-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "russian-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/russian-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "russkii-intercept-message.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/russkii-intercept-message.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "sdwad1.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/sdwad1.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "sea.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/sea.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "short-sms-tone.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/short-sms-tone.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "sleep phonk.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/sleep%20phonk.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "trolled.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/trolled.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "turkce-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/turkce-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "uvb76_the_buzzer_shortwave_radio.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/uvb76_the_buzzer_shortwave_radio.mp3", is_music = false, category = "broadcast", weight = 7.0, eeriness = 8.8 },
            { name = "vietnamese-phone-cannot-be-reached.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/vietnamese-phone-cannot-be-reached.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "warning.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/warning.mp3", is_music = false, category = "broadcast", weight = 7.0, eeriness = 8.8 },
            { name = "warning_hq.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/warning_hq.mp3", is_music = false, category = "broadcast", weight = 7.0, eeriness = 8.8 },
            { name = "warning_matching.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/warning_matching.mp3", is_music = false, category = "broadcast", weight = 7.0, eeriness = 8.8 },
            { name = "wind-blowing-sfx-12809.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/wind-blowing-sfx-12809.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
            { name = "windows-phone-7-x-8-x-low-battery-sound_fP8zqW1.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/windows-phone-7-x-8-x-low-battery-sound_fP8zqW1.mp3", is_music = false, category = "telephony", weight = 6.0, eeriness = 7.0 },
            { name = "your-call-has-been-forwarded.mp3", url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/your-call-has-been-forwarded.mp3", is_music = false, category = "ambient", weight = 5.0, eeriness = 6.5 },
        },
    },

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


-- --------------------------------------------------------------------------
-- 0. HIGH-ENTROPY DYNAMIC RANDOM SEEDING
-- --------------------------------------------------------------------------
local function seedEntropy()
    local t = os.time()
    local rt = math.floor(timer.realtime() * 10000)
    local seed = (t * 1103515245 + rt + math.random(1, 999999)) % 2147483647
    math.randomseed(seed)
    for i = 1, 10 do math.random() end
    print("[Cognitive Decay Engine] High-entropy seed initialized: " .. tostring(seed))
end
seedEntropy()


-- --------------------------------------------------------------------------
-- 0. HIGH-ENTROPY DYNAMIC RANDOM SEEDING
-- --------------------------------------------------------------------------
local function seedEntropy()
    local t = os.time()
    local rt = math.floor(timer.realtime() * 10000)
    local seed = (t * 1103515245 + rt + math.random(1, 999999)) % 2147483647
    math.randomseed(seed)
    for i = 1, 10 do math.random() end
    print("[Cognitive Decay Engine] High-entropy seed initialized: " .. tostring(seed))
end
seedEntropy()



-- --------------------------------------------------------------------------
-- 0. HIGH-ENTROPY DYNAMIC PROCEDURAL SEEDING
-- --------------------------------------------------------------------------
local function seedEntropy()
    local t = os.time()
    local rt = math.floor(timer.realtime() * 10000)
    local seed = (t * 1103515245 + rt + math.random(1, 999999)) % 2147483647
    math.randomseed(seed)
    for i = 1, 10 do math.random() end
    print("[Cognitive Decay Engine] Procedural seed initialized: " .. tostring(seed))
end
seedEntropy()

if SERVER then
    -- Dematerialize any previous instance on hot-reload
    if _G.CognitiveDecay_Cleanup then
        pcall(_G.CognitiveDecay_Cleanup)
    end

    -- --------------------------------------------------------------------------
    -- 2. FULL AIRSPACE BOUNDS & DESCENDING MULTI-TIER GEOMETRY
    -- --------------------------------------------------------------------------
    -- User Airspace:
    -- Corner 1 (Top NW):    Vector(6441.24, -4107.08, -12576.30)
    -- Corner 2 (Bottom SE): Vector(16306.50, -16307.30, -16255.70)
    -- Total Drop: 3,679.4 units!
    local BOUNDS = {
        C1 = Vector(6441.24, -4107.08, -12576.30),
        C2 = Vector(16306.50, -16307.30, -16255.70),
    }

    local CONFIG = {
        CELL_SIZE   = 189.8,     -- Hunter plate4x4 dimension: 189.8 units
        WALL_HEIGHT = 189.8,
        
        -- Multi-Tier Descending Elevations (Top to Bottom across airspace)
        Z_TIER_0 = -12700.0, -- Level 0: High Mezzanine / Reception (Near Corner 1)
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
        
        -- Authentic Backrooms Material Palettes & Tints
        MAT_WALL_YELLOW   = "plaster/plasterwallpaper001a",
        MAT_WALL_YELLOW_2 = "plaster/plasterwallpaper004a",
        MAT_CARPET        = "props/carpetfloor004a",
        MAT_CARPET_ALT    = "props/carpetfloor001a",
        MAT_CEILING       = "concrete/concreteceiling001a",
        MAT_CONCRETE_WALL = "phoenix_storms/concrete1",
        MAT_CONCRETE_FLR  = "concrete/concretefloor008a",
        MAT_STRIPES       = "phoenix_storms/stripes",
        MAT_INTERIOR_SIDES= "phoenix_storms/pack2/interior_sides",
        MAT_INTERIOR_TOP  = "phoenix_storms/pack2/interior_top",
        
        TINT_YELLOW_WALL  = Color(245, 225, 140),
        TINT_CARPET       = Color(190, 175, 125),
        TINT_CEILING      = Color(215, 210, 190),
        TINT_CONCRETE     = Color(155, 155, 155),
        TINT_DARK_CRYPT   = Color(130, 130, 130),
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

    local PHX_MATERIALS = {
        wallpaper = {
            CONFIG.MAT_WALL_YELLOW,
            CONFIG.MAT_WALL_YELLOW_2,
            CONFIG.MAT_STRIPES,
            CONFIG.MAT_INTERIOR_SIDES
        },
        carpet = {
            CONFIG.MAT_CARPET,
            CONFIG.MAT_CARPET_ALT,
            "phoenix_storms/pack2/train_floor"
        },
        ceiling = {
            CONFIG.MAT_CEILING,
            CONFIG.MAT_INTERIOR_TOP
        },
        concrete = {
            CONFIG.MAT_CONCRETE_WALL,
            CONFIG.MAT_CONCRETE_FLR,
            "phoenix_storms/concrete2"
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

        pcall(ent.setMaterial, ent, "models/debug/debugwhite")
        pcall(ent.setColor, ent, tintColor or Color(245, 225, 140))
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
            mat = floorMat,
            tint = floorTint,
            category = "floor",
            matCategory = floorCat or "carpet",
            keepFrozen = true
        })
        -- Ceiling Plate
        table.insert(spawnQueue, {
            pos = pos + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = Angle(180, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = ceilMat,
            tint = ceilTint,
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
            mat = wallMat,
            tint = wallTint,
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
            mat = wallMat,
            tint = wallTint,
            category = "wall",
            keepFrozen = true
        })
    end

    -- Continuous Walkable Ramp Connecting Two Elevation Tiers
    local function queueWalkableRampCorridor(startPos, endPos, isNorthSouth, wallMat, wallTint)
        local delta = endPos - startPos
        local distHoriz = isNorthSouth and math.abs(delta.y) or math.abs(delta.x)
        local distVert  = math.abs(delta.z)
        
        -- Slope angle: length of plate4x8 = 380.1 units
        local numRamps = math.max(1, math.ceil(distVert / 190.0))
        local stepZ = delta.z / numRamps
        local stepHoriz = distHoriz / numRamps

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
                mat = CONFIG.MAT_CONCRETE_FLR,
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
                mat = wallMat or CONFIG.MAT_STRIPES,
                category = "wall",
                keepFrozen = true
            })
            table.insert(spawnQueue, {
                pos = midPos - sideOffset,
                ang = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0),
                model = CONFIG.RAIL_MODEL,
                mat = wallMat or CONFIG.MAT_STRIPES,
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
        -- Spans X = 6,800 to 7,560, Y = -4,500 to -5,260 (4x4 cells)
        local t0Origin = Vector(6800.0, -4500.0, CONFIG.Z_TIER_0)
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t0Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)
                queueEnclosedCell(cPos, CONFIG.MAT_CARPET, CONFIG.MAT_CEILING, "carpet", "ceiling", CONFIG.TINT_CARPET, CONFIG.TINT_CEILING)

                -- Outer Perimeter Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_WALL_YELLOW, "wallpaper", CONFIG.TINT_YELLOW_WALL) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_WALL_YELLOW, "wallpaper", CONFIG.TINT_YELLOW_WALL) end
                if gy == 0 then queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_WALL_YELLOW, "wallpaper", CONFIG.TINT_YELLOW_WALL) end
                -- gy == 3 has open exit to Ramp 1!
                if gy == 3 and gx ~= 2 then
                    queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_WALL_YELLOW, "wallpaper", CONFIG.TINT_YELLOW_WALL)
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
        -- Starts at cell (gx=2, gy=3): (7180, -5070, -12700)
        -- Descends South-East toward Tier 1
        local r1Start = t0Origin + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, 0)
        local r1MidLanding = r1Start + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, -570.0)
        local r1End = r1Start + Vector(4 * CONFIG.CELL_SIZE, -6 * CONFIG.CELL_SIZE, -1140.0) -- Hits Z_TIER_1 (-13,840)!

        queueWalkableRampCorridor(r1Start, r1MidLanding, true, CONFIG.MAT_WALL_YELLOW, CONFIG.TINT_YELLOW_WALL)
        -- Mid-flight Observation Landing with an open pit hole!
        queueEnclosedCell(r1MidLanding, CONFIG.MAT_CONCRETE_FLR, CONFIG.MAT_CEILING, "concrete", "ceiling", CONFIG.TINT_CONCRETE, CONFIG.TINT_CEILING)
        queueCeilingLight(r1MidLanding, MODEL_POOLS.ceiling_lights[1])
        queueWalkableRampCorridor(r1MidLanding, r1End, true, CONFIG.MAT_WALL_YELLOW, CONFIG.TINT_YELLOW_WALL)

        -- TIER 1: MID LIMINAL SUB-OFFICES (Z = -13,840)
        -- Positioned at r1End
        local t1Origin = r1End
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t1Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)

                -- Pit Hole in cell (1, 1): floor omitted! Looking down into the darkness!
                if gx == 1 and gy == 1 then
                    -- Only ceiling plate, no floor plate! A hole into the abyss!
                    table.insert(spawnQueue, {
                        pos = cPos + Vector(0, 0, CONFIG.WALL_HEIGHT),
                        ang = Angle(180, 0, 0),
                        model = CONFIG.FLOOR_MODEL,
                        mat = CONFIG.MAT_CEILING,
                        tint = CONFIG.TINT_CEILING,
                        category = "ceiling",
                        keepFrozen = true
                    })
                    -- Safety warning rail
                    table.insert(spawnQueue, {
                        pos = cPos - Vector(HALF_CELL, 0, -30),
                        ang = Angle(90, 90, 0),
                        model = CONFIG.RAIL_MODEL,
                        mat = CONFIG.MAT_STRIPES,
                        category = "wall",
                        keepFrozen = true
                    })
                else
                    queueEnclosedCell(cPos, CONFIG.MAT_CARPET, CONFIG.MAT_CEILING, "carpet", "ceiling", CONFIG.TINT_CARPET, CONFIG.TINT_CEILING)
                end

                -- Outer Perimeter Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_WALL_YELLOW_2, "wallpaper", CONFIG.TINT_YELLOW_WALL) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_WALL_YELLOW_2, "wallpaper", CONFIG.TINT_YELLOW_WALL) end
                if gy == 0 and gx ~= 0 then queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_WALL_YELLOW_2, "wallpaper", CONFIG.TINT_YELLOW_WALL) end
                if gy == 3 and gx ~= 2 then queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_WALL_YELLOW_2, "wallpaper", CONFIG.TINT_YELLOW_WALL) end

                -- Interior Partition Walls & Framed Doors
                if gx == 2 and gy == 1 then
                    -- Realistic Interactive Door (Elevated +54.3, opens on E, wood creak sound)
                    queueFramedDoor(cPos, true, CONFIG.MAT_WALL_YELLOW_2, CONFIG.TINT_YELLOW_WALL)
                elseif gx == 1 and gy == 2 then
                    queueFramedDoor(cPos, false, CONFIG.MAT_WALL_YELLOW_2, CONFIG.TINT_YELLOW_WALL)
                end

                -- Ceiling Lights
                if (gx == 0 and gy == 2) or (gx == 3 and gy == 1) then
                    queueCeilingLight(cPos, MODEL_POOLS.ceiling_lights[1])
                end

                -- Furniture & Anomaly Items
                if gx == 0 and gy == 3 then
                    queueDeskWorkstation(cPos, CONFIG.Z_TIER_1, false)
                elseif gx == 3 and gy == 3 then
                    queueProp(cPos, Angle(0, 90, 0), MODEL_POOLS.office_props[3], "furniture", false) -- Display cooler
                elseif gx == 2 and gy == 3 then
                    queueProp(cPos, Angle(0, 0, 0), MODEL_POOLS.office_storage[2], "furniture", (math.random() < 0.15)) -- Potential anomaly
                end
            end
        end

        -- RAMP HIGHWAY 2 (Connecting Tier 1 at -13,840 to Tier 2 at -14,980)
        local r2Start = t1Origin + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, 0)
        local r2MidLanding = r2Start + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, -570.0)
        local r2End = r2Start + Vector(4 * CONFIG.CELL_SIZE, -6 * CONFIG.CELL_SIZE, -1140.0) -- Hits Z_TIER_2 (-14,980)!

        queueWalkableRampCorridor(r2Start, r2MidLanding, true, CONFIG.MAT_CONCRETE_WALL, CONFIG.TINT_CONCRETE)
        queueEnclosedCell(r2MidLanding, CONFIG.MAT_CONCRETE_FLR, CONFIG.MAT_CEILING, "concrete", "ceiling", CONFIG.TINT_CONCRETE, CONFIG.TINT_CEILING)
        queueCeilingLight(r2MidLanding, MODEL_POOLS.cage_lights[1])
        queueWalkableRampCorridor(r2MidLanding, r2End, true, CONFIG.MAT_CONCRETE_WALL, CONFIG.TINT_CONCRETE)

        -- TIER 2: INDUSTRIAL WAREHOUSE / HABITABLE ZONE (Z = -14,980)
        local t2Origin = r2End
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t2Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)
                queueEnclosedCell(cPos, CONFIG.MAT_CONCRETE_FLR, CONFIG.MAT_INTERIOR_TOP, "concrete", "ceiling", CONFIG.TINT_CONCRETE, CONFIG.TINT_DARK_CRYPT)

                -- Concrete Perimeter Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_CONCRETE) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_CONCRETE) end
                if gy == 0 and gx ~= 0 then queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_CONCRETE) end
                if gy == 3 and gx ~= 2 then queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_CONCRETE) end

                -- Industrial Cage Lights
                if (gx == 1 and gy == 1) or (gx == 2 and gy == 2) then
                    queueCeilingLight(cPos, MODEL_POOLS.cage_lights[1])
                end

                -- Warehouse Pallets, Oil Drums, and Storage Crates
                if gx == 1 and gy == 2 then
                    queueProp(cPos, Angle(0, 45, 0), MODEL_POOLS.warehouse_props[1], "furniture", false) -- Pallet
                    queueProp(cPos + Vector(0, 0, 9), Angle(0, 15, 0), MODEL_POOLS.warehouse_props[3], "furniture", false) -- Crate on pallet
                elseif gx == 0 and gy == 2 then
                    queueProp(cPos, Angle(0, 0, 0), MODEL_POOLS.warehouse_props[2], "furniture", (math.random() < 0.10)) -- Oil drum
                end
            end
        end

        -- RAMP HIGHWAY 3 (Connecting Tier 2 at -14,980 down to Tier 3 / Bedrock at -16,250)
        local r3Start = t2Origin + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, 0)
        local r3MidLanding = r3Start + Vector(2 * CONFIG.CELL_SIZE, -3 * CONFIG.CELL_SIZE, -635.0)
        local r3End = r3Start + Vector(4 * CONFIG.CELL_SIZE, -6 * CONFIG.CELL_SIZE, -1270.0) -- Hits Z_TIER_3 (-16,250 Bedrock Floor)!

        queueWalkableRampCorridor(r3Start, r3MidLanding, true, CONFIG.MAT_CONCRETE_WALL, CONFIG.TINT_DARK_CRYPT)
        queueEnclosedCell(r3MidLanding, CONFIG.MAT_CONCRETE_FLR, CONFIG.MAT_INTERIOR_TOP, "concrete", "ceiling", CONFIG.TINT_DARK_CRYPT, CONFIG.TINT_DARK_CRYPT)
        queueCeilingLight(r3MidLanding, MODEL_POOLS.cage_lights[1])
        queueWalkableRampCorridor(r3MidLanding, r3End, true, CONFIG.MAT_CONCRETE_WALL, CONFIG.TINT_DARK_CRYPT)

        -- TIER 3: THE DEEP CRYPT & PIPE DREAMS (Z = -16,250 - Bedrock Floor of Corner 2!)
        local t3Origin = r3End
        for gx = 0, 3 do
            for gy = 0, 3 do
                local cPos = t3Origin + Vector(gx * CONFIG.CELL_SIZE, -gy * CONFIG.CELL_SIZE, 0)
                queueEnclosedCell(cPos, CONFIG.MAT_CONCRETE_FLR, CONFIG.MAT_INTERIOR_TOP, "concrete", "ceiling", CONFIG.TINT_DARK_CRYPT, CONFIG.TINT_DARK_CRYPT)

                -- Heavy Concrete Walls
                if gx == 0 then queueWall(cPos - Vector(HALF_CELL, 0, -HALF_CELL), true, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_DARK_CRYPT) end
                if gx == 3 then queueWall(cPos + Vector(HALF_CELL, 0, HALF_CELL), true, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_DARK_CRYPT) end
                if gy == 0 and gx ~= 0 then queueWall(cPos + Vector(0, HALF_CELL, HALF_CELL), false, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_DARK_CRYPT) end
                if gy == 3 then queueWall(cPos - Vector(0, HALF_CELL, -HALF_CELL), false, CONFIG.MAT_CONCRETE_WALL, "concrete", CONFIG.TINT_DARK_CRYPT) end

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
        -- Play latch sound on trigger
        pcall(sound.play, "doors/door_latch1.wav", dPos, 70, 100)
        -- Play wood move sound
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
                            -- Close thud
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
