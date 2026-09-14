# Puxo do Docker Hub a base oficial e mais leve do Python
FROM python:3.11-slim

# Crio a pasta onde minha aplicacao vai viver la dentro
WORKDIR /app

# Jogo meu codigo paladino.py pra dentro da maquina isolada
COPY paladino.py .

# Rodo meu script e garanto que o container fique em pe pro docker ps enxergar
CMD ["python", "-c", "import paladino, time; print('Paladino online e operando no container!'); [time.sleep(3600) for _ in iter(int, 1)]"]
