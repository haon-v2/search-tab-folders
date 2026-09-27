# Tab Folders for Search

Curve’s sidebar tab folders, ported by **Noah Helms (@haon-v2)** into a separate, optional module for the Search Appearance Mod Loader.

**Search is created by Drice Roland / Office Commun and its contributors.** They deserve full credit for the browser, WebKit foundation, and original Search design. This is an unofficial community contribution, not an official Search release or endorsement.

## Install

1. Update to [Search Appearance Mod Loader 0.3.0 or newer](https://github.com/haon-v2/search-appearance-mods/releases/latest). Use **Search Mod Preview.app**. Unmodified Search does not yet support these packages.
2. Download **curve-tab-folders.json** from [this repository’s releases](https://github.com/haon-v2/curve-tab-folders/releases/latest). Do not unzip or edit the JSON file.
3. In Search Mod Preview, open **Settings → Appearance → Import Mod…** and choose the file.
4. Click **Enable** beside **Curve Tab Folders**. The sidebar opens automatically.
5. Use the folder-plus menu beside **Open Tabs** to create, import, or export folders. Right-click a tab → **Move to Folder**, or drag a sidebar tab onto a folder.

[Curve Tabs](https://github.com/haon-v2/curve-tabs) is a separate, optional appearance mod. You can enable both at once. With both enabled, turn on **Show sidebar with curved tabs** to show folders alongside the curved rail. Selecting a tab in a folder scopes the curved rail to that folder; select a tab outside folders to return to the other tabs.

**First switch from official Search:** expect to sign in to your websites again. The preview has a separate profile; installing this module does not migrate cookies or passwords. Updating an existing preview preserves its profile. A seamless official Search update retaining its profile and sign-ins would require Drice / Office Commun to integrate the loader and distribute it through their signed app. No such integration is promised.

## What is included

- Create and rename folders, with bold titles, right-side disclosure arrows, and indented child tabs.
- Collapse and expand folders; state is saved locally.
- Drag ordinary sidebar tabs onto a folder, or onto **Open Tabs** to move them out.
- Themed dotted guides appear only while hovering over a tab inside a folder.
- Right-click tab moves in the sidebar, standard tab strip, and curved rail.
- New tabs and duplicated tabs inherit the current folder; reopened tabs remember their folder when it still exists.
- Separate folders per Search space.
- Remove a folder while keeping all its tabs open.
- Disable or remove the module without deleting saved folders, closing tabs, or rebuilding webpages.
- Import and export the **Curve Tab Folders JSON** format. Imported tabs stay asleep until selected.

Export **Curve Tab Folders.json** from the original Curve browser, then use **Import Folders…** in this module. Matching folder names are reused; duplicate URLs within a folder are skipped. Imports accept up to 64 folders and 100 tabs per file (1 MB maximum). Only HTTP(S) addresses are imported. Pinned tabs remain in Search’s pinned area, and private tabs cannot be placed in saved folders or exported.

## Architecture and privacy

This repository contains the module package and its documentation, **not another browser build**. The loader implements the native functionality. The package is a small declarative API 2 JSON file that enables the built-in `sidebarFolders` capability. It contains no scripts, network requests, telemetry, remote resources, or executable code.

The loader stores folder metadata locally in `tab-folders.json` and membership in each space’s existing session. Nothing is automatically imported from Curve or official Search. The module and Curve Tabs have independent enable/disable controls.

The host implementation and regression tests are maintained in [search-appearance-mods](https://github.com/haon-v2/search-appearance-mods). Future upstream Search changes are tested by that repository’s update workflow; compatibility is not a guarantee for every future release.

## Development

Validate the package with `python3 validate.py`. The loader’s test suite covers API validation, independent module selection, folder persistence, import/export, drop validation, private-tab exclusion, space isolation, curved-rail coexistence, and an actual app restart.

See [CREDITS.md](CREDITS.md) and [LICENSE](LICENSE).
