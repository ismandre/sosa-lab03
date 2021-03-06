import getpass

class OperationsManager():
	def __init__(self, a: float, b: float) -> None:
		self.a = a
		self.b = b
	def perform_division(self) -> float:
		"""Divides a with b. If b is zero, returns NaN."""
		if (self.b == 0):
			return float('nan')
		return self.a / self.b

if __name__ == "__main__":
	user = input("Username: ")
	password = getpass.getpass("Password: ")
	if user != "root" or password != "123":
		print("Wrong username or password!")
		exit(0)
	else:
		print("Login success!")
		a = float(input("A = "))
		b = float(input("B = "))
		ops_manager = OperationsManager(a, b)
		print(ops_manager.perform_division())