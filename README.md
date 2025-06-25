
-- work in progress

Tool to generate a data mesh style data prodcuts including data tables - pysically defined as Delta tables and filled with generated psydo data.

The data generation and the roll out of the Delta tables is achived by a spark cluster run in seperate docker containers (currently one master and two worker notes) in a network. For the definition, see the docker file and docker-compose file.
In the setting of the author, these docker containers are executed via colima container runtime.


1. Roll out data mesh style Data Product
Tool for auto-generate and roll out a data mesh style data products. 
These data products correspond in the file structure and the content to the Data Products defined in the apps/data_generator_simualtion/DP_.

The data products defined there consist of tables difined in the sub folders. Beside the name, the main components that is contained there is the table definition schema.

The data tables functionality are defined in the abstract class in apps/data_generator_simualtion/abstract and inherited through the abstract class.

In the default setting, the data products are rolled out corresponding to the file structure in the correponding Data Product dir.

2. Data Generator

In the default setting, all tables mentioned in 1. are filled with automatically generated data. This data is currently generated for the following simple data types: INT, DOUBLE, STR.
All columns are filled with data acording to their data types.
