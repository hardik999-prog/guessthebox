[app]

title = The Guess Game
package.name = guessthebox
package.domain = com.hardik

source.dir = .
source.include_exts = py,kv,png,jpg,ogg,wav

version = 0.1

requirements = python3==3.10,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
fullscreen = 0


# ---------------- ANDROID ----------------

android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk_api = 21

android.accept_sdk_license = True
android.allow_backup = True

android.debug_artifact = apk


# ---------------- BUILD ----------------

[buildozer]
log_level = 2
warn_on_root = 1
