![](screen.png)

A noticeboard web-app built using django.

Remember to run these commands to set up the database and static files.
```
$ python manage.py syncdb
$ python manage.py collectstatic
```

You will also need to create ```local_settings.py``` and set
```SECRET_KEY``` in it.