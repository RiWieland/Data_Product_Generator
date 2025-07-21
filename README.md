
-- work in progress

# Purpose
Tool to generate a data mesh style data prodcuts. These data tables - pysically rolled out as Delta tables - contain generated psydo data.


## Description

### Data mesh style Data Product
The data products correspond in the file structure and the content to the Data Products defined in the apps/data_generator_simualtion/DP_ and are rolled out to the data sink defined in the docker compose.
By default, the target of the roll out is on a file system. On the specificied path, a delta table is created.

The data products consist of tables defined in the sub folders. Beside the name, the main components that is contained there is the table definition schema.

The data tables methods (insert, read, etc.) are defined in the abstract class in apps/data_generator_simualtion/abstract and inherited through the abstract class.

In the default setting, the data products are rolled out corresponding to the file structure in the correponding Data Product dir.

### Data Generator

In the default setting, all tables mentioned above are filled with generated data. This data is currently generated for the following simple data types: INT, DOUBLE, STR.
All columns are filled with data acording to their data types.


## Implementation
The data generation and the roll out of the Delta tables is achived by a spark standalone cluster run in seperate docker containers (currently one master and two worker notes). For the definition, see the docker file and docker-compose file.
In the setting of the author, these docker containers are executed via colima container runtime.

<img width="493" alt="image" src="https://github.com/user-attachments/assets/e536dbdd-90e7-4447-b66a-5effaa339efc" />


