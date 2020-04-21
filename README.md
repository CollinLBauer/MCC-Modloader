# MCC-Modloader

A modloader for Halo the Master Chief Collection on PC.

The goal of this project is to provide a simple program that can provide a quick and easy way to swap between mods in MCC on both Steam and UWP. *(Expect Steam support to come first.)* This will work for anything from simple, single file mods (think Forge World enhancements), to total overhauls like campaign reworks.

Instructions will be added to this readme with the first release.

I'm gonna take this fork in a different direction. We'll see what happens.

---

### TODO
- Switch to a compiled language (Rust?)
  - *I want the app to be launched as an executable and not require any runtime dependencies or unneccesary bloat.*
- Populate hash lists
- Create mod file structure
- Vanilla backup functions
- Swap functions (ideally through symbolic linking)
  - if symlinks are used, an uninstaller would probably be nice.
- GUI
- Lots of other things, probably.

Any contributions would be appreciated.

This project uses the GNU GENERAL PUBLIC LICENSE.
