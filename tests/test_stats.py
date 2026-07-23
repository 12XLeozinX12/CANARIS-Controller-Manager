from database.stats import StatsManager

stats = StatsManager()

USER_ID = 2

stats.add_session(USER_ID)

stats.add_button_press(USER_ID)

stats.add_button_press(USER_ID)

stats.add_button_press(USER_ID)

stats.add_analog_distance(USER_ID, 13.5)

stats.set_favorite_controller(USER_ID, "DualShock 4")

print(stats.get_stats(USER_ID))