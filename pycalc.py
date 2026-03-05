# Lecture des opérandes et de l'opérateur depuis la ligne de commandes
import sys
import math

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
  result = 0
  right_decimal, right_integer = math.modf(right)
  for i in range(0, int(right_integer)):
    result = result + left
  if right_decimal != 0:
    result = result + (left / (1 / right_decimal))

print(result)



