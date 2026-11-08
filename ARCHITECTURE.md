# Backrooms Production Engine: Architecture & Rules Specification

## 1. Core Operating Constraints & Production Rules

### Rule I: Volumetric Spatial Maximization
The procedural engine is mandated to utilize the maximum available spatial envelope designated by the user, rather than clustering in a local island:
* **Target Coordinate Envelope:**
  * Minimum Corner: `Vector(6441.24, -16307.30, -16255.70)`
  * Maximum Corner: `Vector(16306.50, -4107.08, -12576.30)`
  * Spatial Dimensions: $\Delta X = 9,865.26\text{ units}$ | $\Delta Y = 12,200.22\text{ units}$ | $\Delta Z = 3,679.40\text{ units}$
* **Multi-Tier Verticality:**
  * Spans multiple vertical elevation levels (Sub-Basement $Z = -16,250$, Main Office Level $Z = -16,060$, Upper Mezzanine $Z = -15,870$, and extended multi-tiers).
* **Prop-Quota Safe Spatial Streaming:**
  * Uses a distance-based chunk grid ($759.2\text{ units}$ super-chunks using `plate16x16.mdl` and $189.8\text{ units}$ micro-cells using `plate4x4.mdl`).
  * Active physical props are only instantiated in the vicinity of players; distant sectors exist as pure mathematical coordinate graphs and seamlessly stream in as players traverse the facility.

---

### Rule II: The Boundary Filler Solver (Watertight Manifold)
Whenever generation expands towards a boundary (map envelope edge, maximum sector cutoff, or dead-end limit), **no open void holes or skybox gaps are permitted to exist under any circumstances**:
* **Automated Boundary Interception:**
  * The solver inspects every cell edge $(x, y, z)$ against the active bounding planes.
  * If an adjacent cell is beyond the boundary or undefined, the solver automatically injects a **Boundary Closure Seal**.
* **Closure Seal Specification:**
  1. **Perimeter Cap Walls:** Instantiates flush, full-height wall partitions (`models/hunter/plates/plate4x4.mdl`) aligned with proper surface normals (`Angle(90, 90, 0)` for North/South, `Angle(90, 0, 0)` for East/West).
  2. **Floor & Ceiling Continuous Overlap:** Floors and ceilings must extend flush to the boundary plane, eliminating any slivers or cracks.
  3. **Architectural Terminations:** Rather than invisible clip planes, boundary terminations manifest as sealed firedoors (`models/props_c17/door01_left.mdl`), heavy drywall bulkheads, or dark concrete maintenance barriers.
  4. **Zero Skybox Leakage:** Total visual containment ensures no ray of map daylight or skybox texture is ever visible to players inside the complex.

---

## 2. Dynamic Backrooms Geometry & Anomaly Pipeline

```mermaid
flowchart TD
    Bounds["User Map Bounds (9,865 x 12,200 x 3,679)"] --> Grid["Multi-Tier Coordinate Grid"]
    
    Grid --> LevelUpper["Level +1: Upper Mezzanine (Z = -15,870)"]
    Grid --> LevelMain["Level 0: Main Complex (Z = -16,060)"]
    Grid --> LevelSub["Level -1: Sub-Basement (Z = -16,250)"]
    
    LevelMain -->|Pitfall Floor Collapse| LevelSub
    LevelMain -->|Seamless Transit Ramp (Roll 150°)| LevelSub
    LevelMain -->|Seamless Transit Ramp (Roll -150°)| LevelUpper
    LevelMain -->|Wall Breach Lintel| RampHole["Ramp Hole Player Passage"]
    
    Grid --> Filler["Boundary Filler Solver"]
    Filler -->|Intercept Horizon| WaterTight["Watertight Perimeter Enclosure"]
```

### Key Mechanics:
1. **Sudden Drop Pitfalls:** Omission of Level 0 floor plates creates 190-unit vertical drops into the dark Level -1 sub-basement.
2. **Seamless Transit Ramps:** $\arcsin(189.8 / 380) = 29.965^\circ$ slope ramps with a horizontal span of $329.21\text{ units}$, meeting top and bottom landings with **$0.00\text{ gap}$**, enclosed by sloped ceilings and continuous left/right side walls.
3. **Wall Breach Ramps:** Lintel wall openings ($100\text{ units}$ vertical clearance) penetrated diagonally by ramp plates, allowing players to walk/crouch between sectors.
4. **Adaptive Sensing & Unfrozen Physics:**
   - Pre-spawn collision sensors push props $24+\text{ units}$ away from wall planes.
   - Downward line traces settle props flush onto the carpet floor ($1.2\text{ units}$ above floor plate).
   - Props unfreeze after $60\text{ms}$ and remain **permanently unfrozen** for real Source VPhysics interaction (kicking chairs, pushing tables, toppling radios).

---

## 3. Next Steps: Building "The Real One" (Production Roadmap)

1. **Chunk Coordinate Streamer:**
   - Coordinate-based hash grid mapping player positions to $(C_x, C_y, C_z)$ super-chunks.
   - FIFO prop pooling: Recycling oldest distant chunks to spawn newly approached sectors within the prop quota.
2. **Boundary Filler Integration:**
   - Automated boundary checking on all chunk borders to guarantee 100% watertight enclosure across all $9,865 \times 12,200 \times 3,679$ units.
3. **Audio Streaming & Acoustic Engine:**
   - BASS audio streaming for citizen radios and ambient hallway drones with 3D spatial falloff.
