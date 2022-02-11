whiile true
do
    count=`ps -ef|grep run.py | grep -v grep`
    if [ "$?" != "0" ]
    then
        echo "$(date "+%Y-%m-%d %H:%M:%S") > 程序挂掉， 开始restart" >> log.tt
        cd /root/blx/tornado_frame_project/yiTuShiBie/src && /root/miniconda3/bin/python run.py >> run.log 2 >&1
    else
        echo " $(date "+%Y-%m-%d %H:%M:%S") > tomcat is running..." >> log.tt
    fi
    sleep 10
done
