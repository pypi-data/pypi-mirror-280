# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)[^1].

<!---
Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

-->

## [Unreleased]

## [2.5.0] - 2024-06-21

### BREAKING CHANGES

* Force libreflow minimum version to `2.6.0` to support replica of a redis cluster.

## [2.4.0] - 2024-06-06

### BREAKING CHANGES

* Force libreflow minimum version to `2.5.0`.
  * All changes of the Subprocess Manager (orginally from libreflow.flows) were applied to the original addon of `kabaret.subprocess_manager`.

### Added

* A command line argument `--show-process-view` as it's called, will show this view of `kabaret.subprocess_manager` when libreflow is started. You can also use it with the `SHOW_PROCESS_VIEW` environment variable by setting it to True.

### Changed

* Kabaret Layout Manager session arguments is updated on the GUI session according to recent changes in Kabaret 2.3.0rc6.

### Fixed

* Create Users From Kitsu: empty list info message is now used.

## [2.3.2] - 2024-06-06

### Added

* Activate the filter (search bar) on the assets, asset libs and films maps.

## [2.3.1] - 2024-06-06

### Added

* New session option to redefine its home oid. This oid can be provided either using the command line argument `--home-oid` or through the environment using the variable `KABARET_HOME_OID`.

## [2.3.0] - 2024-06-06

2.2.0 is skipped to matching with libreflow.flows

### Added

* Create Shots, Assets from Kitsu: for existing entities, default tasks are now updated, in case new tasks need to be added.
* Creation of shots and assets from Kitsu: an option can be checked to create the task default files enabled by default in the task manager.
* The session provides a new command-line option `--search-auto-indexing` to enable the search engine's automatic indexing. This feature can also be enabled by defining the `SEARCH_AUTO_INDEXING` variable in the environment of the session launch script.
* The session now uses the new Kabaret's layout manager which is enabled by default with the session autosave feature.

### Changed

* The padding of the default sequence and shot name filters in *MyTasks* settings are now 2 and 4 respectively.
* This is now possible to select asset libraries and types to create respectively in the `CreateKitsuAssetLibs` and `CreateKitsuAssetsFromTypes` action dialogs from the available ones in Kitsu.
* Clean and harmonise log messages with the session logger for a better readability.

### Fixed

* A `kitsu_name` parameter has been added to the `AssetLib` and `AssetType` classes. This parameter is hidden and not editable by default, and is used by `CreateKitsuAssetLibs` and `CreateKitsuAssetTypes` actions to retrieve the Kitsu episodes and types assets belong to (instead of relying on the mapped name or code).
* User Tasks
  * Libreflow bookmarks no longer break the interface.
  * Episode name is now passed to `get_shot_data()` to properly retrieve kitsu shot entity.

## [2.1.2] - 2023-10-12

### Added

* Enable the use of flow extensions in the whole project.

### Changed

* Methods `ensure_tasks()` of `Shot` and `Asset` objects are not sensitive to the case of the task template name.

## [2.1.1] - 2023-10-06

### Fixed

* User Tasks: libreflow bookmarks now works according with kitsu episodes

## [2.1.0] - 2023-09-19

### Added

* A hidden parameter to actions for creating films, sequences and shots from Kitsu to filter theses entities by name.
* Two options to the `CreateKitsuFilms` action to create shots and sequences in the created episodes.
* Added the new asset level in the librairies
* Code and display names for specic naming conventions of Andarta
* New backend script for handle installation and updates of Libreflow
* Default dialog size for Import Files

### Changed

* User tasks can now handle episodes and is updated to the new flow
* Versioneer has been updated to 0.28, fixing the version number issues making the install anoying at Andarta
* UI elements in the main project page
* Readme to match new steps for install
* Import Files handle the new asset level

### Fixed

* Upload to Kitsu and create film/sequences/shots now allows to use TVShows kitsu projects
* Get episodes in Kitsu with sufixes in names
* Create assets in the updated lib from Kitsu
* User Tasks: Fallback to the old URL for Kitsu My Tasks page

## [2.0.0] - 2023-07-24

Define a flow up and ready to use.
