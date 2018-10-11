@echo off

set MAX_NUMS = 500
set numPixels = 5038848
set width = 2592
set height = 1944

for /l %%locNum in (1, 1, %MAX_NUMS) do {
  set resultArray = system.callSystem("python Capture.py %%locNum")
  #python Capture.py %%locNum
  ./Analyze %resultArray %width %height
}
