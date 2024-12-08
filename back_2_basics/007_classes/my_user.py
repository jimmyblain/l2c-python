# 9-11, 12
# Import the entire module. Must use dot notation.
# Only need to import entire admin module, since this includes user module import.
import admin

# Specify the user module, then call the class
tenant_admin = admin.Admin('super', 'user', 0, 'male')

tenant_admin.describe_user()
tenant_admin.privileges.show_privileges()
