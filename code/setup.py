import cx_Freeze
#setup.py bdist_msi

executables = [cx_Freeze.Executable("Code.py")] #, base = "Win32GUI")] 
cx_Freeze.setup(
    name="LerProg",
    version="1.0.0",
    options={"build_exe": {"packages":["pygame", "sys","random","os","time"],
                           "include_files":["1.png","2.png","3.png","4.png","5.png","6.png",
    "7.png","8.png","9.png","10.png","11.png","12.png","13.png","14.png","15.png","16.png",
    "back.png","BackGround1.jpg","f1.png","f2.png","help.png","helpFile.txt",
    "home.png","ieee.png","ieee_logo.png","ip2.mp3", "jump0.png","levels - Copy.txt","light.png",
    "off.png","on.png","p.png" ,"play.png","q.png",  "qq.png","qqq.png","qqqq.png",
    "replay.png","run.png","run2.png","run3.png",
    "settings.png","settings0.png","skip.png","space.png","StartBackground.png","startButton.png" ,"turn_left.png",
    "turn_right.png","up.png","HOC.jpg","certificate.jpg","helpPic"
    
                                                                    ]}},
    executables = executables
    

    )
