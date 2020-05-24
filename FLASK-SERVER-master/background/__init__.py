from apscheduler.schedulers.background import BackgroundScheduler

from background.BannedTask import BannedScheduler
banned_job = BannedScheduler()
scheduler = BackgroundScheduler()
scheduler.add_job(banned_job.check_banned_scheduler, trigger='interval', minutes=1)

