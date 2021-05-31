#!/usr/bin/python3
#Author: Nathaniel Elderson


import random


welcomeBanner = """		    	__________________________
		   	< Welcome to the HellShell >
 		    	--------------------------
 		    """


cowsayHelp = """           ___________
			       < type help >
			        -----------
			               \   ^__^
			                \  (\033[31mxo\033[0m)\_______
			                   (__)\       )\/\

			                       ||----w |
			                       ||     ||
"""


menu = """
\033[94m [*]quit(q) or exit(0) [*]clear the terminal(clear) [*]dispaly a cool banner(banner)
 [*]to show the commands(help) [*]execute bash commands($ command)

\033[36m [1 ]Automate Android Hacking{droid}           	[7 ]
 [2 ]MAC address spoofer{mac}		        [8 ]
 [3 ]Phish Social Media{phish}                  [9 ]
 [4 ]Bruteforce e-mail accounts{brutemail}      [10]
 [5 ]Bruteforce protected .zip files{brutezip}  [11]
 [6 ]                                           [12]
"""


credits = """

	\033[93m[---]\033[0m        		\033[37m\033[01m\033[04mThe HellShell\033[0m                  \033[94m[---]\033[0m

	\033[93m[---]\033[0m          \033[94mWritten by\033[0m: \033[92m\033[01mNathaniel Elderson\033[0m          \033[94m[---]\033[0m
				Version: 1.0
	\033[93m[---]\033[0m          "It's Impossible", said Pride.          \033[94m[---]\033[0m
	\033[93m[---]\033[0m          "It's Risky", said Experience.          \033[94m[---]\033[0m
	\033[93m[---]\033[0m          "It's Pointless", said Reason.          \033[94m[---]\033[0m

	\033[93m[---]\033[0m       	  If you really a \033[31mHacker\033[0m!              \033[94m[---]\033[0m   
	\033[93m[---]\033[0m       	    Then give it a \033[31mTry\033[0m!                \033[94m[---]\033[0m  

"""


banner1 = """  \033[33m\033[01m___ ___         .__  .__    _________.__           .__  .__
 /   |   \   ____ |  | |  |  /   _____/|  |__   ____ |  | |  |
/    ~    \_/ __ \|  | |  |  \_____  \ |  |  \_/ __ \|  | |  |
\    Y    /\  ___/|  |_|  |__/        \|   Y  \  ___/|  |_|  |__
 \___|_  /  \___  >____/____/_______  /|___|  /\___  >____/____/
       \/       \/                  \/      \/     \/\033[0m
							   version: 1.0
   ▁ ▂ ▄ ▅ ▆ ▇ █ Author: Nathaniel Elderson █ ▇ ▆ ▅ ▄ ▂ ▁
"""


banner2 = """
\033[01m\033[37mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'\033[0m

	\033[93m[---]\033[0m        		\033[37m\033[01m\033[04mThe HellShell\033[0m                  \033[94m[---]\033[0m

	\033[93m[---]\033[0m          \033[94mWritten by\033[0m: \033[92m\033[01mNathaniel Elderson\033[0m          \033[94m[---]\033[0m
				Version: 1.0
	\033[93m[---]\033[0m          "It's Impossible", said Pride.          \033[94m[---]\033[0m
	\033[93m[---]\033[0m          "It's Risky", said Experience.          \033[94m[---]\033[0m
	\033[93m[---]\033[0m          "It's Pointless", said Reason.          \033[94m[---]\033[0m

	\033[93m[---]\033[0m       	  If you really a \033[31mHacker\033[0m!              \033[94m[---]\033[0m   
	\033[93m[---]\033[0m       	    Then give it a \033[31mTry\033[0m!                \033[94m[---]\033[0m  
"""


banner3 = """
                        \033[01m\033[37m..:::::::::..
                    ..:::aad8888888baa:::..
                .::::d:?88888888888?::8b::::.
              .:::d8888:?88888888??a888888b:::.
            .:::d8888888a8888888aa8888888888b:::.
           ::::dP\033[01m\033[31m::::::::\033[0m\033[01m88888888888\033[01m\033[31m::::::::\033[0m\033[01mYb\033[01m::::
          ::::dP\033[01m\033[31m:::::::::\033[0m\033[01mY888888888P\033[01m\033[31m:::::::::\033[0m\033[01mYb\033[01m::::
         ::::d8\033[01m\033[31m:::::::::::\033[0m\033[01mY8888888P\033[01m\033[31m:::::::::::\033[0m\033[01m8b\033[01m::::
        .::::88\033[01m\033[31m::::::::::::\033[0m\033[01mY88888P\033[01m\033[31m::::::::::::\033[0m\033[01m88::::.
        :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
        :::::::Y88888888888P::|::Y88888888888P:::::::
        ::::::::::::::::888:::|:::888::::::::::::::::
        `:::::::::::::::8888888888888b::::::::::::::'
         :::::::::::::::88888888888888::::::::::::::
          :::::::::::::d88888888888888:::::::::::::
           ::::::::::::88::88::88:::88::::::::::::
            `::::::::::88::88::88:::88::::::::::'
              `::::::::88::88::P::::88::::::::'
                `::::::88::88:::::::88::::::'
                   ``:::::::::::::::::::''
                        ``:::::::::''\033[0m

\033[93m[---]\033[0m        		\033[37m\033[01m\033[04mThe HellShell\033[0m                  \033[94m[---]\033[0m

\033[93m[---]\033[0m          \033[94mWritten by\033[0m: \033[92m\033[01mNathaniel Elderson\033[0m          \033[94m[---]\033[0m
			Version: 1.0
\033[93m[---]\033[0m          "It's Impossible", said Pride.          \033[94m[---]\033[0m
\033[93m[---]\033[0m          "It's Risky", said Experience.          \033[94m[---]\033[0m
\033[93m[---]\033[0m          "It's Pointless", said Reason.          \033[94m[---]\033[0m

\033[93m[---]\033[0m       	  If you really a \033[31mHacker\033[0m!              \033[94m[---]\033[0m   
\033[93m[---]\033[0m       	    Then give it a \033[31mTry\033[0m!                \033[94m[---]\033[0m  

"""


def shuffle():
	banners = [banner1, banner2, banner3]
	random.shuffle(banners)
	return banners[0]

