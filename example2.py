from shiba.__init__ import ShibaConnection

cx = ShibaConnection(host='localhost', port=3308, user='root', password='duoc')
# cx.create_database('hola2')
cx.use_database('hola2')

""" table_builder = cx.create_table('example1')
table_builder.string('name').primary()
table_builder.build() """


table_builder = cx.create_table('example2')
table_builder.increments().primary()
table_builder.string('name').foreign(foreign_name='fk_exam1_name', table_name='example1', column_name='name')

# ADD ENUM 
table_builder.enum('color', ['rojo', 'azul', 'negro'])
table_builder.build()

print (table_builder)
