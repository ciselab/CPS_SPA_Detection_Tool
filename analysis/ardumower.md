# ardumower

## Result number #1

### File name(s)
code/ardumower/i2c.cpp

### Compare results

####Values added
Values: [('nDevices', '0', '152', 'I2CScanner')]
Not available in: https://github.com/Ardumower/ardumower/blob/fd9e354e3eebe475a3f84388f64bd63a79216ef7/code/ardumower/i2c.cpp
Added in: https://github.com/Ardumower/ardumower/blob/12c5245cbfad6667aeb02787acaaa69901c82467/code/ardumower/i2c.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('nDevices', '0', '151', 'I2CScanner')]
Available in: https://github.com/Ardumower/ardumower/blob/c4e924cd49bf12d3247f624d4696cad74fc75d97/code/ardumower/i2c.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/fd9e354e3eebe475a3f84388f64bd63a79216ef7/code/ardumower/i2c.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('millis', '10000', '94', 'I2Creset'), ('i', '0', '126', 'I2CreadFrom'), ('i', '0', '127', 'I2CreadFrom')]
Available in: https://github.com/Ardumower/ardumower/blob/01fcb89af5153d9eb0ed74efd95a80b94ba147b8/code/ardumower/i2c.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/c4e924cd49bf12d3247f624d4696cad74fc75d97/code/ardumower/i2c.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('nDevices', '0', '147', 'I2CScanner')]
Not available in: https://github.com/Ardumower/ardumower/blob/9250f71d655cbf3671d7cfdf011b59d08df43861/code/ardumower/i2c.cpp
Added in: https://github.com/Ardumower/ardumower/blob/b07e4b72a5d8431441a8bc779a20c60c9af8b99e/code/ardumower/i2c.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #2

### File name(s)
ardumower/pid.cpp

### Compare results

####Values added
Values: [('y_min', '0', '90', 'VelocityPID'), ('y_max', '0', '89', 'VelocityPID'), ('Ta', '1.0', '83', 'VelocityPID'), ('lastControlTime', '1000000.0', '81', 'VelocityPID')]
Not available in: https://github.com/Ardumower/ardumower/blob/9a2afa1e99246af5dfb6e009d59276cca0ecbb3f/ardumower/pid.cpp
Added in: https://github.com/Ardumower/ardumower/blob/3b4de894657e160ee543ea9b1b63feb9fe647c5e/ardumower/pid.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('lastControlTime', '1000000.0', '38', 'PID')
OLD:('lastControlTime', '1000000.0', '37', 'PID')
CHANGED:('lastControlTime', '1000000.0', '37', 'PID')
Version 1(new): https://github.com/Ardumower/ardumower/blob/54f4753675d236e0b4fee57fb92abd9122345f42/ardumower/pid.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/1844733dc6977b79c0632fd3dbe9bc9626db62ee/ardumower/pid.cpp
####True or False Positive:
False
####Note:
Only a line change occurred.

### Number of warnings:
2

## Result number #3

### File name(s)
code/ardumower/drivers.cpp

### Compare results

####Values added
Values: [('address', '0', '273', 'checkAT24C32'), ('r', '0', '272', 'checkAT24C32'), ('b', '0', '271', 'checkAT24C32')]
Not available in: https://github.com/Ardumower/ardumower/blob/e0e6c1c24a3adc56eb9fa5fb47703372b1503161/code/ardumower/drivers.cpp
Added in: https://github.com/Ardumower/ardumower/blob/8c8ae5423778037028195850dac45c618c393306/code/ardumower/drivers.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('delay', '20', '302', 'byte')]
Not available in: https://github.com/Ardumower/ardumower/blob/b403f053db7800f7943f73cc09c7c056b166500d/code/ardumower/drivers.cpp
Added in: https://github.com/Ardumower/ardumower/blob/e0e6c1c24a3adc56eb9fa5fb47703372b1503161/code/ardumower/drivers.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('t', '0', '311', 'measureLawnCapacity'), ('year', '1', '328', 'getDayOfWeek'), ('month', '12', '327', 'getDayOfWeek')]
Available in: https://github.com/Ardumower/ardumower/blob/5773dddf929f7caf4797cf6284d33f069599e824/code/ardumower/drivers.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/b403f053db7800f7943f73cc09c7c056b166500d/code/ardumower/drivers.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('dayOfWeek', '1', '297', 'boolean')]
Not available in: https://github.com/Ardumower/ardumower/blob/96bc69b4bbae7e32830b76ad954f3e9be5728c9d/code/ardumower/drivers.cpp
Added in: https://github.com/Ardumower/ardumower/blob/0e4b3fb1476aa51f335f2ea13338fce80251a85a/code/ardumower/drivers.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #4

### File name(s)
tests/imuahrs/imu.cpp

### Compare results

####Values added
Values: [('looptime', '1000', '619', 'Kalman'), ('P_11', '0', '615', 'Kalman'), ('x_bias', '0', '614', 'Kalman'), ('R_angle', '0.01', '612', 'Kalman'), ('Q_gyro', '0.0003', '611', 'Kalman'), ('Q_angle', '0.01', '610', 'Kalman')]
Not available in: https://github.com/Ardumower/ardumower/blob/073b0d87d51e76d5bcf0d588dcffc12d9c1ee338/tests/imuahrs/imu.cpp
Added in: https://github.com/Ardumower/ardumower/blob/24452018fb33a5b464aba43c66625ccae8fc06ee/tests/imuahrs/imu.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('looptime', '1000.0', '700', 'Complementary2'), ('k', '10', '699', 'Complementary2'), ('looptime', '1000.0', '715', 'Complementary'), ('a', '0.0', '714', 'Complementary'), ('tau', '0.075', '713', 'Complementary')]
Not available in: https://github.com/Ardumower/ardumower/blob/f9117be54c365601df3e0276aa9c54821c42a6ca/tests/imuahrs/imu.cpp
Added in: https://github.com/Ardumower/ardumower/blob/8f1d027f77c92c5a7633289fa36618ead3ae38c7/tests/imuahrs/imu.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #5

### File name(s)
ardumower/pfod.cpp

### Compare results

