[app]
title = The Guess Game
package.name = guessthebox
package.domain = com.hardik

source.dir = .
source.include_exts = py,kv,png,jpg,ogg,wav

version = 0.1
requirements = python3==3.10.13,kivy,kivymd,pillow
orientation = portrait
fullscreen = 0

# ANDROID
android.api = 31
android.minapi = 21
android.arch = arm64-v8a
android.allow_backup = True

# IMPORTANT FIXES
android.accept_sdk_license = True
android.sdk_build_tools = 31.0.0

[buildozer]
log_level = 2
warn_on_root = 1
