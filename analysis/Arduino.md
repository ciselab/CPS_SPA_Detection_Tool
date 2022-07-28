# Arduino

## Result number #1

### File name(s)
cores/esp8266/umm_malloc/umm_info.c

### Compare results

####Values removed
Values: [('NULL', '0', '177', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/7a43092df0c8734577870f5630ee0062150c1074/cores/esp8266/umm_malloc/umm_info.c
Removed in: https://github.com/esp8266/Arduino/blob/83523c025903412e8d5184febc274a48a9a3a3e7/cores/esp8266/umm_malloc/umm_info.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #2

### File name(s)
libraries/ESP8266WebServer/src/detail/RequestHandler.h

### Compare results

####Values removed
Values: [('length', '1', '65', 'handle')]
Available in: https://github.com/esp8266/Arduino/blob/e8b27912d724aa4bc5a78bcb535d08c7bed0a998/libraries/ESP8266WebServer/src/detail/RequestHandler.h
Removed in: https://github.com/esp8266/Arduino/blob/e62d5a92b981392d6f65fcec4d27a78b80c5bc1d/libraries/ESP8266WebServer/src/detail/RequestHandler.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #3

### File name(s)
cores/esp8266/uart.cpp

### Compare results

####Values removed
Values: [(1843200, '3686400', '1041', 'uart_detect_baudrate'), ('uart_nr', '1', '1033', 'uart_detect_baudrate')]
Available in: https://github.com/esp8266/Arduino/blob/cd7d137774c885135d958834d4dee878bf8b935f/cores/esp8266/uart.cpp
Removed in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/uart.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1843200, '3686400', '1024', 'uart_detect_baudrate'), ('uart_nr', '1', '1016', 'uart_detect_baudrate')]
Available in: https://github.com/esp8266/Arduino/blob/c720c0d9e8db2a2911ddd797c0876d675f58ddfb/cores/esp8266/uart.cpp
Removed in: https://github.com/esp8266/Arduino/blob/2cf76ba784daa9eefa6a939944c0d66ec92ab2ef/cores/esp8266/uart.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('uart_buff_switch', '0', '921', 'uart_set_debug'), ('uart_buff_switch', '1', '914', 'uart_set_debug'), ('uart_buff_switch', '0', '910', 'uart_set_debug')]
Not available in: https://github.com/esp8266/Arduino/blob/7436f3802aa6a6a7ec5e62ca05ca528eb1ea79ca/cores/esp8266/uart.cpp
Added in: https://github.com/esp8266/Arduino/blob/f3ca09006d1560c37e0560dcbd75f176dd129a81/cores/esp8266/uart.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #4

### File name(s)
cores/esp8266/uart.c

### Compare results

####Values added
Values: [(1843200, '3686400', '773', 'uart_detect_baudrate'), ('uart_nr', '1', '765', 'uart_detect_baudrate')]
Not available in: https://github.com/esp8266/Arduino/blob/29580e8166b6ec3562929cb9bdc4bcd741c12faf/cores/esp8266/uart.c
Added in: https://github.com/esp8266/Arduino/blob/e4d9c279ef1991256793745242c177148ca58b2a/cores/esp8266/uart.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('system_set_os_print', '1', '570', 'uart_set_debug')]
Available in: https://github.com/esp8266/Arduino/blob/f8f205d54af42f34502ad011fd015e104b63d911/cores/esp8266/uart.c
Removed in: https://github.com/esp8266/Arduino/blob/29580e8166b6ec3562929cb9bdc4bcd741c12faf/cores/esp8266/uart.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #5

### File name(s)
cores/esp8266/reboot_uart_dwnld.cpp

### Compare results

