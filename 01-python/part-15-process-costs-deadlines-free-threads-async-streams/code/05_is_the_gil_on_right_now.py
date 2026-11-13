"""Zero to AI Engineer · Python · Part 15 of 25
Slide: Is the GIL On Right Now?
Run: python 05_is_the_gil_on_right_now.py
"""
import sys, sysconfig

free_build = sysconfig.get_config_var(
    "Py_GIL_DISABLED") == 1
gil_on = (sys._is_gil_enabled()
          if hasattr(sys, "_is_gil_enabled")
          else True)
print(f"free-threaded build: {free_build}")
print(f"GIL active now: {gil_on}")
# A non-safe extension can re-enable
# the GIL at import, so check gil_on
# after imports, not just the build flag.
