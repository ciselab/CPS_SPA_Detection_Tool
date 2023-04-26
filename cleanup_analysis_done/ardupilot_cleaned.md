# ardupilot

## Result number #1
### File name(s):libraries/AP_HAL/HAL.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:9
OLD:8
CHANGED:(7, '8', '20', 'AP_HAL')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/8c2074907b9b8ba9e390391b232d42f576fedfc6/libraries/AP_HAL/HAL.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/ebc1f9acf67646f60d225151a86eaf612742b05c/libraries/AP_HAL/HAL.cpp
####True or False Positive:
False
####Note:
This maps the historical use of uartB as SERIAL3. The value 9 was added to the mapping. The value 8 is still there, this was not changed to 9.
[ANALYSE]

## Result number #2
### File name(s):libraries/AP_Baro/AP_Baro_BMP280.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:256.0
OLD:25600.0
CHANGED:('p', '25600.0', '194', 'AP_Baro_BMP280')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/740e3224386c810f5068fd543e27d1d778f53c69/libraries/AP_Baro/AP_Baro_BMP280.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/cb8a34f78456674af1ec8f712395d89012586ecc/libraries/AP_Baro/AP_Baro_BMP280.cpp
####True or False Positive:
True
####Note:
The Barometer scale was fixed in commit 740e3224386c810f5068fd543e27d1d778f53c69. No further explanation was given why this change was needed.
[ANALYSE]

## Result number #3
### File name(s):ArduCopter/heli.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:0.001
OLD:1000.0
CHANGED:('get_control_in', '1000.0', '146', 'Copter')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/55ad1548e412e12c049397505c21ac976bfbc8b2/ArduCopter/heli.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/5ac13c0355fcefff47f30fd3fc96d3f89aa56bc6/ArduCopter/heli.cpp
####True or False Positive:
True
####Note:
The heli rotor speed was fixed in commit 55ad1548e412e12c049397505c21ac976bfbc8b2. No further explanation was given why this change was needed.
[ANALYSE]

## Result number #4
### File name(s):libraries/AP_Landing/AP_Landing_Deepstall.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.001
OLD:1000.0
CHANGED:(200, '1000.0', '513', 'AP_Landing_Deepstall')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/202b40562fc40893e9144749c34d2e5cda57f75f/libraries/AP_Landing/AP_Landing_Deepstall.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/cc150f75c78e770c69c690b720448034d4964c66/libraries/AP_Landing/AP_Landing_Deepstall.cpp
####True or False Positive:
False
####Note:
The value was changed form 1e-3 to 1000, not from 0.001. Besides a different notation, the value did not change.
This change was done in commit 202b40562fc40893e9144749c34d2e5cda57f75f.
[ANALYSE]

## Result number #5
### File name(s):libraries/AP_RCProtocol/examples/RCProtocolTest/RCProtocolTest.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:1073
OLD:1070
CHANGED:(1060, '1070', '217', 'loop')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/80e1c0ebb0f97f9890682f673c4761a98b68dba9/libraries/AP_RCProtocol/examples/RCProtocolTest/RCProtocolTest.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/4e88adf86e0b7758ea25e5095f7ed7698410095c/libraries/AP_RCProtocol/examples/RCProtocolTest/RCProtocolTest.cpp
####True or False Positive:
False
####Note:
The dsm_output was changed in this line. But this is a testing file, not a file of interest.
[ANALYSE]

## Result number #6
### File name(s):libraries/AP_Notify/ToshibaLED_I2C.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('red', '16', '65', 'ToshibaLED_I2C')
OLD:('red', '4', '61', 'ToshibaLED_I2C')
CHANGED:('red', '4', '61', 'ToshibaLED_I2C')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/56180089351cac15ebf3eb87fa36d217d915f033/libraries/AP_Notify/ToshibaLED_I2C.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/0b69e4346436a9f67be7f6b61e5a178404090544/libraries/AP_Notify/ToshibaLED_I2C.cpp
####True or False Positive:
False
####Note:
Setting of the RGB color for the ToshibaLED I2C driver. '(uint8_t)(red>>4)' was changed to '(uint8_t)(red / 16)'.
The driver was fixed in commit 56180089351cac15ebf3eb87fa36d217d915f033 with commit message "AP_Notify: ToshibaLED_I2C: Fix driver after I2CDevice conversion".
Does not fit for HCFT AP.
[ANALYSE]

## Result number #7
### File name(s):ArduPlane/Attitude.cpp
ArduPlane/servos.cpp
ArduPlane/Attitude.pde
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.01
OLD:100
CHANGED:('target_airspeed', '100', '395', 'set_servos')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/5bfd1200d60204e26c34e57a85a914ba3dc0ad83/ArduPlane/Attitude.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/9c1ac2d9e6856bc8e561fed6d60ab43a7ad3b42b/ArduPlane/Attitude.pde
####True or False Positive:
False
####Note:
Instead of 'value divided by 100', the notation changed to 'value times 0.01'.
Which does not change the result, besided that the value did not needed to be casted to float before the calculation.
Could be interesting to verify how much of an performance impact this has. Though this change does not fit for HCFT AP.
[ANALYSE]

## Result number #8
### File name(s):libraries/AP_HAL_ChibiOS/CANFDIface.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:2
OLD:1
CHANGED:(1, '1', '1067', 'CH_IRQ_HANDLER')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/f57b1b9c4bed8c37fb7a341cce822e479efd96bf/libraries/AP_HAL_ChibiOS/CANFDIface.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/439a944801fd0240a3ddb77eb0fddf8e421e8bbc/libraries/AP_HAL_ChibiOS/CANFDIface.cpp
####True or False Positive:
False
####Note:
Change in CAN inferface handler.
[ANALYSE]

