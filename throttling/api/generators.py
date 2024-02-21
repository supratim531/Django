ID = 1

def employee_id_generator():
  global ID
  emp_id = f"CODEZ-EMP-{ID}"
  ID += 1
  return emp_id
