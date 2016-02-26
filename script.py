import billboard
import json
from time import sleep

chart = billboard.ChartData('hot-100', date=None, fetch=True)
while chart.previousDate:
    f = open("dump/" + chart.date + ".json","w")
    f.write(json.dumps(chart, default=lambda o: o.__dict__))
    print chart.date
    f.close()

    chart = billboard.ChartData('hot-100', chart.previousDate)
    sleep(12) # try not to hammer Billboard.