## Result number #9
### File name(s):libraries/AP_NavEKF3/AP_NavEKF3_Measurements.cpp
libraries/AP_NavEKF2/AP_NavEKF2_Measurements.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:0.2
OLD:0.1
CHANGED:('gyro_diff_limit', '0.1', '1322', 'NavEKF3_core')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/53c4b163ce61a8d58651cb07e54bcfa0bbbdae44/libraries/AP_NavEKF3/AP_NavEKF3_Measurements.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/4605870788427302ed73991878e1b770992abf47/libraries/AP_NavEKF3/AP_NavEKF3_Measurements.cpp
####True or False Positive:
True
####Note:
The gyro_diff_limit has been changed from 0.1 to 0.2f, this change was done in commit 53c4b163ce61a8d58651cb07e54bcfa0bbbdae44.
Sensitivity changes were done base on user supplied logs.
[ANALYSE]

####Values changed
NEW:5.0
OLD:1.0
CHANGED:('accel_diff_limit', '1.0', '1071', 'NavEKF3_core')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/eeac0a05b960b5ef0a6f0213c7f3ea5c44932a29/libraries/AP_NavEKF3/AP_NavEKF3_Measurements.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/ebb8bb4f6fd846b55f415e19f3a7b7a3fef32c7f/libraries/AP_NavEKF3/AP_NavEKF3_Measurements.cpp
####True or False Positive:
True
####Note:
The accel_diff_limit was changed, together with other changes in commit eeac0a05b960b5ef0a6f0213c7f3ea5c44932a29.
The reasoning was to reduce the sensitivity.
[ANALYSE]

## Result number #10
### File name(s):libraries/AP_Math/AP_Math.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('roll', '0.5', '81', 'quaternion_from_euler')
OLD:('roll', '2', '81', 'quaternion_from_euler')
CHANGED:('roll', '2', '81', 'quaternion_from_euler')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/4d65cda0eaec30d3e185f7fa8ecc237e1f41ec17/libraries/AP_Math/AP_Math.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/8abbbe57139bfa335cdeefb86aecdb5a71c5bd90/libraries/AP_Math/AP_Math.cpp
####True or False Positive:
False
####Note:
The change done was to change 'roll divided by 2' to 'roll time 0.5'. Which does not change the result.
Unsure why this change was done. Changes were made in commit 4d65cda0eaec30d3e185f7fa8ecc237e1f41ec17.
[ANALYSE]

## Result number #11
### File name(s):libraries/DataFlash/DataFlash_Backend.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE TRUE]
####Values changed
NEW:65
OLD:64
CHANGED:('msg', '64', '411', 'DataFlash_Backend')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/4c794ebba3d2928c58bf51648e0ffc4d12cf2b1a/libraries/DataFlash/DataFlash_Backend.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/6daa2412357e903edb6abe8b750bda3d3a5a5968/libraries/DataFlash/DataFlash_Backend.cpp
####True or False Positive:
True
####Note:
Added a Null termination to the log_Message.msg.
[ANALYSE]

## Result number #12
### File name(s):ArduPlane/control_modes.pde
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE TRUE]
####Values changed
NEW:254
OLD:0
CHANGED:('oldSwitchPosition', '0', '73', 'reset_control_switch')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/4f242aedec3e3f31a46ab2e6a0f13c854facb777/ArduPlane/control_modes.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/6ed78c89ac6846fb38b045a7aa1f1898f3681930/ArduPlane/control_modes.pde
####True or False Positive:
True
####Note:
From the commit message: "the mode would not revert if the switch was in position 0".
[ANALYSE]

####Values changed
NEW:0
OLD:1
CHANGED:('change_command', '1', '42', 'read_control_switch')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/764d86216eb415289486f948641e6c63be230cbf/ArduPlane/control_modes.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/d13d117e61de348a14f176e8097444340b88a276/ArduPlane/control_modes.pde
####True or False Positive:
True
####Note:
From commit message: "fixed mission reset by setting waypoint to zero".
[ANALYSE]

## Result number #13
### File name(s):libraries/AP_GPS/AP_GPS_NMEA.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE TRUE]
####Values changed
NEW:1000
OLD:100
CHANGED:(514, '100', '367', 'AP_GPS_NMEA')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/3108d661d229e135ed8cc66fe1066793c923ae93/libraries/AP_GPS/AP_GPS_NMEA.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/cad260a4818e3e1186a4528fe14c1a7e2ee22f9a/libraries/AP_GPS/AP_GPS_NMEA.cpp
####True or False Positive:
True
####Note:
Corrected Knots m/sec calculation.
[ANALYSE]

## Result number #14
### File name(s):libraries/AP_Math/tests/test_scurve.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('t2_out', '0.25000018', '15', 'TEST')
OLD:('t2_out', '0.0', '14', 'TEST')
CHANGED:('t2_out', '0.0', '14', 'TEST')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/a8b86e9c45bf04709e5d22bd641955cbb36b2ec6/libraries/AP_Math/tests/test_scurve.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/75411afd21511ed4cca4a5a0185f5038e0b99bd3/libraries/AP_Math/tests/test_scurve.cpp
####True or False Positive:
False
####Note:
Testing file, which is not of interest for this AP. The value was changed from '0.0' to '0.25000018'.
[ANALYSE]

