# Duck Hunt 5 - Build Instructions

This document outlines the steps to package the Duck Hunt 5 game for Windows distribution using Unreal Engine.

## Prerequisites

*   **Unreal Engine 5.4.0 (or newer):** Ensure the correct version of Unreal Engine is installed via the Epic Games Launcher.
*   **Visual Studio (for Windows builds):** Even for Blueprint-only projects, Unreal Engine often requires components from Visual Studio for packaging. The "Desktop development with C++" workload is recommended, including the latest MSVC toolchain and Windows SDK. The Unreal Engine installer usually prompts for these if missing.
*   **Project Cloned/Downloaded:** You should have the complete project files.

## Standard Unreal Engine Packaging Process (Windows)

As of the current project stage (Sprint 0), the game uses the standard Unreal Engine packaging process. No custom build scripts are implemented yet.

1.  **Open the Project:**
    *   Open the `DuckHunt5.uproject` file in Unreal Engine.

2.  **Select Build Configuration:**
    *   In the main toolbar, next to the "Platforms" button, you can choose the build configuration.
    *   For a distributable build, `Shipping` is recommended.
    *   For testing, `Development` can also be used.
    *   `(Editor -> File -> Package Project -> Build Configuration)` (Older UE versions)
    *   In UE5, this is often set in the Packaging Settings or directly in the Platforms dropdown menu.
        *   Go to **Platforms -> Windows -> Package Project**.
        *   Before clicking "Package Project", you might want to check **Platforms -> Windows -> Project Packaging Settings...** (or **Edit -> Project Settings -> Project -> Packaging**).

3.  **Configure Packaging Settings (Optional but Recommended):**
    *   Navigate to **Edit -> Project Settings**.
    *   Under the **Project** section, select **Packaging**.
    *   Key settings to review:
        *   **Build Configuration:** Set to `Shipping` for release builds.
        *   **Full Rebuild:** Check this for the first package or if you encounter issues.
        *   **Use Pak File:** Generally recommended to package assets into a single `.pak` file.
        *   **Maps to Include:**
            *   Expand "List of maps to include in a packaged build."
            *   Add your main persistent level (e.g., `Persistent_Lakeside` once created) and any other levels that should be part of the game package.
        *   **Advanced Settings:**
            *   **Cook everything in the project content directory (ignore list of maps above):** Can be used if you want to ensure all content is cooked, but specifying maps is usually better for optimized builds.
            *   **Create compressed cooked packages:** Recommended for smaller build sizes.

4.  **Initiate Packaging:**
    *   In the main editor toolbar, click on **Platforms**.
    *   Hover over **Windows** (or your target platform).
    *   Select **Package Project**.
    *   You will be prompted to choose a directory where the packaged game will be saved. Create a new folder (e.g., `DuckHunt5_Build_Windows`) outside of your project directory to keep things clean.
    *   Click "Select Folder".

5.  **Wait for Packaging to Complete:**
    *   Unreal Engine will start the packaging process. This can take some time, depending on the project size and your computer's performance.
    *   You can monitor the progress in the **Output Log** window (`Window -> Output Log`).

6.  **Locate the Packaged Game:**
    *   Once packaging is complete, navigate to the folder you selected in step 4.
    *   You should find a `Windows` (or `WindowsNoEditor` in older versions, now typically just `Windows`) subfolder containing the game executable (e.g., `DuckHunt5.exe`) and other necessary files.

## Running the Packaged Game

*   Navigate to the output directory (e.g., `DuckHunt5_Build_Windows/Windows/`).
*   Run the `DuckHunt5.exe` (or your project's executable name).

## Notes & Future Improvements

*   **Build Size:** As the project grows, specific cooking and compression settings will be refined to manage build size.
*   **Dedicated Build Server/CI/CD:** For more complex projects or team collaboration, setting up automated builds using Continuous Integration (CI) tools (like Jenkins, GitLab CI, GitHub Actions) with Unreal Automation Tool (UAT) would be considered.
*   **Custom Build Steps:** If any custom pre-build or post-build steps become necessary (e.g., copying specific files, running external tools), this document will be updated with instructions for those scripts.

---

This `BUILD.md` will be updated as build processes are refined or automated.
