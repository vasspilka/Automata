import config
import os

backend_path = os.path.dirname(os.path.realpath(__file__))

print("Installing Python requirements")
ans = raw_input("Run pip install with sudo? y/n \n")
if ans == 'y' or ans == 'yes':
    os.system("sudo pip install -r " + backend_path + "/../requirements.txt")
else:
    os.system("pip install -r " + backend_path + "/../requirements.txt")

print("\n\nCreating `.htaccess` in Automata")
with open(backend_path + '/../.htaccess', 'w') as htaccess:
    htaccess.write("""<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteRule (.*) http://%s:%s/$1 [P,QSA]
</IfModule>""" % (config.HOST, config.PORT))

import db
DB = db.Database(config.SQL.HOST, config.SQL.USERNAME,
                 config.SQL.PASSWORD, config.SQL.DATABASE)

print("\n\nConnected to database")

ans = raw_input("Do you want to delete the old tables?\n"
                + "Type n if no previous tables. y/n  \n")

if ans == 'y' or ans == 'yes':
    print("Deleting old users and automata tables\n")
    DB.query("DROP TABLE users; DROP TABLE automata;", data=[])

tables = open(backend_path + '/etc/automata.sql', 'r')
print("\nCreating new tables\n")
DB.query(tables.read(), data=[])

print("\nSetup complete succesfully")
