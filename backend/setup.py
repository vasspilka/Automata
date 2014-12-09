import config
import db
import os

current_folder_path, current_folder_name = os.path.split(os.getcwd())

if (current_folder_name == "backend"):
  print("Creating `.htaccess` in " + current_folder_path)

  with open('../.htaccess', 'w') as htaccess:
    htaccess.write("""<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteRule api/(.*) http://%s:%s/$1 [P,QSA]
</IfModule>""" % (config.HOST, config.PORT))

    DB=db.Database(config.SQL.HOST, config.SQL.USERNAME, config.SQL.PASSWORD, config.SQL.DATABASE)
    print("Connected to database\n")

    ans = raw_input('Do you want to delete the old tables?\nType n if no previous tables. y/n  \n')
    if (ans == 'y' or ans == 'yes'):
      print("Deleting old users and automata tables\n")
      DB.query("DROP TABLE users; DROP TABLE automata;",data=[])

    tables = open('etc/automata.sql', 'r')
    print("\nCreating new tables\n")
    DB.query(tables.read(),data=[])

    print("\n Setup complete succesfully")
else:
    print("Please `cd` into the backend directory")