## Result number #15
### File name(s):libraries/AP_Math/matrixN.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE TRUE]
####Values changed
NEW:2
OLD:0.5
CHANGED:('i', '0.5', '51', 'T')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/ce53ae63ae3bb03f2d148dd7dee41551436ff014/libraries/AP_Math/matrixN.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/39ae285a7fd0737942c70c6b22ae91a4251ed97f/libraries/AP_Math/matrixN.cpp
####True or False Positive:
True
####Note:
Performance optimatization.
[ANALYSE]

## Result number #16
### File name(s):Tools/AP_Bootloader/support.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE FALSE]
####Values changed
NEW:500
OLD:100
CHANGED:('chThdSleepMicroseconds', '100', '46', 'cin_word')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/0ebd05aa1a2a38f728c30ad10b4eb15c2b2ae5e4/Tools/AP_Bootloader/support.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/fe4aa4bbc75fd46efe1c08baae8347cf47f127b2/Tools/AP_Bootloader/support.cpp
####True or False Positive:
False
####Note:
This is an MWN antipattern instead of an HCFT.
[ANALYSE]

## Result number #17
### File name(s):libraries/AP_OSD/AP_OSD_Backend.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:1
OLD:32
CHANGED:('buff', '32', '31', 'AP_OSD_Backend')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/de3244e26c056aa17f890101ce4e9eff814667c1/libraries/AP_OSD/AP_OSD_Backend.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/785cf293cde16b9f0d98f86985aace283f6134e2/libraries/AP_OSD/AP_OSD_Backend.cpp
####True or False Positive:
True
####Note:
Increased buff for '+1 for snprintf null-termination'. Change done in commit de3244e26c056aa17f890101ce4e9eff814667c1.
[ANALYSE]

## Result number #18
### File name(s):ArduCopter/control_modes.pde
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:30000.0
OLD:3000
CHANGED:('control_in', '3000', '205', 'trim_accel')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/f3ff7aa0a894bf0bd12051cc45ef063134d57132/ArduCopter/control_modes.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/69f1841d8ee34488913bb833e0348635b788e190/ArduCopter/control_modes.pde
####True or False Positive:
True
####Note:
Chang of inflight trim done in commit f3ff7aa0a894bf0bd12051cc45ef063134d57132.
[ANALYSE]

## Result number #19
### File name(s):ArduPlane/failsafe.cpp
ArduPlane/failsafe.pde
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.0
OLD:0
CHANGED:('k_flap_auto', '0', '99', 'Plane')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/2f4661c52f6cf6d2f360d70f5a9e2f81f5b31552/ArduPlane/failsafe.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/1ae669bb01ebaa2aee107fd69b595e6288460b56/ArduPlane/failsafe.cpp
####True or False Positive:
False
####Note:
Change of using a float '0.0' instead of '0'.
[ANALYSE]

## Result number #20
### File name(s):libraries/SITL/SIM_FlightAxis.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:8
OLD:6
CHANGED:('rcin_chan_count', '6', '309', 'FlightAxis')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/7cdab2a6c95844ca9015a0af5f03899be00431cf/libraries/SITL/SIM_FlightAxis.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/3b0cd9f101398a57a8dfec2f0b2a0758971be99c/libraries/SITL/SIM_FlightAxis.cpp
####True or False Positive:
True
####Note:
Increases support of channels from 6 to 8.
[ANALYSE]

## Result number #21
### File name(s):libraries/AP_RangeFinder/AP_RangeFinder_GYUS42v2.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE TRUE]
####Values changed
NEW:0.01
OLD:5
CHANGED:('buffer', '5', '68', 'AP_RangeFinder_GYUS42v2')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/0f7c3e39640911fd19677eda5674cfe116c7a6c8/libraries/AP_RangeFinder/AP_RangeFinder_GYUS42v2.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/6ec497229b4d7c8872082a0e2491e803a0da482e/libraries/AP_RangeFinder/AP_RangeFinder_GYUS42v2.cpp
####True or False Positive:
True
####Note:
Adjustments made for use with Meters instead of cm.
[ANALYSE]

