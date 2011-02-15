#!/usr/bin/env bash
# automates the steps in http://www.allbuttonspressed.com/projects/djangoappengine
set -eux
rm -rf django djangoappengine djangotoolbox django-dbindexer dbindexer 
curl https://bitbucket.org/wkornewald/django-nonrel/get/tip.tar.gz | tar zxf -
curl https://bitbucket.org/wkornewald/djangoappengine/get/tip.tar.gz | tar zxf -
curl https://bitbucket.org/wkornewald/djangotoolbox/get/tip.tar.gz | tar zxf -
curl https://bitbucket.org/wkornewald/django-dbindexer/get/tip.tar.gz | tar zxf -
mv django-nonrel/django django
mv djangotoolbox/djangotoolbox djangotoolbox-djangotoolbox
rm -rf djangotoolbox
mv djangotoolbox-djangotoolbox djangotoolbox
mv django-dbindexer/dbindexer dbindexer

