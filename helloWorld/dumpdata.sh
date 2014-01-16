python manage.py dumpdata \
         --exclude sessions \
         --exclude contenttypes \
         --exclude auth \
         --indent 2 > initial_data.json
