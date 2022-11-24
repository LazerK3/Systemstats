try:

    import time, datetime, os

    basedir = "C:\Local_Data"
    timesdir = "times"
    sleeptime = 10

    currenttime = time.time()

    os.chdir(basedir)
    print(basedir)
    filename = timesdir + "/" + str(datetime.datetime.now().strftime("Year_%Y-Month_%m-Day_%d Hour_%H-Minute_%M-Second_%S"))

    with open(filename, 'w') as f:
        pass

    while True:
        with open(filename, 'a') as f:
            a = time.time()
            f.write(str(f"{a-currenttime}###"))
        time.sleep(sleeptime)

except Exception as e:
    with open("exeption", "w") as a:
       a.write(str(e))

finally:
    print("Program has ended")
