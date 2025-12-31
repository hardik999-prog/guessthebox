[app]
title = The Guess Game
package.name = guessthebox
package.domain = com.hardik

source.dir = .
source.include_exts = py,kv,png,jpg,ogg,wav

version = 0.1

requirements = python3==3.9,kivy,kivymd,pillow

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.minapi = 21
android.api = 31
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