####Values changed
NEW:IRAM_ATTR
OLD:ICACHE_RAM_ATTR
CHANGED:('__wsr_vecbase', '1073741824', '83', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/656a33e6f82482535782213a6e96c2bd49b22a39/cores/esp8266/reboot_uart_dwnld.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/83f5f29cfdaa85b5b8874e29cb342a662feebff3/cores/esp8266/reboot_uart_dwnld.cpp
####True or False Positive:
False
####Note:
Function name has been changed.

### Number of warnings:
1

## Result number #6

### File name(s)
libraries/ESP8266WiFiMesh/src/TcpIpMeshBackend.cpp

### Compare results

####Values changed
NEW:TransmissionStatusType
OLD:transmission_status_t
CHANGED:(6, '0', '407', 'transmission_status_t')
Version 1(new): https://github.com/esp8266/Arduino/blob/16801f3dacf5e913ffef0c53051b83a8d155413a/libraries/ESP8266WiFiMesh/src/TcpIpMeshBackend.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/a49f0470963a5282d87a6fe662ba55b1ab308c2d/libraries/ESP8266WiFiMesh/src/TcpIpMeshBackend.cpp
####True or False Positive:
False
####Note:
`uint8_t targetBSSID[6] {0};` can be found on line 405. Changed return type, incorrect detection of function name.

####Values removed
Values: [('attemptNumber', '1', '321', 'transmission_status_t')]
Available in: https://github.com/esp8266/Arduino/blob/5834c547173d273def4a5337fac814a6856785c4/libraries/ESP8266WiFiMesh/src/TcpIpMeshBackend.cpp
Removed in: https://github.com/esp8266/Arduino/blob/86025c788438427f9195b56f51ce40a8304de6d2/libraries/ESP8266WiFiMesh/src/TcpIpMeshBackend.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #7

### File name(s)
cores/esp8266/core_esp8266_si2c.cpp

### Compare results

####Values removed
Values: [('twi_dcount', '1', '140', 'twi_setClock'), ('twi_dcount', '2', '139', 'twi_setClock'), ('twi_dcount', '3', '138', 'twi_setClock'), ('twi_dcount', '5', '137', 'twi_setClock'), ('twi_dcount', '8', '136', 'twi_setClock'), ('twi_dcount', '14', '135', 'twi_setClock'), ('twi_dcount', '32', '134', 'twi_setClock'), ('twi_dcount', '64', '133', 'twi_setClock'), ('twi_dcount', '1', '131', 'twi_setClock'), ('twi_dcount', '1', '130', 'twi_setClock'), ('twi_dcount', '3', '129', 'twi_setClock'), ('twi_dcount', '8', '128', 'twi_setClock'), ('twi_dcount', '19', '127', 'twi_setClock'), ('twi_dcount', '38', '126', 'twi_setClock'), ('twi_setClockStretchLimit', '230', '161', 'twi_init'), ('address', '1', '173', 'twi_setAddress'), ('bitCount', '8', '775', 'ICACHE_RAM_ATTR'), ('bitCount', '8', '743', 'ICACHE_RAM_ATTR'), ('bitCount', '8', '699', 'ICACHE_RAM_ATTR'), ('i', '0', '201', 'twi_write_stop'), ('twi_dcount', '1', '218', 'twi_write_bit'), ('i', '0', '214', 'twi_write_bit'), ('twi_dcount', '2', '229', 'twi_read_bit'), ('i', '0', '226', 'twi_read_bit'), ('byte', '128', '240', 'twi_write_byte'), ('byte', '0', '247', 'twi_read_byte'), ('t', '0', '273', 'twi_writeTo'), ('i', '0', '268', 'twi_writeTo'), ('t', '0', '294', 'twi_readFrom'), ('i', '0', '289', 'twi_readFrom'), (0, '0', '509', 'eventTask'), ('twi_txBufferLength', '1', '508', 'eventTask')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/core_esp8266_si2c.cpp
Removed in: https://github.com/esp8266/Arduino/blob/2a5d21597724faa6d65c420b7263c0f8b6f000ce/cores/esp8266/core_esp8266_si2c.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #8

### File name(s)
cores/esp8266/core_esp8266_si2c.c
cores/esp8266/si2c.c

### Compare results

####Values removed
Values: [('bitCount', '8', '695', 'ICACHE_RAM_ATTR'), ('t', '0', '270', 'twi_writeTo'), ('t', '0', '291', 'twi_readFrom'), ('bitCount', '8', '769', 'ICACHE_RAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/8ae0746e4aeaf7c2a8881831f370b40347e47a50/cores/esp8266/core_esp8266_si2c.c
Removed in: https://github.com/esp8266/Arduino/blob/aa22c07312a3f4b065a810cb91999e587b49166d/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('byte', '0', '244', 'twi_read_byte'), ('i', '0', '265', 'twi_writeTo'), ('i', '0', '285', 'twi_readFrom'), (0, '0', '504', 'eventTask'), ('twi_txBufferLength', '1', '503', 'eventTask')]
Not available in: https://github.com/esp8266/Arduino/blob/2105b8b06fef3e155dcdb775436ca1f77dccd586/cores/esp8266/core_esp8266_si2c.c
Added in: https://github.com/esp8266/Arduino/blob/cb05b86d49717ce155db618b9cb9e9cc18ced92f/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('clockCount', '20', '219', 'uint8_t')]
Available in: https://github.com/esp8266/Arduino/blob/6464ae0c7917cfcaac2b5ccf0cb71c3a4140b8b2/cores/esp8266/core_esp8266_si2c.c
Removed in: https://github.com/esp8266/Arduino/blob/2105b8b06fef3e155dcdb775436ca1f77dccd586/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('twi_dcount', '64', '55', 'twi_setClock'), ('i', '0', '206', 'twi_readFrom'), ('clockCount', '20', '219', 'uint8_t'), ('twi_dcount', '3', '50', 'twi_setClock')]
Available in: https://github.com/esp8266/Arduino/blob/438d3f1d1125aecbb7f08e7e19166152fd54d6e6/cores/esp8266/core_esp8266_si2c.c
Removed in: https://github.com/esp8266/Arduino/blob/6464ae0c7917cfcaac2b5ccf0cb71c3a4140b8b2/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('clockCount', '20', '203', 'uint8_t')]
Not available in: https://github.com/esp8266/Arduino/blob/3f15903566e0f6c4bcded7c0ea20e111d7beee44/cores/esp8266/core_esp8266_si2c.c
Added in: https://github.com/esp8266/Arduino/blob/099f3a4147f915d88b382f93ef056df5a9aecdc1/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('twi_dcount', '1', '52', 'twi_setClock'), ('i', '0', '191', 'twi_readFrom'), ('twi_dcount', '1', '50', 'twi_setClock')]
Available in: https://github.com/esp8266/Arduino/blob/d1a0c53805b148759e4247215cf709fd7a60901d/cores/esp8266/core_esp8266_si2c.c
Removed in: https://github.com/esp8266/Arduino/blob/3f15903566e0f6c4bcded7c0ea20e111d7beee44/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('twi_dcount', '1', '112', 'twi_write_bit')]
Available in: https://github.com/esp8266/Arduino/blob/8ec074e9fa719e5952caca54ed1ce1f79a9f7999/cores/esp8266/core_esp8266_si2c.c
Removed in: https://github.com/esp8266/Arduino/blob/d862cdbb5adce2505e58cc7d17512becbf70cb9e/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('i', '0', '153', 'twi_writeTo')]
Not available in: https://github.com/esp8266/Arduino/blob/735277fff97b0cf392346477428e7e9e8288a5fa/cores/esp8266/core_esp8266_si2c.c
Added in: https://github.com/esp8266/Arduino/blob/8ec074e9fa719e5952caca54ed1ce1f79a9f7999/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('byte', '0', '138', 'twi_read_byte')]
Not available in: https://github.com/esp8266/Arduino/blob/fbec557ddb12ad6663bd387a2980197dca79e576/cores/esp8266/si2c.c
Added in: https://github.com/esp8266/Arduino/blob/3d0dafcbc0066b71b8e601d69e8feeccec5780c5/cores/esp8266/core_esp8266_si2c.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
9

## Result number #9

### File name(s)
libraries/ESP8266WiFi/src/ESP8266WiFi.cpp

### Compare results

####Values removed
Values: [('bssid', '5', '860', 'String'), (18, '0', '855', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/6f00503bc37acd89fd4305151ac02e817fd06124/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/fd443d4e17ea7f896c7968153ca30795244c3c0d/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(18, '0', '748', 'String')]
Not available in: https://github.com/esp8266/Arduino/blob/b1b19299bbe5f508f88872cc57b6ecff25b22245/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Added in: https://github.com/esp8266/Arduino/blob/49b0821beb52fc3d6cdf180d5a6fcd71089c2d5e/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('dns_getserver', '0', '375', 'IPAddress')]
Available in: https://github.com/esp8266/Arduino/blob/7f318d72cfe117d822fe16aae6e3e9a520f12a75/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/6436a175c4a3df20ab178895dd64d7901fd9fa5d/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('delay', '0', '523', 'int8_t')]
Not available in: https://github.com/esp8266/Arduino/blob/f1dcfb279409c0b6885a8b5476bbb1a6f49365e9/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Added in: https://github.com/esp8266/Arduino/blob/7f318d72cfe117d822fe16aae6e3e9a520f12a75/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('bssid', '5', '477', 'String'), (18, '0', '472', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/d4ddb66fc468f10e0b710e5cdbfb87641cf24032/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/505ba22e0515029ea19ccbd365f15284c8a17208/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(18, '0', '472', 'String'), ('delay', '0', '430', 'int8_t')]
Not available in: https://github.com/esp8266/Arduino/blob/1aa8e8e6c8ede0ecdc741e88834e6a0dd44c0b78/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Added in: https://github.com/esp8266/Arduino/blob/d4ddb66fc468f10e0b710e5cdbfb87641cf24032/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('bssid', '5', '477', 'String'), (18, '0', '472', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/c77fbb23831de303bdf46c5e461504bed5bdffdb/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/36a4131f358e92e0a3c097a851a7c341c440142a/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_scanResult', '0', '384', 'int8_t')]
Available in: https://github.com/esp8266/Arduino/blob/9bb29fc777485cee105df0e958a1e33edab02018/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/389e5fb878eacbaad4cc29dbff5f66463553a2cd/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_scanResult', '0', '384', 'int8_t')]
Not available in: https://github.com/esp8266/Arduino/blob/9a1ff7f70dab5b948e4cd48f90ddc0fba5a17be8/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Added in: https://github.com/esp8266/Arduino/blob/9bb29fc777485cee105df0e958a1e33edab02018/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_scanResult', '0', '383', 'int8_t')]
Available in: https://github.com/esp8266/Arduino/blob/e6e57a8b8198a3ab1fe236b8dc1f4427277f0cd4/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/9a1ff7f70dab5b948e4cd48f90ddc0fba5a17be8/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_scanCount', '0', '350', 'int8_t'), ('_scanResult', '0', '349', 'int8_t')]
Not available in: https://github.com/esp8266/Arduino/blob/5a86c20f1e57509f80667908c7217e111208ad5a/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Added in: https://github.com/esp8266/Arduino/blob/c415ebe8b42dff7da390d905482da780b0bf79fd/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_scanResult', '0', '237', 'int8_t')]
Available in: https://github.com/esp8266/Arduino/blob/6c344ffbb1c8f7dfc4cc39406dd3d811b7d3db2f/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/eb98948d49fa7e3d0736b2c72a0f4d7eab75c408/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_scanCount', '0', '237', 'int8_t'), ('_scanResult', '0', '236', 'int8_t')]
Not available in: https://github.com/esp8266/Arduino/blob/b4f21fc6b0c829748d456d20202c084198a6bfa5/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
Added in: https://github.com/esp8266/Arduino/blob/d54952a21a96fe6a98944df5d9f848aac97a7286/libraries/ESP8266WiFi/src/ESP8266WiFi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
13

## Result number #10

### File name(s)
libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp

### Compare results

####Values added
Values: [(1, '0', '1363', '_SendAbort'), (1, '90', '1359', '_SendAbort')]
Not available in: https://github.com/esp8266/Arduino/blob/cfdcff102826ece0a83f68174eb5856cc788bffe/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
Added in: https://github.com/esp8266/Arduino/blob/594831d6058e8e204eb655b839564579b740c286/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(0, '8', '1537', 'WiFiClientSecure'), ('extBytes', '2', '1535', 'WiFiClientSecure'), ('comp', '1', '1528', 'WiFiClientSecure'), ('extBytes', '2', '1466', 'WiFiClientSecure'), ('cipher', '2', '1464', 'WiFiClientSecure'), ('rand', '32', '1462', 'WiFiClientSecure'), ('protoVer', '2', '1461', 'WiFiClientSecure'), ('hand', '4', '1459', 'WiFiClientSecure'), ('fragResp', '5', '1457', 'WiFiClientSecure'), (4, '255', '1439', 'WiFiClientSecure'), (4, '8', '1438', 'WiFiClientSecure'), (5, '255', '1436', 'WiFiClientSecure'), (5, '8', '1435', 'WiFiClientSecure'), ('flip', '2', '1429', 'WiFiClientSecure'), (255, '8', '1428', 'WiFiClientSecure'), ('suites_P', '255', '1424', 'WiFiClientSecure'), ('suites_P', '8', '1423', 'WiFiClientSecure'), ('clientHelloTail_P', '1', '1416', 'WiFiClientSecure'), ('mfl', '4', '1413', 'WiFiClientSecure'), ('mfl', '3', '1412', 'WiFiClientSecure'), ('mfl', '2', '1411', 'WiFiClientSecure'), ('mfl', '1', '1410', 'WiFiClientSecure'), (0, '1', '1403', 'WiFiClientSecure'), (24, '0', '1388', 'WiFiClientSecure'), ('to_copy', '0', '407', 'size_t'), ('res_subject', '32', '719', 'insecure_end_chain'), ('res_issuer', '32', '718', 'insecure_end_chain'), ('i', '255', '702', 'insecure_end_chain'), ('hex', '4', '701', 'insecure_end_chain'), (0, '0', '699', 'insecure_end_chain'), ('res', '1', '698', 'insecure_end_chain'), ('res', '20', '693', 'insecure_end_chain'), ('suites', '0', '924', 'br_ssl_client_base_init'), ('cipher_list', '0', '920', 'br_ssl_client_base_init'), ('suites', '0', '950', 'br_ssl_server_base_init'), ('cipher_list', '0', '946', 'br_ssl_server_base_init'), (1, '0', '1357', '_SendAbort'), (1, '90', '1353', '_SendAbort')]
Not available in: https://github.com/esp8266/Arduino/blob/8258db53da9a9858b8d001bb310db4902433d72a/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
Added in: https://github.com/esp8266/Arduino/blob/85ba53a24994db5ec2aff3b7adfa05330a637413/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('res', '20', '683', 'insecure_end_chain'), ('suites', '0', '914', 'br_ssl_client_base_init'), ('cipher_list', '0', '910', 'br_ssl_client_base_init'), ('suites', '0', '940', 'br_ssl_server_base_init'), ('cipher_list', '0', '936', 'br_ssl_server_base_init'), (1, '0', '1347', '_SendAbort'), (1, '90', '1343', '_SendAbort')]
Not available in: https://github.com/esp8266/Arduino/blob/a0634a71a9240ea2ecb326d01159a31ae511a531/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
Added in: https://github.com/esp8266/Arduino/blob/c18b402c31dc27ffc4b8817035ad8a44670c1b2e/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('suites', '0', '916', 'br_ssl_server_base_init'), ('cipher_list', '0', '912', 'br_ssl_server_base_init')]
Not available in: https://github.com/esp8266/Arduino/blob/69311c8fe1466a0202b743552091394b1e3ef4ca/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
Added in: https://github.com/esp8266/Arduino/blob/fe01433f788cb4bf6f0ce457184bc1a1d58a6498/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('cnt', '0', '1402', '_BearSSLCheckStack'), ('cnt', '0', '1430', '_BearSSLSerialPrint')]
Available in: https://github.com/esp8266/Arduino/blob/74ca42f829b0f9618cc3cf585395895e7521c910/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
Removed in: https://github.com/esp8266/Arduino/blob/19a0a0b6fd5a5af64a5f88590755ee645f709d4d/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('cnt', '0', '1330', '_BearSSLSerialPrint')]
Not available in: https://github.com/esp8266/Arduino/blob/cd43337f4f1d1bafbbacb2c3839a2760495556c5/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
Added in: https://github.com/esp8266/Arduino/blob/cc284bb5330258109888db83640aad19e11de744/libraries/ESP8266WiFi/src/WiFiClientSecureBearSSL.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
6

## Result number #11

### File name(s)
libraries/LittleFS/src/LittleFS.h

### Compare results

####Values added
Values: [('rc', '1', '648', 'next'), ('nameLen', '3', '663', '_getAttr')]
Not available in: https://github.com/esp8266/Arduino/blob/9de8373f1bbe885e922a36af1c1326f0e71f94f2/libraries/LittleFS/src/LittleFS.h
Added in: https://github.com/esp8266/Arduino/blob/c90c329a4847cc1beb7b687ac66ed3b6e3a9fadd/libraries/LittleFS/src/LittleFS.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('ftime', '0', '614', 'uint32_t'), ('ftime', '0', '611', 'uint32_t')]
Available in: https://github.com/esp8266/Arduino/blob/35d22edeec649b9578ebf1eb1067aa7f67f1f013/libraries/LittleFS/src/LittleFS.h
Removed in: https://github.com/esp8266/Arduino/blob/9de8373f1bbe885e922a36af1c1326f0e71f94f2/libraries/LittleFS/src/LittleFS.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('ftime', '0', '606', 'uint32_t'), ('ftime', '0', '554', 'time_t')]
Available in: https://github.com/esp8266/Arduino/blob/fa5040d5dafaa82334a2c5c345b2cb9449bacc7b/libraries/LittleFS/src/LittleFS.h
Removed in: https://github.com/esp8266/Arduino/blob/bea64dfa6987655ad9c51fda0949fdd4ab2a7d01/libraries/LittleFS/src/LittleFS.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('nameLen', '3', '542', 'time_t'), ('nameLen', '3', '511', 'FileImplPtr'), ('rc', '1', '579', 'next')]
Not available in: https://github.com/esp8266/Arduino/blob/1b3ac4f5e916108bf231e4e0082dafb888816572/libraries/LittleFS/src/LittleFS.h
Added in: https://github.com/esp8266/Arduino/blob/72dd589599e0b7d2e208eafeeca01a83b2d4cb94/libraries/LittleFS/src/LittleFS.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #12

### File name(s)
cores/esp8266/Stream.cpp

### Compare results

####Values removed
Values: [('index', '0', '231', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/953dfd945f03816db1943fa1345a9550fe61b422/cores/esp8266/Stream.cpp
Removed in: https://github.com/esp8266/Arduino/blob/c720c0d9e8db2a2911ddd797c0876d675f58ddfb/cores/esp8266/Stream.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('fraction', '1.0', '172', 'Stream')
OLD:('fraction', '1.0', '175', 'ICACHE_FLASH_ATTR')
CHANGED:('fraction', '1.0', '175', 'ICACHE_FLASH_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/1f32b7f66e22c5c26a54328e4f0997db369a9cbb/cores/esp8266/Stream.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/f165a0afcdadcfd392fc1f7adef27b2cc2d7748d/cores/esp8266/Stream.cpp
####True or False Positive:
False
####Note:
Changed return type, incorrect detection of function name.

####Values changed
NEW:('fraction', '1.0', '182', 'ICACHE_FLASH_ATTR')
OLD:('fraction', '1.0', '180', 'Stream')
CHANGED:('fraction', '1.0', '180', 'Stream')
Version 1(new): https://github.com/esp8266/Arduino/blob/160f99c31c6e9fe7734f6422a1d85a3704d3ae70/cores/esp8266/Stream.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/04fe8e8b58707147b751cc45b8b97adb7bacace5/cores/esp8266/Stream.cpp
####True or False Positive:
False
####Note:
Changed return type, incorrect detection of function name.

### Number of warnings:
3

## Result number #13

### File name(s)
cores/esp8266/mmu_iram.h

### Compare results

####Values removed
Values: [(3, '8', '188', 'int16_t'), ('_text_end', '32', '207', 'mmu_sec_heap')]
Available in: https://github.com/esp8266/Arduino/blob/60fe7b4ca8cdca25366af8a7c0a7b70d32c797f8/cores/esp8266/mmu_iram.h
Removed in: https://github.com/esp8266/Arduino/blob/b7a2f44b50a4c0675dde027d962a173128b201e8/cores/esp8266/mmu_iram.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #14

### File name(s)
libraries/DNSServer/src/DNSServer.cpp

### Compare results

####Values removed
Values: [('pos', '0', '95', 'String'), ('_buffer', '12', '90', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/42aa983628087d58567aa8b936db04eb4cc1b262/libraries/DNSServer/src/DNSServer.cpp
Removed in: https://github.com/esp8266/Arduino/blob/656bf146bc2340c19976ba220494a76cc003313b/libraries/DNSServer/src/DNSServer.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #15

### File name(s)
cores/esp8266/Updater.h

### Compare results

####Values added
Values: [('delay', '1', '106', 'size_t')]
Not available in: https://github.com/esp8266/Arduino/blob/f54386e1c01ccc6cdf6185f4ca1406f30e5d8739/cores/esp8266/Updater.h
Added in: https://github.com/esp8266/Arduino/blob/e613e42249830f6221f11c4951c5b1840a728dbd/cores/esp8266/Updater.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #16

### File name(s)
libraries/ESP8266WiFi/src/ESP8266WiFiSTA.cpp

### Compare results

####Values added
Values: [(18, '0', '645', 'String')]
Not available in: https://github.com/esp8266/Arduino/blob/ca79f2ce39724527052319717a731b3501d5f0b2/libraries/ESP8266WiFi/src/ESP8266WiFiSTA.cpp
Added in: https://github.com/esp8266/Arduino/blob/f0eb5509a02134aad2158ecc97167e209fa1c098/libraries/ESP8266WiFi/src/ESP8266WiFiSTA.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(18, '0', '641', 'String')]
Not available in: https://github.com/esp8266/Arduino/blob/68c0a1cc9e9427be10d1babdb994c43fed9c2271/libraries/ESP8266WiFi/src/ESP8266WiFiSTA.cpp
Added in: https://github.com/esp8266/Arduino/blob/ca79f2ce39724527052319717a731b3501d5f0b2/libraries/ESP8266WiFi/src/ESP8266WiFiSTA.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #17

### File name(s)
cores/esp8266/Esp.cpp

### Compare results

####Values changed
NEW:('currentOffset', '0', '761', 'size_t')
OLD:('currentOffset', '0', '757', 'size_t')
CHANGED:('currentOffset', '0', '757', 'size_t')
Version 1(new): https://github.com/esp8266/Arduino/blob/f60defc3d306152c13a20065aaa3d81ea17e690b/cores/esp8266/Esp.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/9fcf14f81fa9be589530e9596b7c5a264dc81ee8/cores/esp8266/Esp.cpp
####True or False Positive:
False
####Note:
Changed line number.

####Values added
Values: [('address', '4', '753', 'size_t'), ('aligned', '4', '748', 'size_t'), ('currentOffset', '0', '746', 'size_t'), ('size', '3', '745', 'size_t')]
Not available in: https://github.com/esp8266/Arduino/blob/36b444dba3b7e46629e9f8e60d4ebdc487d84f4d/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/79ea883fb3099e86030e69f867648dfabcd270b5/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(3, '3', '700', 'SpiFlashOpResult')]
Not available in: https://github.com/esp8266/Arduino/blob/ce200ed72e5511d89d92998065df879f0cfcd6aa/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/85ea47e9bcddb51064b71342f7e25ffcd40e9d9f/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('cooldownMicros', '2', '549', 'uint8_t'), ('bytesLeft', '0', '698', 'SpiFlashOpResult')]
Not available in: https://github.com/esp8266/Arduino/blob/9b41d9ac5e50e7726010120fe9c265a8df1d7eea/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/3c9a75f8311633eb7b47c6940f397fe06db86c8c/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('bytesLeft', '0', '614', 'SpiFlashOpResult')
OLD:('bytesLeft', '0', '606', 'spi_flash_write_puya')
CHANGED:('bytesLeft', '0', '606', 'spi_flash_write_puya')
Version 1(new): https://github.com/esp8266/Arduino/blob/fabd169abceebb0a5fee306850b9176d98b80795/cores/esp8266/Esp.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/d1b70dfc1d457739fbe9cfb60260d3a4c298eff5/cores/esp8266/Esp.cpp
####True or False Positive:
False
####Note:
Changed return type.

####Values removed
Values: [('rc', '0', '586', 'spi_flash_write_puya')]
Available in: https://github.com/esp8266/Arduino/blob/f5a882d03d30451ebcfa832293021748a372503a/cores/esp8266/Esp.cpp
Removed in: https://github.com/esp8266/Arduino/blob/d1b70dfc1d457739fbe9cfb60260d3a4c298eff5/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:_FS_start
OLD:_SPIFFS_start
CHANGED:('_SPIFFS_start', '1075838976', '529', 'uint32_t')
Version 1(new): https://github.com/esp8266/Arduino/blob/a389a995fb12459819e33970ec80695f1eaecc58/cores/esp8266/Esp.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/Esp.cpp
####True or False Positive:
False
####Note:
Changed var name.

####Values added
Values: [('bytesLeft', '0', '607', 'spi_flash_write_puya'), ('rc', '0', '588', 'spi_flash_write_puya')]
Not available in: https://github.com/esp8266/Arduino/blob/72ad9353fc5ea9b681be1beb3a384ebe04b6e21d/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/4c04c63c2a7773ac92b0860735d62e79a66b83bb/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('bufSize', '512', '531', 'String')]
Not available in: https://github.com/esp8266/Arduino/blob/32bd42b0281237d29e18bb769afad02bc6782a64/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/1640cc302d7eacf2aadaebe71dc0f4058a9e755c/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('buff', '200', '321', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/f57ab609ecc5a63ac23d2363db1916405bf56ab1/cores/esp8266/Esp.cpp
Removed in: https://github.com/esp8266/Arduino/blob/898737422e530fe9093dcefc3a7b1dd07795f778/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_SPIFFS_start', '1075838976', '353', 'uint32_t')]
Not available in: https://github.com/esp8266/Arduino/blob/0d969e97600c76b83bb0f8f41fe981ae629c1d57/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/5763dbba3b1ce1c6ff927054f03c664a73b42cce/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_SPIFFS_start', '1075838976', '353', 'uint32_t')]
Available in: https://github.com/esp8266/Arduino/blob/6f2069deac3efaa624ad99b5e4479ca09c32ef04/cores/esp8266/Esp.cpp
Removed in: https://github.com/esp8266/Arduino/blob/0d969e97600c76b83bb0f8f41fe981ae629c1d57/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('FLASH_SECTOR_SIZE', '1', '370', 'EspClass'), ('FLASH_SECTOR_SIZE', '1', '369', 'EspClass')]
Available in: https://github.com/esp8266/Arduino/blob/d828312299457312222effbd8c93f9cb5058d8e8/cores/esp8266/Esp.cpp
Removed in: https://github.com/esp8266/Arduino/blob/6f2069deac3efaa624ad99b5e4479ca09c32ef04/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('bytes', '2', '232', 'FlashMode_t')
OLD:('bytes', '2', '225', 'FlashMode_t')
CHANGED:('bytes', '2', '225', 'FlashMode_t')
Version 1(new): https://github.com/esp8266/Arduino/blob/c77fbb23831de303bdf46c5e461504bed5bdffdb/cores/esp8266/Esp.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/788095c66e220c6fe2e88b5205845c851502e475/cores/esp8266/Esp.cpp
####True or False Positive:
False
####Note:
Changed line number.

####Values changed
NEW:('bytes', '2', '225', 'FlashMode_t')
OLD:('bytes', '2', '239', 'FlashMode_t')
CHANGED:('bytes', '2', '239', 'FlashMode_t')
Version 1(new): https://github.com/esp8266/Arduino/blob/788095c66e220c6fe2e88b5205845c851502e475/cores/esp8266/Esp.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/f11c65e9a77eb721eff4388a96c1bc936d561149/cores/esp8266/Esp.cpp
####True or False Positive:
False
####Note:
Change of line number.

####Values changed
NEW:200
OLD:150
CHANGED:('buff', '150', '293', 'String')
Version 1(new): https://github.com/esp8266/Arduino/blob/e85605325405d1e80044c7c1dab7afece3ca46ae/cores/esp8266/Esp.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/26eede862f1e13ab9f9ba81aafb3162865edb02e/cores/esp8266/Esp.cpp
####True or False Positive:
True
####Note:
Changed buff size.

####Values added
Values: [('bytes', '2', '235', 'FlashMode_t'), ('buff', '150', '293', 'String')]
Not available in: https://github.com/esp8266/Arduino/blob/becc1d32eddd572465692b0b683145c37609e8a2/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/26eede862f1e13ab9f9ba81aafb3162865edb02e/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:16384
OLD:12288
CHANGED:('getFlashChipSize', '12288', '300', 'EspClass')
Version 1(new): https://github.com/esp8266/Arduino/blob/5a19cc24bf8cbddc4563da9fb4f843ea0dd2ec28/cores/esp8266/Esp.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/5852c484ca2784aca640b10f937ab1a7fdc0ccb0/cores/esp8266/Esp.cpp
####True or False Positive:
True
####Note:
[recheck] adjustments made due to the size of the chip.

####Values added
Values: [(8, '1024', '301', 'EspClass'), ('getFlashChipSize', '12288', '300', 'EspClass')]
Not available in: https://github.com/esp8266/Arduino/blob/dc52cf82c5f828e0846f652f45204e5b103f9474/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/5852c484ca2784aca640b10f937ab1a7fdc0ccb0/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('buff', '150', '287', 'String')]
Not available in: https://github.com/esp8266/Arduino/blob/4fdd546ad5b431eab08b80a9ddf91d6a224a6f10/cores/esp8266/Esp.cpp
Added in: https://github.com/esp8266/Arduino/blob/dc52cf82c5f828e0846f652f45204e5b103f9474/cores/esp8266/Esp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
20

## Result number #18

### File name(s)
cores/esp8266/core_esp8266_wiring_analog.c

### Compare results

####Values removed
Values: [('high', '0', '42', 'analogRead'), ('low', '0', '41', 'analogRead')]
Available in: https://github.com/esp8266/Arduino/blob/2d9c5d8297e9065dc982b9f75cf55e84b4afcb15/cores/esp8266/core_esp8266_wiring_analog.c
Removed in: https://github.com/esp8266/Arduino/blob/f8ddfe8d0a17928c1e4e01ccb0a85d2d359ef05c/cores/esp8266/core_esp8266_wiring_analog.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #19

### File name(s)
libraries/ESP8266WiFi/src/WiFiServer.cpp

### Compare results

####Values removed
Values: [('lastPollTime', '0', '96', 'WiFiClient')]
Available in: https://github.com/esp8266/Arduino/blob/f2f1fad298db9a94151268e4de2bf4f677542805/libraries/ESP8266WiFi/src/WiFiServer.cpp
Removed in: https://github.com/esp8266/Arduino/blob/d815c36753600a8e8f7f9610740dbd659a09818d/libraries/ESP8266WiFi/src/WiFiServer.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #20

### File name(s)
libraries/ESP8266WiFiMesh/src/TypeConversionFunctions.cpp
libraries/ESP8266WiFiMesh/src/UtilityFunctions.cpp

### Compare results

####Values removed
Values: [('base', '36', '30', 'String'), ('currentCharacter', '1', '49', 'uint64_t'), ('result', '0', '47', 'uint64_t'), ('base', '36', '45', 'uint64_t')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/libraries/ESP8266WiFiMesh/src/TypeConversionFunctions.cpp
Removed in: https://github.com/esp8266/Arduino/blob/d20177ae3553e90caaf90678b38b45e760f1ece1/libraries/ESP8266WiFiMesh/src/UtilityFunctions.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #21

### File name(s)
cores/esp8266/core_esp8266_main.cpp

### Compare results

####Values added
Values: [('UART_CLK_FREQ', '115200', '400', 'user_init')]
Not available in: https://github.com/esp8266/Arduino/blob/bc302511f53ca0709f1f4bbf2c048ba9aaf7bd34/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('wifi_fpm_do_sleep', '268435455', '346', '__disableWiFiAtBootTime'), ('wifi_set_opmode_current', '0', '343', '__disableWiFiAtBootTime')]
Not available in: https://github.com/esp8266/Arduino/blob/da6ec83b5fdbd5b02f04cf143dcf8e158a8cfd36/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/1cc6960a5516afb8b244e87574a57986101247bb/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('DBG_MMU_PRINT_IRAM_BANK_REG', '0', '323', 'app_entry_redefinable')]
Available in: https://github.com/esp8266/Arduino/blob/8b662ed3b345d2ded3c2ac484949b03e10bdc43c/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/e76a98d335bdd06da7a5869d0f41f0b2665ca1e8/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('UART_CLK_FREQ', '115200', '349', 'user_init')]
Not available in: https://github.com/esp8266/Arduino/blob/3e567e94898df2ace9264630900697bc30c5d69c/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/8b662ed3b345d2ded3c2ac484949b03e10bdc43c/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('UART_CLK_FREQ', '115200', '331', 'user_init')
OLD:('UART_CLK_FREQ', '115200', '320', 'user_init')
CHANGED:('UART_CLK_FREQ', '115200', '320', 'user_init')
Version 1(new): https://github.com/esp8266/Arduino/blob/6cb16997d8cedacc0dc5b1acda9a3e868b7b4395/cores/esp8266/core_esp8266_main.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/afe40211ef2011e642fa8fd963389f7dadcf612c/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
False
####Note:
Line change.

####Values added
Values: [('aligned', '16', '296', 'app_entry_redefinable'), ('UART_CLK_FREQ', '115200', '320', 'user_init')]
Not available in: https://github.com/esp8266/Arduino/blob/8d2eca56847a0344ea1b76ce62598bd4bcf2657b/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/50fab5162fdc09430a73f581043b4b669837ccf1/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('aligned', '16', '291', 'app_entry_redefinable'), ('UART_CLK_FREQ', '115200', '315', 'user_init')]
Available in: https://github.com/esp8266/Arduino/blob/3767791fbc4ce348095ea9f305817f9f89c594ac/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/554435780b3db892d0002cec5e707ea3ec984532/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(0, '0', '113', 'esp_schedule')]
Available in: https://github.com/esp8266/Arduino/blob/cb6b30a47de5e81f54f548e447a2615aac00d63e/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/916eb89b0754a06a4eab165b345319f26ac7cc03/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('aligned', '16', '244', 'app_entry_redefinable')]
Not available in: https://github.com/esp8266/Arduino/blob/05be1a09e6b4985a21b2b9446e56773a5557d0a8/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/d2a487dfd98f92de587e621b86c4bc4a4ec56e78/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('aligned', '16', '207', 'ICACHE_RAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/e486887f18255a819c6a4e602752b646a058b965/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/85e68093e94b4e5c5e711888b8b5facee1bd4f9f/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('UART_CLK_FREQ', '115200', '172', 'user_init')]
Not available in: https://github.com/esp8266/Arduino/blob/170911a6896e578f3cdba9b7b6e4f589446d0a67/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/5d5ea92a4d004ab009d5f642629946a0cb8893dd/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('info', '0', '125', 'user_init')]
Available in: https://github.com/esp8266/Arduino/blob/dc08418f086bdc6a850582b9ede5e313df4065b4/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/d815c36753600a8e8f7f9610740dbd659a09818d/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('system_set_os_print', '1', '117', 'init_done'), ('UART_CLK_FREQ', '74480', '135', 'user_init')]
Available in: https://github.com/esp8266/Arduino/blob/432198f178528d870ee90c6eed9ad754136e3e1a/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/dc08418f086bdc6a850582b9ede5e313df4065b4/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('info', '0', '135', 'user_init'), ('UART_CLK_FREQ', '74480', '129', 'user_init')]
Not available in: https://github.com/esp8266/Arduino/blob/e85605325405d1e80044c7c1dab7afece3ca46ae/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/66be67ced260766f7480cecd1b7f2d450f818fef/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('UART_CLK_FREQ', '74480', '129', 'user_init')]
Available in: https://github.com/esp8266/Arduino/blob/8f6d1e33d2629b28fa7e3803ddd5e0f5c77e3a47/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/e85605325405d1e80044c7c1dab7afece3ca46ae/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('info', '0', '135', 'user_init')]
Available in: https://github.com/esp8266/Arduino/blob/7c45873ffb02243839fc68ea124c19f17f845ad9/cores/esp8266/core_esp8266_main.cpp
Removed in: https://github.com/esp8266/Arduino/blob/8f6d1e33d2629b28fa7e3803ddd5e0f5c77e3a47/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('info', '0', '135', 'user_init'), ('UART_CLK_FREQ', '74480', '129', 'user_init')]
Not available in: https://github.com/esp8266/Arduino/blob/01d0f6142936a91bc8d8a8fd9a93590c175eb45e/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/dc52cf82c5f828e0846f652f45204e5b103f9474/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(0, '0', '83', 'esp_schedule'), ('UART_CLK_FREQ', '115200', '134', 'user_init')]
Not available in: https://github.com/esp8266/Arduino/blob/8e7a20c08d5afc43d9a10ad21bd20b44185fe8a7/cores/esp8266/core_esp8266_main.cpp
Added in: https://github.com/esp8266/Arduino/blob/ddb2343bc029f5a7659cfeed2dffaee7f62dc949/cores/esp8266/core_esp8266_main.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
18

## Result number #22

### File name(s)
cores/esp8266/main.cpp

### Compare results

####Values changed
NEW:(0, '0', '56', 'esp_schedule')
OLD:(0, '0', '52', 'loop_schedule')
CHANGED:(0, '0', '52', 'loop_schedule')
Version 1(new): https://github.com/esp8266/Arduino/blob/e21371d6d01ec724c26c38dbcd6b1eab7c00eeea/cores/esp8266/main.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/e199fc349c2932e35be46cfd683af43a655edccb/cores/esp8266/main.cpp
####True or False Positive:
False
####Note:
Line change.

####Values changed
NEW:(0, '0', '52', 'loop_schedule')
OLD:(0, '0', '48', 'loop_task')
CHANGED:(0, '0', '48', 'loop_task')
Version 1(new): https://github.com/esp8266/Arduino/blob/e199fc349c2932e35be46cfd683af43a655edccb/cores/esp8266/main.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/04fe8e8b58707147b751cc45b8b97adb7bacace5/cores/esp8266/main.cpp
####True or False Positive:
False
####Note:
Line change.

### Number of warnings:
2

## Result number #23

### File name(s)
cores/esp8266/core_esp8266_wiring_pwm.cpp

### Compare results

####Values changed
NEW:__analogWriteMode
OLD:__analogWrite
CHANGED:('val', '0', '52', '__analogWrite')
Version 1(new): https://github.com/esp8266/Arduino/blob/f2d83ba43df9f1c2ef1ff8ad5748ade6e3353de6/cores/esp8266/core_esp8266_wiring_pwm.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/f5fd5912fe09d7eec8a909326287379570579ea6/cores/esp8266/core_esp8266_wiring_pwm.cpp
####True or False Positive:
False
####Note:
Findable on line 56. Moved to a different line and name function has been changed.

####Values added
Values: [('res', '1', '86', '__analogWriteResolution')]
Not available in: https://github.com/esp8266/Arduino/blob/ccdde5f396d442f73dc101a1badeed3291f4652c/cores/esp8266/core_esp8266_wiring_pwm.cpp
Added in: https://github.com/esp8266/Arduino/blob/f5fd5912fe09d7eec8a909326287379570579ea6/cores/esp8266/core_esp8266_wiring_pwm.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('res', '1', '90', '__analogWriteResolution')]
Available in: https://github.com/esp8266/Arduino/blob/eec4dc490b0eefc310a7ad45f321ae9baf9e1f6d/cores/esp8266/core_esp8266_wiring_pwm.cpp
Removed in: https://github.com/esp8266/Arduino/blob/ccdde5f396d442f73dc101a1badeed3291f4652c/cores/esp8266/core_esp8266_wiring_pwm.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('analogMap', '1', '79', '__analogWrite')]
Not available in: https://github.com/esp8266/Arduino/blob/a67986915512c5304bd7c161cf0d9c65f66e0892/cores/esp8266/core_esp8266_wiring_pwm.cpp
Added in: https://github.com/esp8266/Arduino/blob/0e735e386dc17261ab230ad093f2d6d3ad1b6e9b/cores/esp8266/core_esp8266_wiring_pwm.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('val', '0', '61', '__analogWrite')]
Not available in: https://github.com/esp8266/Arduino/blob/ea1fdb210f84fbed421340a1341376e179e4addb/cores/esp8266/core_esp8266_wiring_pwm.cpp
Added in: https://github.com/esp8266/Arduino/blob/a67986915512c5304bd7c161cf0d9c65f66e0892/cores/esp8266/core_esp8266_wiring_pwm.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
5

## Result number #24

### File name(s)
cores/esp8266/core_esp8266_wiring_pwm.c

### Compare results

####Values removed
Values: [('pwm_steps_changed', '1', '119', 'prep_pwm_steps'), ('pwm_temp_steps_len', '4', '117', 'prep_pwm_steps'), (1, '2', '116', 'prep_pwm_steps'), ('pwm_steps_changed', '0', '113', 'prep_pwm_steps'), ('i', '1', '110', 'prep_pwm_steps'), ('pwm_temp_steps_len', '1', '105', 'prep_pwm_steps'), ('pwm_temp_masks', '17', '91', 'prep_pwm_steps'), ('pwm_temp_steps', '17', '90', 'prep_pwm_steps'), ('pwm_temp_steps_len', '0', '89', 'prep_pwm_steps'), ('timer1_write', '1', '165', 'pwm_start_timer'), ('pwm_range', '1', '200', '__analogWrite'), (1, '2', '198', '__analogWrite')]
Available in: https://github.com/esp8266/Arduino/blob/9791a48d4ae60f8a0778c2616511fff1104d1935/cores/esp8266/core_esp8266_wiring_pwm.c
Removed in: https://github.com/esp8266/Arduino/blob/ebda795f34e6d09f5676782f0917ad298d9a9cdd/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_pwm_isr_data', '0', '190', '__analogWrite')]
Available in: https://github.com/esp8266/Arduino/blob/b7c7bc038d2f4acc062bf209162e963f14464b9c/cores/esp8266/core_esp8266_wiring_pwm.c
Removed in: https://github.com/esp8266/Arduino/blob/9791a48d4ae60f8a0778c2616511fff1104d1935/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('pwm_steps_changed', '0', '151', 'ICACHE_RAM_ATTR'), ('GP16O', '1', '146', 'ICACHE_RAM_ATTR'), ('pwm_mask', '65535', '143', 'ICACHE_RAM_ATTR'), ('current_step', '0', '137', 'ICACHE_RAM_ATTR'), ('GP16O', '0', '133', 'ICACHE_RAM_ATTR'), ('current_step', '65535', '130', 'ICACHE_RAM_ATTR'), ('T1I', '0', '127', 'ICACHE_RAM_ATTR'), ('current_step', '0', '125', 'ICACHE_RAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/6feecc5122dd76b358c86e257d2a7802f64f745a/cores/esp8266/core_esp8266_wiring_pwm.c
Removed in: https://github.com/esp8266/Arduino/blob/b7c7bc038d2f4acc062bf209162e963f14464b9c/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('pwm_range', '1', '138', '__analogWrite')]
Available in: https://github.com/esp8266/Arduino/blob/1d2237bc9d81f1eca420dff04c27385201d3f8a0/cores/esp8266/core_esp8266_wiring_pwm.c
Removed in: https://github.com/esp8266/Arduino/blob/6feecc5122dd76b358c86e257d2a7802f64f745a/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('GP16O', '1', '109', 'ICACHE_RAM_ATTR'), ('GP16O', '0', '100', 'ICACHE_RAM_ATTR')]
Not available in: https://github.com/esp8266/Arduino/blob/0c703b3baf0f3137161373560d1914b880d57af3/cores/esp8266/core_esp8266_wiring_pwm.c
Added in: https://github.com/esp8266/Arduino/blob/1ae423021a3327b416919b95c17de6eafeffcffc/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:ICACHE_RAM_ATTR
OLD:pwm_timer_isr
CHANGED:('current_step', '65535', '97', 'pwm_timer_isr')
Version 1(new): https://github.com/esp8266/Arduino/blob/0c703b3baf0f3137161373560d1914b880d57af3/cores/esp8266/core_esp8266_wiring_pwm.c
Version 2(old): https://github.com/esp8266/Arduino/blob/6ae438b035029d59d4885cc1dd1707560f7044b3/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
False
####Note:
Added linker attributes to function. 

####Values changed
NEW:('pwm_mask', '65535', '106', 'pwm_timer_isr')
OLD:('pwm_mask', '65535', '105', 'pwm_timer_isr')
CHANGED:('pwm_mask', '65535', '105', 'pwm_timer_isr')
Version 1(new): https://github.com/esp8266/Arduino/blob/6ae438b035029d59d4885cc1dd1707560f7044b3/cores/esp8266/core_esp8266_wiring_pwm.c
Version 2(old): https://github.com/esp8266/Arduino/blob/6ab3c76e036bb8a6e791eeaf13ec53ec7062ee2b/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
False
####Note:
Change line number.

####Values added
Values: [('PWMRANGE', '1', '136', '__analogWrite')]
Not available in: https://github.com/esp8266/Arduino/blob/3ff208c3e937d8172abd30367934506dd2265eaa/cores/esp8266/core_esp8266_wiring_pwm.c
Added in: https://github.com/esp8266/Arduino/blob/7512339b0cb687e39dc6df2e3a757a3e4dde7719/cores/esp8266/core_esp8266_wiring_pwm.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
8

## Result number #25

### File name(s)
cores/esp8266/Updater.cpp

### Compare results

####Values added
Values: [('written', '0', '225', 'size_t')]
Not available in: https://github.com/esp8266/Arduino/blob/5c7b40740aedfdceddc9faf8324076707e8c2164/cores/esp8266/Updater.cpp
Added in: https://github.com/esp8266/Arduino/blob/0389657614e954ef19ab585cd198c0e59a107dfc/cores/esp8266/Updater.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #26

### File name(s)
libraries/ESP8266WiFiMesh/src/ESP8266WiFiMesh.cpp

### Compare results

####Values removed
Values: [('optimistic_yield', '10000', '568', 'ESP8266WiFiMesh'), ('optimistic_yield', '10000', '530', 'ESP8266WiFiMesh'), ('optimistic_yield', '10000', '503', 'transmission_status_t'), ('optimistic_yield', '10000', '479', 'transmission_status_t')]
Available in: https://github.com/esp8266/Arduino/blob/f382fc9d77a868fae7e6f467c994406a83e33367/libraries/ESP8266WiFiMesh/src/ESP8266WiFiMesh.cpp
Removed in: https://github.com/esp8266/Arduino/blob/7571c729f599bac9159c0261d7b62e731f16516d/libraries/ESP8266WiFiMesh/src/ESP8266WiFiMesh.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('optimistic_yield', '10000', '568', 'ESP8266WiFiMesh'), ('optimistic_yield', '10000', '530', 'ESP8266WiFiMesh'), ('optimistic_yield', '10000', '503', 'transmission_status_t'), ('optimistic_yield', '10000', '479', 'transmission_status_t')]
Not available in: https://github.com/esp8266/Arduino/blob/1dcd4c4a7b98aea498881372efc5faa80103cca3/libraries/ESP8266WiFiMesh/src/ESP8266WiFiMesh.cpp
Added in: https://github.com/esp8266/Arduino/blob/f382fc9d77a868fae7e6f467c994406a83e33367/libraries/ESP8266WiFiMesh/src/ESP8266WiFiMesh.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('delay', '3', '108', 'WiFiMesh'), ('wait', '1500', '106', 'WiFiMesh')]
Available in: https://github.com/esp8266/Arduino/blob/6f05da45cf1c636fae8bae8cea3018f107e97d0c/libraries/ESP8266WiFiMesh/src/ESP8266WiFiMesh.cpp
Removed in: https://github.com/esp8266/Arduino/blob/bdb5e0c0d9ee53b4b352419eb2e692ba01515cf8/libraries/ESP8266WiFiMesh/src/ESP8266WiFiMesh.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #27

### File name(s)
libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp

### Compare results

####Values changed
NEW:('', '0', '', 'int8_t')
OLD:('delay', '0', '252', 'int8_t')
CHANGED:('delay', '0', '252', 'int8_t')
Version 1(new): https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/60fe7b4ca8cdca25366af8a7c0a7b70d32c797f8/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
####True or False Positive:
Incorrect
####Note:
Result lost information about line number.

####Values removed
Values: [('delay', '0', '84', 'wl_status_t'), ('bestBSSID', '6', '80', 'wl_status_t'), ('delay', '0', '68', 'wl_status_t')]
Available in: https://github.com/esp8266/Arduino/blob/f1651fba89c292d28378ef1fb393f32b5792de7b/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
Removed in: https://github.com/esp8266/Arduino/blob/fceb390a1a76ea426584cee6d544bcec816e7f39/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('connectTimeout', '5000', '136', 'wl_status_t')]
Available in: https://github.com/esp8266/Arduino/blob/348c58b6441ac57e1be646a8141402e848684ecd/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
Removed in: https://github.com/esp8266/Arduino/blob/f1651fba89c292d28378ef1fb393f32b5792de7b/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('connectTimeout', '5000', '128', 'wl_status_t')]
Not available in: https://github.com/esp8266/Arduino/blob/02259a412c5a280a4d9713e47ae7ea6e04ffe361/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
Added in: https://github.com/esp8266/Arduino/blob/38fe6fc488d5a4b1a99f1694fa20f66123a830fe/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('delay', '0', '54', 'wl_status_t'), ('bestBSSID', '6', '47', 'wl_status_t')]
Not available in: https://github.com/esp8266/Arduino/blob/03da6393d57c005af786fd7a16224694fcb614e3/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
Added in: https://github.com/esp8266/Arduino/blob/bc37b9ea6856225055088d1afc6c780b807895c9/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('ip', '3', '111', 'wl_status_t')]
Not available in: https://github.com/esp8266/Arduino/blob/108a40acfd3af5fd703b049c9b28dc9dd1a7d131/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
Added in: https://github.com/esp8266/Arduino/blob/03da6393d57c005af786fd7a16224694fcb614e3/libraries/ESP8266WiFi/src/ESP8266WiFiMulti.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
6

## Result number #28

### File name(s)
cores/esp8266/core_esp8266_waveform_phase.cpp

### Compare results

####Values removed
Values: [('delay', '0', '214', 'startWaveformClockCycles_weak')]
Available in: https://github.com/esp8266/Arduino/blob/117f1630994cd68b3068a72524ca7ce846e1328e/cores/esp8266/core_esp8266_waveform_phase.cpp
Removed in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/core_esp8266_waveform_phase.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('loopPins', '1', '318', 'IRAM_ATTR')
OLD:('loopPins', '1', '318', 'ICACHE_RAM_ATTR')
CHANGED:('loopPins', '1', '318', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/656a33e6f82482535782213a6e96c2bd49b22a39/cores/esp8266/core_esp8266_waveform_phase.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/f5fd5912fe09d7eec8a909326287379570579ea6/cores/esp8266/core_esp8266_waveform_phase.cpp
####True or False Positive:
False
####Note:
Added linker attributes to function. 

####Values changed
NEW:('loopPins', '1', '318', 'ICACHE_RAM_ATTR')
OLD:('loopPins', '1', '312', 'ICACHE_RAM_ATTR')
CHANGED:('loopPins', '1', '312', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/f5fd5912fe09d7eec8a909326287379570579ea6/cores/esp8266/core_esp8266_waveform_phase.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/f8115c32c937733c07232a33a8d6187af669d032/cores/esp8266/core_esp8266_waveform_phase.cpp
####True or False Positive:
False
####Note:
Change line number.

### Number of warnings:
3

## Result number #29

### File name(s)
cores/esp8266/core_esp8266_waveform.cpp

### Compare results

####Values removed
Values: [('microsecondsToClockCycles', '1', '106', 'setTimer1Callback'), ('delay', '0', '147', 'startWaveformClockCycles'), ('microsecondsToClockCycles', '10', '143', 'startWaveformClockCycles'), ('microsecondsToClockCycles', '10', '139', 'startWaveformClockCycles')]
Available in: https://github.com/esp8266/Arduino/blob/36e047e908cfa6eafaaf824988070b49f2c2ff2a/cores/esp8266/core_esp8266_waveform.cpp
Removed in: https://github.com/esp8266/Arduino/blob/0e735e386dc17261ab230ad093f2d6d3ad1b6e9b/cores/esp8266/core_esp8266_waveform.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('delay', '0', '147', 'startWaveformClockCycles')
OLD:('delay', '0', '146', 'startWaveformCycles')
CHANGED:('delay', '0', '146', 'startWaveformCycles')
Version 1(new): https://github.com/esp8266/Arduino/blob/ea1fdb210f84fbed421340a1341376e179e4addb/cores/esp8266/core_esp8266_waveform.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/1af4ea661f4123d6aa1df87d3e0eadaf93e4c918/cores/esp8266/core_esp8266_waveform.cpp
####True or False Positive:
False
####Note:
Change line number.

####Values changed
NEW:('delay', '0', '146', 'startWaveformCycles')
OLD:('delay', '0', '142', 'startWaveform')
CHANGED:('delay', '0', '142', 'startWaveform')
Version 1(new): https://github.com/esp8266/Arduino/blob/1af4ea661f4123d6aa1df87d3e0eadaf93e4c918/cores/esp8266/core_esp8266_waveform.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/core_esp8266_waveform.cpp
####True or False Positive:
False
####Note:
Change line number.

### Number of warnings:
3

## Result number #30

### File name(s)
cores/esp8266/core_esp8266_waveform.c

### Compare results

####Values added
Values: [('startPin', '0', '206', 'ICACHE_RAM_ATTR'), ('microsecondsToClockCycles', '1', '103', 'setTimer1Callback'), ('delay', '0', '140', 'startWaveform'), ('microsecondsToClockCycles', '10', '136', 'startWaveform'), ('microsecondsToClockCycles', '10', '132', 'startWaveform')]
Not available in: https://github.com/esp8266/Arduino/blob/6e0c0e3dcc8e793b2c328cd0e9a3514f7dee5d09/cores/esp8266/core_esp8266_waveform.c
Added in: https://github.com/esp8266/Arduino/blob/8a64a1236f447009bd53fec4863aff9bf5428b59/cores/esp8266/core_esp8266_waveform.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '0', '219', 'stopWaveform')]
Available in: https://github.com/esp8266/Arduino/blob/bc2d4ec18bdaf160b2859d3681dacbc6c9e20516/cores/esp8266/core_esp8266_waveform.c
Removed in: https://github.com/esp8266/Arduino/blob/d742df84e53667b8456e94f70d1f21264b73aecb/cores/esp8266/core_esp8266_waveform.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #31

### File name(s)
cores/esp8266/spiffs/spiffs_check.c

### Compare results

####Values added
Values: [(0, '0', '981', 's32_t'), (0, '0', '979', 's32_t'), ('obj_id_log_ix', '0', '978', 's32_t')]
Not available in: https://github.com/esp8266/Arduino/blob/ca88cb2b67265d745b652711fb400c408d8da585/cores/esp8266/spiffs/spiffs_check.c
Added in: https://github.com/esp8266/Arduino/blob/c363b2d4f6f068d9521e875681552b0f673c73e2/cores/esp8266/spiffs/spiffs_check.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #32

### File name(s)
cores/esp8266/umm_malloc/umm_integrity.c

### Compare results

####Values removed
Values: [('ok', '0', '96', 'umm_integrity_check'), ('ok', '0', '79', 'umm_integrity_check'), ('prev', '0', '70', 'umm_integrity_check'), ('ok', '0', '60', 'umm_integrity_check'), ('ok', '0', '47', 'umm_integrity_check'), ('prev', '0', '37', 'umm_integrity_check'), ('ok', '1', '28', 'umm_integrity_check')]
Available in: https://github.com/esp8266/Arduino/blob/7a43092df0c8734577870f5630ee0062150c1074/cores/esp8266/umm_malloc/umm_integrity.c
Removed in: https://github.com/esp8266/Arduino/blob/83523c025903412e8d5184febc274a48a9a3a3e7/cores/esp8266/umm_malloc/umm_integrity.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #33

### File name(s)
libraries/ESP8266WiFi/src/include/UdpContext.h

### Compare results

####Values removed
Values: [('delay', '0', '414', 'sendTimeout')]
Available in: https://github.com/esp8266/Arduino/blob/60fe7b4ca8cdca25366af8a7c0a7b70d32c797f8/libraries/ESP8266WiFi/src/include/UdpContext.h
Removed in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('count', '0', '520', '_recv')]
Not available in: https://github.com/esp8266/Arduino/blob/af1bc71a9ea09bd92aed033e6a2b6ec2b10c311a/libraries/ESP8266WiFi/src/include/UdpContext.h
Added in: https://github.com/esp8266/Arduino/blob/a3281fe2f3436a3bce9604033344ae483bf5d0ed/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_tx_buf_head', '0', '411', 'send'), ('_tx_buf_offset', '0', '461', '_reserve'), ('pbuf_unit_size', '128', '452', '_reserve'), ('_rx_buf_offset', '0', '555', '_recv'), ('count', '0', '500', '_recv')]
Not available in: https://github.com/esp8266/Arduino/blob/4f27ce16b34064bb423a9b9783d50b5acaf8f3d0/libraries/ESP8266WiFi/src/include/UdpContext.h
Added in: https://github.com/esp8266/Arduino/blob/af1bc71a9ea09bd92aed033e6a2b6ec2b10c311a/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_tx_buf_head', '0', '434', 'send')]
Not available in: https://github.com/esp8266/Arduino/blob/4b2bf459332c8bd2b4bb8b967a00573986129fd8/libraries/ESP8266WiFi/src/include/UdpContext.h
Added in: https://github.com/esp8266/Arduino/blob/b8e4ca48a4b4330e4c42312d3923afd288cc2d95/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_tx_buf_offset', '0', '306', '_reserve'), ('pbuf_unit_size', '128', '301', '_reserve'), ('_rx_buf_offset', '0', '348', '_recv')]
Available in: https://github.com/esp8266/Arduino/blob/2126146e20042878026f03a19107555f32e3431c/libraries/ESP8266WiFi/src/include/UdpContext.h
Removed in: https://github.com/esp8266/Arduino/blob/a41f55c469dbf3ecfa3aa051fa95322d8d316e2e/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:128
OLD:512
CHANGED:('pbuf_unit_size', '512', '308', '_reserve')
Version 1(new): https://github.com/esp8266/Arduino/blob/3d1fbc60ab5c96294a6c68ea6bb9f292cb11aead/libraries/ESP8266WiFi/src/include/UdpContext.h
Version 2(old): https://github.com/esp8266/Arduino/blob/a44632b8cf9f54fe7226765fcbe6528ac83fc262/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
True
####Note:
Moved to line 296, the size of the `pbuf_unit_size` changed.

####Values changed
NEW:512
OLD:1024
CHANGED:('pbuf_unit_size', '1024', '307', '_reserve')
Version 1(new): https://github.com/esp8266/Arduino/blob/874cf0ef98bbcafd9abbdac2fec776f1ec5b1231/libraries/ESP8266WiFi/src/include/UdpContext.h
Version 2(old): https://github.com/esp8266/Arduino/blob/25d814bdfb4b025b234d8415b68fd24ea221a58e/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
True
####Note:
Moved to line 308, the size of the `pbuf_unit_size` changed.

####Values changed
NEW:('_rx_buf_offset', '0', '351', '_recv')
OLD:('_rx_buf_offset', '0', '328', '_recv')
CHANGED:('_rx_buf_offset', '0', '328', '_recv')
Version 1(new): https://github.com/esp8266/Arduino/blob/25d814bdfb4b025b234d8415b68fd24ea221a58e/libraries/ESP8266WiFi/src/include/UdpContext.h
Version 2(old): https://github.com/esp8266/Arduino/blob/3049d48d560dfe1a676de3fe8e4aeec5f8ebf059/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
False
####Note:
[check] Line number change

####Values changed
NEW:512
OLD:1024
CHANGED:('pbuf_unit_size', '1024', '284', '_reserve')
Version 1(new): https://github.com/esp8266/Arduino/blob/3049d48d560dfe1a676de3fe8e4aeec5f8ebf059/libraries/ESP8266WiFi/src/include/UdpContext.h
Version 2(old): https://github.com/esp8266/Arduino/blob/5354464a010a5e042bcf1514ec1bd9242de02940/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
True
####Note:
The size of the `pbuf_unit_size` changed.

### Number of warnings:
9

## Result number #34

### File name(s)
cores/esp8266/spiffs_api.h
cores/esp8266/spiffs_api.cpp

### Compare results

####Values removed
Values: [('config', '0', '179', '_tryMount'), ('_stat', '0', '379', '_getStat')]
Available in: https://github.com/esp8266/Arduino/blob/5313c56f24c26a97054f647f1cbc2758fd5b85f5/cores/esp8266/spiffs_api.h
Removed in: https://github.com/esp8266/Arduino/blob/2126146e20042878026f03a19107555f32e3431c/cores/esp8266/spiffs_api.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('mode', '0', '429', 'FileImplPtr'), ('mode', '0', '474', 'getSpiffsMode')]
Available in: https://github.com/esp8266/Arduino/blob/1d5d1c18c6609f79fbc640fc978fb05b0755c253/cores/esp8266/spiffs_api.cpp
Removed in: https://github.com/esp8266/Arduino/blob/1f32b7f66e22c5c26a54328e4f0997db369a9cbb/cores/esp8266/spiffs_api.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_stat', '0', '322', '_getStat')]
Not available in: https://github.com/esp8266/Arduino/blob/cd9791eebe3e927e95cd148267549a6790c63abc/cores/esp8266/spiffs_api.cpp
Added in: https://github.com/esp8266/Arduino/blob/f4bd97e8eeb16c40c05a9721f2fa65691179896a/cores/esp8266/spiffs_api.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('mode', '0', '401', 'getSpiffsMode')]
Not available in: https://github.com/esp8266/Arduino/blob/98423fa79daf3160946deec8afb597094e2f7876/cores/esp8266/spiffs_api.cpp
Added in: https://github.com/esp8266/Arduino/blob/041f971a8b59bfe23281514cf625ffc3f714ecc8/cores/esp8266/spiffs_api.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #35

### File name(s)
cores/esp8266/core_esp8266_wiring.cpp

### Compare results

####Values removed
Values: [('micros_overflow_tick', '0', '215', 'init')]
Available in: https://github.com/esp8266/Arduino/blob/60fe7b4ca8cdca25366af8a7c0a7b70d32c797f8/cores/esp8266/core_esp8266_wiring.cpp
Removed in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/core_esp8266_wiring.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('delay_end', '0', '48', '__delay')
OLD:('delay_end', '0', '48', 'delay')
CHANGED:('delay_end', '0', '48', 'delay')
Version 1(new): https://github.com/esp8266/Arduino/blob/d9684351c2d11dfe441e89edac43396689ac8ac5/cores/esp8266/core_esp8266_wiring.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/core_esp8266_wiring.cpp
####True or False Positive:
False
####Note:
Changed `delay` to `__delay`.

### Number of warnings:
2

## Result number #36

### File name(s)
cores/esp8266/core_esp8266_wiring.c

### Compare results

####Values added
Values: [(1, '0', '76', 'uint64_t')]
Not available in: https://github.com/esp8266/Arduino/blob/2126146e20042878026f03a19107555f32e3431c/cores/esp8266/core_esp8266_wiring.c
Added in: https://github.com/esp8266/Arduino/blob/5b925697ec1bee4ec8e366acace20cfd1fb51d18/cores/esp8266/core_esp8266_wiring.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '0', '64', 'millis')]
Available in: https://github.com/esp8266/Arduino/blob/1db2c8aa89818031576ab1f80e504faaeafc0951/cores/esp8266/core_esp8266_wiring.c
Removed in: https://github.com/esp8266/Arduino/blob/652703ef417ba9192727e0e39d23f67e29b70fac/cores/esp8266/core_esp8266_wiring.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('micros_overflow_tick', '0', '91', 'init')]
Not available in: https://github.com/esp8266/Arduino/blob/4cf67378233520a0babd8727743eeb05a0ee9e5f/cores/esp8266/core_esp8266_wiring.c
Added in: https://github.com/esp8266/Arduino/blob/c17e86842eb55d72877f364f7b703f96c344f554/cores/esp8266/core_esp8266_wiring.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #37

### File name(s)
cores/esp8266/wiring.c

### Compare results

####Values added
Values: [('delay_end', '0', '51', 'delay')]
Not available in: https://github.com/esp8266/Arduino/blob/168156d210897bacb4e703a822bc444784c04da5/cores/esp8266/wiring.c
Added in: https://github.com/esp8266/Arduino/blob/c55b5a89eb71779e0f5491e75477cfca384a2aa5/cores/esp8266/wiring.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('m', '0', '53', 'micros')]
Available in: https://github.com/esp8266/Arduino/blob/04fe8e8b58707147b751cc45b8b97adb7bacace5/cores/esp8266/wiring.c
Removed in: https://github.com/esp8266/Arduino/blob/168156d210897bacb4e703a822bc444784c04da5/cores/esp8266/wiring.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #38

### File name(s)
cores/esp8266/spiffs_hal.cpp

### Compare results

####Values removed
Values: [('optimistic_yield', '10000', '34', 'spi_flash_read_locked'), ('AutoInterruptLock', '5', '41', 'spi_flash_write_locked'), ('optimistic_yield', '10000', '40', 'spi_flash_write_locked'), ('AutoInterruptLock', '5', '47', 'spi_flash_erase_sector_locked'), ('optimistic_yield', '10000', '46', 'spi_flash_erase_sector_locked')]
Available in: https://github.com/esp8266/Arduino/blob/fac840b6a8740536212242dbf9ecf1d35df312a1/cores/esp8266/spiffs_hal.cpp
Removed in: https://github.com/esp8266/Arduino/blob/c355f626f24645415b508d7823dbe638ca1dd3e4/cores/esp8266/spiffs_hal.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('optimistic_yield', '10000', '34', 'spi_flash_read_locked'), ('AutoInterruptLock', '5', '41', 'spi_flash_write_locked'), ('optimistic_yield', '10000', '40', 'spi_flash_write_locked'), ('AutoInterruptLock', '5', '47', 'spi_flash_erase_sector_locked'), ('optimistic_yield', '10000', '46', 'spi_flash_erase_sector_locked')]
Not available in: https://github.com/esp8266/Arduino/blob/bbd8c9b41152630e0b178a6264e5686aedf5db64/cores/esp8266/spiffs_hal.cpp
Added in: https://github.com/esp8266/Arduino/blob/fac840b6a8740536212242dbf9ecf1d35df312a1/cores/esp8266/spiffs_hal.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #39

### File name(s)
libraries/SPI/SPI.cpp

### Compare results

####Values removed
Values: [('fifoPtr', '4294967295', '560', 'SPIClass'), (3, '4', '548', 'SPIClass'), ('size', '8', '545', 'SPIClass')]
Available in: https://github.com/esp8266/Arduino/blob/3cc12b1e08968aa6f35395d6a3bb265e197e91d5/libraries/SPI/SPI.cpp
Removed in: https://github.com/esp8266/Arduino/blob/8c01516f8ab0931d93ed8a4a97957bfe3ea4a7a6/libraries/SPI/SPI.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('size', '8', '397', 'SPIClass'), ('setDataBits', '8', '228', 'uint8_t')]
Not available in: https://github.com/esp8266/Arduino/blob/070f2b3a14aebb164b20c1462b0f599a6c075702/libraries/SPI/SPI.cpp
Added in: https://github.com/esp8266/Arduino/blob/27f45a205abfb9efb28df419bf85b00e71e1e6d8/libraries/SPI/SPI.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #40

### File name(s)
libraries/LittleFS/src/LittleFS.cpp

### Compare results

####Values removed
Values: [('creation', '0', '72', 'FileImplPtr'), ('ptr', '1', '133', 'DirImplPtr'), ('ptr', '0', '131', 'DirImplPtr'), ('ptr', '1', '135', 'DirImplPtr'), ('ptr', '0', '133', 'DirImplPtr')]
Available in: https://github.com/esp8266/Arduino/blob/b4d2ab102b60759f4ff6e5678557af12f07e4a4f/libraries/LittleFS/src/LittleFS.cpp
Removed in: https://github.com/esp8266/Arduino/blob/bea64dfa6987655ad9c51fda0949fdd4ab2a7d01/libraries/LittleFS/src/LittleFS.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #41

### File name(s)
cores/esp8266/core_esp8266_noniso.cpp

### Compare results

####Values added
Values: [('digit', '9', '106', 'dtostrf'), ('digit', '0', '103', 'dtostrf'), ('digitcount', '1', '80', 'dtostrf'), ('tenpow', '1.0', '79', 'dtostrf'), ('rounding', '2.0', '71', 'dtostrf')]
Not available in: https://github.com/esp8266/Arduino/blob/f762721603489a0f1741604a71835620253f6c43/cores/esp8266/core_esp8266_noniso.cpp
Added in: https://github.com/esp8266/Arduino/blob/cd56dc0901003cc140fd1df55758b76cbff8091e/cores/esp8266/core_esp8266_noniso.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('digit', '9', '101', 'dtostrf'), ('digit', '0', '98', 'dtostrf'), ('digitcount', '1', '79', 'dtostrf'), ('tenpow', '1.0', '78', 'dtostrf'), ('rounding', '2.0', '70', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/core_esp8266_noniso.cpp
Removed in: https://github.com/esp8266/Arduino/blob/f762721603489a0f1741604a71835620253f6c43/cores/esp8266/core_esp8266_noniso.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #42

### File name(s)
cores/esp8266/core_esp8266_noniso.c

### Compare results

####Values removed
Values: [('digit', '9', '149', 'dtostrf'), ('digit', '0', '146', 'dtostrf'), ('digitcount', '1', '127', 'dtostrf'), ('tenpow', '1.0', '126', 'dtostrf'), ('rounding', '2.0', '118', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/6d3109e8c79303d0a09538df523dd7ad29c6159a/cores/esp8266/core_esp8266_noniso.c
Removed in: https://github.com/esp8266/Arduino/blob/6883beedec8581aa37c38fb14dddffbe6796cddc/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('digit', '0', '207', 'dtostrf'), ('digitcount', '1', '188', 'dtostrf'), ('tenpow', '1.0', '187', 'dtostrf'), ('rounding', '2.0', '179', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/1f32b7f66e22c5c26a54328e4f0997db369a9cbb/cores/esp8266/core_esp8266_noniso.c
Removed in: https://github.com/esp8266/Arduino/blob/6d3109e8c79303d0a09538df523dd7ad29c6159a/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('digitcount', '1', '187', 'dtostrf'), ('tenpow', '1.0', '186', 'dtostrf'), ('out', '0', '208', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/659e467141a9738a883d5cc7e9670a4f1b8934f0/cores/esp8266/core_esp8266_noniso.c
Removed in: https://github.com/esp8266/Arduino/blob/1cd99391c3b31e23a47955e922ffa7a6eac9f867/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('out', '0', '203', 'dtostrf')]
Not available in: https://github.com/esp8266/Arduino/blob/dece2408302713dfbef59ae5d688c24fcf23187b/cores/esp8266/core_esp8266_noniso.c
Added in: https://github.com/esp8266/Arduino/blob/80ccbaef0dd744dcad1ce7805292be60cb50c143/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('signInt_Part', '1', '171', 'dtostrf'), ('signInt_Part', '1', '167', 'dtostrf')]
Not available in: https://github.com/esp8266/Arduino/blob/93f954d3638afa9d6b1717a5003f5f7fdbb6a11c/cores/esp8266/core_esp8266_noniso.c
Added in: https://github.com/esp8266/Arduino/blob/dece2408302713dfbef59ae5d688c24fcf23187b/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('n', '0', '151', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/f165a0afcdadcfd392fc1f7adef27b2cc2d7748d/cores/esp8266/core_esp8266_noniso.c
Removed in: https://github.com/esp8266/Arduino/blob/0bd2ea194895157f7420a4de17c7fb9731df6c70/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('result', '0', '128', 'ltoa'), ('out', '0', '167', 'utoa'), ('result', '0', '152', 'utoa'), ('out', '0', '188', 'ultoa'), ('result', '0', '173', 'ultoa'), ('rounding', '0.5', '217', 'dtostrf'), ('n', '0', '193', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/0efbe3a0c8f63760e1930b3fa8ec218cd2fd2701/cores/esp8266/core_esp8266_noniso.c
Removed in: https://github.com/esp8266/Arduino/blob/be6b8f8a2dd042418e5c61b82a8b4a08e7905b96/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('n', '0', '193', 'dtostrf')]
Not available in: https://github.com/esp8266/Arduino/blob/18effc3f9e357e5fbdc8e629a12d73cf3be30b44/cores/esp8266/core_esp8266_noniso.c
Added in: https://github.com/esp8266/Arduino/blob/0efbe3a0c8f63760e1930b3fa8ec218cd2fd2701/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('end', '1', '98', 'reverse'), ('sign', '1', '52', 'atof'), ('n', '0', '214', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/e6f3a59a52ae0654cd194981a88672de07f1cb68/cores/esp8266/core_esp8266_noniso.c
Removed in: https://github.com/esp8266/Arduino/blob/18effc3f9e357e5fbdc8e629a12d73cf3be30b44/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('result', '0', '192', 'ultoa'), ('rounding', '0.5', '243', 'dtostrf'), ('n', '0', '214', 'dtostrf')]
Not available in: https://github.com/esp8266/Arduino/blob/6aaa9ab3e6904d2ddee9b9a865284a66d3c5a903/cores/esp8266/core_esp8266_noniso.c
Added in: https://github.com/esp8266/Arduino/blob/e6f3a59a52ae0654cd194981a88672de07f1cb68/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('end', '1', '57', 'reverse'), ('out', '0', '91', 'itoa'), ('result', '0', '72', 'itoa'), ('out', '0', '118', 'ltoa'), ('result', '0', '99', 'ltoa'), ('out', '0', '142', 'utoa'), ('result', '0', '126', 'utoa'), ('out', '0', '166', 'ultoa'), ('result', '0', '150', 'ultoa'), ('rounding', '0.5', '201', 'dtostrf'), ('n', '0', '172', 'dtostrf')]
Not available in: https://github.com/esp8266/Arduino/blob/4cf67378233520a0babd8727743eeb05a0ee9e5f/cores/esp8266/core_esp8266_noniso.c
Added in: https://github.com/esp8266/Arduino/blob/6aaa9ab3e6904d2ddee9b9a865284a66d3c5a903/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('__s', '0', '40', 'dtostre'), ('__s', '0', '46', 'dtostrf')]
Available in: https://github.com/esp8266/Arduino/blob/2d9c5d8297e9065dc982b9f75cf55e84b4afcb15/cores/esp8266/core_esp8266_noniso.c
Removed in: https://github.com/esp8266/Arduino/blob/4dd9b0481fedd5fb2386865525e4e186cd88b10a/cores/esp8266/core_esp8266_noniso.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
12

## Result number #43

### File name(s)
cores/esp8266/core_esp8266_non32xfer.cpp

### Compare results

####Values removed
Values: [(3, '8', '108', 'IRAM_ATTR'), ('pWord', '0', '107', 'IRAM_ATTR'), ('epc', '3', '106', 'IRAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/0203dea024af68b4b0dbfbc5d7a98ee29839f02b/cores/esp8266/core_esp8266_non32xfer.cpp
Removed in: https://github.com/esp8266/Arduino/blob/8ffe41b7df9292ff04a6ce22de2815d075330a35/cores/esp8266/core_esp8266_non32xfer.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('is_read', '1', '116', 'IRAM_ATTR'), ('valmask', '0', '114', 'IRAM_ATTR'), (3, '8', '108', 'IRAM_ATTR'), ('pWord', '0', '107', 'IRAM_ATTR'), ('epc', '3', '106', 'IRAM_ATTR')]
Not available in: https://github.com/esp8266/Arduino/blob/8b662ed3b345d2ded3c2ac484949b03e10bdc43c/cores/esp8266/core_esp8266_non32xfer.cpp
Added in: https://github.com/esp8266/Arduino/blob/67e1dfc5a4187e82e879cdaab5afda1c0f131583/cores/esp8266/core_esp8266_non32xfer.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #44

### File name(s)
cores/esp8266/core_esp8266_wiring_digital.cpp

### Compare results

####Values changed
NEW:IRAM_ATTR
OLD:ICACHE_RAM_ATTR
CHANGED:('pin', '0', '228', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/656a33e6f82482535782213a6e96c2bd49b22a39/cores/esp8266/core_esp8266_wiring_digital.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/f5fd5912fe09d7eec8a909326287379570579ea6/cores/esp8266/core_esp8266_wiring_digital.cpp
####True or False Positive:
False
####Note:
[check] Added linker attributes to function.

####Values added
Values: [('system_set_os_print', '0', '240', 'initPins')]
Not available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/core_esp8266_wiring_digital.cpp
Added in: https://github.com/esp8266/Arduino/blob/93a52f923b1d46acaee91be20e2fc1a8629f55c2/cores/esp8266/core_esp8266_wiring_digital.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #45

### File name(s)
cores/esp8266/core_esp8266_wiring_digital.c

### Compare results

####Values removed
Values: [('xt_rsil', '15', '129', 'ICACHE_RAM_ATTR'), ('i', '0', '118', 'ICACHE_RAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/214d8bc8b8cb59fff65727484789d097b2727785/cores/esp8266/core_esp8266_wiring_digital.c
Removed in: https://github.com/esp8266/Arduino/blob/6b0a117e3d0f0ee7e2f6eeb3662aff2c46fb699a/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:ICACHE_RAM_ATTR
OLD:interrupt_handler
CHANGED:('i', '0', '118', 'interrupt_handler')
Version 1(new): https://github.com/esp8266/Arduino/blob/214d8bc8b8cb59fff65727484789d097b2727785/cores/esp8266/core_esp8266_wiring_digital.c
Version 2(old): https://github.com/esp8266/Arduino/blob/466fa6f5a9390c4250baceecb50c7c471d8a4c2a/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
False
####Note:
[check] Added linker attributes to function.

####Values changed
NEW:interrupt_handler
OLD:ICACHE_RAM_ATTR
CHANGED:('i', '0', '117', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/466fa6f5a9390c4250baceecb50c7c471d8a4c2a/cores/esp8266/core_esp8266_wiring_digital.c
Version 2(old): https://github.com/esp8266/Arduino/blob/6c20126a5ffec5227cb1d31fcfe74f82f4857df9/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
False
####Note:
[check] Added linker attributes to function.

####Values changed
NEW:ICACHE_RAM_ATTR
OLD:interrupt_handler
CHANGED:('i', '0', '117', 'interrupt_handler')
Version 1(new): https://github.com/esp8266/Arduino/blob/6c20126a5ffec5227cb1d31fcfe74f82f4857df9/cores/esp8266/core_esp8266_wiring_digital.c
Version 2(old): https://github.com/esp8266/Arduino/blob/57642c10b6491a30be932097edd45280500b9b70/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
False
####Note:
[check] Added linker attributes to function.

####Values added
Values: [('xt_rsil', '15', '128', 'interrupt_handler')]
Not available in: https://github.com/esp8266/Arduino/blob/8e699b426ba10fdc694bbc6706970e7b30f6b24c/cores/esp8266/core_esp8266_wiring_digital.c
Added in: https://github.com/esp8266/Arduino/blob/57642c10b6491a30be932097edd45280500b9b70/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('i', '0', '123', 'interrupt_handler'), ('U1IE', '0', '168', 'initPins'), ('U0IE', '0', '167', 'initPins'), ('system_set_os_print', '0', '166', 'initPins')]
Not available in: https://github.com/esp8266/Arduino/blob/c77f11906cf3220989019df70cee66ce4ad65f37/cores/esp8266/core_esp8266_wiring_digital.c
Added in: https://github.com/esp8266/Arduino/blob/d0137574d006c475b6b423db35417ecca39422e0/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('i', '0', '118', 'interrupt_handler'), ('U1IE', '0', '163', 'initPins'), ('U0IE', '0', '162', 'initPins'), ('system_set_os_print', '0', '161', 'initPins')]
Available in: https://github.com/esp8266/Arduino/blob/ddf03fc92b8d1e2997b3ba65d039130197a6aa0f/cores/esp8266/core_esp8266_wiring_digital.c
Removed in: https://github.com/esp8266/Arduino/blob/c77f11906cf3220989019df70cee66ce4ad65f37/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('U1IE', '0', '160', 'initPins'), ('U0IE', '0', '159', 'initPins'), ('system_set_os_print', '0', '158', 'initPins')]
Not available in: https://github.com/esp8266/Arduino/blob/d4e6561b5253348c87ca0222adea1cea3e303865/cores/esp8266/core_esp8266_wiring_digital.c
Added in: https://github.com/esp8266/Arduino/blob/c94128c02d11810058e9699a320e60101ef6282e/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '0', '69', '__pinMode'), ('val', '1', '100', '__digitalWrite'), ('pin', '0', '152', '__detachInterrupt')]
Available in: https://github.com/esp8266/Arduino/blob/2472970933b298bfb573eac062095de2f1b1f56c/cores/esp8266/core_esp8266_wiring_digital.c
Removed in: https://github.com/esp8266/Arduino/blob/fbec557ddb12ad6663bd387a2980197dca79e576/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('val', '1', '118', '__digitalWrite')
OLD:('val', '1', '119', 'digitalWrite')
CHANGED:('val', '1', '119', 'digitalWrite')
Version 1(new): https://github.com/esp8266/Arduino/blob/6ea230a1bc6b74901f0e9b6a7416183abeee2c35/cores/esp8266/core_esp8266_wiring_digital.c
Version 2(old): https://github.com/esp8266/Arduino/blob/e40d18e10739ee61c7bd194b8c63f79ce0f692cb/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
False
####Note:
[check] changed `digitalWrite` to `__digitalWrite`.

####Values added
Values: [(67, '1', '82', 'pinMode'), (1, '0', '80', 'pinMode'), ('val', '1', '119', 'digitalWrite'), ('pin', '0', '186', 'detachInterrupt')]
Not available in: https://github.com/esp8266/Arduino/blob/4cf67378233520a0babd8727743eeb05a0ee9e5f/cores/esp8266/core_esp8266_wiring_digital.c
Added in: https://github.com/esp8266/Arduino/blob/e40d18e10739ee61c7bd194b8c63f79ce0f692cb/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('pin', '0', '170', 'detachInterrupt')]
Not available in: https://github.com/esp8266/Arduino/blob/f8ddfe8d0a17928c1e4e01ccb0a85d2d359ef05c/cores/esp8266/core_esp8266_wiring_digital.c
Added in: https://github.com/esp8266/Arduino/blob/4d70000595175ae23f2927f4e2f8ad6526720266/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(0, '0', '111', 'digitalWrite')]
Available in: https://github.com/esp8266/Arduino/blob/31a85397634222b867eb3e6b30c19052e7bb4eb7/cores/esp8266/core_esp8266_wiring_digital.c
Removed in: https://github.com/esp8266/Arduino/blob/d754597ec39558f3e76403ed9036ada4ab64050d/cores/esp8266/core_esp8266_wiring_digital.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
13

## Result number #46

### File name(s)
libraries/ESP8266WiFiMesh/src/EncryptedConnectionData.cpp

### Compare results

####Values changed
NEW:('sessionKey', '1', '147', 'uint64_t')
OLD:('sessionKey', '1', '146', 'uint64_t')
CHANGED:('sessionKey', '1', '146', 'uint64_t')
Version 1(new): https://github.com/esp8266/Arduino/blob/f059e5732272ca825577920e22122c7673058b9c/libraries/ESP8266WiFiMesh/src/EncryptedConnectionData.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/2ec2679d6eb55fc35d26a893b0a1e37a9da41170/libraries/ESP8266WiFiMesh/src/EncryptedConnectionData.cpp
####True or False Positive:
False
####Note:
[check] Line number change.

####Values added
Values: [('SHA256_NATURAL_LENGTH', '0', '132', 'uint64_t'), (8, '0', '131', 'uint64_t')]
Not available in: https://github.com/esp8266/Arduino/blob/2fef67dcb0bbcb5aaa6096b12c14c1d1a5994333/libraries/ESP8266WiFiMesh/src/EncryptedConnectionData.cpp
Added in: https://github.com/esp8266/Arduino/blob/962a23d253b2e0d8eb2e4be6fbaa442e9902d32b/libraries/ESP8266WiFiMesh/src/EncryptedConnectionData.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #47

### File name(s)
libraries/ESP8266WebServer/src/Parsing-impl.h

### Compare results

####Values removed
Values: [('NULL', '16', '546', 'String'), ('i', '0', '536', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/da138456a6394670540d19aa448c5291c35b2c02/libraries/ESP8266WebServer/src/Parsing-impl.h
Removed in: https://github.com/esp8266/Arduino/blob/c720c0d9e8db2a2911ddd797c0876d675f58ddfb/libraries/ESP8266WebServer/src/Parsing-impl.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #48

### File name(s)
libraries/ESP8266WebServer/src/Parsing.cpp
libraries/ESP8266WebServer/src/Parsing

### Compare results

####Values removed
Values: [('delay', '1', '51', 'readBytesWithTimeout'), (0, '0', '46', 'readBytesWithTimeout'), ('NULL', '16', '604', 'String'), ('i', '0', '594', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/libraries/ESP8266WebServer/src/Parsing.cpp
Removed in: https://github.com/esp8266/Arduino/blob/7036297920934979fd5c3cd00b2527d52037d9af/libraries/ESP8266WebServer/src/Parsing
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('NULL', '16', '598', 'String'), ('i', '0', '588', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/64dd492eaa09746031605ef48dc465713f38ccf8/libraries/ESP8266WebServer/src/Parsing.cpp
Removed in: https://github.com/esp8266/Arduino/blob/a063c2b36f84721ca7418df5b05fe5f73380a1e9/libraries/ESP8266WebServer/src/Parsing.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('delay', '1', '41', 'readBytesWithTimeout'), ('dataLength', '0', '37', 'readBytesWithTimeout'), ('NULL', '16', '568', 'String'), ('i', '0', '558', 'String')]
Not available in: https://github.com/esp8266/Arduino/blob/b72cf2cdcf178d844cc0019d60e414f85e20a2b1/libraries/ESP8266WebServer/src/Parsing.cpp
Added in: https://github.com/esp8266/Arduino/blob/f6516b004fca47a06ddcb3789434fc201d926566/libraries/ESP8266WebServer/src/Parsing.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('NULL', '16', '519', 'String'), ('i', '0', '509', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/34fcc911bc57840ff667a12b8ee92cf238722595/libraries/ESP8266WebServer/src/Parsing.cpp
Removed in: https://github.com/esp8266/Arduino/blob/319caba2403c9f5680180449bc6165f35842541a/libraries/ESP8266WebServer/src/Parsing.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_uploadWriteByte', '13', '451', 'ESP8266WebServer'), ('i', '0', '443', 'ESP8266WebServer'), ('_uploadWriteByte', '10', '440', 'ESP8266WebServer'), ('_uploadWriteByte', '13', '439', 'ESP8266WebServer'), ('readStringUntil', '13', '429', 'ESP8266WebServer'), ('_uploadWriteByte', '10', '407', 'ESP8266WebServer'), ('_uploadWriteByte', '13', '406', 'ESP8266WebServer'), ('_uploadWriteByte', '10', '400', 'ESP8266WebServer'), ('_uploadWriteByte', '13', '399', 'ESP8266WebServer'), ('indexOf', '2', '339', 'ESP8266WebServer'), ('length', '1', '321', 'ESP8266WebServer'), ('length', '1', '319', 'ESP8266WebServer'), ('nameStart', '2', '316', 'ESP8266WebServer'), ('postArgsLen', '0', '303', 'ESP8266WebServer'), ('RequestArgument', '32', '302', 'ESP8266WebServer'), ('retry', '0', '293', 'ESP8266WebServer')]
Available in: https://github.com/esp8266/Arduino/blob/eb8c1faa5165db4ef79ac0751a152257365a4165/libraries/ESP8266WebServer/src/Parsing.cpp
Removed in: https://github.com/esp8266/Arduino/blob/b4cc0c263eff9c392ba22445e49ffa04fb2326f6/libraries/ESP8266WebServer/src/Parsing.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('retry', '0', '257', 'ESP8266WebServer')]
Not available in: https://github.com/esp8266/Arduino/blob/559670baaa7a4c4ab17777130ee1e1d5c795e26a/libraries/ESP8266WebServer/src/Parsing.cpp
Added in: https://github.com/esp8266/Arduino/blob/278c980ed81c39501699ef7e93deaced9a3f5e5f/libraries/ESP8266WebServer/src/Parsing.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_uploadWriteByte', '13', '337', 'ESP8266WebServer'), ('indexOf', '2', '277', 'ESP8266WebServer'), ('length', '1', '259', 'ESP8266WebServer'), ('length', '1', '257', 'ESP8266WebServer'), ('nameStart', '2', '254', 'ESP8266WebServer'), ('postArgsLen', '0', '241', 'ESP8266WebServer'), ('RequestArgument', '32', '240', 'ESP8266WebServer')]
Not available in: https://github.com/esp8266/Arduino/blob/36d0968ada0413dd74fc082d6aebd12e7a059ab7/libraries/ESP8266WebServer/src/Parsing.cpp
Added in: https://github.com/esp8266/Arduino/blob/0897f9e2e31dc61e54a9b25dd9f2cf0395aa8992/libraries/ESP8266WebServer/src/Parsing.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
7

## Result number #49

### File name(s)
cores/esp8266/Print.cpp

### Compare results

####Values removed
Values: [('n', '0', '271', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/759ba27b62f4531d83df782a4f3c0bfc6e1c6754/cores/esp8266/Print.cpp
Removed in: https://github.com/esp8266/Arduino/blob/f762721603489a0f1741604a71835620253f6c43/cores/esp8266/Print.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #50

### File name(s)
libraries/ESP8266WiFiMesh/src/FloodingMesh.cpp

### Compare results

####Values removed
Values: [('messageIDEndIndex', '1', '372', 'String'), (6, '0', '369', 'String'), ('broadcastTargetEndIndex', '1', '353', 'String'), ('broadcastTargetEndIndex', '1', '352', 'String'), ('metadataDelimiter', '1', '347', 'String')]
Available in: https://github.com/esp8266/Arduino/blob/2fef67dcb0bbcb5aaa6096b12c14c1d1a5994333/libraries/ESP8266WiFiMesh/src/FloodingMesh.cpp
Removed in: https://github.com/esp8266/Arduino/blob/962a23d253b2e0d8eb2e4be6fbaa442e9902d32b/libraries/ESP8266WiFiMesh/src/FloodingMesh.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:metadataDelimiter
OLD:broadcastMetadataDelimiter
CHANGED:('broadcastMetadataDelimiter', '1', '347', 'String')
Version 1(new): https://github.com/esp8266/Arduino/blob/2fef67dcb0bbcb5aaa6096b12c14c1d1a5994333/libraries/ESP8266WiFiMesh/src/FloodingMesh.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/3132325bf8b3116b2b974dcac26d2509606bb0b1/libraries/ESP8266WiFiMesh/src/FloodingMesh.cpp
####True or False Positive:
False
####Note:
[check] Name change.

### Number of warnings:
2

## Result number #51

### File name(s)
cores/esp8266/Schedule.cpp

### Compare results

####Values changed
NEW:('optimistic_yield', '100000', '165', 'run_scheduled_functions')
OLD:('yieldNow', '100', '138', 'run_scheduled_functions')
CHANGED:('yieldNow', '100', '138', 'run_scheduled_functions')
Version 1(new): https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/Schedule.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/59315836f283cf8eb56f7fea7cdcf0f79b3799e9/cores/esp8266/Schedule.cpp
####True or False Positive:
False
####Note:
Change in function structure.

####Values added
Values: [('yieldNow', '100', '148', 'run_scheduled_recurrent_functions')]
Not available in: https://github.com/esp8266/Arduino/blob/3f35506684599f9b55853666b92f61fcb036e189/cores/esp8266/Schedule.cpp
Added in: https://github.com/esp8266/Arduino/blob/6e51ef0cc8a17706b8981999bfb64e1b039726ee/cores/esp8266/Schedule.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #52

### File name(s)
cores/esp8266/core_esp8266_sigma_delta.c

### Compare results

####Values removed
Values: [('target', '1', '185', 'ICACHE_FLASH_ATTR'), ('prescale', '0', '183', 'ICACHE_FLASH_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/900083e3ffa87e3babd1934b9fac750d15c44213/cores/esp8266/core_esp8266_sigma_delta.c
Removed in: https://github.com/esp8266/Arduino/blob/4c8da955863c47faf3f0b24cecc1d89acd97d621/cores/esp8266/core_esp8266_sigma_delta.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #53

### File name(s)
libraries/SPISlave/src/hspi_slave.c

### Compare results

####Values removed
Values: [('out', '0', '129', 'hspi_slave_setData')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/libraries/SPISlave/src/hspi_slave.c
Removed in: https://github.com/esp8266/Arduino/blob/b4c28e74d66c5386f0b540379050d62bfbd0d4ca/libraries/SPISlave/src/hspi_slave.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('out', '0', '129', 'hspi_slave_setData'), (0, '32', '66', 'ICACHE_RAM_ATTR'), (24, '255', '64', 'ICACHE_RAM_ATTR'), (16, '255', '63', 'ICACHE_RAM_ATTR'), (8, '255', '62', 'ICACHE_RAM_ATTR'), ('data', '255', '61', 'ICACHE_RAM_ATTR'), (32, '0', '58', 'ICACHE_RAM_ATTR'), ('out', '0', '135', 'hspi_slave_setData')]
Available in: https://github.com/esp8266/Arduino/blob/891113678c0498298bb82a2849e7d2bd87138c92/libraries/SPISlave/src/hspi_slave.c
Removed in: https://github.com/esp8266/Arduino/blob/13589b1ce91343db9a1c3cebf5d9429a89919636/libraries/SPISlave/src/hspi_slave.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('SPI1S', '0', '111', 'hspi_slave_end'), ('out', '0', '125', 'hspi_slave_setData')]
Not available in: https://github.com/esp8266/Arduino/blob/f9ac524b13348e18a1ceb00261d947d6c1e0f9b5/libraries/SPISlave/src/hspi_slave.c
Added in: https://github.com/esp8266/Arduino/blob/891113678c0498298bb82a2849e7d2bd87138c92/libraries/SPISlave/src/hspi_slave.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('out', '0', '109', 'hspi_slave_setData')]
Available in: https://github.com/esp8266/Arduino/blob/217ba9e0726e23f5a25c8159da621f0696fd7939/libraries/SPISlave/src/hspi_slave.c
Removed in: https://github.com/esp8266/Arduino/blob/f9ac524b13348e18a1ceb00261d947d6c1e0f9b5/libraries/SPISlave/src/hspi_slave.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('status_len', '1', '81', 'hspi_slave_begin'), ('status_len', '4', '78', 'hspi_slave_begin')]
Not available in: https://github.com/esp8266/Arduino/blob/4217e49b548bf613eb1ee042cc38797f67009af2/libraries/SPISlave/src/hspi_slave.c
Added in: https://github.com/esp8266/Arduino/blob/217ba9e0726e23f5a25c8159da621f0696fd7939/libraries/SPISlave/src/hspi_slave.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
5

## Result number #54

### File name(s)
bootloaders/eboot/eboot.c

### Compare results

####Values removed
Values: [(1, '0', '282', 'main'), (0, '0', '263', 'main'), ('args', '2', '259', 'main'), (1, '0', '255', 'main'), ('v', '2', '253', 'main'), (0, '0', '246', 'main'), ('S', '0', '239', 'main'), ('print_version', '0', '225', 'main'), ('res', '9', '221', 'main')]
Available in: https://github.com/esp8266/Arduino/blob/8b662ed3b345d2ded3c2ac484949b03e10bdc43c/bootloaders/eboot/eboot.c
Removed in: https://github.com/esp8266/Arduino/blob/07b4c09b901504c64e23db7712923540b36c379a/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(1, '0', '280', 'main'), ('e', '2', '278', 'main'), (0, '0', '261', 'main'), (1, '0', '253', 'main'), ('v', '2', '251', 'main'), ('args', '2', '241', 'main'), ('S', '0', '237', 'main'), ('fmt', '5', '36', 'print_version'), ('fmt', '4', '35', 'print_version'), ('fmt', '3', '34', 'print_version'), ('fmt', '1', '32', 'print_version'), ('fmt', '0', '31', 'print_version'), ('fmt', '7', '30', 'print_version')]
Available in: https://github.com/esp8266/Arduino/blob/cf1b8e067a35bf31ac1f41e9f31163e71c151109/bootloaders/eboot/eboot.c
Removed in: https://github.com/esp8266/Arduino/blob/bbc14c0979abe50349c223d2717ca8e5be6a9a96/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('buff', '4', '101', 'uint8_t'), ('buff', '4', '103', 'uint8_t'), ('SPI0C', '15377171', '256', 'main'), ('SPI0CLK', '12355', '255', 'main'), ('flashinfo', '0', '245', 'main'), ('spi_flash_get_id', '255', '243', 'main'), ('print_version', '0', '222', 'main'), ('res', '9', '218', 'main')]
Available in: https://github.com/esp8266/Arduino/blob/ea879b6ef64fb3be4f1d1337dd248025eb9d9ee2/bootloaders/eboot/eboot.c
Removed in: https://github.com/esp8266/Arduino/blob/51daecc236fbff0d1ed30a9c63a3af6e8b5c7392/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('buff', '4', '103', 'uint8_t'), ('SPI0CLK', '8194', '261', 'main'), ('SPI0C', '15377171', '256', 'main'), ('SPI0CLK', '12355', '255', 'main'), ('flashinfo', '0', '245', 'main'), ('spi_flash_get_id', '255', '243', 'main'), ('print_version', '0', '222', 'main'), ('res', '9', '218', 'main'), ('buff', '4', '101', 'uint8_t')]
Available in: https://github.com/esp8266/Arduino/blob/9985a32914f16bea727769d73e288f9a3a4621fd/bootloaders/eboot/eboot.c
Removed in: https://github.com/esp8266/Arduino/blob/9b41d9ac5e50e7726010120fe9c265a8df1d7eea/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:0
OLD:6
CHANGED:('fmt', '6', '37', 'print_version')
Version 1(new): https://github.com/esp8266/Arduino/blob/9985a32914f16bea727769d73e288f9a3a4621fd/bootloaders/eboot/eboot.c
Version 2(old): https://github.com/esp8266/Arduino/blob/1d0bc5efdf7e175608cc1c038b592b511143ed26/bootloaders/eboot/eboot.c
####True or False Positive:
False
####Note:
Added missing ``.

####Values added
Values: [('buff', '4', '101', 'uint8_t'), ('aligned', '4', '101', 'uint8_t'), ('i', '255', '178', 'copy_raw'), ('size', '4', '139', 'copy_raw'), ('buffer_size', '1', '130', 'copy_raw'), ('args', '0', '230', 'main'), ('args', '2', '215', 'main'), ('print_version', '0', '199', 'main'), ('res', '9', '195', 'main')]
Not available in: https://github.com/esp8266/Arduino/blob/5b500e4e34ecae3d5aaa61604f8a45326150b022/bootloaders/eboot/eboot.c
Added in: https://github.com/esp8266/Arduino/blob/1d0bc5efdf7e175608cc1c038b592b511143ed26/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('buffer_size', '1', '104', 'copy_raw'), ('args', '0', '160', 'main'), ('args', '2', '149', 'main'), ('print_version', '0', '133', 'main'), ('res', '9', '130', 'main')]
Not available in: https://github.com/esp8266/Arduino/blob/cef5abd3cf0fa46583cd30a1f700f39bc82a2e4f/bootloaders/eboot/eboot.c
Added in: https://github.com/esp8266/Arduino/blob/32bd42b0281237d29e18bb769afad02bc6782a64/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('args', '2', '127', 'main')
OLD:('args', '2', '133', 'main')
CHANGED:('args', '2', '133', 'main')
Version 1(new): https://github.com/esp8266/Arduino/blob/f3f500936d831be890a62a959e21ceff4fd246ef/bootloaders/eboot/eboot.c
Version 2(old): https://github.com/esp8266/Arduino/blob/73740d6e6d5c0a684438d73a78d319c4c3cd5686/bootloaders/eboot/eboot.c
####True or False Positive:
False
####Note:
[check] Line number change.

####Values changed
NEW:('res', '9', '120', 'main')
OLD:('res', '9', '153', 'main')
CHANGED:('res', '9', '153', 'main')
Version 1(new): https://github.com/esp8266/Arduino/blob/73740d6e6d5c0a684438d73a78d319c4c3cd5686/bootloaders/eboot/eboot.c
Version 2(old): https://github.com/esp8266/Arduino/blob/bdf24031ebf5435834ee854e04c0d8c0e2da6a8a/bootloaders/eboot/eboot.c
####True or False Positive:
False
####Note:
[check] Line number change.

####Values added
Values: [('res', '9', '153', 'main')]
Not available in: https://github.com/esp8266/Arduino/blob/d5b578b161bc7d63f6e9c1bd942b602d2dc59f87/bootloaders/eboot/eboot.c
Added in: https://github.com/esp8266/Arduino/blob/bdf24031ebf5435834ee854e04c0d8c0e2da6a8a/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('load_app_from_flash_raw', '0', '166', 'main'), ('args', '2', '159', 'main')]
Not available in: https://github.com/esp8266/Arduino/blob/48e0d44860f338af6106988ffc296982c43c5bdf/bootloaders/eboot/eboot.c
Added in: https://github.com/esp8266/Arduino/blob/d5b578b161bc7d63f6e9c1bd942b602d2dc59f87/bootloaders/eboot/eboot.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
11

## Result number #55

### File name(s)
variants/wifio/WifioWiring.cpp

### Compare results

####Values changed
NEW:twi_setClock
OLD:i2c_freq
CHANGED:('i2c_freq', '100000', '118', 'initVariant')
Version 1(new): https://github.com/esp8266/Arduino/blob/fbec557ddb12ad6663bd387a2980197dca79e576/variants/wifio/WifioWiring.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/ad216c0ef57d4e3c26ef4f0f927b4cf3aa440146/variants/wifio/WifioWiring.cpp
####True or False Positive:
False
####Note:
[check] Name var change.

### Number of warnings:
1

## Result number #56

### File name(s)
cores/esp8266/umm_malloc/umm_local.c

### Compare results

####Values removed
Values: [('fmt', '1', '212', 'ICACHE_FLASH_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/8b662ed3b345d2ded3c2ac484949b03e10bdc43c/cores/esp8266/umm_malloc/umm_local.c
Removed in: https://github.com/esp8266/Arduino/blob/da6ec83b5fdbd5b02f04cf143dcf8e158a8cfd36/cores/esp8266/umm_malloc/umm_local.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('fmt', '1', '209', 'ICACHE_FLASH_ATTR')]
Not available in: https://github.com/esp8266/Arduino/blob/b26388812a52218041c470652805bdca7fd0d320/cores/esp8266/umm_malloc/umm_local.c
Added in: https://github.com/esp8266/Arduino/blob/e815b9219bee129f470a16c748117a59cfe45d96/cores/esp8266/umm_malloc/umm_local.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #57

### File name(s)
cores/esp8266/spiffs_api.cpp

### Compare results

####Values removed
Values: [('mode', '0', '439', 'FileImplPtr'), ('mode', '0', '429', 'FileImplPtr'), ('mode', '0', '474', 'getSpiffsMode')]
Available in: https://github.com/esp8266/Arduino/blob/1d5d1c18c6609f79fbc640fc978fb05b0755c253/cores/esp8266/spiffs_api.cpp
Removed in: https://github.com/esp8266/Arduino/blob/1f32b7f66e22c5c26a54328e4f0997db369a9cbb/cores/esp8266/spiffs_api.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_stat', '0', '322', '_getStat')]
Not available in: https://github.com/esp8266/Arduino/blob/cd9791eebe3e927e95cd148267549a6790c63abc/cores/esp8266/spiffs_api.cpp
Added in: https://github.com/esp8266/Arduino/blob/f4bd97e8eeb16c40c05a9721f2fa65691179896a/cores/esp8266/spiffs_api.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('mode', '0', '401', 'getSpiffsMode')]
Not available in: https://github.com/esp8266/Arduino/blob/98423fa79daf3160946deec8afb597094e2f7876/cores/esp8266/spiffs_api.cpp
Added in: https://github.com/esp8266/Arduino/blob/041f971a8b59bfe23281514cf625ffc3f714ecc8/cores/esp8266/spiffs_api.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #58

### File name(s)
libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp

### Compare results

####Values removed
Values: [('wifi_fpm_do_sleep', '268435455', '876', 'ESP8266WiFiGenericClass')]
Available in: https://github.com/esp8266/Arduino/blob/3ff573103ba0db669152afc2fe9c60a4be826b33/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
Removed in: https://github.com/esp8266/Arduino/blob/1cc6960a5516afb8b244e87574a57986101247bb/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('mac', '6', '195', 'WiFiEventHandler')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
Removed in: https://github.com/esp8266/Arduino/blob/273f4000f0dcb936e457cba3e71d824a7dfb9007/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('wifi_fpm_do_sleep', '268435455', '600', 'ESP8266WiFiGenericClass')
OLD:('uint32_t', '0', '533', 'ESP8266WiFiGenericClass')
CHANGED:('uint32_t', '0', '533', 'ESP8266WiFiGenericClass')
Version 1(new): https://github.com/esp8266/Arduino/blob/216680bb576d845547349ab992043c6d6f83fe73/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/5c4db3acf4353870b6a5663ba06d712d67e6c179/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
####True or False Positive:
Incorrect
####Note:
[check] Different vars.

####Values added
Values: [('mac', '6', '179', 'WiFiEventHandler'), ('', '0', '', 'WiFiEventHandler')]
Not available in: https://github.com/esp8266/Arduino/blob/3e9dede14ef980880387d504512a338d52051e69/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
Added in: https://github.com/esp8266/Arduino/blob/de166c9dd73bd1da0baa35b2a62695035196018a/libraries/ESP8266WiFi/src/ESP8266WiFiGeneric.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #59

### File name(s)
variants/wifio/WifioProtocol.h

### Compare results

####Values removed
Values: [('delayMicroseconds', '10', '133', 'expectCommand'), ('t', '0', '127', 'expectCommand'), ('nIt', '0', '126', 'expectCommand')]
Available in: https://github.com/esp8266/Arduino/blob/14e500ac675cbc9dbdd2416e7219015e67dcc96e/variants/wifio/WifioProtocol.h
Removed in: https://github.com/esp8266/Arduino/blob/045c446213a57aa350c7527cc2b90b29425bc58c/variants/wifio/WifioProtocol.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #60

### File name(s)
cores/esp8266/abi.cpp

### Compare results

####Values added
Values: [('xt_rsil', '15', '74', '__cxa_guard_acquire')]
Not available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/abi.cpp
Added in: https://github.com/esp8266/Arduino/blob/82a1382864a621eaabe934a42797b6ebccdf6c9f/cores/esp8266/abi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('xt_rsil', '15', '81', '__cxa_guard_acquire')]
Available in: https://github.com/esp8266/Arduino/blob/0713a01db885e831c8e2c606287ef5c4e78242f7/cores/esp8266/abi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/6280e98b0360f85fdac2b8f10707fffb4f6e6e31/cores/esp8266/abi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('xt_rsil', '15', '81', '__cxa_guard_acquire')]
Not available in: https://github.com/esp8266/Arduino/blob/2126146e20042878026f03a19107555f32e3431c/cores/esp8266/abi.cpp
Added in: https://github.com/esp8266/Arduino/blob/4a958c844401bbef880481fef38c5bec083f85be/cores/esp8266/abi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('xt_rsil', '15', '69', '__cxa_guard_acquire')]
Available in: https://github.com/esp8266/Arduino/blob/6fc141772c85d33640c32cea83bf7236ca64df7a/cores/esp8266/abi.cpp
Removed in: https://github.com/esp8266/Arduino/blob/737f6c28ea8c3d47d5c4fa3fd82da8657df17295/cores/esp8266/abi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('xt_rsil', '15', '69', '__cxa_guard_acquire')]
Not available in: https://github.com/esp8266/Arduino/blob/c6c7d2475059fff19f7127b0a4aba082c7ca7200/cores/esp8266/abi.cpp
Added in: https://github.com/esp8266/Arduino/blob/6fc141772c85d33640c32cea83bf7236ca64df7a/cores/esp8266/abi.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
5

## Result number #61

### File name(s)
cores/esp8266/Tone.cpp

### Compare results

####Values added
Values: [('duration', '1000', '42', '_startTone')]
Not available in: https://github.com/esp8266/Arduino/blob/1af4ea661f4123d6aa1df87d3e0eadaf93e4c918/cores/esp8266/Tone.cpp
Added in: https://github.com/esp8266/Arduino/blob/ea1fdb210f84fbed421340a1341376e179e4addb/cores/esp8266/Tone.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('microsecondsToClockCycles', '25', '40', '_startTone')
OLD:('uint32_t', '25', '39', '_startTone')
CHANGED:('uint32_t', '25', '39', '_startTone')
Version 1(new): https://github.com/esp8266/Arduino/blob/1af4ea661f4123d6aa1df87d3e0eadaf93e4c918/cores/esp8266/Tone.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/c548958f6ebbf372e3771e8a9012a5faab34d73b/cores/esp8266/Tone.cpp
####True or False Positive:
False
####Note:
Changed from line 39 to 38, added `microsecondsToClockCycles`.

####Values changed
NEW:25
OLD:100
CHANGED:('uint32_t', '100', '39', '_startTone')
Version 1(new): https://github.com/esp8266/Arduino/blob/c548958f6ebbf372e3771e8a9012a5faab34d73b/cores/esp8266/Tone.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/Tone.cpp
####True or False Positive:
True
####Note:
Changed low period frequency.

####Values removed
Values: [(2.0, '0.5', '66', 'tone')]
Available in: https://github.com/esp8266/Arduino/blob/ebda795f34e6d09f5676782f0917ad298d9a9cdd/cores/esp8266/Tone.cpp
Removed in: https://github.com/esp8266/Arduino/blob/be7a732b9d92f4a52c1df699429b81b638661a9c/cores/esp8266/Tone.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('i', '255', '115', 'noTone'), ('T1INDEX', '1', '130', 'ICACHE_RAM_ATTR'), ('T1INDEX', '2', '126', 'ICACHE_RAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/a4448989009a4193f11852be5e8d49e85b6b817a/cores/esp8266/Tone.cpp
Removed in: https://github.com/esp8266/Arduino/blob/ebda795f34e6d09f5676782f0917ad298d9a9cdd/cores/esp8266/Tone.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:ICACHE_RAM_ATTR
OLD:t1IntHandler
CHANGED:('T1INDEX', '1', '123', 't1IntHandler')
Version 1(new): https://github.com/esp8266/Arduino/blob/748f3f93fa18b9e057e91e542d3e432296df5205/cores/esp8266/Tone.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/4b55ee14efcbd05d8c2162db1f347f465da73b87/cores/esp8266/Tone.cpp
####True or False Positive:
False
####Note:
[check] Added linker attributes to function.

####Values added
Values: [('T1INDEX', '1', '123', 't1IntHandler')]
Not available in: https://github.com/esp8266/Arduino/blob/7beda37da1ae1df6a132abfa21b5b5cd43bea4b8/cores/esp8266/Tone.cpp
Added in: https://github.com/esp8266/Arduino/blob/4b55ee14efcbd05d8c2162db1f347f465da73b87/cores/esp8266/Tone.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
7

## Result number #62

### File name(s)
libraries/ESP8266WebServer/src/ESP8266WebServer.h

### Compare results

####Values removed
Values: [('contentLength', '0', '215', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/7a368747e0c15ff3578547ea7bb040701f43fd0a/libraries/ESP8266WebServer/src/ESP8266WebServer.h
Removed in: https://github.com/esp8266/Arduino/blob/c720c0d9e8db2a2911ddd797c0876d675f58ddfb/libraries/ESP8266WebServer/src/ESP8266WebServer.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('', '0', '', 'addHook')]
Not available in: https://github.com/esp8266/Arduino/blob/c18f7cb1e6077908165bb9c260473432fd5e8720/libraries/ESP8266WebServer/src/ESP8266WebServer.h
Added in: https://github.com/esp8266/Arduino/blob/33083861c80bbcd5904f017ce7aa1b81df610679/libraries/ESP8266WebServer/src/ESP8266WebServer.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('delay', '1', '104', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/866ab26433a33c578601d512d28bb2810bd55186/libraries/ESP8266WebServer/src/ESP8266WebServer.h
Removed in: https://github.com/esp8266/Arduino/blob/8fdb824e11d4d74100f3f43bd5cecb42b8894da4/libraries/ESP8266WebServer/src/ESP8266WebServer.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #63

### File name(s)
libraries/ESP8266httpUpdate/src/ESP8266httpUpdate.cpp

### Compare results

####Values changed
NEW:(240, '4', '283', 'HTTPUpdateResult')
OLD:(240, '4', '280', 't_httpUpdate_return')
CHANGED:(240, '4', '280', 't_httpUpdate_return')
Version 1(new): https://github.com/esp8266/Arduino/blob/bf7f33d91847ef301b46e4842a253090bc59a62b/libraries/ESP8266httpUpdate/src/ESP8266httpUpdate.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/c450023a321c4f375336e0ff56b833e7e3c5ca0d/libraries/ESP8266httpUpdate/src/ESP8266httpUpdate.cpp
####True or False Positive:
False
####Note:
[check] Changed line number and function name.

####Values added
Values: [('buf', '4', '241', 't_httpUpdate_return'), ('delay', '100', '229', 't_httpUpdate_return')]
Not available in: https://github.com/esp8266/Arduino/blob/02e6b2fc16c02c61df593abce759d8b2ce42ed63/libraries/ESP8266httpUpdate/src/ESP8266httpUpdate.cpp
Added in: https://github.com/esp8266/Arduino/blob/5a4ced251d5937065ec8ee6e58352f4e5a1892d1/libraries/ESP8266httpUpdate/src/ESP8266httpUpdate.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #64

### File name(s)
cores/esp8266/hwdt_app_entry.cpp

### Compare results

####Values changed
NEW:sp_suspend
OLD:sp_yield
CHANGED:('sp_yield', '8', '956', 'STATIC')
Version 1(new): https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/hwdt_app_entry.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/8a42163a50e97fddd2dd1d7522fbe6bfc5eeb929/cores/esp8266/hwdt_app_entry.cpp
####True or False Positive:
False
####Note:
Usage of `sp_suspend` vs  `sp_yield`.

### Number of warnings:
1

## Result number #65

### File name(s)
cores/esp8266/IPAddress.cpp

### Compare results

####Values added
Values: [('acc', '0', '184', 'IPAddress'), ('count0', '8', '136', 'size_t'), ('count0', '0', '129', 'size_t'), ('n', '0', '122', 'size_t')]
Not available in: https://github.com/esp8266/Arduino/blob/241531aa4c237ed61e4b6605d7dcf539fdf90d2c/cores/esp8266/IPAddress.cpp
Added in: https://github.com/esp8266/Arduino/blob/5c4db3acf4353870b6a5663ba06d712d67e6c179/cores/esp8266/IPAddress.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:String
OLD:IPAddress
CHANGED:('bytes', '0', '70', 'IPAddress')
Version 1(new): https://github.com/esp8266/Arduino/blob/b28e879af6d544152bba7125364405439c578617/cores/esp8266/IPAddress.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/664d92fbd04cabfdf21e96f5cf174219db64ada4/cores/esp8266/IPAddress.cpp
####True or False Positive:
False
####Note:
Changed return type.

####Values added
Values: [('bytes', '0', '70', 'IPAddress'), ('szRet', '20', '69', 'IPAddress')]
Not available in: https://github.com/esp8266/Arduino/blob/f165a0afcdadcfd392fc1f7adef27b2cc2d7748d/cores/esp8266/IPAddress.cpp
Added in: https://github.com/esp8266/Arduino/blob/664d92fbd04cabfdf21e96f5cf174219db64ada4/cores/esp8266/IPAddress.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #66

### File name(s)
cores/esp8266/libb64/cdecode.c

### Compare results

####Values changed
NEW:('len', '0', '85', 'base64_decode_chars_signed')
OLD:('len', '0', '84', 'base64_decode_chars')
CHANGED:('len', '0', '84', 'base64_decode_chars')
Version 1(new): https://github.com/esp8266/Arduino/blob/d85e78380647246d76cbe63be2af3025642f8f10/cores/esp8266/libb64/cdecode.c
Version 2(old): https://github.com/esp8266/Arduino/blob/bda06d686c06be9a94771bb4d29538af32d7ccf7/cores/esp8266/libb64/cdecode.c
####True or False Positive:
False
####Note:
[check] Line number change.

### Number of warnings:
1

## Result number #67

### File name(s)
cores/esp8266/umm_malloc/umm_malloc.cpp

### Compare results

####Values removed
Values: [('prevBlockSize', '0', '874', 'umm_realloc')]
Available in: https://github.com/esp8266/Arduino/blob/e6fc76ab5f788c33a16bfd6bc55c97eb3fd9032b/cores/esp8266/umm_malloc/umm_malloc.cpp
Removed in: https://github.com/esp8266/Arduino/blob/7356cd1ef13c7a7da4631be01060f6f40806fa23/cores/esp8266/umm_malloc/umm_malloc.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('nextBlockSize', '0', '834', 'umm_realloc')
OLD:('nextBlockSize', '0', '565', 'umm_realloc')
CHANGED:('nextBlockSize', '0', '565', 'umm_realloc')
Version 1(new): https://github.com/esp8266/Arduino/blob/8b662ed3b345d2ded3c2ac484949b03e10bdc43c/cores/esp8266/umm_malloc/umm_malloc.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/b26388812a52218041c470652805bdca7fd0d320/cores/esp8266/umm_malloc/umm_malloc.cpp
####True or False Positive:
False
####Note:
[check] Line number change.

####Values removed
Values: [('c', '0', '725', 'umm_realloc'), ('UMM_NFREE', '0', '393', 'umm_malloc_core'), ('c', '0', '657', 'umm_realloc'), ('c', '0', '645', 'umm_realloc'), ('nextBlockSize', '0', '524', 'umm_realloc'), ('prevBlockSize', '0', '523', 'umm_realloc')]
Available in: https://github.com/esp8266/Arduino/blob/7a43092df0c8734577870f5630ee0062150c1074/cores/esp8266/umm_malloc/umm_malloc.cpp
Removed in: https://github.com/esp8266/Arduino/blob/83523c025903412e8d5184febc274a48a9a3a3e7/cores/esp8266/umm_malloc/umm_malloc.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('block_0th', '0', '1289', 'ICACHE_FLASH_ATTR'), ('c', '0', '1420', '_umm_free'), ('c', '0', '1419', '_umm_free'), ('c', '0', '1395', '_umm_free'), ('UMM_NFREE', '0', '1394', '_umm_free'), ('bestSize', '32767', '1477', '_umm_malloc'), ('UMM_NFREE', '0', '1476', '_umm_malloc'), ('UMM_NFREE', '0', '1474', '_umm_malloc'), ('blockSize', '0', '1434', '_umm_malloc'), (0, '0', '1789', '_umm_realloc'), (0, '0', '1741', '_umm_realloc'), ('c', '0', '1732', '_umm_realloc'), ('__builtin_return_address', '0', '1844', 'umm_malloc'), ('__builtin_return_address', '0', '1875', 'umm_calloc'), ('__builtin_return_address', '0', '1904', 'umm_realloc')]
Available in: https://github.com/esp8266/Arduino/blob/127199ab6da2c57adc0fb3631d1ce6f7c8941b25/cores/esp8266/umm_malloc/umm_malloc.cpp
Removed in: https://github.com/esp8266/Arduino/blob/7a43092df0c8734577870f5630ee0062150c1074/cores/esp8266/umm_malloc/umm_malloc.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #68

### File name(s)
cores/esp8266/umm_malloc/umm_malloc.c

### Compare results

####Values removed
Values: [('blockNo', '0', '982', 'ICACHE_FLASH_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/ce28a76a24beb9216f245d33336d97b5d8d83ebf/cores/esp8266/umm_malloc/umm_malloc.c
Removed in: https://github.com/esp8266/Arduino/blob/8e46a3371d73cb43deb70ac088e6337b74bfe50e/cores/esp8266/umm_malloc/umm_malloc.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('c', '0', '1314', '_umm_free'), ('UMM_NFREE', '0', '1388', '_umm_malloc'), ('c', '0', '1335', '_umm_free'), ('UMM_NFREE', '0', '1386', '_umm_malloc'), ('NULL', '0', '1760', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/4a958c844401bbef880481fef38c5bec083f85be/cores/esp8266/umm_malloc/umm_malloc.c
Removed in: https://github.com/esp8266/Arduino/blob/ce28a76a24beb9216f245d33336d97b5d8d83ebf/cores/esp8266/umm_malloc/umm_malloc.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('__builtin_return_address', '0', '1700', 'umm_calloc'), ('__builtin_return_address', '0', '1729', 'umm_realloc'), ('NULL', '0', '1760', 'size_t')]
Not available in: https://github.com/esp8266/Arduino/blob/589eb29eb322b12976b6bc64761372123838d60c/cores/esp8266/umm_malloc/umm_malloc.c
Added in: https://github.com/esp8266/Arduino/blob/4a958c844401bbef880481fef38c5bec083f85be/cores/esp8266/umm_malloc/umm_malloc.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:ICACHE_FLASH_ATTR
OLD:umm_info
CHANGED:('blockNo', '0', '972', 'umm_info')
Version 1(new): https://github.com/esp8266/Arduino/blob/707c87fdb603744389aae575c4da12928eaff95b/cores/esp8266/umm_malloc/umm_malloc.c
Version 2(old): https://github.com/esp8266/Arduino/blob/339140c756cea6acc9c0c023477f054c6f9990bb/cores/esp8266/umm_malloc/umm_malloc.c
####True or False Positive:
False
####Note:
[check] Added linker attributes to function.

### Number of warnings:
4

## Result number #69

### File name(s)
libraries/ESP8266WiFiMesh/src/JsonTranslator.cpp

### Compare results

####Values added
Values: [('longResult', '0', '278', 'getMeshMessageCount')]
Not available in: https://github.com/esp8266/Arduino/blob/e64125a53c19bb210e357b806c8d4ee793d88ccd/libraries/ESP8266WiFiMesh/src/JsonTranslator.cpp
Added in: https://github.com/esp8266/Arduino/blob/2ec2679d6eb55fc35d26a893b0a1e37a9da41170/libraries/ESP8266WiFiMesh/src/JsonTranslator.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:getUnsynchronizedMessageID
OLD:getUnencryptedMessageID
CHANGED:('c_str', '0', '257', 'getUnencryptedMessageID')
Version 1(new): https://github.com/esp8266/Arduino/blob/962a23d253b2e0d8eb2e4be6fbaa442e9902d32b/libraries/ESP8266WiFiMesh/src/JsonTranslator.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/2fef67dcb0bbcb5aaa6096b12c14c1d1a5994333/libraries/ESP8266WiFiMesh/src/JsonTranslator.cpp
####True or False Positive:
False
####Note:
Changed function name.

####Values added
Values: [('endIndex', '1', '160', 'getConnectionState'), ('c_str', '0', '240', 'getDuration'), ('c_str', '0', '278', 'getDesync'), ('c_str', '0', '288', 'getUnencryptedMessageID'), ('longResult', '65535', '299', 'getMeshMessageCount'), ('c_str', '0', '298', 'getMeshMessageCount')]
Not available in: https://github.com/esp8266/Arduino/blob/d20177ae3553e90caaf90678b38b45e760f1ece1/libraries/ESP8266WiFiMesh/src/JsonTranslator.cpp
Added in: https://github.com/esp8266/Arduino/blob/f8ec4f1c72b9e48c882022bded6387df587ea076/libraries/ESP8266WiFiMesh/src/JsonTranslator.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #70

### File name(s)
libraries/GDBStub/src/internal/gdbstub.c

### Compare results

####Values removed
Values: [('doDebug', '1', '731', 'ATTR_GDBFN')]
Available in: https://github.com/esp8266/Arduino/blob/7f4dd52ed1f680865c1583da494a16ee630be8ab/libraries/GDBStub/src/internal/gdbstub.c
Removed in: https://github.com/esp8266/Arduino/blob/542b05e5436297456bff4dd2d84ef03d76f8d8b2/libraries/GDBStub/src/internal/gdbstub.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #71

### File name(s)
cores/esp8266/MD5Builder.cpp

### Compare results

####Values changed
NEW:33
OLD:32
CHANGED:('out', '32', '80', 'String')
Version 1(new): https://github.com/esp8266/Arduino/blob/77ab33f7bf2c7fdba04c0f1dc8a015a4dae2095c/cores/esp8266/MD5Builder.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/2cf902cb7655bb821b202aab4ef628e48582bb24/cores/esp8266/MD5Builder.cpp
####True or False Positive:
True
####Note:
[Recheck] Changed from line 80 to 79. Changed the size of `out`.

### Number of warnings:
1

## Result number #72

### File name(s)
libraries/ESP8266WiFi/src/include/ClientContext.h

### Compare results

####Values removed
Values: [('_rx_buf', '0', '586', '_consume')]
Available in: https://github.com/esp8266/Arduino/blob/f4178e58dcfe32ec1f4b7d9cfb31e3ad5559327a/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_datalen', '0', '485', 'size_t'), ('_rx_buf', '0', '317', 'discard_received'), ('_rx_buf_offset', '0', '319', 'discard_received')]
Available in: https://github.com/esp8266/Arduino/blob/0049090e488f74bb75f92643a0f1b5d60d1a48b0/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/f4178e58dcfe32ec1f4b7d9cfb31e3ad5559327a/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_rx_buf_offset', '0', '601', '_consume'), ('_rx_buf_offset', '0', '604', '_consume')]
Available in: https://github.com/esp8266/Arduino/blob/c720c0d9e8db2a2911ddd797c0876d675f58ddfb/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/3b1e8eab20a970318c5e611417dcadf8413c5171/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('_rx_buf_offset', '0', '576', '_consume')
OLD:('_rx_buf_offset', '0', '580', '_consume')
CHANGED:('_rx_buf_offset', '0', '580', '_consume')
Version 1(new): https://github.com/esp8266/Arduino/blob/2d58be744baeb2dd446ceb68762eb8465a09ddcc/libraries/ESP8266WiFi/src/include/ClientContext.h
Version 2(old): https://github.com/esp8266/Arduino/blob/e752e96e9fd63436b689aa3e6cb3010f27b55aae/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
False
####Note:
[check] Line number change.

####Values added
Values: [('_rx_buf', '0', '574', '_consume')]
Not available in: https://github.com/esp8266/Arduino/blob/240ae5ef264b7e3175e7e17b88848221c7588484/libraries/ESP8266WiFi/src/include/ClientContext.h
Added in: https://github.com/esp8266/Arduino/blob/e752e96e9fd63436b689aa3e6cb3010f27b55aae/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_rx_buf_offset', '0', '562', '_consume'), ('_connect_pending', '0', '138', 'connect'), ('_connect_pending', '1', '131', 'connect'), ('_rx_buf_offset', '0', '566', '_consume')]
Available in: https://github.com/esp8266/Arduino/blob/4bfa2ae8897471d3a0db81e5c6442ba86ac9228b/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/0937b076c8ac31d3dbfe7ed4ccc3a2efd7378396/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('delay', '1', '136', 'connect'), ('_rx_buf_offset', '0', '561', '_consume'), ('_rx_buf', '0', '560', '_consume'), ('_written', '0', '442', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/912c0db0910752d029d329ad20cbff8316a1db08/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/4bfa2ae8897471d3a0db81e5c6442ba86ac9228b/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_send_waiting', '0', '461', 'size_t'), ('_send_waiting', '0', '440', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/25c95ac185ab08f9c166e58b7e3f26ca440743f1/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('delay', '0', '336', 'wait_until_sent')]
Not available in: https://github.com/esp8266/Arduino/blob/e5493552215f279b0ca3c069d5ebcdfe06773d62/libraries/ESP8266WiFi/src/include/ClientContext.h
Added in: https://github.com/esp8266/Arduino/blob/561426c0c77e9d05708f2c4bf2a956d3552a3706/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_rx_buf_offset', '0', '554', '_consume')]
Not available in: https://github.com/esp8266/Arduino/blob/775eb9b34375daff2e301886815ddf91f3416df6/libraries/ESP8266WiFi/src/include/ClientContext.h
Added in: https://github.com/esp8266/Arduino/blob/5a5af55d3a9823e42fb4ba7c90c6d27beb11562c/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_send_waiting', '0', '440', 'size_t'), ('_rx_buf_offset', '0', '549', '_consume'), ('_send_waiting', '0', '460', 'size_t'), ('delay', '1', '333', 'wait_until_sent'), ('prevsndbuf', '1', '312', 'wait_until_sent'), ('_rx_buf_offset', '0', '553', '_consume')]
Available in: https://github.com/esp8266/Arduino/blob/83a8076db87b77de6a7b500c18b85057e38ed117/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/d0171574d857cfc8cb09a192ecbd541ebdbf08b3/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_rx_buf', '0', '547', '_consume')]
Not available in: https://github.com/esp8266/Arduino/blob/b08d282673055b4758cd73d3cd99573f619112a5/libraries/ESP8266WiFi/src/include/ClientContext.h
Added in: https://github.com/esp8266/Arduino/blob/83a8076db87b77de6a7b500c18b85057e38ed117/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_rx_buf', '0', '454', '_consume')]
Not available in: https://github.com/esp8266/Arduino/blob/5116a46f09a4c52c9a0e37665c2c1841bf00bfb0/libraries/ESP8266WiFi/src/include/ClientContext.h
Added in: https://github.com/esp8266/Arduino/blob/26980b39e35151117720220ef1d57f56a0a51acf/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_rx_buf_offset', '0', '438', '_consume'), ('_rx_buf', '0', '437', '_consume')]
Not available in: https://github.com/esp8266/Arduino/blob/7de81270a35e3867a5593e44c11f85a5c4b93e09/libraries/ESP8266WiFi/src/include/ClientContext.h
Added in: https://github.com/esp8266/Arduino/blob/eebcc656edcfae35494c7c11481cd377e96aac9d/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('_send_waiting', '0', '343', 'size_t'), ('_send_waiting', '0', '328', 'size_t'), ('_rx_buf_offset', '0', '414', '_consume'), ('_rx_buf_offset', '0', '408', '_consume')]
Available in: https://github.com/esp8266/Arduino/blob/a41f55c469dbf3ecfa3aa051fa95322d8d316e2e/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/7de81270a35e3867a5593e44c11f85a5c4b93e09/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('can_send', '0', '346', '_write_some')
OLD:('_rx_buf', '0', '210', 'flush')
CHANGED:('_rx_buf', '0', '210', 'flush')
Version 1(new): https://github.com/esp8266/Arduino/blob/8db4dcea426b2a1b7d1cca6d5bf4c351284f2240/libraries/ESP8266WiFi/src/include/ClientContext.h
Version 2(old): https://github.com/esp8266/Arduino/blob/a2b82ed6b6d74d271adf1759ae4bf945b7270adc/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
False
####Note:
[check] Different var.

####Values removed
Values: [('_rx_buf', '0', '190', '_consume'), ('_pcb', '0', '253', '_error')]
Available in: https://github.com/esp8266/Arduino/blob/8819c1e91ce22197ecb621606bad6d1ccfb707a2/libraries/ESP8266WiFi/src/include/ClientContext.h
Removed in: https://github.com/esp8266/Arduino/blob/88c6ee418d3a9129c53ea80f9de4e600939c1cd7/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_rx_buf_offset', '0', '152', 'flush'), ('_rx_buf', '0', '151', 'flush'), ('_rx_buf_offset', '0', '206', '_consume'), ('_rx_buf_offset', '0', '199', '_consume'), ('_rx_buf', '0', '198', '_consume'), ('_pcb', '0', '256', '_error')]
Not available in: https://github.com/esp8266/Arduino/blob/2328e07637cc8276bfcf336aeade694fe61084c8/libraries/ESP8266WiFi/src/include/ClientContext.h
Added in: https://github.com/esp8266/Arduino/blob/55f07f1e08868b855f2ae2fb3b7b42004ff8022f/libraries/ESP8266WiFi/src/include/ClientContext.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
18

## Result number #73

### File name(s)
libraries/ESP8266WiFiMesh/src/EspnowMeshBackend.cpp

### Compare results

####Values removed
Values: [('numberOfScheduledResponses', '2', '1477', 'std'), ('numberDeleted', '0', '1009', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/d01e6391bb7145a74c914cf024bc1dd5e3450cb9/libraries/ESP8266WiFiMesh/src/EspnowMeshBackend.cpp
Removed in: https://github.com/esp8266/Arduino/blob/40e1f02ffb8a762c2b5094cdbc9171d16d112655/libraries/ESP8266WiFiMesh/src/EspnowMeshBackend.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('numberDeleted', '0', '1001', 'size_t')]
Not available in: https://github.com/esp8266/Arduino/blob/a49f0470963a5282d87a6fe662ba55b1ab308c2d/libraries/ESP8266WiFiMesh/src/EspnowMeshBackend.cpp
Added in: https://github.com/esp8266/Arduino/blob/16801f3dacf5e913ffef0c53051b83a8d155413a/libraries/ESP8266WiFiMesh/src/EspnowMeshBackend.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [(6, '0', '972', 'transmission_status_t')]
Available in: https://github.com/esp8266/Arduino/blob/5834c547173d273def4a5337fac814a6856785c4/libraries/ESP8266WiFiMesh/src/EspnowMeshBackend.cpp
Removed in: https://github.com/esp8266/Arduino/blob/86025c788438427f9195b56f51ce40a8304de6d2/libraries/ESP8266WiFiMesh/src/EspnowMeshBackend.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
3

## Result number #74

### File name(s)
cores/esp8266/spiffs/spiffs_nucleus.c

### Compare results

####Values added
Values: [('i', '0', '2223', 'u32_t'), ('hash', '5381', '2221', 'u32_t')]
Not available in: https://github.com/esp8266/Arduino/blob/6a7551e1f02e17df62e7e5c3efeee7818f4ba33b/cores/esp8266/spiffs/spiffs_nucleus.c
Added in: https://github.com/esp8266/Arduino/blob/6ac48124bd10151cdbc5c1003e41e4483f8f1f11/cores/esp8266/spiffs/spiffs_nucleus.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #75

### File name(s)
cores/esp8266/cbuf.cpp

### Compare results

####Values changed
NEW:IRAM_ATTR
OLD:ICACHE_RAM_ATTR
CHANGED:('_begin', '1', '116', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/656a33e6f82482535782213a6e96c2bd49b22a39/cores/esp8266/cbuf.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/a16e1e5b8a700bfa0a886685d9d9f59e37fe406b/cores/esp8266/cbuf.cpp
####True or False Positive:
False
####Note:
[check] Changed linker attributes to function.

####Values removed
Values: [('_begin', '1', '35', 'ICACHE_RAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/9d7c2fd5be4c734d8915f91b821fdcd7602de055/cores/esp8266/cbuf.cpp
Removed in: https://github.com/esp8266/Arduino/blob/e2a73ef385cbaa77f1853149280e07059f368961/cores/esp8266/cbuf.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #76

### File name(s)
cores/esp8266/core_esp8266_i2s.cpp

### Compare results

####Values changed
NEW:IRAM_ATTR
OLD:ICACHE_RAM_ATTR
CHANGED:('SLC_BUF_LEN', '4', '174', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/656a33e6f82482535782213a6e96c2bd49b22a39/cores/esp8266/core_esp8266_i2s.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/e99df4fe1a86d5348379a27bd7d6d654cf26525b/cores/esp8266/core_esp8266_i2s.cpp
####True or False Positive:
False
####Note:
[check] Changed linker attributes to function.

####Values changed
NEW:('scd_div_best', '1', '457', 'i2s_set_rate')
OLD:('scd_div_best', '1', '448', 'i2s_set_rate')
CHANGED:('scd_div_best', '1', '448', 'i2s_set_rate')
Version 1(new): https://github.com/esp8266/Arduino/blob/e0cfb5a9950a05f245d3ff2573bf2272525c89e9/cores/esp8266/core_esp8266_i2s.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/1e016a4237fb3d4aa6304232067ed987b47a4e4a/cores/esp8266/core_esp8266_i2s.cpp
####True or False Positive:
False
####Note:
[check] Line number change.

####Values changed
NEW:('scd_div_best', '1', '448', 'i2s_set_rate')
OLD:('scd_div_best', '1', '447', 'i2s_set_rate')
CHANGED:('scd_div_best', '1', '447', 'i2s_set_rate')
Version 1(new): https://github.com/esp8266/Arduino/blob/1e016a4237fb3d4aa6304232067ed987b47a4e4a/cores/esp8266/core_esp8266_i2s.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/ec7644227ef19ebbf23a839154a878b7e9f7d577/cores/esp8266/core_esp8266_i2s.cpp
####True or False Positive:
False
####Note:
[check] Line number change.

####Values changed
NEW:save_rate
OLD:i2s_set_rate
CHANGED:('i2s_set_rate', '44100', '533', 'i2s_rxtx_begin')
Version 1(new): https://github.com/esp8266/Arduino/blob/19d09eae2b5ff9ed7cc48b5fa2c912d1297462b9/cores/esp8266/core_esp8266_i2s.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/core_esp8266_i2s.cpp
####True or False Positive:
False
####Note:
[check] Changed function name.

### Number of warnings:
4

## Result number #77

### File name(s)
cores/esp8266/core_esp8266_i2s.c

### Compare results

####Values removed
Values: [('I2SIC', '63', '274', 'i2s_begin'), ('_i2s_sample_rate', '0', '265', 'i2s_begin')]
Available in: https://github.com/esp8266/Arduino/blob/decfbdda5fb2677fa7b280ecd6b4bb9551c1a896/cores/esp8266/core_esp8266_i2s.c
Removed in: https://github.com/esp8266/Arduino/blob/8ae553d99e461459a95a59a1bfaa63a35474be65/cores/esp8266/core_esp8266_i2s.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('SLC_BUF_LEN', '4', '95', 'ICACHE_RAM_ATTR'), ('SLCIC', '4294967295', '91', 'ICACHE_RAM_ATTR'), ('SLCIC', '4294967295', '130', 'i2s_slc_begin'), ('y', '0', '115', 'i2s_slc_begin'), ('SLC_BUF_LEN', '4', '114', 'i2s_slc_begin'), ('i2s_slc_queue_len', '0', '110', 'i2s_slc_begin'), ('SLCIE', '0', '160', 'i2s_slc_end'), ('SLCIC', '4294967295', '159', 'i2s_slc_end'), ('i2s_curr_slc_buf_pos', '0', '187', 'i2s_write_sample'), ('optimistic_yield', '10000', '180', 'i2s_write_sample'), ('i2s_curr_slc_buf_pos', '0', '201', 'i2s_write_sample_nb'), ('sample', '16', '209', 'i2s_write_lr'), ('right', '65535', '208', 'i2s_write_lr'), ('scd_div_best', '1', '229', 'i2s_set_rate'), ('sbd_div_best', '1', '228', 'i2s_set_rate'), ('I2SBASEFREQ', '32', '225', 'i2s_set_rate'), ('i2s_set_rate', '44100', '287', 'i2s_begin'), ('I2SIE', '0', '275', 'i2s_begin'), ('I2SIC', '63', '274', 'i2s_begin'), ('_i2s_sample_rate', '0', '265', 'i2s_begin')]
Not available in: https://github.com/esp8266/Arduino/blob/f9110f51c200e056947c275dbc3e96ecb80ccdef/cores/esp8266/core_esp8266_i2s.c
Added in: https://github.com/esp8266/Arduino/blob/decfbdda5fb2677fa7b280ecd6b4bb9551c1a896/cores/esp8266/core_esp8266_i2s.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #78

### File name(s)
cores/esp8266/core_esp8266_vm.cpp

### Compare results

####Values added
Values: [('__vm_cache_line', '0', '390', 'install_vm_exception_handler')]
Not available in: https://github.com/esp8266/Arduino/blob/dcdd4313cb1996a526e253d3be8536f8a27626c8/cores/esp8266/core_esp8266_vm.cpp
Added in: https://github.com/esp8266/Arduino/blob/9fcf14f81fa9be589530e9596b7c5a264dc81ee8/cores/esp8266/core_esp8266_vm.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:IRAM_ATTR
OLD:ICACHE_RAM_ATTR
CHANGED:(240, '4', '320', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/dcdd4313cb1996a526e253d3be8536f8a27626c8/cores/esp8266/core_esp8266_vm.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/8ffe41b7df9292ff04a6ce22de2815d075330a35/cores/esp8266/core_esp8266_vm.cpp
####True or False Positive:
False
####Note:
[check] Changed linker attributes to function.

### Number of warnings:
2

## Result number #79

### File name(s)
libraries/ESP8266WiFi/src/WiFiUdp.cpp

### Compare results

####Values removed
Values: [(2, '0', '215', 'IPAddress'), (4, '0', '214', 'IPAddress'), ('_remotePort', '1', '228', 'uint16_t'), (2, '0', '225', 'uint16_t'), (4, '0', '224', 'uint16_t')]
Available in: https://github.com/esp8266/Arduino/blob/fea362a3b53507ece698717b7f869f6befefd6b4/libraries/ESP8266WiFi/src/WiFiUdp.cpp
Removed in: https://github.com/esp8266/Arduino/blob/71c705a1876af76ff642a5693cba48ffe2d4a404/libraries/ESP8266WiFi/src/WiFiUdp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [(4, '0', '224', 'uint16_t')]
Not available in: https://github.com/esp8266/Arduino/blob/75d9cf40be5ec357dc55cf4d4c5bbe2024426a02/libraries/ESP8266WiFi/src/WiFiUdp.cpp
Added in: https://github.com/esp8266/Arduino/blob/c28a63c9d5679e637f8cdff60213d60269674af8/libraries/ESP8266WiFi/src/WiFiUdp.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #80

### File name(s)
cores/esp8266/libb64/cencode.cpp

### Compare results

####Values added
Values: [(252, '2', '59', 'base64_encode_block'), ('codechar', '0', '113', 'base64_encode_blockend')]
Not available in: https://github.com/esp8266/Arduino/blob/6bd4b1c4f72c6362207f4a5ed72d7531959c1e82/cores/esp8266/libb64/cencode.cpp
Added in: https://github.com/esp8266/Arduino/blob/14262af0d19a9a3b992d5aa310a684d47b6fb876/cores/esp8266/libb64/cencode.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #81

### File name(s)
libraries/ESP8266WiFi/src/WiFiClient.h

### Compare results

####Values removed
Values: [('size_sent', '0', '121', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/7f7a1ac4203c14c2e878dba65b9be041e8f9278a/libraries/ESP8266WiFi/src/WiFiClient.h
Removed in: https://github.com/esp8266/Arduino/blob/8db4dcea426b2a1b7d1cca6d5bf4c351284f2240/libraries/ESP8266WiFi/src/WiFiClient.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('doneLen', '0', '63', 'size_t'), ('obuf', '1460', '62', 'size_t')]
Available in: https://github.com/esp8266/Arduino/blob/3e7b8515e4640edaf23283a6d0528dbb73a13127/libraries/ESP8266WiFi/src/WiFiClient.h
Removed in: https://github.com/esp8266/Arduino/blob/36d0968ada0413dd74fc082d6aebd12e7a059ab7/libraries/ESP8266WiFi/src/WiFiClient.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #82

### File name(s)
cores/esp8266/HardwareSerial.cpp

### Compare results

####Values changed
NEW:esp_delay
OLD:delay
CHANGED:('delay', '100', '146', 'HardwareSerial')
Version 1(new): https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/HardwareSerial.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/c9f27410f7a7f4860602c412c3de666dddc8700c/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
False
####Note:
[check] Name var change.

####Values added
Values: [('detectedBaudrate', '0', '136', 'HardwareSerial')]
Not available in: https://github.com/esp8266/Arduino/blob/007e495e0d88eabc6dae31fad311df38f8914607/cores/esp8266/HardwareSerial.cpp
Added in: https://github.com/esp8266/Arduino/blob/c37903c33b8859a5bac2d2441ff708ed63ff671f/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('got', '0', '138', 'size_t')]
Not available in: https://github.com/esp8266/Arduino/blob/e4d9c279ef1991256793745242c177148ca58b2a/cores/esp8266/HardwareSerial.cpp
Added in: https://github.com/esp8266/Arduino/blob/dc03293d82e5eb8f37b269aa09f54035f25cd8e8/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('delay', '100', '130', 'HardwareSerial')
OLD:('_uart', '1', '108', 'HardwareSerial')
CHANGED:('_uart', '1', '108', 'HardwareSerial')
Version 1(new): https://github.com/esp8266/Arduino/blob/e4d9c279ef1991256793745242c177148ca58b2a/cores/esp8266/HardwareSerial.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/3a110aa698dd17e0d80704db47c8e43c986b0f86/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
False
####Note:
[check] Different var.

####Values removed
Values: [('delay', '0', '121', 'uart_wait_tx_empty'), ('tmp', '0', '128', 'uart_flush'), ('uart', '15', '316', 'uart_set_pins'), ('uart', '15', '309', 'uart_set_pins'), ('delay', '0', '328', 'uart0_write_char'), ('delay', '0', '333', 'uart1_write_char'), ('system_set_os_print', '0', '352', 'uart_set_debug'), ('system_set_os_print', '1', '347', 'uart_set_debug'), ('system_set_os_print', '1', '343', 'uart_set_debug')]
Available in: https://github.com/esp8266/Arduino/blob/e255f25cfd626cb902d8f55fbe006505435ccdad/cores/esp8266/HardwareSerial.cpp
Removed in: https://github.com/esp8266/Arduino/blob/7960b633576fb5d64c1ff44324fd000af6b17020/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('system_set_os_print', '1', '343', 'uart_set_debug')]
Not available in: https://github.com/esp8266/Arduino/blob/531d748936e549f4c034ddf19b6af6739f2efa22/cores/esp8266/HardwareSerial.cpp
Added in: https://github.com/esp8266/Arduino/blob/e255f25cfd626cb902d8f55fbe006505435ccdad/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('system_set_os_print', '1', '522', 'uart_set_debug'), ('system_set_os_print', '1', '518', 'uart_set_debug')]
Not available in: https://github.com/esp8266/Arduino/blob/e97bc80cee5eb56c6bdcedf2e0a6c6a810b338b1/cores/esp8266/HardwareSerial.cpp
Added in: https://github.com/esp8266/Arduino/blob/d68b9717b531b2b4a1b3481a435c00572d81aaa4/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('system_set_os_print', '1', '468', 'uart_set_debug'), ('system_set_os_print', '1', '460', 'uart_set_debug')]
Available in: https://github.com/esp8266/Arduino/blob/cfe7ae1118f817f42c020464e2444e51e37da559/cores/esp8266/HardwareSerial.cpp
Removed in: https://github.com/esp8266/Arduino/blob/c8772cfcd04630d8c2457096ab6d1f137db7a141/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('conf1', '0', '297', 'uart_t'), ('system_set_os_print', '0', '457', 'uart_set_debug'), ('system_set_os_print', '1', '452', 'uart_set_debug'), ('system_set_os_print', '1', '448', 'uart_set_debug')]
Available in: https://github.com/esp8266/Arduino/blob/34b09f7e23d09d06050fa4b87944983749f9d77f/cores/esp8266/HardwareSerial.cpp
Removed in: https://github.com/esp8266/Arduino/blob/669609f3d7cc1b63dc5854ebc46236d2ecfe08a7/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('USTXC', '255', '178', 'uart_wait_for_tx_fifo'), ('tmp', '0', '226', 'uart_flush'), ('conf1', '0', '297', 'uart_t'), ('system_set_os_print', '0', '457', 'uart_set_debug'), ('system_set_os_print', '1', '452', 'uart_set_debug'), ('system_set_os_print', '1', '448', 'uart_set_debug')]
Not available in: https://github.com/esp8266/Arduino/blob/b752822aef0c052f7897a5fcfa399b86a25b0f57/cores/esp8266/HardwareSerial.cpp
Added in: https://github.com/esp8266/Arduino/blob/34b09f7e23d09d06050fa4b87944983749f9d77f/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('UART_INT_ST', '0', '107', 'ICACHE_RAM_ATTR')]
Available in: https://github.com/esp8266/Arduino/blob/66ded562f3bcdd1f512582617b3586d91168af4f/cores/esp8266/HardwareSerial.cpp
Removed in: https://github.com/esp8266/Arduino/blob/fcbd7dbed03842dbe9d9e1ed140de45063dd61e4/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:('UART_INT_ST', '0', '107', 'ICACHE_RAM_ATTR')
OLD:('UART_INT_ST', '0', '107', 'uart_interrupt_handler')
CHANGED:('UART_INT_ST', '0', '107', 'uart_interrupt_handler')
Version 1(new): https://github.com/esp8266/Arduino/blob/2b3302c714f9b32e1b9f77d32990109a1fe7930b/cores/esp8266/HardwareSerial.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/be5f1f83c154fcd80b6bf3223a7e1482042f445d/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
False
####Note:
[check] Added linker attributes to function.

####Values removed
Values: [(0, '255', '76', 'uart0_rx_handler'), (0, '511', '125', 'uart0_interrupt_enable'), (0, '0', '133', 'uart0_interrupt_disable'), ('UART_FIFO', '0', '185', 'uart_write_char')]
Available in: https://github.com/esp8266/Arduino/blob/39e087a19e0f0ce53b16133f747e8836a316f626/cores/esp8266/HardwareSerial.cpp
Removed in: https://github.com/esp8266/Arduino/blob/160f99c31c6e9fe7734f6422a1d85a3704d3ae70/cores/esp8266/HardwareSerial.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
13

## Result number #83

### File name(s)
libraries/SDFS/src/SDFS.cpp

### Compare results

####Values added
Values: [('uint8_t', '512', '154', 'SDFSImpl')]
Not available in: https://github.com/esp8266/Arduino/blob/1bb0815fed4e0601f49e934b601e4912ff25a4e9/libraries/SDFS/src/SDFS.cpp
Added in: https://github.com/esp8266/Arduino/blob/c487ca5233721ac49ca0dcfe103c73df9a4301ad/libraries/SDFS/src/SDFS.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #84

### File name(s)
cores/esp8266/core_esp8266_postmortem.c
cores/esp8266/core_esp8266_postmortem.cpp

### Compare results

####Values added
Values: [('__builtin_return_address', '0', '309', '__stack_chk_fail')]
Not available in: https://github.com/esp8266/Arduino/blob/d979b57d7640b78d59d7d59db744fe75bbcee9ac/cores/esp8266/core_esp8266_postmortem.cpp
Added in: https://github.com/esp8266/Arduino/blob/5b3d290de8df597a98f1c13fc216754040ab1a7b/cores/esp8266/core_esp8266_postmortem.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('s_panic_what', '0', '296', '__panic_func'), ('__builtin_return_address', '0', '306', '__stack_chk_fail')]
Not available in: https://github.com/esp8266/Arduino/blob/a70e834d1ea26316d28ae41b4623550d7b47ed34/cores/esp8266/core_esp8266_postmortem.cpp
Added in: https://github.com/esp8266/Arduino/blob/d979b57d7640b78d59d7d59db744fe75bbcee9ac/cores/esp8266/core_esp8266_postmortem.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:400
OLD:416
CHANGED:('offset', '416', '153', '__wrap_system_restart_local')
Version 1(new): https://github.com/esp8266/Arduino/blob/f45da1cf259d4eafad3308b508fa6f5ce3cdc9f3/cores/esp8266/core_esp8266_postmortem.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/7a43092df0c8734577870f5630ee0062150c1074/cores/esp8266/core_esp8266_postmortem.cpp
####True or False Positive:
True
####Note:
[Recheck] Changed the amount of stack taken by the `REASON_EXCEPTION_RST` exception handler.

####Values removed
Values: [('s_panic_what', '0', '246', '__panic_func')]
Available in: https://github.com/esp8266/Arduino/blob/8e46a3371d73cb43deb70ac088e6337b74bfe50e/cores/esp8266/core_esp8266_postmortem.c
Removed in: https://github.com/esp8266/Arduino/blob/f706c83b66261df58b7d6148e343fd21cbd77206/cores/esp8266/core_esp8266_postmortem.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('s_panic_what', '0', '246', '__panic_func')]
Not available in: https://github.com/esp8266/Arduino/blob/6280e98b0360f85fdac2b8f10707fffb4f6e6e31/cores/esp8266/core_esp8266_postmortem.c
Added in: https://github.com/esp8266/Arduino/blob/8e46a3371d73cb43deb70ac088e6337b74bfe50e/cores/esp8266/core_esp8266_postmortem.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('s_panic_what', '0', '239', '__panic_func')]
Not available in: https://github.com/esp8266/Arduino/blob/4a958c844401bbef880481fef38c5bec083f85be/cores/esp8266/core_esp8266_postmortem.c
Added in: https://github.com/esp8266/Arduino/blob/855b03ce4d3616b4243b5b55c28eb54331a00022/cores/esp8266/core_esp8266_postmortem.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('sf', '2', '118', 'print_pcs'), ('sf', '3', '117', 'print_pcs'), ('n', '0', '112', 'print_pcs')]
Available in: https://github.com/esp8266/Arduino/blob/0650b69b5a334dfc460c3782ea686396e961e642/cores/esp8266/core_esp8266_postmortem.c
Removed in: https://github.com/esp8266/Arduino/blob/b500a1f26a2df8cd06b32d9846c2d526a41eb921/cores/esp8266/core_esp8266_postmortem.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
7

## Result number #85

### File name(s)
libraries/Ticker/src/Ticker.h

### Compare results

####Values added
Values: [('', '0', '', 'attach_ms_scheduled_accurate')]
Not available in: https://github.com/esp8266/Arduino/blob/482516e393b169f727afd10df374dc5d6ddb1cc9/libraries/Ticker/src/Ticker.h
Added in: https://github.com/esp8266/Arduino/blob/bc170e6d635bb7788e8907da4451c88b51fb628f/libraries/Ticker/src/Ticker.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #86

### File name(s)
cores/esp8266/time.cpp

### Compare results

####Values added
Values: [('tz', '1', '213', 'setTZ')]
Not available in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/time.cpp
Added in: https://github.com/esp8266/Arduino/blob/a05a71fa9d2e6b143cb34f01b47e22c4b66b80a1/cores/esp8266/time.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('', '0', '', 'settimeofday')]
Not available in: https://github.com/esp8266/Arduino/blob/af1bc71a9ea09bd92aed033e6a2b6ec2b10c311a/cores/esp8266/time.cpp
Added in: https://github.com/esp8266/Arduino/blob/40eb5747e4b7d3458e9406c3c446948bbffa767b/cores/esp8266/time.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:setTZ
OLD:configTime
CHANGED:('tz', '1', '196', 'configTime')
Version 1(new): https://github.com/esp8266/Arduino/blob/b02643e7fadc5c7d618613058f70835d9c16649a/cores/esp8266/time.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/abdd2bdbb6a5caf31807d82ebd7b447947a9c360/cores/esp8266/time.cpp
####True or False Positive:
False
####Note:
[check] Changed function name.

####Values changed
NEW:('sntp_getservername', '2', '85', 'sntp_set_timezone_in_seconds')
OLD:('sntp_get_current_timestamp', '1000000', '91', '_gettimeofday_r')
CHANGED:('sntp_get_current_timestamp', '1000000', '91', '_gettimeofday_r')
Version 1(new): https://github.com/esp8266/Arduino/blob/f066ed2495c8d6f04841243d90f6deaef21a0119/cores/esp8266/time.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/05d28bc045d331edc37fb4f6622dacf518e12723/cores/esp8266/time.cpp
####True or False Positive:
False
####Note:
[check] Different var.

####Values added
Values: [('sntp_set_timezone_in_seconds', '0', '125', 'configTime')]
Not available in: https://github.com/esp8266/Arduino/blob/3b1ad418b3ddc8437e9096980f82e9503b2b0242/cores/esp8266/time.cpp
Added in: https://github.com/esp8266/Arduino/blob/05d28bc045d331edc37fb4f6622dacf518e12723/cores/esp8266/time.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('tzram', '1', '124', 'configTime'), ('tz', '1', '122', 'configTime')]
Not available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/time.cpp
Added in: https://github.com/esp8266/Arduino/blob/ffe5476fc42b06ebde5688527200c6690e8e519f/cores/esp8266/time.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('sntp_get_current_timestamp', '1000000', '100', '_gettimeofday_r')]
Available in: https://github.com/esp8266/Arduino/blob/f706c83b66261df58b7d6148e343fd21cbd77206/cores/esp8266/time.cpp
Removed in: https://github.com/esp8266/Arduino/blob/3dbac1cab44377e76c4b7947abad20d56afe4d6d/cores/esp8266/time.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
7

## Result number #87

### File name(s)
cores/esp8266/time.c

### Compare results

####Values added
Values: [('sntp_get_current_timestamp', '1000000', '97', '_gettimeofday_r')]
Not available in: https://github.com/esp8266/Arduino/blob/cbfbc1ad637182a0b1979bcff6b0e75ae9f57e7e/cores/esp8266/time.c
Added in: https://github.com/esp8266/Arduino/blob/9913e5210779d2f3c4197760d6813270dbba6232/cores/esp8266/time.c
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('timezone', '3600', '74', 'configTime')]
Available in: https://github.com/esp8266/Arduino/blob/1c8bcf6cb27439accc54b42797de7ed9ddd6d979/cores/esp8266/time.c
Removed in: https://github.com/esp8266/Arduino/blob/5b925697ec1bee4ec8e366acace20cfd1fb51d18/cores/esp8266/time.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
2

## Result number #88

### File name(s)
cores/esp8266/WString.h

### Compare results

####Values removed
Values: [(0, '255', '267', 'setSSO')]
Available in: https://github.com/esp8266/Arduino/blob/eea9999dc5eaf464a432f77d5b65269f9baf198d/cores/esp8266/WString.h
Removed in: https://github.com/esp8266/Arduino/blob/78a1a66e6dcd0437167869c363cd29160c35fe96/cores/esp8266/WString.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #89

### File name(s)
cores/esp8266/core_esp8266_waveform_pwm.cpp

### Compare results

####Values removed
Values: [('delay', '0', '395', 'startWaveformClockCycles_weak'), ('delay', '0', '375', 'startWaveformClockCycles_weak')]
Available in: https://github.com/esp8266/Arduino/blob/25e1b3b61c6e37a648e49292916f4ed672304dfb/cores/esp8266/core_esp8266_waveform_pwm.cpp
Removed in: https://github.com/esp8266/Arduino/blob/c312a2eaf1356ceaafad7c4935fa850e087c84fe/cores/esp8266/core_esp8266_waveform_pwm.cpp
####True or False Positive:
[todo]
####Note:
[todo]

####Values changed
NEW:IRAM_ATTR
OLD:ICACHE_RAM_ATTR
CHANGED:('GP16O', '1', '601', 'ICACHE_RAM_ATTR')
Version 1(new): https://github.com/esp8266/Arduino/blob/656a33e6f82482535782213a6e96c2bd49b22a39/cores/esp8266/core_esp8266_waveform_pwm.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/f5fd5912fe09d7eec8a909326287379570579ea6/cores/esp8266/core_esp8266_waveform_pwm.cpp
####True or False Positive:
False
####Note:
[check] Changed linker attributes to function.

####Values changed
NEW:('leftover', '0', '225', '_cleanAndRemovePWM')
OLD:('leftover', '0', '217', '_cleanAndRemovePWM')
CHANGED:('leftover', '0', '217', '_cleanAndRemovePWM')
Version 1(new): https://github.com/esp8266/Arduino/blob/f5fd5912fe09d7eec8a909326287379570579ea6/cores/esp8266/core_esp8266_waveform_pwm.cpp
Version 2(old): https://github.com/esp8266/Arduino/blob/ccdde5f396d442f73dc101a1badeed3291f4652c/cores/esp8266/core_esp8266_waveform_pwm.cpp
####True or False Positive:
False
####Note:
[check] Line number change.

### Number of warnings:
3

## Result number #90

### File name(s)
libraries/SDFS/src/SDFS.h

### Compare results

####Values added
Values: [('_valid', '1', '490', 'SDFSDirImpl'), ('tmpName', '260', '432', 'SDFSDirImpl')]
Not available in: https://github.com/esp8266/Arduino/blob/1bb0815fed4e0601f49e934b601e4912ff25a4e9/libraries/SDFS/src/SDFS.h
Added in: https://github.com/esp8266/Arduino/blob/c487ca5233721ac49ca0dcfe103c73df9a4301ad/libraries/SDFS/src/SDFS.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_valid', '1', '479', 'next')]
Not available in: https://github.com/esp8266/Arduino/blob/d4d89244bdad1fc11438dc4de10f171c1365f223/libraries/SDFS/src/SDFS.h
Added in: https://github.com/esp8266/Arduino/blob/bea64dfa6987655ad9c51fda0949fdd4ab2a7d01/libraries/SDFS/src/SDFS.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values removed
Values: [('ftime', '0', '356', 'time_t')]
Available in: https://github.com/esp8266/Arduino/blob/72dd589599e0b7d2e208eafeeca01a83b2d4cb94/libraries/SDFS/src/SDFS.h
Removed in: https://github.com/esp8266/Arduino/blob/d4d89244bdad1fc11438dc4de10f171c1365f223/libraries/SDFS/src/SDFS.h
####True or False Positive:
[todo]
####Note:
[todo]

####Values added
Values: [('_time', '0', '445', 'next'), ('_valid', '1', '437', 'next')]
Not available in: https://github.com/esp8266/Arduino/blob/44bda41cf665f4e5bc1ee0162b84380e51b0f63c/libraries/SDFS/src/SDFS.h
Added in: https://github.com/esp8266/Arduino/blob/72dd589599e0b7d2e208eafeeca01a83b2d4cb94/libraries/SDFS/src/SDFS.h
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
4

## Result number #91

### File name(s)
cores/esp8266/cont_util.cpp

### Compare results

####Values removed
Values: [(64, '4', '76', 'cont_repaint_stack')]
Available in: https://github.com/esp8266/Arduino/blob/f706c83b66261df58b7d6148e343fd21cbd77206/cores/esp8266/cont_util.cpp
Removed in: https://github.com/esp8266/Arduino/blob/5632e8156f24ac890183766a9945d6ffb080b3b0/cores/esp8266/cont_util.cpp
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

## Result number #92

### File name(s)
cores/esp8266/cont_util.c

### Compare results

####Values added
Values: [(64, '4', '75', 'cont_repaint_stack')]
Not available in: https://github.com/esp8266/Arduino/blob/1b1b0a28a825cca187d4dcea79fe2cb8a7411059/cores/esp8266/cont_util.c
Added in: https://github.com/esp8266/Arduino/blob/8e46a3371d73cb43deb70ac088e6337b74bfe50e/cores/esp8266/cont_util.c
####True or False Positive:
[todo]
####Note:
[todo]

### Number of warnings:
1