####Values removed
Values: [(1, '8000', '214', 'sendMotorMenu'), (0.001, '0.05', '213', 'sendMotorMenu'), (1, '255', '212', 'sendMotorMenu'), (1, '100', '211', 'sendMotorMenu'), (1000, '0', '206', 'sendMotorMenu'), (1000, '0', '205', 'sendMotorMenu'), (0.1, '40', '204', 'sendMotorMenu'), ('motorLeftSpeed', '0', '257', 'processMotorMenu'), ('STATE_MANUAL', '0', '257', 'processMotorMenu'), ('motorRightSpeed', '0', '256', 'processMotorMenu'), ('STATE_MANUAL', '0', '256', 'processMotorMenu'), ('STATE_OFF', '0', '255', 'processMotorMenu'), (1, '3', '253', 'processMotorMenu'), ('motorBiDirSpeedRatio2', '0.01', '251', 'processMotorMenu'), ('motorBiDirSpeedRatio1', '0.01', '250', 'processMotorMenu'), ('motorAccel', '0.001', '249', 'processMotorMenu'), ('motorForwTimeMax', '10', '248', 'processMotorMenu'), ('motorReverseTime', '1', '247', 'processMotorMenu'), ('motorRollTimeMax', '1', '246', 'processMotorMenu'), ('motorSpeedMaxPwm', '1', '245', 'processMotorMenu'), ('motorSpeedMax', '1', '244', 'processMotorMenu'), ('motorRightSenseCurrent', '1', '241', 'processMotorMenu'), ('motorLeftSenseCurrent', '1', '237', 'processMotorMenu'), ('motorPowerMax', '0.1', '234', 'processMotorMenu'), (0.0001, '0.2', '281', 'sendMowMenu'), (1, '8000', '280', 'sendMowMenu'), (1, '255', '275', 'sendMowMenu'), (3000, '0', '272', 'sendMowMenu'), (0.1, '100', '271', 'sendMowMenu'), ('STATE_MANUAL', '0', '307', 'processMowMenu'), ('STATE_OFF', '0', '306', 'processMowMenu'), (1, '2', '304', 'processMowMenu'), (0.0001, '0.2', '302', 'processMowMenu'), ('motorMowRPM', '1', '301', 'processMowMenu'), ('motorMowSpeedMax', '1', '299', 'processMowMenu'), ('motorMowSenseCurrent', '1', '296', 'processMowMenu'), ('motorMowPowerMax', '0.1', '294', 'processMowMenu'), (1, '3000', '345', 'sendSonarMenu'), ('sonarTriggerBelow', '1', '351', 'processSonarMenu'), (0.1, '100', '365', 'sendPerimeterMenu'), (1, '8000', '364', 'sendPerimeterMenu'), (1, '8000', '363', 'sendPerimeterMenu'), (0.1, '100', '373', 'processPerimeterMenu'), ('perimeterTrackRevTime', '1', '372', 'processPerimeterMenu'), ('perimeterTrackRollTime', '1', '371', 'processPerimeterMenu'), (0.1, '30', '411', 'sendImuMenu'), (0.1, '20', '410', 'sendImuMenu'), (0.1, '30', '420', 'processImuMenu'), (0.1, '20', '419', 'processImuMenu'), (0.01, '10', '453', 'sendBatteryMenu'), (600, '400', '452', 'sendBatteryMenu'), ('batFull', '0.72', '446', 'sendBatteryMenu'), ('batFull', '0.72', '445', 'sendBatteryMenu'), (30, '0', '444', 'sendBatteryMenu'), ('chgFactor', '0.01', '475', 'processBatteryMenu'), ('chgSenseZero', '1', '474', 'processBatteryMenu'), ('batVoltage', '0.01', '470', 'processBatteryMenu'), ('batSwitchOffIfBelow', '0.1', '465', 'processBatteryMenu'), ('batGoHomeIfBelow', '0.1', '464', 'processBatteryMenu'), (1, '8000', '483', 'sendStationMenu'), (1, '8000', '482', 'sendStationMenu'), (1, '8000', '481', 'sendStationMenu'), ('stationForwTime', '1', '490', 'processStationMenu'), ('stationRollTime', '1', '489', 'processStationMenu'), ('stationRevTime', '1', '488', 'processStationMenu'), (0.1, '50', '508', 'sendOdometryMenu'), (0.1, '30', '507', 'sendOdometryMenu'), (1, '2000', '506', 'sendOdometryMenu'), ('odometryTicksPerRevolution', '1', '517', 'processOdometryMenu'), ('odometryWheelBaseCm', '0.1', '516', 'processOdometryMenu'), ('odometryTicksPerCm', '0.1', '515', 'processOdometryMenu'), (59, '0', '533', 'sendDateTimeMenu'), (23, '0', '532', 'sendDateTimeMenu'), (2020, '2013', '531', 'sendDateTimeMenu'), (12, '1', '530', 'sendDateTimeMenu'), (31, '1', '529', 'sendDateTimeMenu'), (6, '0', '528', 'sendDateTimeMenu'), ('ACT_RTC', '0', '545', 'processDateTimeMenu'), ('minute', '1', '543', 'processDateTimeMenu'), ('hour', '1', '542', 'processDateTimeMenu'), ('year', '1', '541', 'processDateTimeMenu'), ('month', '1', '540', 'processDateTimeMenu'), ('day', '1', '539', 'processDateTimeMenu'), ('dayOfWeek', '1', '538', 'processDateTimeMenu'), (59, '0', '560', 'sendTimerDetailMenu'), (23, '0', '559', 'sendTimerDetailMenu'), (59, '0', '558', 'sendTimerDetailMenu'), (23, '0', '557', 'sendTimerDetailMenu'), ('stopmin', '5', '612', 'processTimerDetailMenu'), ('startmin', '5', '602', 'processTimerDetailMenu'), ('pfodCmd', '3', '592', 'processTimerDetailMenu'), ('minute', '1', '586', 'processTimerDetailMenu'), ('hour', '1', '585', 'processTimerDetailMenu'), ('minute', '1', '584', 'processTimerDetailMenu'), ('hour', '1', '583', 'processTimerDetailMenu'), ('pfodCmd', '2', '581', 'processTimerDetailMenu'), ('pfodCmd', '2', '634', 'processTimerMenu'), ('STATE_OFF', '0', '725', 'processCommandMenu'), (1, '3', '724', 'processCommandMenu'), ('STATE_REMOTE', '0', '713', 'processCommandMenu'), ('STATE_FORWARD', '0', '707', 'processCommandMenu'), ('STATE_PERI_TRACK', '0', '702', 'processCommandMenu'), ('STATE_MANUAL', '0', '697', 'processCommandMenu'), ('STATE_PERI_FIND', '0', '694', 'processCommandMenu'), ('STATE_OFF', '0', '690', 'processCommandMenu'), ('STATE_ROLL_WAIT', '0', '780', 'processCompassMenu'), ('PI', '2', '779', 'processCompassMenu'), ('STATE_ROLL_WAIT', '0', '776', 'processCompassMenu'), ('PI', '2', '775', 'processCompassMenu'), ('STATE_ROLL_WAIT', '0', '772', 'processCompassMenu'), ('STATE_ROLL_WAIT', '0', '768', 'processCompassMenu'), ('imuRollHeading', '0', '767', 'processCompassMenu'), ('motorRightSpeed', '0', '823', 'processManualMenu'), ('STATE_MANUAL', '0', '812', 'processManualMenu'), ('STATE_MANUAL', '0', '806', 'processManualMenu'), ('motorSpeedMax', '2', '800', 'processManualMenu'), ('sign', '1.0', '799', 'processManualMenu'), ('sign', '1.0', '798', 'processManualMenu'), ('STATE_MANUAL', '0', '797', 'processManualMenu'), ('motorSpeedMax', '2', '791', 'processManualMenu'), ('sign', '1.0', '790', 'processManualMenu'), ('sign', '1.0', '789', 'processManualMenu'), ('STATE_MANUAL', '0', '788', 'processManualMenu'), ('beep', '2', '871', 'processArduMagResult'), ('substring', '11', '857', 'processArduMagResult'), ('pfodCmd', '9', '856', 'processArduMagResult'), ('pfodCmd', '8', '855', 'processArduMagResult'), ('type', '1', '854', 'processArduMagResult'), ('type', '0', '853', 'processArduMagResult'), ('millis', '200', '1037', 'pfodLoop'), ('millis', '200', '1008', 'pfodLoop'), ('perimeterCaptureIdx', '0', '1004', 'pfodLoop'), ('samples', '32', '1003', 'pfodLoop'), ('millis', '200', '979', 'pfodLoop'), ('millis', '200', '956', 'pfodLoop'), ('millis', '200', '915', 'pfodLoop'), ('millis', '500', '908', 'pfodLoop'), ('millis', '60000', '895', 'pfodLoop'), ('millis', '200', '880', 'pfodLoop'), ('nextPlotTime', '0', '1138', 'readSerialPfod'), ('nextPlotTime', '0', '1132', 'readSerialPfod'), ('nextPlotTime', '0', '1126', 'readSerialPfod'), ('nextPlotTime', '0', '1117', 'readSerialPfod'), ('nextPlotTime', '0', '1110', 'readSerialPfod'), ('nextPlotTime', '0', '1103', 'readSerialPfod'), ('nextPlotTime', '0', '1097', 'readSerialPfod'), ('beep', '1', '1078', 'readSerialPfod')]
Available in: https://github.com/Ardumower/ardumower/blob/23841dfeb7f43e732a87b3fa85f2f41105bd89f4/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/99b9d83baa40f1827c6f384ca934efc3a4f141a3/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(0.01, '1.0', '218', 'sendMotorMenu'), (1, '8000', '215', 'sendMotorMenu'), (1, '255', '212', 'sendMotorMenu'), ('batSwitchOffIfBelow', '0.1', '465', 'processBatteryMenu'), ('day', '1', '539', 'processDateTimeMenu'), ('dayOfWeek', '1', '538', 'processDateTimeMenu'), ('startmin', '5', '602', 'processTimerDetailMenu'), ('pfodCmd', '3', '592', 'processTimerDetailMenu'), ('nextPlotTime', '0', '1074', 'readSerialPfod'), ('beep', '1', '1055', 'readSerialPfod'), (0.01, '1.0', '216', 'sendMotorMenu'), (1, '8000', '213', 'sendMotorMenu'), ('motorLeftSpeed', '0', '255', 'processMotorMenu'), ('stationRollTime', '1', '487', 'processStationMenu'), ('stopmin', '5', '610', 'processTimerDetailMenu'), ('startmin', '5', '600', 'processTimerDetailMenu'), ('pfodCmd', '2', '579', 'processTimerDetailMenu'), ('pfodCmd', '2', '632', 'processTimerMenu')]
Available in: https://github.com/Ardumower/ardumower/blob/8996f79e1029c38215369b983cb6ef2627c80224/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/5e3026bdd20e88a7e6b7911179690d03738ae488/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

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

