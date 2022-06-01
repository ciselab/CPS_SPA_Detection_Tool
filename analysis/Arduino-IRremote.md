# Arduino-IRremote

## Result number #1

### File name(s)
src/ir_BoseWave.cpp

### Compare results

#### Result #1

####Values removed
Values: [('BOSEWAVE_REPEAT_SPACE', '1000', '65', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_BoseWave.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/15a1fbc8d02fc610808f62494589d1cd2c4e2d93/src/ir_BoseWave.cpp
####True or False Positive:
False
####Note:
Changed 1000 to MICROS_IN_ONE_MILLI. It went from being hard-coded to using a var, though this has not something to do with performance.

#### Result #2

####Values removed
Values: [('enableIROut', '38', '47', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/22451e789a7ba113d384720cde92e80c66bf5c2c/src/ir_BoseWave.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_BoseWave.cpp
####True or False Positive:
False
####Note:
The value 38 was changed to the BOSEWAVE_KHZ var. This was a fix for a potential HCFT situation.

#### Result #3

####Values removed
Values: [('tOffset', '1', '71', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_BoseWave.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/51087db8b7a7d3eb1dab79f6a02c70ef0aefed75/src/ir_BoseWave.cpp
####True or False Positive:
False
####Note:
Instead of using a counter `tOffset`, `results.rawbuf[1]` is increased manually. Does not fit the type for HCFT.

#### Result #4

####Values removed
Values: [('space', '0', '59', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_BoseWave.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_BoseWave.cpp
####True or False Positive:
False
####Note:
The LED was set to end being off, this line was removed in the new version.

#### Result #5

####Values added
Values: [('space', '0', '57', 'IRsend'), ('aNumberOfRepeats', '1', '45', 'IRsend'), ('enableIROut', '38', '43', 'IRsend'), ('tDecodedValue', '8', '111', 'IRrecv'), ('tDecodedValue', '255', '110', 'IRrecv'), ('tOffset', '1', '70', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/f9d32954c624e0e7c0fc06d553d418a0980f72b6/src/ir_BoseWave.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/3e808fec61bcc3285ec11a39611e5ccc50b9799d/src/ir_BoseWave.cpp
####True or False Positive:
True
####Note:
`space`: regarding the led be turned off in the end: False
`aNumberOfRepeats`: Canged code structure: False
`enableIROut`: Hardcoded IR carrier frequency, see result #2 for the fix: True
`tDecodedValue`: (For both) Rewrote how to handle a success scenario: False
`tOffset`: Changed the name `index` to `tOffset`: False

#### Result #6

####Values removed
Values: [('index', '1', '122', 'IRrecv'), ('index', '0', '110', 'IRrecv'), ('complement', '0', '108', 'IRrecv'), ('command', '0', '107', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_BoseWave.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_BoseWave.cpp
####True or False Positive:
Incorrect
####Note:
`index`: (For both; incorrect find, value is there: False
`complement`: Incorrect find, value is there: False
`command`: Incorrect find, value is there: False

#### Result #7

####Values removed
Values: [('command', '0', '108', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/8834de0bf0fcbf68efc343447bbbb91ac0f4770b/src/ir_BoseWave.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/e8d461604bfec93b7314532cf8766d81d549bc4d/src/ir_BoseWave.cpp
####True or False Positive:
Incorrect
####Note:
`command`: Incorrect find, value is there

### Number of warnings:
7

## Result number #2

### File name(s)
src/ir_DistanceProtocol.cpp

### Compare results

#### Result #8

####Values added
Values: [('tMaxDurationIndex', '0', '136', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/58a2725663ecc0c62ac312460fc9d1adcc1f479d/src/ir_DistanceProtocol.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/94fa49a0f858c60b593d1437da59c873c6c3d547/src/ir_DistanceProtocol.cpp
####True or False Positive:
Incorrect
####Note:
`tMaxDurationIndex` is available on line 151 in the older version.

### Number of warnings:
1

## Result number #3

### File name(s)
src/ir_RC5_RC6.cpp

### Compare results

#### Result #9

####Values removed
Values: [('enableIROut', '36', '491', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/27fa380bdabcffc1a24b532d8da7eb338ad8d184/src/ir_RC5_RC6.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_RC5_RC6.cpp
####True or False Positive:
False
####Note:
Changed `enableIROut` from `36` to `RC5_RC6_KHZ` to avoid a potential HCFT.

#### Result #10

####Values removed
Values: [('used', '0', '483', 'IRrecv'), ('data', '0', '482', 'IRrecv'), ('val', '1', '192', 'getRClevel'), ('used', '0', '188', 'getRClevel'), ('avail', '3', '181', 'getRClevel'), ('avail', '2', '179', 'getRClevel'), ('avail', '1', '177', 'getRClevel'), (1, '0', '173', 'getRClevel')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/3283ef70875d2cafa69be93564045fba76128450/src/ir_RC5_RC6.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/8007e6539fffac67b609c05b1ec82d59cffe075c/src/ir_RC5_RC6.cpp
####True or False Positive:
False
####Note:
Big rewrite of the functions `IRrecv::decodeRC6`, no direct replacement for variables.

#### Result #11

####Values added
Values: [('val', '1', '192', 'getRClevel'), (1, '0', '173', 'getRClevel')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/2ccae65ef6e866947714028da9100a77bf12e219/src/ir_RC5_RC6.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/1acdcce7b2d015a20a4ce0e4162a3458da669351/src/ir_RC5_RC6.cpp
####True or False Positive:
False
####Note:
Changed `val` variable 1 to `MARK`. Fixed ambiguity of what the 1 or 0 meant.

#### Result #12

####Values removed
Values: [('space', '0', '647', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/3ca432fc670c97550ebb066e61de00e67f3afe44/src/ir_RC5_RC6.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/aac8748a3d07e2c6605f65880f63ea2435a4aede/src/ir_RC5_RC6.cpp
####True or False Positive:
False
####Note:
Changed `space(0);  // Always end with the LED off` to `ledOff();  // Always end with the LED off`. Fixed ambiguity what space() meant, code is better readable.

#### Result #13

####Values removed
Values: [('toggleBit', '1', '614', 'IRsend'), (1, '0', '543', 'IRrecv'), (1, '1', '541', 'IRrecv'), ('offset', '1', '496', 'IRrecv'), ('used', '0', '495', 'IRrecv'), ('data', '0', '494', 'IRrecv'), ('toggleBit', '1', '628', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/7ecfa03d06fe67fb60573321cd031f35d1a01897/src/ir_RC5_RC6.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_RC5_RC6.cpp
####True or False Positive:
Incorrect
####Note:
Issue with the result, `toggleBit` was found on line 614 in the file where it was supposed to be removed. In the file it should be available in, is was on line 625.
`toggleBit` on line 628 is available in the "available file"; and moved in the other file.
`1,0` and `1,1` was moved to a different line.
`offset`, `used`, `data` were moved to a different line.

#### Result #14

####Values added
Values: [('used', '0', '485', 'getRClevel'), ('avail', '3', '478', 'getRClevel'), ('avail', '2', '476', 'getRClevel'), ('avail', '1', '474', 'getRClevel')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_RC5_RC6.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/a876cb1679a01e6db31a4e856630ee89adeb7348/src/ir_RC5_RC6.cpp
####True or False Positive:
Incorrect
####Note:
Method `getRClevel` is available in the beginning of the file. The file has been extended by 308 extra lines of code.

#### Result #15

####Values added
Values: [('nbits', '1', '263', 'IRsend')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e8f8f2dd63ecb0d50c8a3f209d1e7389f4d4ee53/src/ir_RC5_RC6.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/052e160a3752b4b2d71c8d606333f75c5371f7f6/src/ir_RC5_RC6.cpp
####True or False Positive:
False
####Note:
Moved `nbits` out of the for loop.

#### Result #16

####Values removed
Values: [('enableIROut', '36', '218', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_RC5_RC6.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_RC5_RC6.cpp
####True or False Positive:
Incorrect
####Note:
`enableIROut` available on a different line.

### Number of warnings:
8

## Result number #4

### File name(s)
ir_RC5_RC6.cpp

### Compare results

#### Result #17

####Values added
Values: [('enableIROut', '36', '133', 'IRsend')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/88e243fe068e06d2ed602fefe6bd5effd07006e1/ir_RC5_RC6.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/eb0360e75888b8491bb2e0a6883fca8ea360135a/ir_RC5_RC6.cpp
####True or False Positive:
Incorrect
####Note:
Available on a different line (125).

### Number of warnings:
1

## Result number #5

### File name(s)
src/ir_Kaseikyo.cpp

### Compare results

#### Result #18

####Values removed
Values: [('enableIROut', '37', '287', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/22451e789a7ba113d384720cde92e80c66bf5c2c/src/ir_Kaseikyo.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_Kaseikyo.cpp
####True or False Positive:
False
####Note:
Changed `enableIROut(36)` to `enableIROut(KASEIKYO_KHZ)`, fixed a potential for HCFT.

#### Result #19

####Values added
Values: [('offset', '1', '241', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_Kaseikyo.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_Kaseikyo.cpp
####True or False Positive:
Incorrect
####Note:
Incorrrect result, variable with same value is available.

#### Result #20

####Values removed
Values: [('enableIROut', '37', '257', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_Kaseikyo.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/977debf4e6c7331a96d9798b82dc5ce682da4950/src/ir_Kaseikyo.cpp
####True or False Positive:
True
####Note:
`enableIROut` available in a different line (273). Though this value has been changed before from 36, see result #36.

### Number of warnings:
3

## Result number #6

### File name(s)
src/private/IRTimer.hpp

### Compare results

#### Result #21

####Values removed
Values: [('sSliceNumberForSendPWM', '0', '1330', 'enableSendPWM')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/1ce638b7f64cbb7abdf48fd41c87819ee252e0a8/src/private/IRTimer.hpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/fb798a5505f0a887f5b89321d21a0eae767a1f17/src/private/IRTimer.hpp
####True or False Positive:
Incorrect
####Note:
`sSliceNumberForSendPWM` has been moved from a void function to in a #define (line 1324), no changes to the var value.

#### Result #22

####Values added
Values: [('sSliceNumberForSendPWM', '0', '1330', 'enableSendPWM')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/2077fd1f508aa44da4fa1cc612347efa8aa35b85/src/private/IRTimer.hpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/1ce638b7f64cbb7abdf48fd41c87819ee252e0a8/src/private/IRTimer.hpp
####True or False Positive:
False
####Note:
Different implementation with `sSliceNumberForSendPWM`.

### Number of warnings:
2

## Result number #7

### File name(s)
src/ir_NEC.cpp

### Compare results

####Values removed
Values: [('enableIROut', '38', '357', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/22451e789a7ba113d384720cde92e80c66bf5c2c/src/ir_NEC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/e6b39b72df25a77c28cef62a073fd6c8475e4d28/src/ir_NEC.cpp
####True or False Positive:
False
####Note:
`enableIROut` changed from hardcoded value 38 to using `NEC_KHZ` to set the value (still on line 357, and it still has a value of 38 kHz).

####Values added
Values: [('offset', '1', '202', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_NEC.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_NEC.cpp
####True or False Positive:
Incorrect
####Note:
`offset` is available on line 202 in both files, no changes were made.

####Values removed
Values: [('enableIROut', '38', '266', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_NEC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_NEC.cpp
####True or False Positive:
Incorrect
####Note:
`enableIROut` is available on line 264.

####Values removed
Values: [('aAddress', '16', '85', 'IRsend'), ('enableIROut', '38', '78', 'IRsend'), ('tCommand', '8', '204', 'IRrecv'), ('tCommand', '255', '203', 'IRrecv'), ('data', '16', '202', 'IRrecv'), ('offset', '1', '167', 'IRrecv'), ('data', '0', '166', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/c55628ab24d2a0e735f910d199915d0ca3b4a15f/src/ir_NEC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/f9d32954c624e0e7c0fc06d553d418a0980f72b6/src/ir_NEC.cpp
####True or False Positive:
False
####Note:
`aAddress` is available on line 70, though this is an incorrect finding, the value 16 does not belong to `aAddress` but to calling `sendPulseDistanceWidthData`: Incorrect
`enableIROut` is available on line 58: Incorrect
`tCommand` available on line 143: Incorrect
Other `tCommand` is available on line 142: Incorrect
`data` changed from being hardcoded `data >> 16` to `results.value >> NEC_ADDRESS_BITS`: False
`offset` available on line 93, changed structure of function: Incorrect


####Values added
Values: [('aAddress', '16', '92', 'IRsend'), ('enableIROut', '38', '85', 'IRsend'), ('tCommand', '8', '197', 'IRrecv'), ('tCommand', '255', '196', 'IRrecv'), ('data', '16', '195', 'IRrecv'), ('offset', '1', '166', 'IRrecv'), ('data', '0', '165', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_NEC.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/e8f8f2dd63ecb0d50c8a3f209d1e7389f4d4ee53/src/ir_NEC.cpp
####True or False Positive:
False
####Note:
For `aAddress`, `sendPulseDistanceWidthData` was changed, see line 39: Incorrect
`enableIROut` available on line 27: Incorrect
`tCommand` structure changed: False
`data` structure changed: False
`offset` available on line 64: Incorrect
`data` available on line 63: Incorrect


####Values removed
Values: [('offset', '1', '65', 'IRrecv'), ('data', '0', '64', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_NEC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_NEC.cpp
####True or False Positive:
Incorrect
####Note:
`offset` available on line 64: Incorrect
`data` available on line 63: Incorrect

####Values removed
Values: [(1, '0', '103', 'IRrecv'), (1, '1', '101', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/b651caaf682ad4eb26bbae7e6d20f3f3b7c396b3/src/ir_NEC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_NEC.cpp
####True or False Positive:
False
####Note:
Changed structure.

### Number of warnings:
7

## Result number #8

### File name(s)
src/ir_Dish.cpp

### Compare results

####Values removed
Values: [('space', '0', '43', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/3ca432fc670c97550ebb066e61de00e67f3afe44/src/ir_Dish.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/aac8748a3d07e2c6605f65880f63ea2435a4aede/src/ir_Dish.cpp
####True or False Positive:
False
####Note:
Changed `space(0)` to turn off the LED to `ledOff()`. 

####Values added
Values: [('space', '0', '52', 'IRsend')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/df1a126897f283119b0e187fd30dfa6d79509584/src/ir_Dish.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Dish.cpp
####True or False Positive:
False
####Note:
Added `space(0)` to end with the LED off.

### Number of warnings:
2

## Result number #9

### File name(s)
src/ir_Whynter.cpp

### Compare results

####Values removed
Values: [('space', '0', '47', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_Whynter.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_Whynter.cpp
####True or False Positive:
False
####Note:
Added `space(0)` to end with the LED off.

####Values removed
Values: [('offset', '1', '54', 'IRrecv'), ('data', '0', '53', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Whynter.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_Whynter.cpp
####True or False Positive:
Incorrect
####Note:
`offset` available on line 54: incorrect
`data` available on line 53: incorrect

####Values removed
Values: [(1, '0', '93', 'IRrecv'), (1, '1', '91', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/b651caaf682ad4eb26bbae7e6d20f3f3b7c396b3/src/ir_Whynter.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Whynter.cpp
####True or False Positive:
False
####Note:
Uncommented code, changed structure.

####Values added
Values: [('data', '0', '53', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/0d4805a1299ea5ba944000dac4f41b2f2f128458/src/ir_Whynter.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/b651caaf682ad4eb26bbae7e6d20f3f3b7c396b3/src/ir_Whynter.cpp
####True or False Positive:
Incorrect
####Note:
`data` available on line 54.

### Number of warnings:
4

## Result number #10

### File name(s)
ir_Whynter.cpp

### Compare results

####Values added
Values: [(1, '0', '76', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/88e243fe068e06d2ed602fefe6bd5effd07006e1/ir_Whynter.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/eb0360e75888b8491bb2e0a6883fca8ea360135a/ir_Whynter.cpp
####True or False Positive:
Incorrect
####Note:
Available on lin 72.

### Number of warnings:
1

## Result number #11

### File name(s)
src/ir_JVC.cpp

### Compare results

####Values removed
Values: [('enableIROut', '38', '226', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/27fa380bdabcffc1a24b532d8da7eb338ad8d184/src/ir_JVC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_JVC.cpp
####True or False Positive:
False
####Note:
Changed `enableIROut(38)` to `enableIROut(JVC_KHZ)`, avoided hard-coding in target file.

####Values added
Values: [('offset', '1', '155', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_JVC.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_JVC.cpp
####True or False Positive:
Incorrect
####Note:
`offset` available on same line.

####Values removed
Values: [('enableIROut', '38', '223', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_JVC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_JVC.cpp
####True or False Positive:
Incorrect
####Note:
`enableIROut` available on line 219.

####Values removed
Values: [('offset', '1', '60', 'IRrecv'), ('data', '0', '59', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/aac2a966377c9ec99007131614d3826e990a1881/src/ir_JVC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_JVC.cpp
####True or False Positive:
Incorrect
####Note:
Available on the same lines.

####Values removed
Values: [('offset', '1', '57', 'IRrecv'), ('data', '0', '56', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/85cd7fdd65d52601020dd0cb69d927e1530e7fd5/src/ir_JVC.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_JVC.cpp
####True or False Positive:
Incorrect
####Note:
`offset` available on line 58: incorrect
`data` available on line 58: incorrect

### Number of warnings:
5

## Result number #12

### File name(s)
ir_JVC.cpp

### Compare results

####Values added
Values: [('data', '0', '59', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/88e243fe068e06d2ed602fefe6bd5effd07006e1/ir_JVC.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/eb0360e75888b8491bb2e0a6883fca8ea360135a/ir_JVC.cpp
####True or False Positive:
Incorrect
####Note:
`data` available on line 54

### Number of warnings:
1

## Result number #13

### File name(s)
src/irPronto.cpp

### Compare results

####Values added
Values: [('aSerial', '0', '243', 'IRrecv'), (1, '2', '242', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/irPronto.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/7ecfa03d06fe67fb60573321cd031f35d1a01897/src/irPronto.cpp
####True or False Positive:
False
####Note:
Changed function name and added functionality. Still available on line 239 and 238.

####Values added
Values: [('size', '0', '286', 'size_t')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/44d6a7da150637ab72846743f00501990cab4dc5/src/irPronto.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/51087db8b7a7d3eb1dab79f6a02c70ef0aefed75/src/irPronto.cpp
####True or False Positive:
Incorrect
####Note:
Available on line 257.

####Values removed
Values: [('stream', '0', '146', 'IRrecv'), (1, '2', '145', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/efbdb1d440e4d1246479fc726fe004d79c686fe5/src/irPronto.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/85bf1c76a9d726ecf5d6fce4d454b70763767b6e/src/irPronto.cpp
####True or False Positive:
Incorrect
####Note:
Available on line 150 and 151.

####Values removed
Values: [('skip', '0', '130', 'sendPronto'), ('skip', '0', '126', 'sendPronto'), ('skip', '0', '123', 'sendPronto'), (1000000, '0.5', '105', 'sendPronto'), ('cp', '0.241246', '104', 'sendPronto'), ('i', '3', '439', 'decode'), ('i', '4', '434', 'decode'), ('rptLen', '2', '428', 'decode'), ('code', '0', '405', 'decode'), ('code', '0', '388', 'decode'), ('i', '3', '461', 'irDump'), (2, '2', '459', 'irDump'), ('code', '2', '457', 'irDump'), ('FF', '255', '456', 'irDump')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/2bce3d6936f685374163687c3ca3f57c2437ae01/src/irPronto.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/f94b85756260a3cdb5191b6141dfb875606f31ff/src/irPronto.cpp
####True or False Positive:
False
####Note:
Changed structure.

####Values removed
Values: [('skip', '0', '126', 'sendPronto'), ('skip', '0', '123', 'sendPronto'), ('skip', '0', '122', 'sendPronto'), ('skip', '0', '120', 'sendPronto'), ('skip', '0', '119', 'sendPronto'), (1000000, '0.5', '102', 'sendPronto'), ('cp', '0.241246', '101', 'sendPronto'), ('i', '3', '469', 'decode'), ('i', '4', '464', 'decode'), ('rptLen', '2', '458', 'decode'), ('code', '0', '435', 'decode'), ('code', '0', '423', 'decode'), ('i', '3', '492', 'irDump'), (2, '2', '490', 'irDump'), ('code', '2', '488', 'irDump'), ('FF', '255', '487', 'irDump')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/635e8a923d6367d55cce000cb38f3d6934dc417c/src/irPronto.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/563c82c6c4fbce090590fd0c30f7c8301a4b2652/src/irPronto.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
5

## Result number #14

### File name(s)
irPronto.cpp

### Compare results

####Values changed
NEW:('code', '2', '488', 'irDump')
OLD:('code', '2', '480', 'irDump')
CHANGED:('code', '2', '480', 'irDump')
Version 1(new): https://github.com/z3t0/Arduino-IRremote/blob/845e912e9f291dbbdfbafe0dba63154bdae931df/irPronto.cpp
Version 2(old): https://github.com/z3t0/Arduino-IRremote/blob/3dec9973919d5a55bb15c20763d80ac7db9d129a/irPronto.cpp
####True or False Positive:
False
####Note:
Only a line number change happened (for this).

### Number of warnings:
1

## Result number #15

### File name(s)
src/ir_Lego.cpp

### Compare results

####Values removed
Values: [('enableIROut', '38', '190', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_Lego.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_Lego.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('space', '0', '214', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/3d27531c8380a5a8c73eac53ad6bb6ac224d6c77/src/ir_Lego.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_Lego.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #16

### File name(s)
src/ir_MagiQuest.cpp

### Compare results

####Values removed
Values: [(2, '1', '122', 'IRrecv'), (2, '1', '134', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/22451e789a7ba113d384720cde92e80c66bf5c2c/src/ir_MagiQuest.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/9acbb72760b6c8628305a30d7bdd178e3162a4df/src/ir_MagiQuest.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(0, '2', '62', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/23ed2f8335c2dbdfd974aba32471eebe229af4ca/src/ir_MagiQuest.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/d002441f9131bae2b1b65c7148fda0ccdc44164a/src/ir_MagiQuest.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(2, '1', '132', 'IRrecv'), (2, '1', '126', 'IRrecv'), ('MAGIQUEST_BITS', '6', '97', 'IRrecv'), ('offset', '1', '90', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/7ecfa03d06fe67fb60573321cd031f35d1a01897/src/ir_MagiQuest.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_MagiQuest.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('space', '0', '80', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_MagiQuest.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_MagiQuest.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('enableIROut', '38', '55', 'IRsend')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/f9d32954c624e0e7c0fc06d553d418a0980f72b6/src/ir_MagiQuest.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/8b1d47cebb92aa6a3c4d1967ea2ba4084b657722/src/ir_MagiQuest.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(2, '1', '126', 'IRrecv'), (2, '1', '120', 'IRrecv'), ('MAGIQUEST_BITS', '2', '96', 'IRrecv'), ('MAGIQUEST_BITS', '2', '87', 'IRrecv'), ('offset', '1', '80', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/6d3b21a8080c9d05b230942c5c13b016eb788b53/src/ir_MagiQuest.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_MagiQuest.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
6

## Result number #17

### File name(s)
src/ir_LG.cpp

### Compare results

####Values removed
Values: [('offset', '1', '263', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/6c0722d1ceb434376709db8ef70c93cbef93e899/src/ir_LG.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_LG.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('offset', '1', '214', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_LG.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_LG.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('enableIROut', '38', '259', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_LG.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_LG.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('space', '0', '94', 'IRsend'), ('enableIROut', '38', '74', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_LG.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_LG.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('data', '0', '23', 'IRrecv'), ('space', '0', '91', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/85cd7fdd65d52601020dd0cb69d927e1530e7fd5/src/ir_LG.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_LG.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
5

## Result number #18

### File name(s)
ir_LG.cpp

### Compare results

####Values added
Values: [('space', '0', '77', 'IRsend'), ('enableIROut', '38', '60', 'IRsend')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/eb0360e75888b8491bb2e0a6883fca8ea360135a/ir_LG.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/ec371483acceeadfbdb650bced7d672a4402a2d3/ir_LG.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(1, '0', '39', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/88e243fe068e06d2ed602fefe6bd5effd07006e1/ir_LG.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/eb0360e75888b8491bb2e0a6883fca8ea360135a/ir_LG.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #19

### File name(s)
src/ir_Denon.cpp

### Compare results

####Values removed
Values: [('offset', '1', '200', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/1ea58baec77b830bb691d840c5276c549358b071/src/ir_Denon.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/3ca432fc670c97550ebb066e61de00e67f3afe44/src/ir_Denon.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('DENON_AUTO_REPEAT_SPACE', '1000', '106', 'size_t'), ('aNumberOfRepeats', '1', '95', 'size_t'), ('enableIROut', '38', '85', 'size_t'), ('offset', '1', '194', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/0d4aceb316f6f62f8ddb5d11e30c13f0d970ced9/src/ir_Denon.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1ea58baec77b830bb691d840c5276c549358b071/src/ir_Denon.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('DENON_AUTO_REPEAT_SPACE', '1000', '106', 'size_t'), ('aNumberOfRepeats', '1', '95', 'size_t'), ('enableIROut', '38', '85', 'size_t'), ('offset', '1', '193', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/4b42ea4e3c5d9e9c1404a76b535756a129868bc3/src/ir_Denon.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/d002441f9131bae2b1b65c7148fda0ccdc44164a/src/ir_Denon.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('offset', '1', '192', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_Denon.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_Denon.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('enableIROut', '38', '35', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/c55628ab24d2a0e735f910d199915d0ca3b4a15f/src/ir_Denon.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/f9d32954c624e0e7c0fc06d553d418a0980f72b6/src/ir_Denon.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('offset', '1', '64', 'IRrecv'), ('data', '0', '63', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Denon.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_Denon.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('offset', '1', '63', 'IRrecv'), ('data', '0', '62', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/0d4805a1299ea5ba944000dac4f41b2f2f128458/src/ir_Denon.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Denon.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
7

## Result number #20

### File name(s)
src/ir_Samsung.cpp

### Compare results

####Values removed
Values: [('enableIROut', '38', '257', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/22451e789a7ba113d384720cde92e80c66bf5c2c/src/ir_Samsung.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_Samsung.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('offset', '1', '212', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/7ecfa03d06fe67fb60573321cd031f35d1a01897/src/ir_Samsung.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_Samsung.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('enableIROut', '38', '257', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_Samsung.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_Samsung.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('offset', '1', '53', 'IRrecv'), ('data', '0', '52', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Samsung.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_Samsung.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '0', '88', 'IRrecv'), (1, '1', '86', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/b651caaf682ad4eb26bbae7e6d20f3f3b7c396b3/src/ir_Samsung.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/668752283b5cbe1bc7281b31d588d0acce9e0f68/src/ir_Samsung.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
5

## Result number #21

### File name(s)
ir_Samsung.cpp

### Compare results

####Values added
Values: [(1, '0', '80', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/88e243fe068e06d2ed602fefe6bd5effd07006e1/ir_Samsung.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/eb0360e75888b8491bb2e0a6883fca8ea360135a/ir_Samsung.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #22

### File name(s)
src/ir_Sony.cpp

### Compare results

####Values removed
Values: [('enableIROut', '40', '215', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/22451e789a7ba113d384720cde92e80c66bf5c2c/src/ir_Sony.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/cae4f4e16d47691d44021c76e35d03ca90a797f6/src/ir_Sony.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(1, '0', '199', 'IRrecv'), (1, '1', '197', 'IRrecv'), ('offset', '0', '161', 'IRrecv'), ('bits', '0', '160', 'IRrecv'), ('data', '0', '159', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/e85ae16e6780f9d3a0e83487f0bac30e635a7b25/src/ir_Sony.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/4fb32a608c42727cc2d6d3529eafb229e70c437f/src/ir_Sony.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('space', '0', '245', 'IRsend')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/a79b87110c7e3fdd43cf13e09ce183cc10b1a84d/src/ir_Sony.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/1e8026609cb741023ff1053e8ae317b0bca377c8/src/ir_Sony.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '0', '80', 'IRrecv'), (1, '1', '78', 'IRrecv'), ('offset', '0', '48', 'IRrecv'), ('data', '0', '47', 'IRrecv')]
Available in: https://github.com/z3t0/Arduino-IRremote/blob/2d664bc29595ca0214f1c41ff1474d79038c79be/src/ir_Sony.cpp
Removed in: https://github.com/z3t0/Arduino-IRremote/blob/2992d5e87a9c84b1960e2cd8a5dff722c39bbffb/src/ir_Sony.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('space', '0', '40', 'IRsend')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/2bce3d6936f685374163687c3ca3f57c2437ae01/src/ir_Sony.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/b651caaf682ad4eb26bbae7e6d20f3f3b7c396b3/src/ir_Sony.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
5

## Result number #23

### File name(s)
ir_Sony.cpp

### Compare results

####Values added
Values: [(1, '0', '79', 'IRrecv')]
Not available in: https://github.com/z3t0/Arduino-IRremote/blob/88e243fe068e06d2ed602fefe6bd5effd07006e1/ir_Sony.cpp
Added in: https://github.com/z3t0/Arduino-IRremote/blob/eb0360e75888b8491bb2e0a6883fca8ea360135a/ir_Sony.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #24

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

