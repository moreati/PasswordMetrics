# -*- coding: utf-8 -*-
"""Unicode art approximations of mobile operating system keyboards.

Limitations
 - US centric
 - Doesn't account for (e.g. email, numeric) keyboard variations
 - Doesn't account for manufacturer or carrier customisations
 - Doesn't account for custom keyboards
 - Incomplete.

Sources:
 - http://jfranklin.me/prez/ACSAC-Poster-FINAL.pdf
"""

from __future__ import unicode_literal

IOS_8x_DEPTH_1 = r'''
q w e r t y u i o p
 a s d f g h j k l
   z x c v b n m
'''.strip('\n')

IOS_8_0_DEPTH_2 = r'''
1 2 3 4 5 6 7 8 9 0
- / : ; ( ) $ & @ "
   .  ,  ?  !  '
'''.strip('\n')

IOS_8_0_DEPTH_3 = r'''
[ ] { } # % ^ * + =
_ \ | ~ < > € £ ¥ •
   .  ,  ? !  '
'''.strip('\n')

ANDROID_5_0_DEPTH_1 = r'''
q w e r t y u i o p
 a s d f g h j k l
   z x c v b n m
   ,           .
'''.strip('\n')

ANDROID_5_0_DEPTH_2 = r'''
1 2 3 4 5 6 7 8 9 0
 @ # $ % & - + ( )
   * " ' : ; ! ?
   , _       / .
'''.strip('\n')

ANDROID_5_0_DEPTH_3 = r'''
~ ` | • √ π ÷ × ¶ Δ
 £ ¢ € ¥ ^ ° = { }
   \ © ® ™ ℅ [ ]
   , <       > .
'''.strip('\n')

WINDOWS_PHONE_8_1_DEPTH_1 = ur'''
q w e r t y u i o p
 a s d f g h j k l
   z x c v b n m
               .
'''.strip('\n')

WINDOWS_PHONE_8_1_DEPTH_2 = r'''
1 2 3 4 5 6 7 8 9 0
@ # $ % & * ( ) - \\
   ! ; : ' @ ? /
             , .
'''.strip('\n')

WINDOWS_PHONE_8_1_DEPTH_3 = r'''
1 2 3 4 5 6 7 8 9 0
^ [ ] { } < > € £ ¥
   • - + = _ ~ |
             , -
'''.strip('\n')