## Result number #22
### File name(s):libraries/AP_Logger/AP_Logger_Block.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:4294967295
OLD:65535
CHANGED:(16, '65535', '532', 'uint32_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/dec5b97275433cc0965681e2838b35a8ff9abf02/libraries/AP_Logger/AP_Logger_Block.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/49bf0a3057cba85cf2794aa787e52ab011de549f/libraries/AP_Logger/AP_Logger_Block.cpp
####True or False Positive:
True
####Note:
Fix to log on 256Mbit flash chips, done in commit dec5b97275433cc0965681e2838b35a8ff9abf02.
[ANALYSE]

## Result number #23
### File name(s):ArduCopter/radio.pde
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:1
OLD:11
CHANGED:('failsafeCounter', '11', '172', 'throttle_failsafe')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/2335b74bc37556d0bbc2a828dd8c4484d0cb2a7a/ArduCopter/radio.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/f3a95ff3cb9f46f0858279aa6cca568a04492580/ArduCopter/radio.pde
####True or False Positive:
True
####Note:
failsafeCounter changed from hardcoded 11, to more dynamic FS_COUNTER+1 (which is above the function defined as 3).
There is also an unused/empty if statement above.
[ANALYSE]

## Result number #24
### File name(s):libraries/AP_Logger/LogStructure.h
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:12
OLD:10
CHANGED:('cell_voltages', '10', '801', 'log_Current_Cells')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/82423384bf82b9c0f4c719cf2e8ac63f9ed21b61/libraries/AP_Logger/LogStructure.h
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/255c685a8a9bf486bf988dc014956ff8c27e0ca0/libraries/AP_Logger/LogStructure.h
####True or False Positive:
True
####Note:
Increases support for 12 battery cell voltages, done in commit 82423384bf82b9c0f4c719cf2e8ac63f9ed21b61.
[ANALYSE]

## Result number #25
### File name(s):libraries/AP_HAL_SITL/sitl_gps.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:1000
OLD:15
CHANGED:(2, '15', '180', 'gps_time')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/d5a5a97a3d79021898710fe527999c10671309f6/libraries/AP_HAL_SITL/sitl_gps.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/f6d475c1e6a39da34e88ac5f9702bac0de5df775/libraries/AP_HAL_SITL/sitl_gps.cpp
####True or False Positive:
True
####Note:
Changed calculation of an epoch, using GPS_LEAPSECONDS_MILLIS as part of the calculation. Changed in commit d5a5a97a3d79021898710fe527999c10671309f6 (interesting comments in this commit).
The value '15' has been changed to 'GPS_LEAPSECONDS_MILLIS / 1000ULL'. GPS_LEAPSECONDS_MILLIS has been defined as '18000ULL' in https://github.com/ArduPilot/ardupilot/blob/d5a5a97a3d79021898710fe527999c10671309f6/libraries/AP_GPS/AP_GPS.h.
This results that the new value was changed from '15' to '18'.
[ANALYSE]

## Result number #26
### File name(s):libraries/AP_GPS/AP_GPS_SBF.h
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:256
OLD:128
CHANGED:('bytes', '128', '162', 'PACKED')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/be371e09f9c017262aed60325afea4f755bac60b/libraries/AP_GPS/AP_GPS_SBF.h
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/5f8633e3221f9d5970daca8b8b5b39211bb572ee/libraries/AP_GPS/AP_GPS_SBF.h
####True or False Positive:
True
####Note:
Increased buffer size.
[ANALYSE]

## Result number #27
### File name(s):libraries/AC_AttitudeControl/AC_AttitudeControl_Heli.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.0
OLD:0
CHANGED:('_angle_boost', '0', '305', 'AC_AttitudeControl_Heli')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/e5d6d45851c369651e356c6a51312c1039161e52/libraries/AC_AttitudeControl/AC_AttitudeControl_Heli.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/5148e41c1af92457cb18152e37c1e6cf8c565193/libraries/AC_AttitudeControl/AC_AttitudeControl_Heli.cpp
####True or False Positive:
False
####Note:
Changed from 0 to 0.0f.
[ANALYSE]

## Result number #28
### File name(s):ArduCopter/esc_calibration.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE FALSE]
####Values changed
NEW:('delay', '3', '150', 'Copter')
OLD:('delay', '10', '137', 'Copter')
CHANGED:('delay', '10', '137', 'Copter')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/d186e1c6484d90ce294977beebc045e03876fe88/ArduCopter/esc_calibration.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/e3934fac807b5a12aba1bebccdc2fc328f9a50ea/ArduCopter/esc_calibration.cpp
####True or False Positive:
False
####Note:
Increased delay, this would be a MWN instead of a HCFT antipattern.
[ANALYSE]

## Result number #29
### File name(s):ArduCopter/esc_calibration.pde
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:5000
OLD:3000
CHANGED:('delay', '3000', '129', 'esc_calibration_auto')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/3b5228922ec01add0a5f7d06636185ade56d415d/ArduCopter/esc_calibration.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/ad3bce105c8be969d68b2f45028343cf2de3409b/ArduCopter/esc_calibration.pde
####True or False Positive:
False
####Note:
Not HCFT, but MWN.
[ANALYSE]

## Result number #30
### File name(s):libraries/AP_Math/vector3.h
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0
OLD:0.0
CHANGED:('z', '0.0', '156', 'zero')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/d2deee07dfb93297cc4bccbc84dabe65892b2dfe/libraries/AP_Math/vector3.h
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/97b7130bb9d21c4f2778c3fcd1956aabef433824/libraries/AP_Math/vector3.h
####True or False Positive:
False
####Note:
Changed from 0.0 to 0.
[ANALYSE]

## Result number #31
### File name(s):libraries/AP_HAL_ChibiOS/sdcard.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:('bouncebuffer', '4096', '61', 'sdcard_init')
OLD:('bouncebuffer', '512', '59', 'sdcard_init')
CHANGED:('bouncebuffer', '512', '59', 'sdcard_init')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/a220b37bf84960a5a85d1ddef84cb50e2e545073/libraries/AP_HAL_ChibiOS/sdcard.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/b84dcd483d21f9b119aff1c6d50c3661ded1b8dd/libraries/AP_HAL_ChibiOS/sdcard.cpp
####True or False Positive:
True
####Note:
Increased bouncebuffer for microSD, from 512 to 4096. Changed done in commit a220b37bf84960a5a85d1ddef84cb50e2e545073.
[ANALYSE]

## Result number #32
### File name(s):libraries/AP_HAL_ChibiOS/SPIDevice.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:2
OLD:1
CHANGED:('busid', '1', '159', 'uint16_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/79f3fd532b5e406e5a502b740da8e31f4002eb6f/libraries/AP_HAL_ChibiOS/SPIDevice.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/01e9c557210ec2fe2c3baab4b69180ba13e49cca/libraries/AP_HAL_ChibiOS/SPIDevice.cpp
####True or False Positive:
False
####Note:
Changed the 'spi_clock_freq' by half. Change done in Commit 79f3fd532b5e406e5a502b740da8e31f4002eb6f.
[ANALYSE]

## Result number #33
### File name(s):libraries/AP_IOMCU/AP_IOMCU.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:5
OLD:20
CHANGED:('wait_count', '20', '377', 'size_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/8ef2046f7b8d898386620be6bbfcc96f490481b4/libraries/AP_IOMCU/AP_IOMCU.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/454717cf6f35cbf3a37dcb0df01bbfdc3675dc84/libraries/AP_IOMCU/AP_IOMCU.cpp
####True or False Positive:
False
####Note:
This is a MWN AP, not HCFT. Adjusted 'wait_count' from 20 to 5.
[ANALYSE]

## Result number #34
### File name(s):libraries/AP_RangeFinder/examples/RFIND_test/RFIND_test.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('var_info', '1.0', '23', 'setup')
OLD:('var_info', '1', '20', 'setup')
CHANGED:('var_info', '1', '20', 'setup')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/4a2b90b707e0dcc554d858f367efc22e1268a4b6/libraries/AP_RangeFinder/examples/RFIND_test/RFIND_test.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/c98e598ae2cc5cf4b100c951972cde8d7d3e110f/libraries/AP_RangeFinder/examples/RFIND_test/RFIND_test.cpp
####True or False Positive:
False
####Note:
Changed from -1 to -1.0f.
[ANALYSE]

## Result number #35
### File name(s):libraries/AP_RangeFinder/examples/RFIND_test/RFIND_test.pde
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('var_info', '1', '49', 'setup')
OLD:('var_info', '13', '48', 'setup')
CHANGED:('var_info', '13', '48', 'setup')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/9c0614c7bb82c8935092cee7fec885c8962b455e/libraries/AP_RangeFinder/examples/RFIND_test/RFIND_test.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/d5f02ec0dfbe223670dc5fc56a3078afbce0c3a7/libraries/AP_RangeFinder/examples/RFIND_test/RFIND_test.pde
####True or False Positive:
False
####Note:
Changed pin location used in a test file.
[ANALYSE]

## Result number #36
### File name(s):ArduCopter/navigation.pde
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:4500
OLD:32000
CHANGED:(32000, '32000', '505', 'calc_loiter')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/df2137ed729aa3811c6e6941527473f97820c2f4/ArduCopter/navigation.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/860f4b260552297253a28b83a7f108302b84b97e/ArduCopter/navigation.pde
####True or False Positive:
True
####Note:
Changed restrictions to max. 45 degrees. Change done in commit df2137ed729aa3811c6e6941527473f97820c2f4.
[ANALYSE]

####Values changed
NEW:500
OLD:1000
CHANGED:(1000, '1000', '222', 'calc_nav_rate')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/77f47a45d0f1a9dd132bd23d2ff78f93f4dd7cf6/ArduCopter/navigation.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/64cfaf74b7abc75d8a1398d44111de9b5908453e/ArduCopter/navigation.pde
####True or False Positive:
True
####Note:
Adjusted rate error limit. Adjustment was done in commit 77f47a45d0f1a9dd132bd23d2ff78f93f4dd7cf6 to prevent bad oscillations due to GPS latency.
[ANALYSE]

####Values changed
NEW:150
OLD:200
CHANGED:(200, '200', '188', 'calc_nav_rate')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/bdc1c41e62e42a10f32e8d63468e2d6e4a5daa7a/ArduCopter/navigation.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/36f947acb9f16cda55be2fe51d30b0d02f0e81a8/ArduCopter/navigation.pde
####True or False Positive:
True
####Note:
Adjusted 'cross_speed' calculation, change done in commit bdc1c41e62e42a10f32e8d63468e2d6e4a5daa7a.
[ANALYSE]

####Values changed
NEW:250
OLD:150
CHANGED:(150, '150', '114', 'calc_loiter')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/efce991bfb1bb13bf2ece7df3cf88a60fbe07799/ArduCopter/navigation.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/c35ad2d4931fe85ae43657a553fa76029670dce9/ArduCopter/navigation.pde
####True or False Positive:
True
####Note:
Adjusted 'y_target_speed' calculation, change done in commit efce991bfb1bb13bf2ece7df3cf88a60fbe07799.
[ANALYSE]

####Values changed
NEW:100
OLD:50
CHANGED:('wp_distance', '50', '277', 'int16_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/8cb645f3c2a92cd51370452d1cbb4fbee88ed5cc/ArduCopter/navigation.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/6784989e83c565797169b9b5c4ef2fbb35078acc/ArduCopter/navigation.pde
####True or False Positive:
True
####Note:
Changed the max speed calculation. In-code commit was not updated.
[ANALYSE]

####Values changed
NEW:1400
OLD:800
CHANGED:(800, '800', '194', 'calc_nav_rate')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/d83ad1acd49283ddbfafef1cbb6fe7b154c7eec9/ArduCopter/navigation.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/c1aa015ef114021cb8e6ba9a430f135b7216faff/ArduCopter/navigation.pde
####True or False Positive:
True
####Note:
Increased velocity, change done in commit 8cb645f3c2a92cd51370452d1cbb4fbee88ed5cc. This commit did not change the in-code explanation of this calculation.
[ANALYSE]

## Result number #37
### File name(s):ArduCopterMega/navigation.pde
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:3500
OLD:4000
CHANGED:(4000, '4000', '171', 'calc_rate_nav')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/4223dff94e318e88b9a642ec043f6e5b8df8a6d1/ArduCopterMega/navigation.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/c637bf09470fb01155aa960378f9a0ec56523df5/ArduCopterMega/navigation.pde
####True or False Positive:
True
####Note:
Limit RTL to 35 degrees, change done in commit 4223dff94e318e88b9a642ec043f6e5b8df8a6d1.
[ANALYSE]

## Result number #38
### File name(s):libraries/AP_HAL_AVR/utility/print_vprintf.cpp
libraries/AP_HAL/utility/print_vprintf.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:6
OLD:7
CHANGED:('prec', '7', '176', 'print_vprintf')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/0d662c52b3bf382efc7a01951c344fb12e840287/libraries/AP_HAL/utility/print_vprintf.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/60122f9877983f1c92f47aa4ab76c38b85119b72/libraries/AP_HAL/utility/print_vprintf.cpp
####True or False Positive:
False
####Note:
Changed part of changing fix length of snprintf, change done in commmit 0d662c52b3bf382efc7a01951c344fb12e840287.
[ANALYSE]

## Result number #39
### File name(s):libraries/AP_Proximity/AP_Proximity_MAV.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.01
OLD:100.0
CHANGED:('max_distance', '100.0', '108', 'AP_Proximity_MAV')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/b8dcdca909003a2e6460def61cd9f6c45e414b90/libraries/AP_Proximity/AP_Proximity_MAV.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/5b745aa1f16307ebafac0fbb534c20d644de4e9f/libraries/AP_Proximity/AP_Proximity_MAV.cpp
####True or False Positive:
False
####Note:
Changed calculation by instead of divided by 100, does times 0.01.
[ANALYSE]

## Result number #40
### File name(s):libraries/AP_Math/crc.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:1
OLD:8
CHANGED:('crc', '8', '173', 'uint32_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/ff2cfbaafbdf1b09b21a12ea0d8c7a951b7ed0b5/libraries/AP_Math/crc.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/fb48d8ee1bc019fd343e4508b5cc888d0f034117/libraries/AP_Math/crc.cpp
####True or False Positive:
False
####Note:
No change seen at location.
[ANALYSE]

## Result number #41
### File name(s):libraries/AP_HAL_ChibiOS/CanIface.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:2
OLD:1
CHANGED:(1, '1', '997', 'CH_IRQ_HANDLER')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/f57b1b9c4bed8c37fb7a341cce822e479efd96bf/libraries/AP_HAL_ChibiOS/CanIface.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/439a944801fd0240a3ddb77eb0fddf8e421e8bbc/libraries/AP_HAL_ChibiOS/CanIface.cpp
####True or False Positive:
False
####Note:
The 'CH_IRQ_HANDLER(CAN2_RX1_IRQ_Handler)' is on line 1017 in the new file. No change was done.
[ANALYSE]

## Result number #42
### File name(s):libraries/AP_HAL_Linux/RCInput_RCProtocol.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:80
OLD:40
CHANGED:('b', '40', '129', 'RCInput_RCProtocol')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/a153799e261de0fcc0008730e0f755e367f87d60/libraries/AP_HAL_Linux/RCInput_RCProtocol.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/209bb132fad14d46c3eca820bf13a0e4a4338cd5/libraries/AP_HAL_Linux/RCInput_RCProtocol.cpp
####True or False Positive:
True
####Note:
Added support for FrSky FPort input, done in commit a153799e261de0fcc0008730e0f755e367f87d60.
[ANALYSE]

## Result number #43
### File name(s):libraries/AP_HAL_ChibiOS/Util.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:8
OLD:11
CHANGED:('serialid', '11', '261', 'Util')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/fbf24f04927f2f31d793c7c0db56fbf8a3130aba/libraries/AP_HAL_ChibiOS/Util.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/e5435e02ad6e13650ad0156a292af186fb8edcd8/libraries/AP_HAL_ChibiOS/Util.cpp
####True or False Positive:
False
####Note:
Changed serial number format to match format used by HAL_PX4, done in commit fbf24f04927f2f31d793c7c0db56fbf8a3130aba.
[ANALYSE]

## Result number #44
### File name(s):libraries/AP_GPS/AP_GPS_MAV.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.01
OLD:100.0
CHANGED:('vd', '100.0', '151', 'AP_GPS_MAV')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/747de2c28cf29edc33a9f33b606c38d373cfb14b/libraries/AP_GPS/AP_GPS_MAV.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/0cd97ce3d8f394e2b853b1f835abf74e6488daf5/libraries/AP_GPS/AP_GPS_MAV.cpp
####True or False Positive:
False
####Note:
Changed 'divided by' by similar 'times by'. According to commit 747de2c28cf29edc33a9f33b606c38d373cfb14b, this should be faster to process.
[ANALYSE]

## Result number #45
### File name(s):libraries/AP_HAL/tests/test_prescaler.cpp
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:0.2
OLD:0.13
CHANGED:('rate_delta', '0.13', '14', 'test_prescaler')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/bb3bedb90dbba4eb5b782e02d8bd8719ad1eddef/libraries/AP_HAL/tests/test_prescaler.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/ea1af70f2be0c353bafbad6cf61c72e5178c0fce/libraries/AP_HAL/tests/test_prescaler.cpp
####True or False Positive:
True
####Note:
Part of changes regarding the value chosen for the 'dshot prescaler calculation'. This change was made as:
'if using dshot then always pick the high value. choosing low seems to not agree with some ESCs despite the fact that BLHeli32 is supposed not to care what the bitrate is'
[ANALYSE]

## Result number #46
### File name(s):libraries/AP_InertialSensor/AP_InertialSensor_MPU6000.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('channel', '26', '184', 'uint16_t')
OLD:('channel', '70', '186', 'uint16_t')
CHANGED:('channel', '70', '186', 'uint16_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/d9cb29ea8baf6828be8fee574de468545a83dc4c/libraries/AP_InertialSensor/AP_InertialSensor_MPU6000.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/ece01da10e5e79a933c69a664c7fa4119290cf6e/libraries/AP_InertialSensor/AP_InertialSensor_MPU6000.cpp
####True or False Positive:
False
####Note:
Changed to correct 'Correct DRDY pin'.
[ANALYSE]

## Result number #47
### File name(s):libraries/AP_Math/tests/test_math_double.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:4.317406628984581
OLD:4.317406177520752
CHANGED:('norm_1', '4.317406177520752', '227', 'TEST')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/0f2f0d4cb277df36d09d55238bae85905f27f52c/libraries/AP_Math/tests/test_math_double.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/519b1a6913eea55d307515405ede40c502cd7cfd/libraries/AP_Math/tests/test_math_double.cpp
####True or False Positive:
False
####Note:
Part of a test.
[ANALYSE]

## Result number #48
### File name(s):libraries/AP_InertialSensor/AP_InertialSensor_MPU6000.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('channel', '26', '184', 'uint16_t')
OLD:('channel', '70', '186', 'uint16_t')
CHANGED:('channel', '70', '186', 'uint16_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/d9cb29ea8baf6828be8fee574de468545a83dc4c/libraries/AP_InertialSensor/AP_InertialSensor_MPU6000.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/ece01da10e5e79a933c69a664c7fa4119290cf6e/libraries/AP_InertialSensor/AP_InertialSensor_MPU6000.cpp
####True or False Positive:
False
####Note:
Same as Result number #46.
[ANALYSE]

## Result number #49
### File name(s):libraries/AP_CANManager/AP_CANTester_KDECAN.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:('mcu', '0', '224', 'AP_CANTester_KDECAN')
OLD:('mcu', '8', '221', 'AP_CANTester_KDECAN')
CHANGED:('mcu', '8', '221', 'AP_CANTester_KDECAN')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/0b505c491ceba0f1fd1d97bf73fe941b2fcc1db2/libraries/AP_CANManager/AP_CANTester_KDECAN.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/603b302ffddb0bc6e29889d557b96fdcf6835f2c/libraries/AP_CANManager/AP_CANTester_KDECAN.cpp
####True or False Positive:
False
####Note:
Change part of commit to 'AP_CANManager: fix casting without ensuring alignment'.
[ANALYSE]

## Result number #50
### File name(s):libraries/AP_Notify/MMLPlayer.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.5
OLD:2
CHANGED:('note_period', '2', '302', 'MMLPlayer')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/dee040b14aaf6eda5990070ef986860a38f6e37b/libraries/AP_Notify/MMLPlayer.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/3df3d002ff87f8e34654481b173fd080a1a1777f/libraries/AP_Notify/MMLPlayer.cpp
####True or False Positive:
False
####Note:
Changed 'divided by' to similar 'times by'.
[ANALYSE]

## Result number #51
### File name(s):ArduCopter/ArduCopter.pde
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE FALSE]
####Values changed
NEW:500
OLD:300
CHANGED:(300, '300', '1888', 'update_altitude')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/c1b759d5d80a02647b0de9eb05bf3c4bcd6430d6/ArduCopter/ArduCopter.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/9e0b0b9fcddab34dde239321fb4417920bdfd046/ArduCopter/ArduCopter.pde
####True or False Positive:
False
####Note:
Change made to the barometer rate, potential FCR antipattern, not HCFT.
[ANALYSE]

####Values changed
NEW:1.0
OLD:1
CHANGED:(0, '1', '1959', 'update_altitude')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/1c0b28c9561b37d7cd5af5dae6858dde30e05bda/ArduCopter/ArduCopter.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/86eff20d5d2171ac98c025cf28cb1df7d0ba10df/ArduCopter/ArduCopter.pde
####True or False Positive:
False
####Note:
Increased accuracy, but not change made to the variable.
[ANALYSE]

## Result number #52
### File name(s):ArduCopterMega/ArduCopterMega.pde
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:200
OLD:150
CHANGED:('altitude_error', '150', '1204', 'update_throttle_mode')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/dd392f8c0a74fa0ff603ae5283792cd335fcdfcb/ArduCopterMega/ArduCopterMega.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/cb6419875983b04658bfcd5703653d6acac214e2/ArduCopterMega/ArduCopterMega.pde
####True or False Positive:
True
####Note:
According to commit message: 'Upped some gains on alt hold based on testing.'. Changed the targed speed from 1.5m/s to 2.0m/s from test results. The in-code comment was not updated in this commit.
[ANALYSE]

####Values changed
NEW:400
OLD:200
CHANGED:('calc_rate_nav', '200', '1381', 'update_navigation')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/b7ce6e036eb71b57d6f6e9906e140b668f111e8f/ArduCopterMega/ArduCopterMega.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/0bea96c3d024a728acee5aaba56ff1c86ef8737d/ArduCopterMega/ArduCopterMega.pde
####True or False Positive:
True
####Note:
Changed 'calc_rate_nav' from 200 to 400, which relates to 'calc a rate dampened pitch to the target'.
Changes made to take into account 'both forward and lateral rates', commit request users to give feedback if there a mistake was made in this change.
[ANALYSE]

## Result number #53
### File name(s):libraries/AC_Fence/AC_Fence.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE TRUE]
####Values changed
NEW:2
OLD:1
CHANGED:('_boundary_num_points', '1', '466', 'Vector2f')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/2822c635ec05744996b893bbb51787ed2598ebf8/libraries/AC_Fence/AC_Fence.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/4dbac3de602c811d353dc3fee43396cd25e6ddce/libraries/AC_Fence/AC_Fence.cpp
####True or False Positive:
True
####Note:
From commit message: correct get_boundary_points to account for closing point.
[ANALYSE]

####Values changed
NEW:0.0
OLD:0
CHANGED:('_alt_max_backup', '0', '160', 'uint8_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/0c0521a555f111a4b21b3b5746ab6053c62dfb33/libraries/AC_Fence/AC_Fence.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/e855cfec028f49ec93cc2bbd3ded87f26151feeb/libraries/AC_Fence/AC_Fence.cpp
####True or False Positive:
False
####Note:
Changed notation style.
[ANALYSE]

## Result number #54
### File name(s):libraries/AP_HAL_AVR_SITL/sitl_ins.cpp
[FILE FOR ANALYSIS]
[RANDOM SELECTED]
[FILE TRUE]
####Values changed
NEW:0.04
OLD:0.4
CHANGED:('ToRad', '0.4', '102', 'SITL_State')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/f5d20b40856b9f1840945fd819a068b1bf42bfc1/libraries/AP_HAL_AVR_SITL/sitl_ins.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/119ffb0fc074fbf8a3f78b865b77d7ae00d82ecf/libraries/AP_HAL_AVR_SITL/sitl_ins.cpp
####True or False Positive:
True
####Note:
Reduced Gyro noise.
[ANALYSE]

####Values changed
NEW:2013
OLD:503
CHANGED:('airspeed_offset', '503', '34', 'uint16_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/119ffb0fc074fbf8a3f78b865b77d7ae00d82ecf/libraries/AP_HAL_AVR_SITL/sitl_ins.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/589b8cdb58d9c3101f666d38f979a139f1fdacbe/libraries/AP_HAL_AVR_SITL/sitl_ins.cpp
####True or False Positive:
True
####Note:
Adjusted airspeed offset.
[ANALYSE]

####Values changed
NEW:503
OLD:2820
CHANGED:('airspeed_offset', '2820', '34', 'uint16_t')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/589b8cdb58d9c3101f666d38f979a139f1fdacbe/libraries/AP_HAL_AVR_SITL/sitl_ins.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/0ffc7dab6b957f547a9f028eeaddd25ba076f2fa/libraries/AP_HAL_AVR_SITL/sitl_ins.cpp
####True or False Positive:
True
####Note:
Adjusted Airspeed offset.
[ANALYSE]

## Result number #55
### File name(s):ArduCopter/control_loiter.cpp
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.0
OLD:0
CHANGED:('target_yaw_rate', '0', '35', 'Copter')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/d89058a75c9da283980ef38063e94a72abc1a6d7/ArduCopter/control_loiter.cpp
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/01ae84dda627a290d94019ab0908a01242f4f603/ArduCopter/control_loiter.cpp
####True or False Positive:
False
####Note:
Changed from '0' to '0.0f'.
[ANALYSE]

## Result number #56
### File name(s):ArduCopter/control_autotune.pde
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.0
OLD:0
CHANGED:('lean_angle', '0', '332', 'autotune_attitude_control')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/36c91970f1ce7782d6e73d92bbc8970f869dae63/ArduCopter/control_autotune.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/9bfb0e1f40eb1689bab9c26e560fcd6ab7bbbacb/ArduCopter/control_autotune.pde
####True or False Positive:
False
####Note:
Changed from '0' to '0.0f'.
[ANALYSE]

## Result number #57
### File name(s):ArduCopter/motors.pde
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:250
OLD:200
CHANGED:('auto_level_counter', '200', '25', 'arm_motors')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/307723960dfac3888e923246c62a96a411073d04/ArduCopter/motors.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/b3bd4bd3c99a47ac59ce342bb33e49962600667c/ArduCopter/motors.pde
####True or False Positive:
True
####Note:
Increased to 'Auto_trim time'.
[ANALYSE]

## Result number #58
### File name(s):ArduCopterMega/motors.pde
ArduCopterMega/radio.pde
[FILE FOR ANALYSIS]
[FILE TRUE]
####Values changed
NEW:0.707
OLD:2
CHANGED:('pwm_out', '2', '78', 'set_servos_4')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/957e1a747b7f27a947d595dfb00e4c907156713e/ArduCopterMega/motors.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/2b697698436ceabb931762f7a4a28bfa93a40bee/ArduCopterMega/motors.pde
####True or False Positive:
True
####Note:
Besides changing from 'divided by' to 'times by', the resulting value has been adjusted. In oder to 'Should be flyable now.'.
[ANALYSE]

## Result number #59
### File name(s):ArduPlane/Attitude.cpp
ArduPlane/Attitude.pde
[FILE FOR ANALYSIS]
[FILE FALSE]
####Values changed
NEW:0.01
OLD:100
CHANGED:('target_airspeed', '100', '395', 'set_servos')
Version 1(new): https://github.com/ArduPilot/ardupilot/blob/5bfd1200d60204e26c34e57a85a914ba3dc0ad83/ArduPlane/Attitude.pde
Version 2(old): https://github.com/ArduPilot/ardupilot/blob/9c1ac2d9e6856bc8e561fed6d60ab43a7ad3b42b/ArduPlane/Attitude.pde
####True or False Positive:
False
####Note:
Changed from 'divided by' to 'times by'.
[ANALYSE]
