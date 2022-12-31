
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["pikachu","squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])      #method
table.add_row(("Bulbasour","Grass"))

table.align = "l"     #attribute
print(table)