####Values removed
Values: [('batFull', '0.72', '444', 'sendBatteryMenu'), ('batFull', '0.72', '443', 'sendBatteryMenu'), (1, '8000', '480', 'sendStationMenu'), (1, '8000', '479', 'sendStationMenu'), (1, '2000', '504', 'sendOdometryMenu'), ('odometryTicksPerRevolution', '1', '515', 'processOdometryMenu'), (59, '0', '556', 'sendTimerDetailMenu'), ('hour', '1', '581', 'processTimerDetailMenu'), ('STATE_OFF', '0', '688', 'processCommandMenu'), ('sign', '1.0', '796', 'processManualMenu'), ('STATE_MANUAL', '0', '795', 'processManualMenu'), ('motorSpeedMax', '2', '789', 'processManualMenu'), ('sign', '1.0', '788', 'processManualMenu'), ('sign', '1.0', '787', 'processManualMenu'), ('STATE_MANUAL', '0', '786', 'processManualMenu'), ('millis', '200', '954', 'pfodLoop'), ('millis', '200', '931', 'pfodLoop'), ('nextPlotTime', '0', '1100', 'readSerialPfod'), ('nextPlotTime', '0', '1091', 'readSerialPfod'), ('nextPlotTime', '0', '1084', 'readSerialPfod'), ('nextPlotTime', '0', '1078', 'readSerialPfod'), ('nextPlotTime', '0', '1072', 'readSerialPfod'), (1, '8000', '484', 'sendStationMenu'), (1, '8000', '483', 'sendStationMenu'), (59, '0', '554', 'sendTimerDetailMenu'), (23, '0', '553', 'sendTimerDetailMenu'), ('hour', '1', '579', 'processTimerDetailMenu'), ('STATE_MANUAL', '0', '806', 'processManualMenu'), ('STATE_MANUAL', '0', '800', 'processManualMenu'), ('motorSpeedMax', '2', '794', 'processManualMenu'), ('sign', '1.0', '793', 'processManualMenu'), ('sign', '1.0', '792', 'processManualMenu'), ('sign', '1.0', '784', 'processManualMenu'), ('millis', '200', '1008', 'pfodLoop'), ('millis', '200', '979', 'pfodLoop'), ('millis', '200', '950', 'pfodLoop'), ('millis', '200', '904', 'pfodLoop'), ('nextPlotTime', '0', '1102', 'readSerialPfod'), ('nextPlotTime', '0', '1096', 'readSerialPfod'), ('nextPlotTime', '0', '1080', 'readSerialPfod')]
Available in: https://github.com/Ardumower/ardumower/blob/d8e6ab4a51df461bbbe93424d4b5f226ff6fb521/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/7076af2539a8d80eb720ee6927b0f9105e1c6bb5/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('STATE_MANUAL', '0', '239', 'processMotorMenu'), (600, '0', '190', 'sendMotorMenu'), ('nextPlotTime', '0', '1069', 'readSerialPfod'), ('nextPlotTime', '0', '1063', 'readSerialPfod'), ('nextPlotTime', '0', '1054', 'readSerialPfod'), ('nextPlotTime', '0', '1047', 'readSerialPfod'), ('nextPlotTime', '0', '1041', 'readSerialPfod'), ('nextPlotTime', '0', '1035', 'readSerialPfod'), ('beep', '1', '1016', 'readSerialPfod')]
Available in: https://github.com/Ardumower/ardumower/blob/1cddc59889d941553c2279c5a828a57918b71f5d/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/1b20ee9b0b55f6609e25c55e0c3602d2396843ec/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('batVoltage', '0.1', '433', 'processBatteryMenu'), (23, '0', '518', 'sendTimerDetailMenu'), ('hour', '1', '544', 'processTimerDetailMenu'), ('STATE_OFF', '0', '651', 'processCommandMenu'), ('PI', '2', '736', 'processCompassMenu'), ('STATE_MANUAL', '0', '758', 'processManualMenu'), ('STATE_MANUAL', '0', '749', 'processManualMenu'), ('millis', '200', '917', 'pfodLoop'), ('millis', '200', '838', 'pfodLoop'), (0.01, '10', '424', 'sendBatteryMenu'), ('batSenseZero', '1', '432', 'processBatteryMenu'), (59, '0', '513', 'sendTimerDetailMenu'), ('minute', '1', '539', 'processTimerDetailMenu'), ('STATE_OFF', '0', '678', 'processCommandMenu'), ('STATE_ROLL_WAIT', '0', '725', 'processCompassMenu'), ('STATE_MANUAL', '0', '759', 'processManualMenu'), ('motorSpeedMax', '2', '753', 'processManualMenu'), ('millis', '200', '938', 'pfodLoop'), ('millis', '200', '863', 'pfodLoop')]
Available in: https://github.com/Ardumower/ardumower/blob/3773004de7c939c8916441023b7d92838b31ff8a/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/1cddc59889d941553c2279c5a828a57918b71f5d/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('STATE_REMOTE', '0', '666', 'processCommandMenu'), ('millis', '200', '909', 'pfodLoop'), ('millis', '60000', '843', 'pfodLoop'), ('nextPlotTime', '0', '1046', 'readSerialPfod'), ('nextPlotTime', '0', '1039', 'readSerialPfod'), ('nextPlotTime', '0', '1033', 'readSerialPfod'), ('beep', '1', '1008', 'readSerialPfod'), ('sign', '1.0', '740', 'processManualMenu')]
Available in: https://github.com/Ardumower/ardumower/blob/6f052d40f2c5e331587562b09707d552b7773fac/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/3773004de7c939c8916441023b7d92838b31ff8a/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(0.1, '30', '403', 'sendBatteryMenu'), (0.1, '30', '402', 'sendBatteryMenu')]
Available in: https://github.com/Ardumower/ardumower/blob/da8fa2af1970ffc5d4a0dc039d7c679fae70a493/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/6f052d40f2c5e331587562b09707d552b7773fac/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

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

