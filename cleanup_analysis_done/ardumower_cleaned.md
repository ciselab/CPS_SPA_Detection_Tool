# ardumower

## Result number #1
### File name(s):ardumower/pfod.cpp
####Values changed
NEW:100
OLD:255
CHANGED:(1, '255', '211', 'sendMotorMenu')
Version 1(new): https://github.com/Ardumower/ardumower/blob/8996f79e1029c38215369b983cb6ef2627c80224/ardumower/pfod.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/7076af2539a8d80eb720ee6927b0f9105e1c6bb5/ardumower/pfod.cpp
####True or False Positive:
True
####Note:
`moterSpeedMax` changed from range 1-100 to 1-255.

####Values changed
NEW:2000
OLD:255
CHANGED:(1, '255', '184', 'sendMotorMenu')
Version 1(new): https://github.com/Ardumower/ardumower/blob/da8fa2af1970ffc5d4a0dc039d7c679fae70a493/ardumower/pfod.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/0b4e86d089b3f8bbb72594aaeb6eb6a96ca45c7e/ardumower/pfod.cpp
####True or False Positive:
True
####Note:
`motorCurrentMax` changed from range 1-2000 to 1-255.

####Values changed
NEW:0.01
OLD:0.1
CHANGED:('batFactor', '0.1', '420', 'processBatteryMenu')
Version 1(new): https://github.com/Ardumower/ardumower/blob/deb10377b29b9068c2bdfa6b6b6602b4db148366/ardumower/pfod.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/4ff4f08670413f135d429d54e116ca7b68d92d1f/ardumower/pfod.cpp
####True or False Positive:
True
####Note:
Battery factor changed from 0.01 to 0.1.

## Result number #2
### File name(s):tests/perimeterV2/perimeter.cpp
####Values changed
NEW:4095.0
OLD:4096.0
CHANGED:(127, '4096.0', '227', 'int16_t')
Version 1(new): https://github.com/Ardumower/ardumower/blob/7ebaf4e6b7bbd52a5c801f50fb410c5fa648bc29/tests/perimeterV2/perimeter.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/652b5ae2ac628bb5b8062681ed95cb2394186d95/tests/perimeterV2/perimeter.cpp
####True or False Positive:
True
####Note:
Normalize changed from 4095 to 4096.

## Result number #3
### File name(s):ardumower/perimeter.cpp
####Values changed
NEW:4095.0
OLD:4096.0
CHANGED:(127, '4096.0', '227', 'int16_t')
Version 1(new): https://github.com/Ardumower/ardumower/blob/7ebaf4e6b7bbd52a5c801f50fb410c5fa648bc29/ardumower/perimeter.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/652b5ae2ac628bb5b8062681ed95cb2394186d95/ardumower/perimeter.cpp
####True or False Positive:
True
####Note:
Normalization changed from 4095.0 to 4096.0.

####Values changed
NEW:3
OLD:6
CHANGED:(1, '6', '152', 'Perimeter')
Version 1(new): https://github.com/Ardumower/ardumower/blob/a3cc41f7ce5984c10f2ece406f32a44920ad19ae/ardumower/perimeter.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/f50a9d8e0958dbd386e3abd3cb00e02e65caf0d5/ardumower/perimeter.cpp
####True or False Positive:
False
####Note:
Variable has been changed, though this seems to be the area from which the filter is being used. So yes, the values has been tweaked, but it is not a HCFT.

## Result number #4
### File name(s):code/ardumower/consoleui.h
####Values changed
NEW:2
OLD:2.0
CHANGED:('PI', '2.0', '495', 'Robot')
Version 1(new): https://github.com/Ardumower/ardumower/blob/86ec6a92433fa8d63e59432ea153bf7112c6c08e/code/ardumower/consoleui.h
Version 2(old): https://github.com/Ardumower/ardumower/blob/693d737018279001c2523595353c549c71c6de5f/code/ardumower/consoleui.h
####True or False Positive:
False
####Note:
Change from int 2 to double 2.0.

####Values changed
NEW:2.0
OLD:2
CHANGED:('PI', '2', '495', 'Robot')
Version 1(new): https://github.com/Ardumower/ardumower/blob/693d737018279001c2523595353c549c71c6de5f/code/ardumower/consoleui.h
Version 2(old): https://github.com/Ardumower/ardumower/blob/f7e982b81757bfad8dd4edd4a502613cdcec2f81/code/ardumower/consoleui.h
####True or False Positive:
False
####Note:
Change from int 2 to double 2.0.
