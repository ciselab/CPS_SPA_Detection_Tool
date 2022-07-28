# Arduino-IRremote

## Result number #1

### File name(s)
src/ir_Template.cpp

### Compare results

####Values removed
Values: [('SHUZU_REPEAT_SPACE', '1000', '188', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/0dc6103435e7c92a0534abc12cd3d09b1c939a81/src/ir_Template.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/15a1fbc8d02fc610808f62494589d1cd2c4e2d93/src/ir_Template.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:38
OLD:37
CHANGED:('enableIROut', '37', '167', 'IRsend')
Version 1(new): https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_Template.cpp
Version 2(old): https://github.com/z3t0/Arduino-IRremote/blob/27fa380bdabcffc1a24b532d8da7eb338ad8d184/src/ir_Template.cpp
####True or False Positive:
True
####Note:
Changed  IR carrier frequency from 38 to 37.

####Values changed
NEW:decodedRawData
OLD:value
CHANGED:('value', '65535', '236', 'IRrecv')
Version 1(new): https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_Template.cpp
Version 2(old): https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_Template.cpp
####True or False Positive:
False
####Note:
Changed name (structure), no value change happened.

####Values removed
Values: [('space', '0', '188', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_Template.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_Template.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('value', '65535', '239', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/968b2eccbc4a81bd3a35b1617f7d21134a909aa3/src/ir_Template.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_Template.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('value', '65535', '208', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/f9d32954c624e0e7c0fc06d553d418a0980f72b6/src/ir_Template.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/7f40acf2d3f9b378147b05dc72464d2040633ac0/src/ir_Template.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('offset', '1', '139', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e4517d69e8328976985f49090ccd86f2bfadb108/src/ir_Template.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/0175bff7e77205120b36ba3f299b537498993376/src/ir_Template.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('offset', '1', '149', 'IRrecv'), ('data', '0', '148', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Template.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_Template.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '0', '180', 'IRrecv'), (1, '1', '178', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/b651caaf682ad4eb26bbae7e6d20f3f3b7c396b3/src/ir_Template.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Template.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
9

## Result number #2

### File name(s)
code/ardumower/consoleui.h

### Compare results

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

####Values added
Values: [('cmd', '0', '442', 'Robot'), ('STATE_ROS', '0', '439', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/eaa315c15cf93d3cb33735f4d4828c3526ed3ab8/code/ardumower/consoleui.h
Added in: https://github.com/Ardumower/ardumower/blob/83c5aa29cdada6734a4dc03078ec85890b48a6ac/code/ardumower/consoleui.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3