####Values removed
Values: [(0, '200', '409', 'sendBatteryMenu'), ('batSenseZero', '1', '420', 'processBatteryMenu'), (1, '8000', '430', 'sendStationMenu'), ('PI', '2', '716', 'processCompassMenu'), ('STATE_ROLL_WAIT', '0', '713', 'processCompassMenu'), ('STATE_ROLL_WAIT', '0', '709', 'processCompassMenu'), ('sign', '1.0', '739', 'processManualMenu'), ('motorSpeedMax', '2', '732', 'processManualMenu'), ('sign', '1.0', '731', 'processManualMenu'), ('sign', '1.0', '730', 'processManualMenu'), ('STATE_MANUAL', '0', '729', 'processManualMenu'), ('millis', '200', '926', 'pfodLoop'), ('millis', '200', '874', 'pfodLoop'), ('millis', '200', '851', 'pfodLoop'), ('nextPlotTime', '0', '1027', 'readSerialPfod'), ('nextPlotTime', '0', '1021', 'readSerialPfod'), ('nextPlotTime', '0', '1015', 'readSerialPfod'), (1, '8000', '428', 'sendStationMenu'), ('STATE_OFF', '0', '664', 'processCommandMenu'), ('STATE_ROLL_WAIT', '0', '719', 'processCompassMenu'), ('STATE_ROLL_WAIT', '0', '715', 'processCompassMenu'), ('STATE_MANUAL', '0', '751', 'processManualMenu'), ('STATE_MANUAL', '0', '745', 'processManualMenu'), ('motorSpeedMax', '2', '739', 'processManualMenu'), ('sign', '1.0', '737', 'processManualMenu'), ('STATE_MANUAL', '0', '736', 'processManualMenu'), ('millis', '200', '953', 'pfodLoop'), ('millis', '200', '924', 'pfodLoop'), ('millis', '200', '895', 'pfodLoop'), ('millis', '200', '872', 'pfodLoop'), ('nextPlotTime', '0', '1053', 'readSerialPfod'), ('nextPlotTime', '0', '1041', 'readSerialPfod')]
Available in: https://github.com/Ardumower/ardumower/blob/deb10377b29b9068c2bdfa6b6b6602b4db148366/ardumower/pfod.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/0b4e86d089b3f8bbb72594aaeb6eb6a96ca45c7e/ardumower/pfod.cpp
####True or False Positive:
[todo]
####Note:
[todo]

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

### Number of warnings:
11

## Result number #6

### File name(s)
code/ardumower/rmcs.h

### Compare results

