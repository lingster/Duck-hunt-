Duck Hunting Game – Design Plan & Software Requirements Document

(Blueprint-focused, Unreal Engine 5)


---

1  Project Overview

Item	Description

Game Title	Duck Hunt 5 (working title)
Genre	Casual first-person shooter, light arcade style
Engine & Tech	Unreal Engine 5.4+, Blueprint (no C++ required)
Target Platforms	Windows PC (1080p, 60 FPS), optional VR (Quest 3 / PCVR)
Business Model	Free demo → paid DLC (extra levels, cosmetics)
Core Experience	“Move, aim, shoot, score” in a stylised lakeside wetland with dynamic day-night lighting (Lumen) and highly detailed assets (Nanite).


Project Pillars

1. Pick-up-and-play fun – intuitive controls within 30 seconds.


2. Dynamic targets – ducks exhibit believable flocking & evasive behaviour.


3. Reactive world – water splashes, foliage rustles, satisfying hit feedback.


4. Session-based progression – quick rounds, leaderboard, replayability.




---

2  High-Level Gameplay Loop

Main Menu → Level Load → Countdown → 
[Loop]  Spawn Ducks → Player Hunts → Score Ticks → Timer Ends / Ammo Depleted → 
Round Summary → (Retry | Next Level | Quit)


---

3  Functional Modules & Mechanics

#	Module / Blueprint Group	Key Responsibilities	Primary Blueprints

3.1	Player Controller	Movement (WASD), sprint, jump, crouch; mouse look; left-click fire; reload (R).	BP_PlayerCharacter, BP_PlayerController
3.2	Weapon System	Ray/line trace hitscan shotgun; pellet spread; ammo count; muzzle flash & recoil animation; shell ejection.	BP_Shotgun, child of BP_WeaponBase
3.3	Duck AI	Spawn, idle, patrol, flock, flee, hit reaction, death; random pathing volumes & splines; ragdoll on kill.	BP_Duck, BT_DuckAI (Behaviour Tree), BP_DuckSpawner
3.4	Scoring & Combo	+100 per duck, +50 headshot bonus; combo multiplier resets after 2 s of inactivity; score->HUD & backend save.	BP_GameInstance (save), BP_ScoreManager
3.5	Round Timer & States	3-minute default; handles pause, game-over, victory; communicates with UI.	BP_GameMode, BP_GameState
3.6	UI / HUD	Crosshair, ammo, timer, score, combo meter, hit markers, damage numbers; menu widgets.	W_HUD, W_MainMenu, W_RoundSummary
3.7	Audio	Gunshot, quacks, wing flaps, environment loops, hit confirms; dynamic mixing via MetaSounds.	MS_Shotgun, MS_DuckFlap
3.8	Environment	World Partition level; lake, reed beds, skybox; dynamic weather toggle.	Persistent_Lakeside, streaming sub-levels
3.9	VFX & Feedback	Niagara particle systems: muzzle flash, water splash, feather burst; camera shake.	NS_Feathers, NS_Splash, BP_CameraShake_Hit
3.10	Progression & Unlocks	Stars earned per score tier → unlock skins, time-of-day variants.	BP_UnlockManager, data tables



---

4  Detailed Functional Requirements

4.1 Player Controller

Movement Speed: Walk = 450 uu/s, Sprint = 600 uu/s.

Collision: Capsule 44 × 96 uu, BlockAllDynamic on world.

Input Mapping Context (Enhanced Input):

Action	Key / Axis	Blueprint Event

Move	WASD	IA_Move → BP_PlayerCharacter
Look	MouseXY	IA_Look
Fire	LMB / RT	IA_Fire
Reload	R / X	IA_Reload



4.2 Weapon System

Pellets per shot: 8; Spread: 3° cone.

Effective range: 4 000 uu; beyond → damage fall-off to 0 at 6 000 uu.

Ammo in clip: 6; reload time: 2 s (interruptible).

Exposes Blueprint event “OnShotHit” with hit result struct for scoring & VFX.


4.3 Duck AI

State	Behaviour	Transition

Idle	Float on water / perch	Timer, player proximity
Patrol	Fly along spline, speed 600 uu/s	Random, bullet near miss
Flee	Zig-zag & climb, speed 900 uu/s	After 5 s or out of volume
Hit	Ragdoll, play Niagara feathers, fall	On damage >0


