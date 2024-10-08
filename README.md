**Hash Agile Assignment: Employee Data Management**
**Overview**
This project involves creating and executing various functions to manage employee data within collections. Functions include creating collections, indexing data, searching data, counting employees, and retrieving department-based facets.

**Programming Language:**
Implemented in: [Language Name (e.g., JavaScript, Python)]
**Function Definitions**
**a) createCollection(p_collection_name)**
Purpose: Creates a collection with the specified name.
Parameters:
p_collection_name: Name of the collection.
**b) indexData(p_collection_name, p_exclude_column)**
Purpose: Indexes employee data into the specified collection, excluding the provided column.
Parameters:
p_collection_name: Name of the collection.
p_exclude_column: Column to be excluded from the data indexing.
**c) searchByColumn(p_collection_name, p_column_name, p_column_value)**
Purpose: Searches the collection for records where the specified column matches the given value.
Parameters:
p_collection_name: Name of the collection.
p_column_name: Column to search within.
p_column_value: Value to search for in the specified column.
**d) getEmpCount(p_collection_name)**
Purpose: Retrieves the count of employees within the specified collection.
Parameters:
p_collection_name: Name of the collection.
**e) delEmpById(p_collection_name, p_employee_id)**
Purpose: Deletes the employee record from the collection based on the employee ID.
Parameters:
p_collection_name: Name of the collection.
p_employee_id: ID of the employee to be deleted.
**f) getDepFacet(p_collection_name)**
Purpose: Retrieves the count of employees grouped by department from the collection.
Parameters:
p_collection_name: Name of the collection.
**Execution Steps**
The functions will be executed in the following order:

1. Define variables:
var v_nameCollection = 'Hash_<Your Name>';
var v_phoneCollection = 'Hash_<Your Phone last four digits>';

2. Create collections:
createCollection(v_nameCollection);
createCollection(v_phoneCollection);

3. Get employee count from v_nameCollection:
getEmpCount(v_nameCollection);

4. Index data into collections, excluding specified columns:
indexData(v_nameCollection, 'Department');
indexData(v_phoneCollection, 'Gender');

5. Get employee count after indexing:
getEmpCount(v_nameCollection);

6. Delete employee with ID 'E02003' from v_nameCollection:
delEmpById(v_nameCollection, 'E02003');

7. Get employee count after deletion:
getEmpCount(v_nameCollection);

8. Search within collections based on column values:
searchByColumn(v_nameCollection, 'Department', 'IT');
searchByColumn(v_nameCollection, 'Gender', 'Male');
searchByColumn(v_phoneCollection, 'Department', 'IT');

9. Retrieve department-based employee counts (facets):
getDepFacet(v_nameCollection);
getDepFacet(v_phoneCollection);

**Conclusion**
This project demonstrates the ability to manage and manipulate employee data collections programmatically. The outlined steps ensure data integrity and efficient querying.
