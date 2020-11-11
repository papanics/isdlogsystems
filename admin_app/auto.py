from pyad import *


#ou = pyad.adcontainer.ADContainer.from_dn("OU=NCCCUsers,DC=int, DC=nccc,DC=com, DC=ph")
#for obj in ou.get_children():
 #       print(obj.OU)

import pyad.adquery
q = pyad.adquery.ADQuery()

q.execute_query(
    attributes = ["cn","title","EmployeeID","sAMAccountName","title","mail", "description"],
    where_clause = "objectClass = '*'",
    base_dn = "OU=NCCCUsers,DC=int,DC=nccc,DC=com,DC=ph"
)

for row in q.get_results():
    print(row["cn"],row["title"],row["EmployeeID"], row["sAMAccountName"], row["mail"], )
