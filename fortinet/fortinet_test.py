'''
Created on Aug 20, 2015

@author: ljiang
'''

import sys
import paramiko
import re

if __name__ == '__main__':
    
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect('172.30.150.231', username='admin', password='')
        stdin, stdout, stderr = ssh.exec_command("config wireless-controller wtp-profile")
        stdin.flush()
        stdin1, stdout1, stderr1 = ssh.exec_command("show")
        stdin1.flush()
        data = stdout1.readlines()  
        #print data
        for l in data:
            print l
        ssh.exec_command('end')
        stdin2, stdout2, stderr2 = ssh.exec_command("diagnose wireless-controller wlac  show data")
        stdin2.flush()
        data2=stdout2.readlines()
        
        data2_string=''.join(data2)

        lst_of_wlan=re.findall(r'wlan=(.*)\sip=.*',data2_string)
        lst_of_mac=re.findall(r'\smac=(.*)\sintra',data2_string)
        print lst_of_wlan
        print lst_of_mac
        
        entries_of_stat_cnt=[]
        if sys.argv[1]=='sta_cnt>0':
            entries_of_stat_cnt=re.findall(r'wlan=.*\ssta_cnt>0\suse=.*',data2_string)
        if sys.argv[1]=='sta_cnt=0':
            entries_of_stat_cnt=re.findall(r'wlan=.*\ssta_cnt=0\suse=.*',data2_string)
        if sys.argv[1]=='sta_cnt<0':
            entries_of_stat_cnt=re.findall(r'wlan=.*\ssta_cnt<0\suse=.*',data2_string)
        print entries_of_stat_cnt
        ssh.close()
    except Exception,details:
        print details
        sys.exit(1)
