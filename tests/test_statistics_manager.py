import time

from core.statistics_manager import StatisticsManager

manager = StatisticsManager()

manager.start_session(

    2,

    "DualShock 4"

)

for i in range(100):

    manager.button_pressed()

manager.analog_moved(25)

time.sleep(3)

manager.finish_session()

print("Finalizado.")