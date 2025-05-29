class Department:
    department_count = 0
    dept_id_counter = 501  

    def __init__(self, name, location):
        self.dept_id = Department.dept_id_counter
        self.name = name
        self.location = location
        Department.department_count += 1
        Department.dept_id_counter += 1

    def display_info(self):
        print("Department Information:")
        print("------------------------")
        print(f"ID: {self.dept_id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")

    @classmethod
    def get_total_departments(cls):
        return cls.department_count

d1 = Department("HR", "Hyderabad")
d2 = Department("Finance", "Mumbai")
d3 = Department("IT", "Bangalore")

d1.display_info()
d2.display_info()
d3.display_info()

print(f"\nTotal Departments: {Department.get_total_departments()}")

class Department:
    department_count = 0
    dept_id_counter = 501

    def __init__(self, name, location):
        self.dept_id = Department.dept_id_counter
        self.name = name
        self.location = location
        Department.department_count += 1
        Department.dept_id_counter += 1

    def display_info(self):
        print("Department Information:")
        print("------------------------")
        print(f"ID: {self.dept_id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")

    @classmethod
    def get_total_departments(cls):
        return cls.department_count

departments = {}

num_depts = int(input("Enter the number of departments to add: "))

for _ in range(num_depts):
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    dept = Department(name, location)
    departments[dept.dept_id] = dept
    print(f"Department {dept.dept_id} added successfully!\n")

print("\nAll Departments:")
for dept in departments.values():
    dept.display_info()

def search_by_id(dept_id):
    if dept_id in departments:
        departments[dept_id].display_info()
    else:
        print(f"No department found with ID {dept_id}")

def search_by_name(name_part):
    found = False
    for dept in departments.values():
        if name_part.lower() in dept.name.lower():
            dept.display_info()
            found = True
    if not found:
        print("No matching department found.")

while True:
    print("\n--- Department Search Menu ---")
    print("1. Search by Department ID")
    print("2. Search by Department Name")
    print("3. Exit")
    option = input("Enter your choice: ")

    if option == "1":
        try:
            did = int(input("Enter Department ID to search: "))
            search_by_id(did)
        except ValueError:
            print("Please enter a valid ID.")
    elif option == "2":
        name_input = input("Enter name to search: ")
        search_by_name(name_input)
    elif option == "3":
        print("Exiting search.")
        break
    else:
        print("Invalid option. Please try again.")
