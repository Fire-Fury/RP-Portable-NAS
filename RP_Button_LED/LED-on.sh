#! /bin/sh

### BEGIN INIT INFO
# Provides:          listen-for-shutdown.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    sudo pkill -f /usr/local/bin/LED-slow-blink.py
    sudo pkill -f /usr/local/bin/LED-fast-blink.py
    echo "Starting LED-on.py"
    /usr/local/bin/LED-on.py &
    ;;
  stop)
    echo "Stopping LED-on.py"
    pkill -f /usr/local/bin/LED-on.py
    /usr/local/bin/ResetGPIO4.py 
    ;;
  *)
    echo "Usage: /etc/init.d/LED-on.sh {start|stop}"
    exit 1
    ;;
esac

exit 0