from prettytable import PrettyTable
table=PrettyTable()

table.add_column("Pokeman name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)