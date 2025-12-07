from sys import stdin

class Staff:
    def __init__ (self, id, name, dept, salary, days):
        self.id = id
        self.dept = dept
        self.name = name
        self.salary = salary
        self.days = days

    def const(self):
        id = self.id
        y = int(id[1:3])
        if id[0] == 'A':
            if y < 4: return 10
            elif y < 9 : return 12
            elif y < 16 : return 14
            else : return 20
        elif id[0] == 'B':
            if y < 4: return 10
            elif y < 9 : return 11
            elif y < 16 : return 13
            else : return 16
        elif id[0] == 'C':
            if y < 4: return 9
            elif y < 9 : return 10
            elif y < 16 : return 12
            else : return 14
        else : 
            if y < 4: return 8
            elif y < 9 : return 9
            elif y < 16 : return 11
            else : return 13
        
    def getTotal(self):
        return self.salary * self.days * self.const()

    def __str__ (self):
        return f"{self.id} {self.name} {self.dept} {self.getTotal() * 1000}"

def main():
    depts = {}
    for _ in range(int(stdin.readline())):
        dept_raw = stdin.readline().split()
        deptId = dept_raw[0]
        dept = " ".join(dept_raw[1:])
        depts[deptId] = dept
    staffs = []
    for _ in range(int(stdin.readline())):
        id = stdin.readline().strip()
        name = stdin.readline().strip()
        salary = int(stdin.readline())
        days = int(stdin.readline())
        staffs.append(Staff(id, name, ''.join(depts[id[3:]]), salary, days))
    for staff in staffs:
        print(staff)


if __name__ == "__main__":
    main()