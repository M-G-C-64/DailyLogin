
def dailylog():
    import pyautogui
    import time
    import webbrowser
    from datetime import date

    dt = date.today()
    dd = int(dt.strftime("%d"))-1

    
    #this is number of days delay to 1st
    dd = dd-3

    sc = dd//7
    idx = dd%7


    webbrowser.open('https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us')
    time.sleep(10)

    for i in range(sc):
        pyautogui.scroll(-275, x=287, y=436)
        time.sleep(1)
    time.sleep(2)

    lst = [(382, 582),(482, 582),(582,582),(682,582),(782,582),(882,582),(982,582)]

    pyautogui.click(x=lst[idx][0], y=lst[idx][1])

    time.sleep(2)
    pyautogui.press('m')

dailylog()