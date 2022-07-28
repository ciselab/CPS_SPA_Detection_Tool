# Arduino

## Result number #1
### File name(s):cores/esp8266/Esp.cpp
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

## Result number #2
### File name(s):libraries/ESP8266WiFi/src/include/UdpContext.h
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
NEW:512
OLD:1024
CHANGED:('pbuf_unit_size', '1024', '284', '_reserve')
Version 1(new): https://github.com/esp8266/Arduino/blob/3049d48d560dfe1a676de3fe8e4aeec5f8ebf059/libraries/ESP8266WiFi/src/include/UdpContext.h
Version 2(old): https://github.com/esp8266/Arduino/blob/5354464a010a5e042bcf1514ec1bd9242de02940/libraries/ESP8266WiFi/src/include/UdpContext.h
####True or False Positive:
True
####Note:
The size of the `pbuf_unit_size` changed.

## Result number #3
### File name(s):bootloaders/eboot/eboot.c
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

## Result number #4
### File name(s):cores/esp8266/Tone.cpp
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

## Result number #5
### File name(s):cores/esp8266/MD5Builder.cpp
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

## Result number #6
### File name(s):cores/esp8266/core_esp8266_postmortem.c
cores/esp8266/core_esp8266_postmortem.cpp
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
