class EmployeeCollection:
    def __init__(self):
        self.collections = {}
    def createCollection(self, p_collection_name):
        if p_collection_name not in self.collections:
            self.collections[p_collection_name] = []
            print(f"Collection '{p_collection_name}' created.")
        else:
            print(f"Collection '{p_collection_name}' already exists.")
    def indexData(self, p_collection_name, p_exclude_column):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return
        sample_data = [
            {"id": "E00001", "name": "Alice", "department": "HR", "gender": "Female"},
            {"id": "E00002", "name": "Bob", "department": "Engineering", "gender": "Male"},
            {"id": "E00003", "name": "Charlie", "department": "Sales", "gender": "Male"},
            {"id": "E00004", "name": "David", "department": "Engineering", "gender": "Male"},
            {"id": "E00005", "name": "Eve", "department": "HR", "gender": "Female"},
        ]
        for record in sample_data:
            indexed_record = {k: v for k, v in record.items() if k != p_exclude_column}
            self.collections[p_collection_name].append(indexed_record)
        print(f"Data indexed into '{p_collection_name}' excluding '{p_exclude_column}'.")

    def searchByColumn(self, p_collection_name, p_column_name, p_column_value):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return []
        results = [
            record for record in self.collections[p_collection_name]
            if record.get(p_column_name) == p_column_value
        ]
        return results
    def getEmpCount(self, p_collection_name):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return 0
        return len(self.collections[p_collection_name])

    def delEmpById(self, p_collection_name, p_employee_id):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return
        initial_count = len(self.collections[p_collection_name])
        self.collections[p_collection_name] = [
            record for record in self.collections[p_collection_name] if record.get("id") != p_employee_id
        ]
        if len(self.collections[p_collection_name]) < initial_count:
            print(f"Employee with ID '{p_employee_id}' deleted from '{p_collection_name}'.")
        else:
            print(f"No employee with ID '{p_employee_id}' found in '{p_collection_name}'.")

    def getDepFacet(self, p_collection_name):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return {}
        department_count = {}
        for record in self.collections[p_collection_name]:
            dept = record.get("department")
            if dept:
                department_count[dept] = department_count.get(dept, 0) + 1
        return department_count
my_name = "Kalpana"
last_four_digits = "3565"
v_nameCollection = f"Hash_{my_name}"
v_phoneCollection = f"Hash_{last_four_digits}"
emp_collection = EmployeeCollection()
emp_collection.createCollection(v_nameCollection)
emp_collection.createCollection(v_phoneCollection)
print(f"Initial Employee Count in '{v_nameCollection}': {emp_collection.getEmpCount(v_nameCollection)}")
emp_collection.indexData(v_nameCollection, 'department')
emp_collection.indexData(v_phoneCollection, 'gender')
emp_collection.delEmpById(v_nameCollection, 'E02003')
print(f"Employee Count after indexing in '{v_nameCollection}': {emp_collection.getEmpCount(v_nameCollection)}")
print(f"Search results for 'IT' in '{v_nameCollection}': {emp_collection.searchByColumn(v_nameCollection, 'department', 'IT')}")
print(f"Search results for 'Male' in '{v_nameCollection}': {emp_collection.searchByColumn(v_nameCollection, 'gender', 'Male')}")
print(f"Search results for 'IT' in '{v_phoneCollection}': {emp_collection.searchByColumn(v_phoneCollection, 'department', 'IT')}")
print(f"Department facet counts in '{v_nameCollection}': {emp_collection.getDepFacet(v_nameCollection)}")
print(f"Department facet counts in '{v_phoneCollection}': {emp_collection.getDepFacet(v_phoneCollection)}")









