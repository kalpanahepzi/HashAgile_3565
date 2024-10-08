**Hash Agile Assignment: Employee Data Management**


**Overview**
This project involves creating and executing various functions to manage employee data within collections. Functions include creating collections, indexing data, searching data, counting employees, and retrieving department-based facets.


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
