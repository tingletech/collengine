"""
  Sample command line loading tool.  
  
  Run as python manage.py load_items -f path/to/file.csv.  
"""

import sys

from django.core.management.base import BaseCommand
from optparse import make_option

from datetime import timedelta
from datetime import date

import time
import django.conf as conf
import django.core.management.base as mb

from item.models import Item

class Command(BaseCommand):
    help = "For loading CSV files into database."
    option_list = BaseCommand.option_list + (
        make_option('-f', '--file', dest='source_file',
                    help='Loads Items.  Need specific format identified in new items.'),
    )
    def handle(self, **options):
        if options['source_file']:
          self.new_docs(options['source_file'])
        else:
          print 'no file specified'

    def new_items(self, source_file):
      import csv
      source_file = csv.reader(open(source_file))
      #Map row cells to Item object.  
      for row in source_file:
          #ID,Date Scanned,Username,,,,,
          item_id = row[0]
          iobj, created = Item.objects.get_or_create(item_id=item_id)
          iobj.save()
