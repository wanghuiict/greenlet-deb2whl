#!/bin/bash

DEB="python-greenlet_0.4.11-1deepin1_sw_64.deb"
DOWNURL="http://packagess.deepin.com:8082/pool/main/p/python-greenlet/$DEB"

if [ ! -f $DEB ]; then 
    wget $DOWNURL || exit 1
fi

md5sum -c deb_md5sum || exit 2
ar vx $DEB && \
{ tar zxvf control.tar.gz;
tar Jxvf data.tar.xz;
rm md5sums control control.tar.gz data.tar.xz debian-binary; }

pushd usr/lib/python2.7/dist-packages/ && \
{ mv greenlet.sw_64-linux-gnu.so greenlet.so;
popd; }

python setup.py bdist_wheel || exit 3
rm -rf ./usr/ ./build/ ./greenlet.egg-info/
