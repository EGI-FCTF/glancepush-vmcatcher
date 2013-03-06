#
# Regular cron jobs for the glancepush-vmcatcher package
#
0 4	* * *	root	[ -x /usr/bin/glancepush-vmcatcher_maintenance ] && /usr/bin/glancepush-vmcatcher_maintenance
