# Lecture des opérandes et de l'opérateur depuis la ligne de commandes
import sys

if len(sys.argv) != 4:
  print("Erreur : argument(s) manquant(s)", file=sys.stderr)
  sys.exit(1)

left = float(sys.argv[1])
operation = sys.argv[2]
right = float(sys.argv[3])

result = None

if operation == "+":
  result = left + right
elif operation == "-":
  result = left - right
elif operation == "*":
  result = left * right
elif operation == "/":
  result = left / right

print(result)



