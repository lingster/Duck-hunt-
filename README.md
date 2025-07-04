# Duck Hunt 5 (Working Title)

## Project Overview

Duck Hunt 5 is a casual first-person shooter game being developed in Unreal Engine 5.4+ using Blueprints. The core gameplay experience is centered around moving, aiming, shooting ducks, and scoring points in a stylized lakeside wetland environment.

This project aims to deliver:
*   Intuitive pick-up-and-play fun.
*   Dynamic duck AI with believable flocking and evasive behaviors.
*   A reactive world with satisfying visual and audio feedback.
*   Session-based progression with quick rounds and replayability.

This `README.md` provides basic information about the project and how to get it running.

## Engine Version

*   **Unreal Engine 5.4.0** or newer.

## How to Open and Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url> DuckHunt5
    cd DuckHunt5
    ```
2.  **Ensure Unreal Engine is Installed:**
    *   Make sure you have Unreal Engine 5.4.0 or a newer version installed via the Epic Games Launcher.
3.  **Generate Project Files (if needed):**
    *   If you don't see a `.sln` file (for Visual Studio) or if the project doesn't open directly, right-click the `DuckHunt5.uproject` file in the project's root directory.
    *   Select "Generate Visual Studio project files" (or the equivalent for your OS/IDE if you intend to open the C++ solution, though this project is Blueprint-focused).
4.  **Open the Project:**
    *   Double-click the `DuckHunt5.uproject` file to open the project in the Unreal Engine editor.
    *   Alternatively, open Unreal Engine from the Epic Games Launcher, go to your library, and browse to the project location to open it.
5.  **Running the Game:**
    *   Once the editor is open and assets are loaded, you can play the game in the editor by clicking the "Play" button in the main toolbar (or by pressing `Alt+P`).
    *   The default starting map should load automatically. If not, you might need to open the main persistent level (e.g., `Persistent_Lakeside` once created) from the Content Browser under `Content/Maps` (or the relevant folder where maps are stored).

## Build Instructions

For detailed instructions on how to package the game for Windows, please refer to the `BUILD.md` file. (Initially, this will describe the standard Unreal Engine packaging process).

## Project Structure

The project follows the folder structure outlined in the `Design.md` document, primarily under the `Content/` directory:
*   `Content/Blueprints`: Contains all game logic Blueprints.
*   `Content/Art`: Contains meshes, materials, and textures.
*   `Content/Audio`: Contains sound assets and MetaSounds.
*   `Content/Effects`: Contains Niagara particle systems.
*   `Content/Input`: Contains Input Actions and Input Mapping Contexts.
*   `Content/Maps`: (Will contain game levels)

## Design Document

For detailed information on gameplay mechanics, features, asset specifications, and architecture, please refer to the `Design.md` file located in the root of the project.

---

This README will be updated as the project progresses.