####Values added
Values: [('Console', '1', '607', 'Robot'), (0, '1', '593', 'Robot'), (0, '1', '586', 'Robot'), (0, '1', '565', 'Robot'), (1, '0', '558', 'Robot'), (0, '0', '551', 'Robot'), (0, '0', '530', 'Robot'), (0, '1', '523', 'Robot'), (1, '0', '516', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/3603a9bfd0db3773770528766111789907696b0b/code/ardumower/rmcs.h
Added in: https://github.com/Ardumower/ardumower/blob/5b7af40bf59a725ee3ce0003eccf791da6ea93be/code/ardumower/rmcs.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('motorRightSpeedRpmSet', '0', '498', 'Robot'), ('motorLeftSpeedRpmSet', '0', '489', 'Robot'), ('STATE_MANUAL', '0', '474', 'Robot'), ('STATE_PERI_FIND', '0', '466', 'Robot'), ('STATE_FORWARD', '0', '462', 'Robot'), ('STATE_OFF', '0', '458', 'Robot'), ('RMCS_interval_imu', '0', '445', 'Robot'), ('RMCS_interval_drop', '0', '425', 'Robot'), ('RMCS_interval_perimeter', '0', '405', 'Robot'), ('RMCS_interval_gps', '0', '385', 'Robot'), ('RMCS_interval_odometry', '0', '365', 'Robot'), ('RMCS_interval_bumper', '0', '345', 'Robot'), ('RMCS_interval_sonar', '0', '325', 'Robot'), ('RMCS_interval_motor_current', '0', '306', 'Robot'), ('RMCS_interval_state', '0', '279', 'Robot'), ('commandParts', '2', '258', 'Robot'), ('commandParts', '0', '256', 'Robot'), ('indexEndOfCommandPart', '1', '247', 'Robot'), ('substring', '7', '230', 'Robot'), (1, '6', '229', 'Robot'), ('frequency', '0', '224', 'Robot'), ('indexArrayCommandParts', '0', '221', 'Robot'), ('indexEndOfCommandPart', '0', '220', 'Robot'), ('commandParts', '10', '218', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/e4a706e9822d0ab4af205eab33ff2519a0c5bbc0/code/ardumower/rmcs.h
Removed in: https://github.com/Ardumower/ardumower/blob/fc109138e3f5034b946dec2528b0469ed7fbd581/code/ardumower/rmcs.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('RMCS_interval_imu', '0', '445', 'Robot'), ('RMCS_interval_drop', '0', '425', 'Robot'), ('RMCS_interval_perimeter', '0', '405', 'Robot'), ('RMCS_interval_gps', '0', '385', 'Robot'), ('RMCS_interval_odometry', '0', '365', 'Robot'), ('RMCS_interval_bumper', '0', '345', 'Robot'), ('RMCS_interval_sonar', '0', '325', 'Robot'), ('RMCS_interval_motor_current', '0', '306', 'Robot'), ('RMCS_interval_state', '0', '279', 'Robot'), ('commandParts', '2', '258', 'Robot'), ('commandParts', '0', '256', 'Robot'), ('indexEndOfCommandPart', '1', '247', 'Robot'), ('substring', '7', '230', 'Robot'), (1, '6', '229', 'Robot'), ('frequency', '0', '224', 'Robot'), ('indexArrayCommandParts', '0', '221', 'Robot'), ('indexEndOfCommandPart', '0', '220', 'Robot'), ('commandParts', '10', '218', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/73fa5a9537b10d0e4515b1e56b4d57e62c6ec153/code/ardumower/rmcs.h
Added in: https://github.com/Ardumower/ardumower/blob/e4a706e9822d0ab4af205eab33ff2519a0c5bbc0/code/ardumower/rmcs.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('indexOf', '3', '183', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/12c5245cbfad6667aeb02787acaaa69901c82467/code/ardumower/rmcs.h
Added in: https://github.com/Ardumower/ardumower/blob/73fa5a9537b10d0e4515b1e56b4d57e62c6ec153/code/ardumower/rmcs.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:STATE_FORWARD
OLD:STATE_STATE_FORWARD
CHANGED:('STATE_STATE_FORWARD', '0', '197', 'Robot')
Version 1(new): https://github.com/Ardumower/ardumower/blob/12c5245cbfad6667aeb02787acaaa69901c82467/code/ardumower/rmcs.h
Version 2(old): https://github.com/Ardumower/ardumower/blob/9250f71d655cbf3671d7cfdf011b59d08df43861/code/ardumower/rmcs.h
####True or False Positive:
False
####Note:
Variable name change occurred.

####Values removed
Values: [('STATE_FORWARD', '0', '485', 'Robot'), ('STATE_OFF', '0', '479', 'Robot'), ('STATE_REMOTE', '0', '475', 'Robot'), ('PI', '2', '468', 'Robot'), ('STATE_ROLL_WAIT', '0', '467', 'Robot'), ('PI', '2', '464', 'Robot'), ('STATE_ROLL_WAIT', '0', '463', 'Robot'), ('STATE_STATION_CHARGING', '0', '460', 'Robot'), ('STATE_STATION', '0', '457', 'Robot'), ('STATE_PERI_TRACK', '0', '431', 'Robot'), ('STATE_PERI_FIND', '0', '428', 'Robot'), (1, '4', '424', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/7cda720ef49be2f6f88ab83ce03f50a1d6caf911/code/ardumower/rmcs.h
Removed in: https://github.com/Ardumower/ardumower/blob/1e75e2dfff3be5aef84f97f789c7bf0aec7705c0/code/ardumower/rmcs.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
6

## Result number #7

### File name(s)
ardumower/adcman.cpp

### Compare results

####Values removed
Values: [('ADC', '2', '199', 'ISR')]
Available in: https://github.com/Ardumower/ardumower/blob/c06f3f489407083af342d81c1f09d83dc40dbe2c/ardumower/adcman.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/931ade6bcda0024bf9ba96d7f431de11a23f0993/ardumower/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('magic', '0', '282', 'boolean')]
Not available in: https://github.com/Ardumower/ardumower/blob/e57cf30e63344dd6ebde0539eb16a8830f7e6208/ardumower/adcman.cpp
Added in: https://github.com/Ardumower/ardumower/blob/6604c0672ffa44f379089a9c4d87419728850358/ardumower/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('value', '4', '164', 'ADC_Handler'), ('ADC', '2', '151', 'ADC_Handler')]
Available in: https://github.com/Ardumower/ardumower/blob/e7219b4e561029165052863133a905f10d28e6dc/ardumower/adcman.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/e57cf30e63344dd6ebde0539eb16a8830f7e6208/ardumower/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('ADC', '2', '151', 'ADC_Handler')]
Not available in: https://github.com/Ardumower/ardumower/blob/7978541769ce436b8f720d99471c6da1555240e2/ardumower/adcman.cpp
Added in: https://github.com/Ardumower/ardumower/blob/e7219b4e561029165052863133a905f10d28e6dc/ardumower/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #8

### File name(s)
ardumower/due.cpp

### Compare results

####Values changed
NEW:('TC2', '0', '212', 'TC6_Handler')
OLD:('TC1', '0', '209', 'TC3_Handler')
CHANGED:('TC1', '0', '209', 'TC3_Handler')
Version 1(new): https://github.com/Ardumower/ardumower/blob/15a7b8e45298f545e3e82b9432ed0961eb09eb6a/ardumower/due.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/e73cf192f6e4b8538e71ce4bdd9375c84800db41/ardumower/due.cpp
####True or False Positive:
False
####Note:
Changed `TC_GetStatus` from using TC2 to using TC1, changed handler from `TC6_Handler` to `TC3_Handler`. Seems to be a change in design, but not one that is related to a HCFT pattern.

### Number of warnings:
1

## Result number #9

### File name(s)
tests/perimeterV2/perimeter.cpp

### Compare results

####Values removed
Values: [(127, '4095.0', '236', 'int16_t'), ('ss', '0', '218', 'int16_t'), ('Hsum', '0', '208', 'int16_t'), (127, '4095.0', '228', 'int16_t'), ('ss', '0', '217', 'int16_t')]
Available in: https://github.com/Ardumower/ardumower/blob/7ebaf4e6b7bbd52a5c801f50fb410c5fa648bc29/tests/perimeterV2/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/6076590a432ddcfd6509fbc77f9690636a857f7b/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

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

####Values added
Values: [(127, '4096.0', '228', 'int16_t'), (127, '4096.0', '227', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/931ade6bcda0024bf9ba96d7f431de11a23f0993/tests/perimeterV2/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/652b5ae2ac628bb5b8062681ed95cb2394186d95/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('sumMin', '0', '204', 'int16_t'), ('sumMax', '0', '203', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/debba3e528d7322125c71613f0d17b410c6d8ed5/tests/perimeterV2/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/931ade6bcda0024bf9ba96d7f431de11a23f0993/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('signalMax', '9999', '109', 'Perimeter'), ('signalMin', '9999', '108', 'Perimeter'), ('callCounter', '0', '107', 'Perimeter'), ('idxPin', '0', '103', 'Perimeter'), ('sum', '0', '177', 'int16_t'), ('sumMin', '0', '174', 'int16_t'), ('sumMax', '0', '173', 'int16_t')]
Available in: https://github.com/Ardumower/ardumower/blob/19f1e3f5bc414d22242a55c06de349a5ae584c8e/tests/perimeterV2/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/add4cdb7f3650183a293fd7f9d44b39a0ba6f556/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('sumMin', '0', '166', 'int16_t')
OLD:('sumMin', '0', '194', 'int16_t')
CHANGED:('sumMin', '0', '194', 'int16_t')
Version 1(new): https://github.com/Ardumower/ardumower/blob/4080b7222dbcea0d58907f3a876fe894c3253ebb/tests/perimeterV2/perimeter.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/0b1ccb199228b53f2c47f1a78413fa68acab2593/tests/perimeterV2/perimeter.cpp
####True or False Positive:
False
####Note:
Incorrectly detected method name, change here is only a change in the method name from `corrFilter` to `convFilter`.

####Values removed
Values: [(1, '6', '152', 'Perimeter'), ('idxPin', '0', '126', 'Perimeter'), (1, '3', '158', 'Perimeter'), ('i', '1', '148', 'Perimeter'), ('i', '1', '147', 'Perimeter'), ('callCounter', '0', '134', 'Perimeter')]
Available in: https://github.com/Ardumower/ardumower/blob/de4a8ee60db2ccaf3445690a2983940585bac914/tests/perimeterV2/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/0b1ccb199228b53f2c47f1a78413fa68acab2593/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '3', '156', 'Perimeter'), ('i', '1', '148', 'Perimeter'), ('i', '1', '147', 'Perimeter'), (1, '3', '154', 'Perimeter')]
Available in: https://github.com/Ardumower/ardumower/blob/6f277499c0dc53466f5790f7275378c4598ef275/tests/perimeterV2/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/de4a8ee60db2ccaf3445690a2983940585bac914/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('sumMax', '0', '189', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/ba24cc3342d81e8ecc8a26f858c0cb2adfd35f25/tests/perimeterV2/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/6f277499c0dc53466f5790f7275378c4598ef275/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('signalAvg', '0', '134', 'Perimeter'), ('signalMax', '9999', '133', 'Perimeter'), ('signalMin', '9999', '132', 'Perimeter'), ('callCounter', '0', '131', 'Perimeter'), ('sum', '0', '191', 'int16_t'), ('sumMin', '0', '188', 'int16_t'), ('sumMax', '0', '187', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/1ff47e835aeca3ea42d95931dde6b848b885747e/tests/perimeterV2/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/ba24cc3342d81e8ecc8a26f858c0cb2adfd35f25/tests/perimeterV2/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
10

## Result number #10

### File name(s)
ardumower/perimeter.cpp

### Compare results

####Values changed
NEW:('sum', '0', '316', 'Perimeter')
OLD:('sum', '0', '317', 'PerimeterClass')
CHANGED:('sum', '0', '317', 'PerimeterClass')
Version 1(new): https://github.com/Ardumower/ardumower/blob/99b9d83baa40f1827c6f384ca934efc3a4f141a3/ardumower/perimeter.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/d8e6ab4a51df461bbbe93424d4b5f226ff6fb521/ardumower/perimeter.cpp
####True or False Positive:
False
####Note:
Only a class name change occurred.

### Number of warnings:
1

## Result number #11

### File name(s)
tests/perimeterV2/adcman.cpp

### Compare results

####Values removed
Values: [('magic', '0', '306', 'boolean')]
Available in: https://github.com/Ardumower/ardumower/blob/1b86351472325dbd0374986aa60ccefb2c62d3c0/tests/perimeterV2/adcman.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/931ade6bcda0024bf9ba96d7f431de11a23f0993/tests/perimeterV2/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('magic', '0', '282', 'boolean')]
Not available in: https://github.com/Ardumower/ardumower/blob/6f277499c0dc53466f5790f7275378c4598ef275/tests/perimeterV2/adcman.cpp
Added in: https://github.com/Ardumower/ardumower/blob/de4a8ee60db2ccaf3445690a2983940585bac914/tests/perimeterV2/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('capturedChannels', '0', '236', 'ADCManager'), ('currSampleCount', '0', '149', 'ISR'), ('currSample', '0', '148', 'ISR'), ('currSample', '1', '147', 'ISR')]
Available in: https://github.com/Ardumower/ardumower/blob/e2308692a00eed8d24a01c862c50acc39042d49c/tests/perimeterV2/adcman.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/6f277499c0dc53466f5790f7275378c4598ef275/tests/perimeterV2/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('currSample', '1', '147', 'ISR'), ('ADC', '2', '135', 'ISR')]
Not available in: https://github.com/Ardumower/ardumower/blob/de7c21058e8cbd7e93bd1057d160195d537a90ac/tests/perimeterV2/adcman.cpp
Added in: https://github.com/Ardumower/ardumower/blob/e2308692a00eed8d24a01c862c50acc39042d49c/tests/perimeterV2/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #12

### File name(s)
ardumower/adcman.cpp

### Compare results

####Values added
Values: [('ADC', '2', '151', 'ADC_Handler')]
Not available in: https://github.com/Ardumower/ardumower/blob/7978541769ce436b8f720d99471c6da1555240e2/ardumower/adcman.cpp
Added in: https://github.com/Ardumower/ardumower/blob/e7219b4e561029165052863133a905f10d28e6dc/ardumower/adcman.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #13

### File name(s)
code/ardumower/settings.h

### Compare results

####Values added
Values: [('millis', '60000', '622', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/92dd22fcd82eb8e6abf6405e1ffdad17a85a2781/code/ardumower/settings.h
Added in: https://github.com/Ardumower/ardumower/blob/f2b2a2fe4c9bdb5c33dbd8d7c03db1e6637607a8/code/ardumower/settings.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #14

### File name(s)
ardumower/due.cpp

### Compare results

####Values changed
NEW:('TC2', '0', '212', 'TC6_Handler')
OLD:('TC1', '0', '209', 'TC3_Handler')
CHANGED:('TC1', '0', '209', 'TC3_Handler')
Version 1(new): https://github.com/Ardumower/ardumower/blob/15a7b8e45298f545e3e82b9432ed0961eb09eb6a/ardumower/due.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/e73cf192f6e4b8538e71ce4bdd9375c84800db41/ardumower/due.cpp
####True or False Positive:
False
####Note:
Changed handler and TC used.

### Number of warnings:
1

## Result number #15

### File name(s)
code/ardumower/imu.cpp

### Compare results

####Values added
Values: [('Q_gyro', '0.0003', '625', 'Kalman'), ('Q_angle', '0.01', '624', 'Kalman')]
Not available in: https://github.com/Ardumower/ardumower/blob/fd9e354e3eebe475a3f84388f64bd63a79216ef7/code/ardumower/imu.cpp
Added in: https://github.com/Ardumower/ardumower/blob/0a316de423a4d26abf69f20b3c370e32e14527f3/code/ardumower/imu.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #16

### File name(s)
ardumower/imu.cpp

### Compare results

####Values added
Values: [('looptime', '1000', '619', 'Kalman'), ('P_11', '0', '615', 'Kalman'), ('x_bias', '0', '614', 'Kalman'), ('R_angle', '0.01', '612', 'Kalman'), ('Q_gyro', '0.0003', '611', 'Kalman'), ('Q_angle', '0.01', '610', 'Kalman')]
Not available in: https://github.com/Ardumower/ardumower/blob/23090ec0995fbeb47aac2baed8d965fefa5fbc9b/ardumower/imu.cpp
Added in: https://github.com/Ardumower/ardumower/blob/690140292ab117b8d3e33fefeb11dd03433ba2c0/ardumower/imu.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('looptime', '1000.0', '700', 'Complementary2'), ('k', '10', '699', 'Complementary2'), ('looptime', '1000.0', '715', 'Complementary'), ('a', '0.0', '714', 'Complementary'), ('tau', '0.075', '713', 'Complementary')]
Not available in: https://github.com/Ardumower/ardumower/blob/6016bb23ea782eee0231b3f61a543f8eb2aea833/ardumower/imu.cpp
Added in: https://github.com/Ardumower/ardumower/blob/0fe7398bd7f69f9e1b35926f4999d633dd9159ea/ardumower/imu.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #17

### File name(s)
code/ardumower/ros.h

### Compare results

####Values added
Values: [(1000.0, '60.0', '34', 'Robot'), (1000.0, '60.0', '33', 'Robot'), (100.0, '2', '31', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/d25c91ec28d43101fba9babe89b2d2cfd203aeb5/code/ardumower/ros.h
Added in: https://github.com/Ardumower/ardumower/blob/f98ae9b2ffb91a849e94146a0f2591915ded0762/code/ardumower/ros.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '3000', '34', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/43143278c6d0a32f4ee49885dd74432fe7b95290/code/ardumower/ros.h
Added in: https://github.com/Ardumower/ardumower/blob/4240f48bb17d4c7d4f7553493059f0dae8896552/code/ardumower/ros.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('motorLeftSpeedRpmSet', '0', '63', 'Robot')
OLD:('motorLeftSpeedRpmSet', '0', '59', 'Robot')
CHANGED:('motorLeftSpeedRpmSet', '0', '59', 'Robot')
Version 1(new): https://github.com/Ardumower/ardumower/blob/43143278c6d0a32f4ee49885dd74432fe7b95290/code/ardumower/ros.h
Version 2(old): https://github.com/Ardumower/ardumower/blob/83c5aa29cdada6734a4dc03078ec85890b48a6ac/code/ardumower/ros.h
####True or False Positive:
False
####Note:
Only a line change occurred.

### Number of warnings:
3

## Result number #18

### File name(s)
code/ardumower/battery.h

### Compare results

####Values added
Values: [('delay', '2000', '11', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/f593a3507442e78463453e5dce4e523770a0b8ee/code/ardumower/battery.h
Added in: https://github.com/Ardumower/ardumower/blob/d06b40ea2ba043f3a90f6eeb086c60468833d215/code/ardumower/battery.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:ACT_BATTERY_SW
OLD:STATE_OFF
CHANGED:('STATE_OFF', '0', '12', 'Robot')
Version 1(new): https://github.com/Ardumower/ardumower/blob/f593a3507442e78463453e5dce4e523770a0b8ee/code/ardumower/battery.h
Version 2(old): https://github.com/Ardumower/ardumower/blob/6bec4d035a68119128de12a73a8f1ea0a3b7dda6/code/ardumower/battery.h
####True or False Positive:
False
####Note:
Change made on how to handle different states.

### Number of warnings:
2

## Result number #19

### File name(s)
code/ardumower/flashmem.cpp

### Compare results

####Values removed
Values: [(0, '0', '178', 'boolean'), ('dataLength', '1', '170', 'boolean'), (0, '0', '163', 'boolean')]
Available in: https://github.com/Ardumower/ardumower/blob/356057540a0ceb15a595882ca943bdb3b9964894/code/ardumower/flashmem.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/e0e6c1c24a3adc56eb9fa5fb47703372b1503161/code/ardumower/flashmem.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #20

### File name(s)
code/ardumower/robot.cpp

### Compare results

####Values added
Values: [('millis', '200', '1362', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/031abab283b6b6e3684243a137936abdef519042/code/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/640cd553528503cd9d2d7e9d8af746f288135b4c/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('millis', '200', '1361', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/46b6b162463a2660b3df29891a6ef2e3aa925396/code/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/031abab283b6b6e3684243a137936abdef519042/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('STATE_FORWARD', '0', '1621', 'Robot'), ('STATE_STATION_FORW', '0', '1617', 'Robot'), ('STATE_STATION_ROLL', '0', '1613', 'Robot'), ('STATE_STATION_REV', '0', '1607', 'Robot'), ('STATE_ERROR', '0', '1606', 'Robot'), ('STATE_FORWARD', '0', '1596', 'Robot'), ('STATE_ERROR', '0', '1581', 'Robot'), ('STATE_STATION', '0', '1577', 'Robot'), ('STATE_OFF', '0', '1571', 'Robot'), ('STATE_STATION_CHARGING', '0', '1569', 'Robot'), ('STATE_STATION', '0', '1560', 'Robot'), ('STATE_PERI_FIND', '0', '1537', 'Robot'), ('STATE_FORWARD', '0', '1444', 'Robot'), ('STATE_FORWARD', '0', '1441', 'Robot'), ('remoteMow', '100.0', '1402', 'Robot'), ('remoteSteer', '100.0', '1396', 'Robot'), ('STATE_STATION', '0', '1384', 'Robot'), ('beep', '2', '1383', 'Robot'), ('beep', '1', '1375', 'Robot'), ('millis', '5000', '1374', 'Robot'), ('stateLast', '0', '1369', 'Robot'), ('STATE_OFF', '0', '1368', 'Robot'), ('beep', '1', '1366', 'Robot'), ('millis', '1000', '1365', 'Robot'), ('loopsPerSecCounter', '0', '1355', 'Robot'), ('loopsPerSecLowCounter', '0', '1353', 'Robot'), ('STATE_ERROR', '0', '1351', 'Robot'), ('millis', '1000', '1333', 'Robot'), ('millis', '200', '1328', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/58b08b4deb203e30be8d038929c198a4839ff5c8/code/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/fd9e354e3eebe475a3f84388f64bd63a79216ef7/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('millis', '200', '1319', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/9250f71d655cbf3671d7cfdf011b59d08df43861/code/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/b50bd744a3f740c6268a6576be79f4de0648bb15/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '200', '1313', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/7cda720ef49be2f6f88ab83ce03f50a1d6caf911/code/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/1e75e2dfff3be5aef84f97f789c7bf0aec7705c0/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('STATE_ERROR', '0', '1309', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/9ebe92100b6274bba933e7d3c754d338d74b994e/code/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/8590eb703c4d1702feb02416a9c18d3a52c65b76/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '200', '2871', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/8b04c643311af0653a2e216db1d611d626ccab9e/code/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/43ad88ac11c09da12aaedb7099168582a829c2a5/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '5000', '2750', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/2dba08e845bfafe4db023a3fe0775c4cdc0eb8cb/code/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/2b871c27aa1eac9d045b055c8f65a67ccae64eff/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('millis', '300', '2750', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/07c32060d05a69b24aae4cca70666f13507ea625/code/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/2dba08e845bfafe4db023a3fe0775c4cdc0eb8cb/code/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
9

## Result number #21

### File name(s)
ardumower/robot.cpp

### Compare results

####Values removed
Values: [('millis', '300', '2432', 'Robot'), ('loopsPerSecCounter', '0', '2424', 'Robot'), ('millis', '1000', '2414', 'Robot'), ('millis', '200', '2409', 'Robot'), ('millis', '300', '2402', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/3909208f39e490ee21e2993fd731ef51ac768fe2/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/929177dc573aa8d83476f59c666dc23ca595f91a/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('millis', '300', '2316', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/dc5e911d9f425b49087ff7ec4ce7b9fe714d3f13/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/b5ceeef3b8b5a714311c8b85106cc2631b769664/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '200', '2314', 'Robot'), ('millis', '300', '2307', 'Robot'), ('millis', '300', '2302', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/c2d54f46b697f534f36f99e53f4271b2ca0b71d3/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/6fffac6d1726bea31756619bff518e4ef2b542ab/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '200', '1888', 'Robot'), ('millis', '300', '1882', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/9e0d25e13ec387459a777d362b3b1c9cd3ce60bc/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/6a9de62a80e395ac3074d55901413a404ffebda4/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('STATE_OFF', '0', '2045', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/ab0eac9ad7db6ff6f34a237ed2588b497d1490f6/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/9e0d25e13ec387459a777d362b3b1c9cd3ce60bc/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '200', '1881', 'Robot'), ('millis', '300', '1875', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/624d8537e31ad7c12382e0a9abc1d80ba643bc32/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/88bffeea60c9f12fe140e99f73b3422d9c17b4dd/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('STATE_STATION_ROLL', '0', '2041', 'Robot'), ('STATE_CHARGE_FORW', '0', '2046', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/ae96d77037877643ccf67714930131aecc6bffb9/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/624d8537e31ad7c12382e0a9abc1d80ba643bc32/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('millis', '300', '1515', 'Robot')]
Available in: https://github.com/Ardumower/ardumower/blob/b0c2a310202431fe4edf7ea314f8cac2558e8e55/ardumower/robot.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/1dd97fdcc3ff242bc6d3bce4f02795888244e3a9/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('millis', '300', '1485', 'Robot')]
Not available in: https://github.com/Ardumower/ardumower/blob/282b96875f381ce0506bcf86ec0a41c839780bb0/ardumower/robot.cpp
Added in: https://github.com/Ardumower/ardumower/blob/e2721de073189cd2a3f30ab5b8cfb9f13ed551d4/ardumower/robot.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
9

## Result number #22

### File name(s)
ardumower/perimeter.cpp

### Compare results

####Values added
Values: [('ss', '0', '218', 'int16_t'), ('sum', '0', '216', 'int16_t'), ('Hsum', '0', '208', 'int16_t'), ('sumMin', '0', '204', 'int16_t'), ('sumMax', '0', '203', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/9881fa6384ea3232a9ef782c30ba04b4d2c9e923/ardumower/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/f3d9dea387f732c8a526ffe095efe70cca5d620b/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('ss', '0', '218', 'int16_t'), ('sum', '0', '216', 'int16_t'), ('Hsum', '0', '208', 'int16_t'), ('sumMin', '0', '204', 'int16_t'), ('sumMax', '0', '203', 'int16_t')]
Available in: https://github.com/Ardumower/ardumower/blob/6076590a432ddcfd6509fbc77f9690636a857f7b/ardumower/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/9881fa6384ea3232a9ef782c30ba04b4d2c9e923/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(127, '4095.0', '236', 'int16_t'), ('ss', '0', '218', 'int16_t'), ('Hsum', '0', '208', 'int16_t'), (127, '4095.0', '228', 'int16_t'), ('ss', '0', '217', 'int16_t')]
Available in: https://github.com/Ardumower/ardumower/blob/7ebaf4e6b7bbd52a5c801f50fb410c5fa648bc29/ardumower/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/6076590a432ddcfd6509fbc77f9690636a857f7b/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

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

####Values added
Values: [(127, '4096.0', '228', 'int16_t'), (127, '4096.0', '227', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/931ade6bcda0024bf9ba96d7f431de11a23f0993/ardumower/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/652b5ae2ac628bb5b8062681ed95cb2394186d95/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('sumMin', '0', '204', 'int16_t'), ('sumMax', '0', '203', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/087ca2633bd99c25ae2aad64d2fdddf05088d891/ardumower/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/931ade6bcda0024bf9ba96d7f431de11a23f0993/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('signalMax', '9999', '109', 'Perimeter'), ('signalMin', '9999', '108', 'Perimeter'), ('callCounter', '0', '107', 'Perimeter'), ('idxPin', '0', '103', 'Perimeter'), ('sum', '0', '177', 'int16_t'), ('sumMin', '0', '174', 'int16_t'), ('sumMax', '0', '173', 'int16_t')]
Available in: https://github.com/Ardumower/ardumower/blob/73a048a8a177a64b129370d1dcb73c38fe8b37d7/ardumower/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/add4cdb7f3650183a293fd7f9d44b39a0ba6f556/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

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

####Values removed
Values: [('i', '1', '144', 'Perimeter'), ('i', '1', '143', 'Perimeter')]
Available in: https://github.com/Ardumower/ardumower/blob/3159b5d090d0811880686f7d9a88676967be5940/ardumower/perimeter.cpp
Removed in: https://github.com/Ardumower/ardumower/blob/f50a9d8e0958dbd386e3abd3cb00e02e65caf0d5/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('idxPin', '0', '128', 'Perimeter')
OLD:('idxPin', '0', '130', 'Perimeter')
CHANGED:('idxPin', '0', '130', 'Perimeter')
Version 1(new): https://github.com/Ardumower/ardumower/blob/25944416753fa3cb9ac053e4a93a3e4047873bd9/ardumower/perimeter.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/e57cf30e63344dd6ebde0539eb16a8830f7e6208/ardumower/perimeter.cpp
####True or False Positive:
False
####Note:
Change of line number.

####Values added
Values: [('i', '1', '148', 'Perimeter'), ('i', '1', '147', 'Perimeter'), ('signalAvg', '0', '137', 'Perimeter'), ('signalMax', '9999', '136', 'Perimeter'), ('signalMin', '9999', '135', 'Perimeter'), ('callCounter', '0', '134', 'Perimeter'), ('idxPin', '0', '130', 'Perimeter'), ('sum', '0', '197', 'int16_t'), ('sumMin', '0', '194', 'int16_t'), ('sumMax', '0', '193', 'int16_t')]
Not available in: https://github.com/Ardumower/ardumower/blob/837bc928c352fd9175f648225dc3492e682d5ab8/ardumower/perimeter.cpp
Added in: https://github.com/Ardumower/ardumower/blob/e57cf30e63344dd6ebde0539eb16a8830f7e6208/ardumower/perimeter.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('sum', '0', '316', 'Perimeter')
OLD:('sum', '0', '317', 'PerimeterClass')
CHANGED:('sum', '0', '317', 'PerimeterClass')
Version 1(new): https://github.com/Ardumower/ardumower/blob/99b9d83baa40f1827c6f384ca934efc3a4f141a3/ardumower/perimeter.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/d8e6ab4a51df461bbbe93424d4b5f226ff6fb521/ardumower/perimeter.cpp
####True or False Positive:
False
####Note:
Change of line number.

### Number of warnings:
12

## Result number #23

### File name(s)
ardumower/pid.cpp

### Compare results

####Values added
Values: [('y_min', '0', '90', 'VelocityPID'), ('y_max', '0', '89', 'VelocityPID'), ('Ta', '1.0', '83', 'VelocityPID'), ('lastControlTime', '1000000.0', '81', 'VelocityPID')]
Not available in: https://github.com/Ardumower/ardumower/blob/9a2afa1e99246af5dfb6e009d59276cca0ecbb3f/ardumower/pid.cpp
Added in: https://github.com/Ardumower/ardumower/blob/3b4de894657e160ee543ea9b1b63feb9fe647c5e/ardumower/pid.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('lastControlTime', '1000000.0', '38', 'PID')
OLD:('lastControlTime', '1000000.0', '37', 'PID')
CHANGED:('lastControlTime', '1000000.0', '37', 'PID')
Version 1(new): https://github.com/Ardumower/ardumower/blob/54f4753675d236e0b4fee57fb92abd9122345f42/ardumower/pid.cpp
Version 2(old): https://github.com/Ardumower/ardumower/blob/1844733dc6977b79c0632fd3dbe9bc9626db62ee/ardumower/pid.cpp
####True or False Positive:
False
####Note:
Change of line number.

### Number of warnings:
2

## Result number #24

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

