import pandas
import datetime
import time
import os
data = pandas.read_csv("works.csv")
alarm_time = list(data['Time'])
alarm_statements = list(data['Statement'])
nearest_alarm = min(alarm_time)
nearest_alarm_statement = alarm_statements[int(alarm_time.index(str(nearest_alarm)))]
print(nearest_alarm_statement)
print(datetime.datetime.now().strftime("%H:%M:%S"))

print("started")
while True:
    if nearest_alarm == datetime.datetime.now().strftime("%H:%M:%S"):
        alarm_time.remove(nearest_alarm)
        alarm_statements.remove(nearest_alarm_statement)
        print("Time has been completed")
        file = open("index.vbs", "w")
        file.write("")
        file.close()
        data = ['Sub DefaultMsgBox()\n', 'MsgBox "'+nearest_alarm_statement+'"\n', 'End Sub\n', '\n', 'DefaultMsgBox()']
        i = -1
        for g in data:
            i = i + 1
            file = open("index.vbs", "a")
            file.write(data[i])
            print(data[i])
            file.close()
        os.startfile("index.vbs")
        time.sleep(1)
        nearest_alarm = min(alarm_time)
        nearest_alarm_statement = alarm_statements[int(alarm_time.index(str(nearest_alarm)))]
