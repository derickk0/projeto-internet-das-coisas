/*
Nome do arquivo: sensores.ino
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
*/

int sensorLuminosidade = A0;
int sensorMovimento = 2;
int sensorTemperatura = A1;
int ledLaranja = 6;
int ledVermelho = 5;
int ledBranco = 7;
int buzzer = 4;

void setup() {
  pinMode(sensorMovimento, INPUT);
  pinMode(ledVermelho, OUTPUT);
  pinMode(ledLaranja, OUTPUT);
  pinMode(ledBranco, OUTPUT);
  pinMode(buzzer, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  // Leitura dos sensores
  int pirValue = digitalRead(sensorMovimento);
  int ldrValue = analogRead(sensorLuminosidade);
  int tempValue = analogRead(sensorTemperatura);
  
  // Convertendo valor analógico da temperatura (LM35)
  float temperature = (tempValue * 5.0 / 1023.0) * 100;

  // Controle da luz
  if (ldrValue < 900) { // ambiente escuro
    digitalWrite(ledBranco, HIGH);
  } else {
    digitalWrite(ledBranco, LOW);
  }

  // Alarme de presença
  if (pirValue == HIGH) {
    digitalWrite(buzzer, HIGH);
    digitalWrite(ledVermelho, HIGH);
  } else {
    digitalWrite(buzzer, LOW);
    digitalWrite(ledVermelho, LOW);
  }

  // Sirene se temperatura for muito alta (ex: +50°C)
  if (temperature > 90.0) {
    digitalWrite(buzzer, HIGH); // Pode ser uma sirene separada
    digitalWrite(ledVermelho, HIGH);
  }

  // Envio de dados para o Python
  Serial.print("Presenca: ");
  Serial.print(pirValue);
  Serial.print(" | Luminosidade: ");
  Serial.print(ldrValue);
  Serial.print(" | Temperatura: ");
  Serial.println(temperature);

  delay(1000); // 1 segundo de intervalo
}