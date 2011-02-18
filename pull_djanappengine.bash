#!/usr/bin/env bash
# automates the steps in http://www.allbuttonspressed.com/projects/djangoappengine
set -eux
rm -rf django djangoappengine djangotoolbox django-dbindexer dbindexer django-nonrel permission_backend_nonrel
rm -rf tablib django_tablib
curl https://bitbucket.org/wkornewald/django-nonrel/get/tip.tar.gz | tar zxf -
curl https://bitbucket.org/wkornewald/djangoappengine/get/tip.tar.gz | tar zxf -
curl https://bitbucket.org/wkornewald/djangotoolbox/get/tip.tar.gz | tar zxf -
curl https://bitbucket.org/wkornewald/django-dbindexer/get/tip.tar.gz | tar zxf -
curl https://bitbucket.org/fhahn/django-permission-backend-nonrel/get/tip.tar.gz | tar zxf -
curl http://pypi.python.org/packages/source/t/tablib/tablib-0.9.4.tar.gz | tar zxf -
curl http://pypi.python.org/packages/source/d/django-tablib/django-tablib-2.2.1.tar.gz | tar zxf -
mv django-nonrel/django django
mv djangotoolbox/djangotoolbox djangotoolbox-djangotoolbox
rm -rf djangotoolbox
mv djangotoolbox-djangotoolbox djangotoolbox
mv django-dbindexer/dbindexer dbindexer
mv django-permission-backend-nonrel/permission_backend_nonrel/ .
mv tablib-0.9.4/tablib .
mv django-tablib-2.2.1/django_tablib/ .
rm -rf django-permission-backend-nonrel django-tablib-2.2.1 tablib-0.9.4

# need to fit under 3000 files; remove non-english locales from django
shopt -s extglob
for i in `find django -name "locale"`
do
  if [ -e $i ]; then
    mkdir -p $i/xx	# hack, sometimes there is only an "en" directory in locale and the next line would fail
    rm -rf $i/!(en*)
  fi
done
