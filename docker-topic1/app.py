import os

name = os.getenv("NAME", "Mundo")
greeting = os.getenv("GREETING", "Olá")

print(f"{greeting}, {name}! Aqui é o Docker Integrador.")