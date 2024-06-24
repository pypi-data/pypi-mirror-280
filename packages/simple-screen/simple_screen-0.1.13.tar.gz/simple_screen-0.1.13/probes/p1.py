import simple_screen as ssc

with ssc.Screen_manager:
    ssc.pen(ssc.YELLOW)
    ssc.paper(ssc.DARK_KHAKI)
    ssc.cls()
    for i in range(5):
        ssc.locate(0, 5+i)
        ssc.Input("Di algo")
    ssc.Input()
    