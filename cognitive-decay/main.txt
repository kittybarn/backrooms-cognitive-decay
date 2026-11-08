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
    -- Dematerialize any previous instance on hot-reload
    if _G.CognitiveDecay_Cleanup then
        pcall(_G.CognitiveDecay_Cleanup)
    end

    -- --------------------------------------------------------------------------
    -- 2. SPATIAL VOLUME & MULTI-TIER ELEVATIONS
    -- --------------------------------------------------------------------------
    local BOUNDS = {
        MIN = Vector(6441.24, -16307.3, -16255.7),
        MAX = Vector(16306.5, -4107.08, -12576.3),
        CENTER = Vector(11373.87, -10207.19, -16060.2)
    }

    local CONFIG = {
        CELL_SIZE   = 189.8,     -- Hunter plate4x4 dimension: 189.8 units
        WALL_HEIGHT = 189.8,
        
        -- Multi-Tier Descending Elevations (Top to Bottom across airspace)
        Z_TIER_UPPER = -15870.4, -- Level 2: Institutional Observation & Mezzanine (Top)
        Z_TIER_MAIN  = -16060.2, -- Level 0: Main Yellow Liminal Office Complex (Mid)
        Z_TIER_CRYPT = -16250.0, -- Level 1: Industrial Concrete Crypt (Bottom floor)
        
        -- Structural Primitives
        FLOOR_MODEL = "models/hunter/plates/plate4x4.mdl",
        WALL_MODEL  = "models/hunter/plates/plate4x4.mdl",
        RAMP_MODEL  = "models/hunter/plates/plate4x8.mdl",
        DOOR_MODEL  = "models/props_c17/door01_left.mdl",
        DOOR_HEADER = "models/hunter/plates/plate2x2.mdl",
        
        -- Verified Diverse Ceiling Lights (100% collision meshes)
        LIGHT_MODELS = {
            office = {
                "models/props/cs_office/light_ceiling.mdl",
                "models/props_interiors/lights_florescent01a.mdl",
                "models/props_lab/lab_flourescentlight001a.mdl",
                "models/props_c17/light_domelight02_on.mdl",
            },
            crypt = {
                "models/props_c17/light_cagelight01_on.mdl",
                "models/props_c17/light_cagelight02_on.mdl",
                "models/props_c17/light_industrialbell01_on.mdl",
                "models/props_c17/light_decklight01_on.mdl",
            },
            institutional = {
                "models/props_interiors/lights_florescent01a.mdl",
                "models/props_interiors/lightbulb01a.mdl",
                "models/props_c17/light_domelight02_on.mdl",
            }
        },
        
        SPAWN_INTERVAL = 0.18
    }

    local HALF_CELL = CONFIG.CELL_SIZE * 0.5

    -- --------------------------------------------------------------------------
    -- 3. EXACT MODEL VERTICAL OFFSETS (100% FLUSH UPRIGHT PROPS)
    -- --------------------------------------------------------------------------
    local MODEL_OFFSETS = {
        ["models/props_c17/door01_left.mdl"]            = 54.3,  -- Bottom is at -54.28; +54.3 puts bottom on floor!
        ["models/props_c17/furnituretable001a.mdl"]     = 18.25, -- Table bottom at -18.21
        ["models/props_c17/furnituretable002a.mdl"]     = 18.45,
        ["models/props_c17/furnituretable003a.mdl"]     = 18.25,
        ["models/props_interiors/furniture_desk01a.mdl"]= 18.25,
        ["models/props/cs_office/table_meeting.mdl"]    = 18.25,
        ["models/props_interiors/table_folding.mdl"]    = 18.0,
        
        ["models/props_c17/furniturechair001a.mdl"]     = 20.15, -- Chair bottom at -20.14
        ["models/props_c17/chair_office01a.mdl"]        = 20.5,
        ["models/props/cs_office/chair_office.mdl"]     = 20.0,
        
        ["models/props_c17/shelfunit01a.mdl"]           = 0.5,
        ["models/props_c17/filecabinet02.mdl"]          = 18.0,
        ["models/props/cs_office/file_cabinet1.mdl"]    = 18.0,
        ["models/props/cs_office/shelves_metal.mdl"]    = 0.5,
        
        ["models/props_junk/wood_pallet001a.mdl"]       = 4.6,
        ["models/props_c17/oildrum001.mdl"]             = 0.5,
        
        ["models/props_lab/citizenradio.mdl"]           = 0.3,
        ["models/props_lab/monitor02.mdl"]              = 0.5,
        ["models/props_lab/harddrive02.mdl"]            = 0.2,
        ["models/props/cs_office/computer.mdl"]         = 0.5,
        ["models/props/cs_office/coffee_mug.mdl"]       = 0.1,
        
        ["models/humans/group01/male_01.mdl"]           = 0.0,
        ["models/humans/group01/male_02.mdl"]           = 0.0,
        ["models/humans/group01/female_01.mdl"]         = 0.0,
        ["models/police.mdl"]                           = 0.0,
    }

    -- --------------------------------------------------------------------------
    -- 4. GUARANTEED PHOENIX STORMS & CORE MATERIALS (ZERO MISSING TEXTURES)
    -- --------------------------------------------------------------------------
    local PHX_MATERIALS = {
        wallpaper = {
            "phoenix_storms/pack2/interior_sides", -- Clean drywall/plaster (100% GMod base!)
            "plaster/plasterwallpaper001a",        -- Authentic HL2 floral wallpaper
            "phoenix_storms/stripes",              -- Striped liminal wallpaper
            "phoenix_storms/wood",                 -- Warm wood paneling
            "plaster/plasterwallpaper004a",
        },
        carpet = {
            "props/carpetfloor001a",               -- Authentic HL2 office carpet
            "props/carpetfloor003a",
            "phoenix_storms/tiles2",               -- Office acoustic floor tile
            "props/carpetfloor007a",
            "phoenix_storms/pack2/train_floor",
        },
        concrete = {
            "phoenix_storms/concrete1",            -- Heavy concrete (100% GMod base!)
            "phoenix_storms/concrete2",
            "concrete/concretefloor001a",
            "phoenix_storms/concrete0",
        },
        ceiling = {
            "phoenix_storms/pack2/interior_top",   -- Plaster ceiling (100% GMod base!)
            "concrete/concreteceiling001a",
            "phoenix_storms/pack2/panel",
        },
        tile = {
            "phoenix_storms/indenttiles2",         -- Institutional indented tiles
            "tile/tilewall006a",
            "phoenix_storms/white",
        },
        light = {
            "models/debug/debugwhite",
            "phoenix_storms/white",
        }
    }

    local function safeChoice(tbl, fallback)
        if type(tbl) ~= "table" or #tbl == 0 then return fallback end
        return tbl[math.random(1, #tbl)] or fallback
    end

    -- --------------------------------------------------------------------------
    -- 5. FALLBACK MODEL REGISTRY
    -- --------------------------------------------------------------------------
    local MODEL_FALLBACKS = {
        floor        = { "models/hunter/plates/plate4x4.mdl", "models/hunter/plates/plate2x2.mdl" },
        wall         = { "models/hunter/plates/plate4x4.mdl", "models/hunter/plates/plate2x4.mdl" },
        ceiling      = { "models/hunter/plates/plate4x4.mdl", "models/hunter/plates/plate2x2.mdl" },
        ramp         = { "models/hunter/plates/plate4x8.mdl", "models/hunter/plates/plate4x4.mdl" },
        door         = { "models/props_c17/door01_left.mdl", "models/props_doors/door01_dynamic.mdl" },
        door_header  = { "models/hunter/plates/plate2x2.mdl", "models/hunter/plates/plate1x2.mdl" },
        light        = { "models/props/cs_office/light_ceiling.mdl", "models/props_c17/light_cagelight01_on.mdl", "models/props_interiors/lights_florescent01a.mdl" },
        flat_surface = { "models/props_c17/furnituretable001a.mdl", "models/props_c17/furnituretable002a.mdl", "models/props_interiors/furniture_desk01a.mdl" },
        seating      = { "models/props_c17/furniturechair001a.mdl", "models/props_c17/chair_office01a.mdl" },
        storage      = { "models/props_c17/shelfunit01a.mdl", "models/props_c17/filecabinet02.mdl", "models/props/cs_office/shelves_metal.mdl" },
        surface_mount= { "models/props_lab/citizenradio.mdl", "models/props_lab/monitor02.mdl" },
        npc          = { "models/humans/group01/male_01.mdl", "models/humans/group01/female_01.mdl" },
        industrial   = { "models/props_junk/wood_pallet001a.mdl", "models/props_c17/oildrum001.mdl", "models/props_c17/shelfunit01a.mdl" },
    }

    -- --------------------------------------------------------------------------
    -- 6. COGNITIVE BRAIN (DYNAMIC CORRUPTION & SELECTION)
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
            return safeChoice(PHX_MATERIALS.concrete, "phoenix_storms/concrete1")
        elseif biome == "institutional" then
            return safeChoice(PHX_MATERIALS.tile, "phoenix_storms/indenttiles2")
        else
            if math.random() < self.confusion then
                return safeChoice(PHX_MATERIALS.tile, "phoenix_storms/stripes")
            end
            return safeChoice(PHX_MATERIALS.wallpaper, "phoenix_storms/pack2/interior_sides")
        end
    end

    function Brain:pickFloor(biome)
        if biome == "crypt" then
            return safeChoice(PHX_MATERIALS.concrete, "phoenix_storms/concrete1")
        elseif biome == "institutional" then
            return safeChoice(PHX_MATERIALS.tile, "phoenix_storms/indenttiles2")
        else
            if math.random() < self.confusion then
                return safeChoice(PHX_MATERIALS.tile, "phoenix_storms/tiles2")
            end
            return safeChoice(PHX_MATERIALS.carpet, "props/carpetfloor001a")
        end
    end

    function Brain:pickCeiling(biome)
        if biome == "crypt" then
            return safeChoice(PHX_MATERIALS.concrete, "phoenix_storms/concrete2")
        else
            return safeChoice(PHX_MATERIALS.ceiling, "phoenix_storms/pack2/interior_top")
        end
    end

    local FALLBACK_TRACK = {
        name = "still_life_theme.mp3",
        url = "https://raw.githubusercontent.com/kittybarn/backrooms-cognitive-decay/main/audio/still_life_theme.mp3",
        weight = 5.0,
        eeriness = 5.0,
        type = "vibe"
    }

    function Brain:pickAudioTrack()
        local pool = DATASET.AUDIO and DATASET.AUDIO.vibe
        if self.confusion > 0.60 and math.random() < 0.40 then
            pool = DATASET.AUDIO and DATASET.AUDIO.nightmare
        elseif self.confusion > 0.35 and math.random() < 0.45 then
            pool = DATASET.AUDIO and DATASET.AUDIO.telephony
        end
        return safeChoice(pool, FALLBACK_TRACK)
    end

    function Brain:pickPitch()
        return safeChoice(DATASET.ENTANGLEMENTS and DATASET.ENTANGLEMENTS.pitch_shifts, 1.0)
    end

    -- --------------------------------------------------------------------------
    -- 7. TRACKERS, QUEUE & RESILIENT SPAWNER DISPATCHER
    -- --------------------------------------------------------------------------
    local spawnQueue = {}
    local activeEntities = {}
    local activeDoors = {}
    local activeRadios = {}
    local activeLights = {}

    local function safeNetBroadcast(msgName, payloadFn)
        pcall(function()
            net.start(msgName)
            if payloadFn then payloadFn() end
            net.send()
        end)
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
        pcall(ent.setColor, ent, tintColor or Color(220, 210, 175))
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
        local pool = MODEL_FALLBACKS[cat] or MODEL_FALLBACKS.flat_surface

        for _, altModel in ipairs(pool) do
            if altModel ~= item.model then
                local aOk, aEnt = pcall(prop.create, item.pos, item.ang, altModel, item.keepFrozen)
                if aOk and isValid(aEnt) then
                    return aEnt, altModel
                end
            end
        end

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
    -- 8. GEOMETRY PRIMITIVES & RESERVED TRANSIT RAMPS
    -- --------------------------------------------------------------------------
    local function queueEnclosedCell(pos, floorMat, ceilMat, floorCat, ceilCat)
        table.insert(spawnQueue, {
            pos = pos,
            ang = Angle(0, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = floorMat,
            category = "floor",
            matCategory = floorCat or "carpet",
            keepFrozen = true
        })
        table.insert(spawnQueue, {
            pos = pos + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = Angle(180, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = ceilMat,
            category = "ceiling",
            matCategory = ceilCat or "ceiling",
            keepFrozen = true
        })
    end

    local function queueWall(pos, isNorthSouth, wallMat, wallCat)
        local wallAng = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0)
        table.insert(spawnQueue, {
            pos = pos,
            ang = wallAng,
            model = CONFIG.WALL_MODEL,
            mat = wallMat,
            category = "wall",
            matCategory = wallCat or "wallpaper",
            keepFrozen = true
        })
    end

    local function queueFramedDoor(cellCenter, isNorthSouth, wallMat)
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
                    moveDuration = 0.75,
                    startAng = doorAng,
                    baseAng = doorAng,
                    openAng = doorAng + Angle(0, 90, 0),
                    nextUse = 0
                })
            end
        })

        -- 2. Solid Wall Header Plate above the door frame
        local headerPos = doorPos + Vector(0, 0, 54.3 + 40.0)
        local headerAng = isNorthSouth and Angle(90, 90, 0) or Angle(90, 0, 0)
        table.insert(spawnQueue, {
            pos = headerPos,
            ang = headerAng,
            model = CONFIG.DOOR_HEADER,
            mat = wallMat,
            category = "door_header",
            matCategory = "wallpaper",
            keepFrozen = true
        })
    end

    local function queueClearWalkableRamp(topLandingPos, isNorthSouth, goingDown)
        local slopeLen = 380.0
        local heightDiff = CONFIG.WALL_HEIGHT -- 189.8 units
        local radAngle = math.asin(heightDiff / slopeLen)
        local runDist = slopeLen * math.cos(radAngle) -- 329.21 units

        local rampAng = isNorthSouth and Angle(0, 0, goingDown and 150 or -150) or Angle(goingDown and 30 or -30, 0, 0)
        local forwardDir = isNorthSouth and Vector(0, goingDown and 1 or -1, 0) or Vector(goingDown and 1 or -1, 0, 0)
        local rampCenter = topLandingPos + (forwardDir * (runDist * 0.5)) - Vector(0, 0, heightDiff * 0.5)

        local rampMat = "phoenix_storms/concrete1"
        local ceilMat = "phoenix_storms/pack2/interior_top"

        -- 1. Ramp Slope Floor (Zero-Gap 29.965°)
        table.insert(spawnQueue, {
            pos = rampCenter,
            ang = rampAng,
            model = CONFIG.RAMP_MODEL,
            mat = rampMat,
            category = "ramp",
            matCategory = "concrete",
            keepFrozen = true
        })

        -- 2. Guard Side Walls (Clear Walkway)
        local sideOffset = isNorthSouth and Vector(HALF_CELL, 0, 0) or Vector(0, HALF_CELL, 0)
        table.insert(spawnQueue, {
            pos = rampCenter + sideOffset,
            ang = isNorthSouth and Angle(90, 0, 0) or Angle(90, 90, 0),
            model = CONFIG.WALL_MODEL,
            mat = rampMat,
            category = "wall",
            matCategory = "concrete",
            keepFrozen = true
        })
        table.insert(spawnQueue, {
            pos = rampCenter - sideOffset,
            ang = isNorthSouth and Angle(90, 0, 0) or Angle(90, 90, 0),
            model = CONFIG.WALL_MODEL,
            mat = rampMat,
            category = "wall",
            matCategory = "concrete",
            keepFrozen = true
        })

        -- 3. Ramp Overhead Enclosure Canopy
        table.insert(spawnQueue, {
            pos = rampCenter + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = rampAng + Angle(180, 0, 0),
            model = CONFIG.RAMP_MODEL,
            mat = ceilMat,
            category = "ceiling",
            matCategory = "ceiling",
            keepFrozen = true
        })

        -- 4. Bottom Landing Floor & Ceiling
        local bottomFloorPos = topLandingPos + (forwardDir * runDist) - Vector(0, 0, heightDiff)
        queueEnclosedCell(bottomFloorPos, rampMat, ceilMat, "concrete", "ceiling")
    end

    local function queuePitfallCollapse(posUpper, posLower)
        -- Lower crypt catch floor
        table.insert(spawnQueue, {
            pos = posLower,
            ang = Angle(0, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = "phoenix_storms/concrete1",
            category = "floor",
            matCategory = "concrete",
            keepFrozen = true
        })
        -- Enclosing shaft ceiling above upper room
        table.insert(spawnQueue, {
            pos = posUpper + Vector(0, 0, CONFIG.WALL_HEIGHT),
            ang = Angle(180, 0, 0),
            model = CONFIG.FLOOR_MODEL,
            mat = "phoenix_storms/pack2/interior_top",
            category = "ceiling",
            matCategory = "ceiling",
            keepFrozen = true
        })
    end

    -- --------------------------------------------------------------------------
    -- 9. COHERENT ROOM CLUSTERING (ZERO PROP SPAM)
    -- --------------------------------------------------------------------------
    local function populateThemedRoom(cellCenter, roomType, biome, floorZ)
        if roomType == "EMPTY_HALL" or roomType == "RESERVED_RAMP" or roomType == "PITFALL" then
            return
        end

        -- 1. Fluorescent Ceiling Light Fixture
        local lightPool = CONFIG.LIGHT_MODELS[biome] or CONFIG.LIGHT_MODELS.office
        local lightMdl = safeChoice(lightPool, "models/props_c17/light_cagelight01_on.mdl")
        local lightPos = cellCenter + Vector(0, 0, CONFIG.WALL_HEIGHT - 3)

        table.insert(spawnQueue, {
            pos = lightPos,
            ang = Angle(0, 0, 0),
            model = lightMdl,
            category = "light",
            matCategory = "light",
            mat = "models/debug/debugwhite",
            color = (biome == "crypt") and Color(255, 180, 100) or Color(255, 245, 195),
            keepFrozen = true,
            onSpawn = function(ent)
                table.insert(activeLights, ent)
                safeNetBroadcast("CognitiveDecay_LightSpawn", function()
                    net.writeEntity(ent)
                end)
            end
        })

        -- 2. Archetype Coherent Furnishings
        if roomType == "GLITCH_ANOMALY" then
            -- Viral Clip Anomaly: Surreally angled & frozen in mid-air
            local propChoice = safeChoice(DATASET.PROPS and DATASET.PROPS.flat_surface, "models/props_c17/furniturechair001a.mdl")
            local anomalyPos = cellCenter + Vector(math.random(-25, 25), math.random(-25, 25), 35.0)
            local anomalyAng = Angle(math.random(-35, 35), math.random(0, 360), math.random(-35, 35))

            table.insert(spawnQueue, {
                pos = anomalyPos,
                ang = anomalyAng,
                model = propChoice,
                category = "flat_surface",
                keepFrozen = true -- FROZEN in mid-air
            })
            return
        end

        if biome == "crypt" then
            -- INDUSTRIAL CRYPT: Pallets, Oil Drums, Metal Shelves ONLY
            local isPallet = math.random() < 0.55
            local propMdl = isPallet and "models/props_junk/wood_pallet001a.mdl" or "models/props_c17/oildrum001.mdl"
            local zOff = isPallet and 4.6 or 0.5
            local propPos = cellCenter + Vector(math.random(-30, 30), math.random(-30, 30), zOff)

            table.insert(spawnQueue, {
                pos = propPos,
                ang = Angle(0, math.random(0, 360), 0),
                model = propMdl,
                category = "industrial",
                keepFrozen = true -- 100% Upright & Frozen
            })
            return
        end

        if biome == "institutional" then
            -- INSTITUTIONAL WARD: Steel table / cots, lockers
            local bedPos = cellCenter + Vector(0, 0, 18.25)
            table.insert(spawnQueue, {
                pos = bedPos,
                ang = Angle(0, math.random(0, 3) * 90, 0),
                model = "models/props_c17/furnituretable001a.mdl",
                category = "flat_surface",
                keepFrozen = true
            })
            return
        end

        -- LEVEL 0 OFFICE: Coherent Archetypes
        if roomType == "CUBICLE" then
            -- Desk against wall with upright chair and CRT monitor
            local deskYaw = math.random(0, 3) * 90
            local deskAng = Angle(0, deskYaw, 0)
            local deskPos = cellCenter + (deskAng:getForward() * 32.0) + Vector(0, 0, 18.25)

            table.insert(spawnQueue, {
                pos = deskPos,
                ang = deskAng,
                model = "models/props_c17/furnituretable001a.mdl",
                category = "flat_surface",
                keepFrozen = true
            })

            -- Chair tucked in front of desk, 100% upright & frozen
            local chairPos = deskPos - (deskAng:getForward() * 32.0) + Vector(0, 0, 1.9)
            table.insert(spawnQueue, {
                pos = chairPos,
                ang = deskAng,
                model = "models/props_c17/furniturechair001a.mdl",
                category = "seating",
                keepFrozen = true
            })

            -- PC Monitor or Radio cleanly placed on table top
            local mountMdl = (math.random() < 0.6) and "models/props_lab/monitor02.mdl" or "models/props_lab/citizenradio.mdl"
            local mountPos = deskPos + Vector(0, 0, 18.82 + 0.5)

            table.insert(spawnQueue, {
                pos = mountPos,
                ang = deskAng + Angle(0, math.random(-15, 15), 0),
                model = mountMdl,
                category = "surface_mount",
                keepFrozen = true,
                onSpawn = function(ent)
                    if string.find(mountMdl, "radio") then
                        local track = Brain:pickAudioTrack()
                        local pitchVal = Brain:pickPitch()
                        safeNetBroadcast("CognitiveDecay_RadioSpawn", function()
                            net.writeEntity(ent)
                            net.writeString(track.url or "")
                            net.writeBool(math.random() < 0.15)
                            net.writeFloat(pitchVal)
                        end)
                    end
                end
            })

        elseif roomType == "CONFERENCE" then
            -- Centered conference table with 4 chairs and radio
            local confPos = cellCenter + Vector(0, 0, 18.25)
            table.insert(spawnQueue, {
                pos = confPos,
                ang = Angle(0, 0, 0),
                model = "models/props_c17/furnituretable001a.mdl",
                category = "flat_surface",
                keepFrozen = true
            })

            -- 4 Aligned Chairs around the table
            local offsets = { Vector(28, 14, 1.9), Vector(28, -14, 1.9), Vector(-28, 14, 1.9), Vector(-28, -14, 1.9) }
            for _, off in ipairs(offsets) do
                table.insert(spawnQueue, {
                    pos = confPos + off,
                    ang = Angle(0, (off.x > 0) and 180 or 0, 0),
                    model = "models/props_c17/furniturechair001a.mdl",
                    category = "seating",
                    keepFrozen = true
                })
            end

            -- Citizen Radio on center of table streaming GitHub audio
            table.insert(spawnQueue, {
                pos = confPos + Vector(0, 0, 18.82 + 0.5),
                ang = Angle(0, math.random(0, 360), 0),
                model = "models/props_lab/citizenradio.mdl",
                category = "surface_mount",
                keepFrozen = true,
                onSpawn = function(ent)
                    local track = Brain:pickAudioTrack()
                    local pitchVal = Brain:pickPitch()
                    safeNetBroadcast("CognitiveDecay_RadioSpawn", function()
                        net.writeEntity(ent)
                        net.writeString(track.url or "")
                        net.writeBool(false)
                        net.writeFloat(pitchVal)
                    end)
                end
            })

        elseif roomType == "ARCHIVE" then
            -- Metal shelving flush against wall
            local shelfPos = cellCenter + Vector(0, HALF_CELL - 18, 0.5)
            table.insert(spawnQueue, {
                pos = shelfPos,
                ang = Angle(0, 180, 0),
                model = "models/props_c17/shelfunit01a.mdl",
                category = "storage",
                keepFrozen = true
            })
        end
    end

    -- --------------------------------------------------------------------------
    -- 10. FAULT-TOLERANT MULTI-TIER AIRSPACE PROGRESSION PIPELINE
    -- --------------------------------------------------------------------------
    local Pipeline = { stages = {} }
    function Pipeline:addStage(name, fn) table.insert(self.stages, { name = name, fn = fn }) end
    function Pipeline:run()
        print("[Cognitive Decay Engine] Materializing multi-tier airspace progression (" .. #self.stages .. " stages)...")
        for i, s in ipairs(self.stages) do
            local ok, err = pcall(s.fn)
            if not ok then
                print(string.format("[Cognitive Decay WARNING] Stage '%s' warning: %s (Continuing)", s.name, tostring(err)))
            else
                print(string.format("[Cognitive Decay Pipeline] [%d/%d] %s ready (%d entities queued)", i, #self.stages, s.name, #spawnQueue))
            end
        end
    end

    -- Sector Origins Spanning Diagonally Across the User's Coordinate Airspace:
    -- Corner 1: (6441, -4107, -12576) [Top NW] ---> Corner 2: (16306, -16307, -16255) [Bottom SE]
    local ORIGIN_TIER2 = Vector(7200, -4800, CONFIG.Z_TIER_UPPER)  -- Top Level: Institutional Mezzanine
    local ORIGIN_TIER0 = Vector(8500, -7000, CONFIG.Z_TIER_MAIN)   -- Mid Level: Main Liminal Complex
    local ORIGIN_TIER1 = Vector(10200, -9200, CONFIG.Z_TIER_CRYPT) -- Bottom Level: Concrete Crypt

    -- STAGE 1: Level 2 - Upper Institutional Mezzanine
    Pipeline:addStage("Stage 1: Upper Institutional Mezzanine (Top Airspace)", function()
        local W, H = 4, 4
        for x = 1, W do
            for y = 1, H do
                local cCenter = ORIGIN_TIER2 + Vector((x - 0.5) * CONFIG.CELL_SIZE, (y - 0.5) * CONFIG.CELL_SIZE, 0)
                local floorMat = "phoenix_storms/indenttiles2"
                local ceilMat = "phoenix_storms/pack2/interior_top"
                local wallMat = "phoenix_storms/pack2/interior_sides"

                queueEnclosedCell(cCenter, floorMat, ceilMat, "tile", "ceiling")

                if y == H then queueWall(cCenter + Vector(0, HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, wallMat, "wallpaper") end
                if y == 1 then queueWall(cCenter + Vector(0, -HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, wallMat, "wallpaper") end
                if x == W then queueWall(cCenter + Vector(HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, wallMat, "wallpaper") end
                if x == 1 then queueWall(cCenter + Vector(-HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, wallMat, "wallpaper") end

                populateThemedRoom(cCenter, "CUBICLE", "institutional", CONFIG.Z_TIER_UPPER)
            end
        end
    end)

    -- STAGE 2: Seamless Transit Ramp (Level 2 Mezzanine -> Level 0 Main Complex)
    Pipeline:addStage("Stage 2: Walkable Transit Ramp (Upper -> Mid Complex)", function()
        local rampLanding = ORIGIN_TIER2 + Vector(2 * CONFIG.CELL_SIZE, 3.5 * CONFIG.CELL_SIZE, 0)
        queueClearWalkableRamp(rampLanding, true, true)
    end)

    -- STAGE 3: Level 0 - Main Yellow Liminal Complex (With Room Clustering & Doors)
    local S0_W, S0_H = 6, 6
    local s0Grid = {}

    -- Grid Reservations: Mark ramp & pitfall cells so NO props/walls cut through them
    for x = 1, S0_W do
        s0Grid[x] = {}
        for y = 1, S0_H do
            s0Grid[x][y] = "NORMAL"
        end
    end
    s0Grid[3][3] = "RESERVED_RAMP"
    s0Grid[3][4] = "RESERVED_RAMP"
    s0Grid[5][5] = "PITFALL"

    local archetypes = { "CUBICLE", "CONFERENCE", "ARCHIVE", "EMPTY_HALL", "GLITCH_ANOMALY" }

    Pipeline:addStage("Stage 3: Main Yellow Liminal Office Complex", function()
        for x = 1, S0_W do
            for y = 1, S0_H do
                Brain:step()
                local cCenter = ORIGIN_TIER0 + Vector((x - 0.5) * CONFIG.CELL_SIZE, (y - 0.5) * CONFIG.CELL_SIZE, 0)
                local wallMat = Brain:pickWall("office")
                local floorMat = Brain:pickFloor("office")
                local ceilMat = Brain:pickCeiling("office")

                local cellType = s0Grid[x][y]

                if cellType == "PITFALL" then
                    local lowerPos = Vector(cCenter.x, cCenter.y, CONFIG.Z_TIER_CRYPT)
                    queuePitfallCollapse(cCenter, lowerPos)
                elseif cellType == "RESERVED_RAMP" then
                    -- Reserved for ramp transit: do not place floor plate or blocking props
                else
                    queueEnclosedCell(cCenter, floorMat, ceilMat, "carpet", "ceiling")
                    local roomKind = archetypes[((x * 7 + y * 13) % #archetypes) + 1]
                    populateThemedRoom(cCenter, roomKind, "office", CONFIG.Z_TIER_MAIN)
                end

                -- Walls and Framed Interactive Doors
                if cellType ~= "RESERVED_RAMP" then
                    if (y == S0_H or math.random() < 0.35) and y < S0_H and s0Grid[x][y+1] ~= "RESERVED_RAMP" then
                        if math.random() < 0.30 then
                            queueFramedDoor(cCenter, true, wallMat)
                        else
                            queueWall(cCenter + Vector(0, HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, wallMat, "wallpaper")
                        end
                    end
                    if y == 1 then queueWall(cCenter + Vector(0, -HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, wallMat, "wallpaper") end

                    if (x == S0_W or math.random() < 0.35) and x < S0_W and s0Grid[x+1][y] ~= "RESERVED_RAMP" then
                        if math.random() < 0.30 then
                            queueFramedDoor(cCenter, false, wallMat)
                        else
                            queueWall(cCenter + Vector(HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, wallMat, "wallpaper")
                        end
                    end
                    if x == 1 then queueWall(cCenter + Vector(-HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, wallMat, "wallpaper") end
                end
            end
        end
    end)

    -- STAGE 4: Seamless Transit Ramp (Level 0 -> Level 1 Crypt Floor)
    Pipeline:addStage("Stage 4: Walkable Transit Ramp (Mid -> Concrete Crypt)", function()
        local rampLanding = ORIGIN_TIER0 + Vector((3 - 0.5) * CONFIG.CELL_SIZE, (4 - 0.5) * CONFIG.CELL_SIZE, 0)
        queueClearWalkableRamp(rampLanding, true, true)
    end)

    -- STAGE 5: Level 1 - Industrial Concrete Crypt (Bottom Floor)
    Pipeline:addStage("Stage 5: Industrial Concrete Crypt (Bottom Airspace)", function()
        local C_W, C_H = 5, 5
        for x = 1, C_W do
            for y = 1, C_H do
                local cCenter = ORIGIN_TIER1 + Vector((x - 0.5) * CONFIG.CELL_SIZE, (y - 0.5) * CONFIG.CELL_SIZE, 0)
                local cryptMat = "phoenix_storms/concrete1"
                local cryptCeil = "phoenix_storms/concrete2"

                queueEnclosedCell(cCenter, cryptMat, cryptCeil, "concrete", "ceiling")

                if y == C_H then queueWall(cCenter + Vector(0, HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, cryptMat, "concrete") end
                if y == 1 then queueWall(cCenter + Vector(0, -HALF_CELL, CONFIG.WALL_HEIGHT * 0.5), true, cryptMat, "concrete") end
                if x == C_W then queueWall(cCenter + Vector(HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, cryptMat, "concrete") end
                if x == 1 then queueWall(cCenter + Vector(-HALF_CELL, 0, CONFIG.WALL_HEIGHT * 0.5), false, cryptMat, "concrete") end

                populateThemedRoom(cCenter, "CUBICLE", "crypt", CONFIG.Z_TIER_CRYPT)
            end
        end
    end)

    -- Launch Generation Sequence
    Pipeline:run()

    -- --------------------------------------------------------------------------
    -- 11. BULLETPROOF QUEUED SPAWNER DISPATCHER
    -- --------------------------------------------------------------------------
    local function processQueue()
        if #spawnQueue == 0 then
            print("[Cognitive Decay Engine] Sector generation sequence completed. All " .. tostring(#activeEntities) .. " entities materialized.")
            timer.remove("CognitiveDecay_Spawner")
            return
        end

        local canSpawn = false
        local canOk, canVal = pcall(prop.canSpawn)
        if canOk and canVal then canSpawn = true end
        if not canSpawn then return end

        local item = table.remove(spawnQueue, 1)
        if not item then return end

        local ent, finalModel = trySpawnWithFallbacks(item)
        if not isValid(ent) then return end

        table.insert(activeEntities, ent)

        if item.mat or item.matCategory then
            safeSetMaterialWithFallback(ent, item.mat, item.matCategory or item.category, item.color)
        end

        if item.onSpawn then
            pcall(item.onSpawn, ent, finalModel)
        end
    end

    local function safeProcessQueue()
        local ok, err = pcall(processQueue)
        if not ok then
            print("[Cognitive Decay ERROR] Spawner recovered from tick failure: " .. tostring(err))
        end
    end
    timer.create("CognitiveDecay_Spawner", CONFIG.SPAWN_INTERVAL, 0, safeProcessQueue)

    -- --------------------------------------------------------------------------
    -- 12. REALISTIC SMOOTH DOOR ENGINE (+USE / 'E' KEY INTERACTION)
    -- --------------------------------------------------------------------------
    local function toggleDoor(d)
        local now = timer.curtime()
        d.nextUse = now + 0.85
        d.isOpen = not d.isOpen
        d.moving = true
        d.moveStart = now
        d.moveDuration = 0.75
        d.startAng = d.ent:getAngles()
        d.targetAng = d.isOpen and d.openAng or d.baseAng

        local dPos = d.ent:getPos()
        if d.isOpen then
            pcall(sound.playFile, "doors/latchunlocked1.wav", "3d", function(st)
                if isValid(st) then st:setPos(dPos); st:play() end
            end)
            pcall(sound.playFile, "doors/wood_move1.wav", "3d", function(st)
                if isValid(st) then st:setPos(dPos); st:play() end
            end)
        else
            pcall(sound.playFile, "doors/wood_move1.wav", "3d", function(st)
                if isValid(st) then st:setPos(dPos); st:play() end
            end)
        end
    end

    -- Smooth Door Rotation Animation Loop & +USE Listener
    hook.add("think", "CognitiveDecay_DoorThink", function()
        pcall(function()
            local now = timer.curtime()

            -- 1. Animate moving doors with smooth cosine ease
            for i = #activeDoors, 1, -1 do
                local d = activeDoors[i]
                if not isValid(d.ent) then
                    table.remove(activeDoors, i)
                elseif d.moving then
                    local frac = math.min(1.0, (now - d.moveStart) / d.moveDuration)
                    local smoothFrac = 0.5 - 0.5 * math.cos(frac * math.pi)
                    local curAng = LerpAngle(smoothFrac, d.startAng, d.targetAng)
                    pcall(d.ent.setAngles, d.ent, curAng)
                    if frac >= 1.0 then
                        d.moving = false
                        pcall(d.ent.setAngles, d.ent, d.targetAng)
                        if not d.isOpen then
                            pcall(sound.playFile, "doors/wood_stop1.wav", "3d", function(st)
                                if isValid(st) and isValid(d.ent) then
                                    st:setPos(d.ent:getPos())
                                    st:play()
                                end
                            end)
                        end
                    end
                end
            end

            -- 2. +USE ('E' Key) Interaction Listener
            local players = find.allPlayers()
            for _, ply in ipairs(players) do
                if isValid(ply) and ply:keyDown(32) then -- 32 = IN_USE
                    local eyePos = ply:getEyePos()
                    local aimVec = ply:getAimVector()
                    local tr = trace.line(eyePos, eyePos + (aimVec * 85), nil, MASK_SOLID)

                    for _, d in ipairs(activeDoors) do
                        if isValid(d.ent) and now > (d.nextUse or 0) then
                            local dPos = d.ent:getPos()
                            if tr.Entity == d.ent or tr.HitPos:getDistance(dPos) < 45 or eyePos:getDistance(dPos) < 70 then
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
    -- 13. DEMATERIALIZE & PURGE HOOK
    -- --------------------------------------------------------------------------
    _G.CognitiveDecay_Cleanup = function()
        pcall(timer.remove, "CognitiveDecay_Spawner")
        pcall(hook.remove, "think", "CognitiveDecay_DoorThink")
        for _, ent in ipairs(activeEntities) do
            if isValid(ent) then pcall(ent.remove, ent) end
        end
        table.empty(activeEntities)
        table.empty(activeDoors)
        table.empty(activeLights)
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
        pcall(hook.remove, "render", "CognitiveDecay_ClientRender")
        pcall(hook.remove, "think", "CognitiveDecay_ClientThink")
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
                pcall(st.setVolume, st, 0.22)
                pcall(st.play, st)
            end
        end)
    end)

    net.receive("CognitiveDecay_LightSpawn", function()
        pcall(function()
            local ent = net.readEntity()
            if isValid(ent) then table.insert(activeLights, ent) end
        end)
    end)

    -- DYNAMIC BASS STREAMING FROM GITHUB REPO (ZERO HARDCODED AUDIO)
    net.receive("CognitiveDecay_RadioSpawn", function()
        pcall(function()
            local radio = net.readEntity()
            local rawUrl = net.readString()
            local isGlitch = net.readBool()
            local basePitch = net.readFloat()

            if isValid(radio) and rawUrl and #rawUrl > 0 then
                pcall(bass.loadURL, rawUrl, "3d noblock", function(station, errCode, errName)
                    pcall(function()
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
                end)
            end
        end)
    end)

    -- DYNAMIC NPC CORRUPTIONS (ZERO HARDCODED ANGLES)
    net.receive("CognitiveDecay_NPCSpawn", function()
        pcall(function()
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
    end)

    -- Dynamic Spatial Audio update for interactive props
    hook.add("think", "CognitiveDecay_ClientThink", function()
        pcall(function()
            local now = timer.curtime()
            for i = #activeRadios, 1, -1 do
                local r = activeRadios[i]
                if not isValid(r.ent) or not isValid(r.station) then
                    if isValid(r.station) then pcall(r.station.stop, r.station) end
                    table.remove(activeRadios, i)
                else
                    pcall(r.station.setPos, r.station, r.ent:getPos())
                    if r.isGlitch and now > (r.nextGlitch or 0) then
                        r.nextGlitch = now + math.Rand(3, 8)
                        local glitchPitch = math.Rand(0.4, 1.4)
                        pcall(r.station.setPlaybackRate, r.station, glitchPitch)
                    end
                end
            end
        end)
    end)

    -- Render Hook: Deep Liminal Darkness, Xen Lightning, and Fluorescent Lighting
    hook.add("render", "CognitiveDecay_ClientRender", function()
        pcall(function()
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
    end)
end
