import ms_modules.health
import config
charge_before = 50000
charge_after = 0
diff = charge_before - charge_after

ms_modules.health.adjust_lifespan(diff)

print(config.lifespan)