Uses Environment Query System (EQS) to pick next waypoint.

Flocking: implements Boids (separation, alignment, cohesion) in Tick.


4.4 Scoring

OnDuckKilled:
  Base += 100
  If headshot → +50
  If ComboActive:
      Multiplier += 0.1 (max 3×)
  Score = Base * Multiplier
  Reset combo timer to 2 s

4.5 UI Requirements

HUD anchored to 16:9 safe-frame.

Score updates via animation curve (0.3 s ease).

Crosshair colours: white → red flash on hit.


4.6 Game Flow

1. Main Menu → Play ➜ loads Persistent_Lakeside with Loading Screen Widget.


2. Pre-Round Countdown (3–2–1-Go).


3. Round Active → timer/ticks.


4. Round End → summary widget, stars awarded, SaveGame update.


5. Loop or exit.




---

5  Non-Functional Requirements

Aspect	Target

Performance	60 FPS @1080p on GTX 1060; ≤ 8 ms GPU cost per frame
Memory	≤ 3 GB peak RAM
Load Time	< 10 s to first playable screen
Accessibility	Colour-blind friendly palette; remappable keys
Localization-ready	All text via String Tables



---

6  Asset & Content Specification

Category	Needed	Source

Duck skeletal mesh & animations	1	Marketplace (free “Stylized Bird Pack”)
Shotgun model & anims	1st-person rig	Marketplace or Sketchfab
Environment props	Rocks, reeds, trees, water shader	Quixel Megascans
Audio	20 SFX, 1 music loop	FreeSound.org / custom



---

7  Blueprint Architecture & Folder Structure

/Blueprints
   /Characters
       BP_PlayerCharacter
       BP_Duck
   /AI
       BT_DuckAI
       EQS_DuckWaypoint
   /Weapons
       BP_WeaponBase
       BP_Shotgun
   /Game
       BP_GameMode
       BP_GameState
       BP_GameInstance
       BP_ScoreManager
   /UI
       W_HUD
       W_MainMenu
       W_RoundSummary
/Art
   /Meshes, /Materials, /Textures
/Audio
   /MetaSounds
/Effects
   /Niagara


---

8  Data Tables & Configs

Table	Fields	Example

DT_DuckSpawn	SpawnChance, MinDelay, MaxDelay, SplinePath	0.35, 2 s, 6 s, Path_01
DT_WeaponStats	Pellets, SpreadDeg, ReloadTime	8, 3.0, 2.0
DT_Unlocks	StarThreshold, RewardType, RewardID	5, Skin, “GoldenDuck”



---

9  Milestones & Deliverables

Sprint	Duration	Deliverable

0	1 wk	Project setup, folder structure, version control
1	2 wks	Basic player controller & weapon fire
2	2 wks	Duck AI prototype (spawn, fly, hit)
3	2 wks	HUD, scoring, round timer
4	2 wks	Polished environment, VFX, audio
5	2 wks	Progression, menus, save/load
Gold	1 wk	Optimisation, QA, release build



---

10  Testing & Acceptance Criteria

Unit Tests (Blueprint Nativization disabled):

Weapon fires only when ammo > 0.

Ducks spawn within defined volume.


Performance Benchmarks: stable 60 FPS on mid-tier PC.

User-flow QA: reach game over, return to menu without hitch >10 times.

Accessibility Review: colour-blind modes verified with Sim Daltonism.



---

11  Risks & Mitigations

Risk	Impact	Mitigation

Spawn density hurts FPS	Medium	Culling volumes; reduce tick-rate of distant AI
Blueprint spaghetti	High	Strict folder structure; event dispatchers; comments
Asset license issues	Low	Use Epic-licensed/free assets only



---

12  Appendices

Reference Docs: Unreal “Lyra” starter game for sample architecture.

Style Guide: Epic’s Official Blueprint Best Practices (naming, comments).



---

✅ Ready for Implementation

This SRD gives a Blueprint developer everything needed—scope, mechanics, assets, architecture, and milestones—to start building Duck Hunt 5 in UE5. If you’d like deeper detail on any module (e.g., full Behaviour Tree for ducks or UI wireframes), let me know!

