# Python Parser and Forwarder Log
This is a self-made project to parse terminal recording log files with a python script and forward to syslog

### Specification
- The main idea of this project is to find ways to parse a log file and extract meaningful data from it
- Forward logs to syslog server default port 514(UDP)

### Enable Terminal Recording
- You need to add below lines in /etc/profile

      #Script to Record the User's Terminal Session
      if [ "x$session_record" = "x" ]
      then
      timestamp=`date "+%m.%d.%Y_%H.%M_%s.%N"`
      output=/var/log/session/$USER.$$.$timestamp  ##PLEASE DONT CHANGE FILE NAME
      session_record=started
      export session_record
      script -t -f -q 2>/dev/null $output
      exit
      fi

- mkdir /var/log/session
- chmod 777 /var/log/session

### Using
- You need to change values in /config/template.yaml

      #Example config for PAFL
      log_server_ip_address: x.x.x.x
      log_server_port: 514
      log_folder: /var/log/session/
      log_deletion_threshold: 0
      log_archive_dir: /var/log/archive-session/

- pip3 install -r ./pafl/requirements.txt  
- pip3 install --user -U ./pafl/
- python3 ~/.local/bin/run.py


### Systemd Service

      cp ./pafl/pafl.service /lib/systemd/system/
      systemctl daemon-reload
      systemctl enable pafl.service
      systemctl start pafl.service
      systemctl status pafl.service
