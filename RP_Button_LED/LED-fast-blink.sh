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
    echo "Starting LED-fast-blink.py"
    /usr/local/bin/LED-fast-blink.py &
    ;;
  stop)
    echo "Stopping LED-fast-blink.py"
    sudo pkill -f /usr/local/bin/LED-fast-blink.py
    /usr/local/bin/ResetGPIO4.py
    ;;
  *)
    echo "Usage: /etc/init.d/LED-fast-blink.sh {start|stop}"
    exit 1
    ;;
esac

exit 0