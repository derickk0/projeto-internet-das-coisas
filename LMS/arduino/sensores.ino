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
  int pirValue = digitalRead(sensorMovimento);
  int ldrValue = analogRead(sensorLuminosidade);
  int tempValue = analogRead(sensorTemperatura);
  
  float voltage = tempValue * (5.0 / 1023.0);
  float temperatureC = (voltage - 0.5) * 100;
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

  if (ldrValue < 900) {
    digitalWrite(ledBranco, HIGH);
  } else {
    digitalWrite(ledBranco, LOW);
  }

  if (pirValue == HIGH) {
    digitalWrite(buzzer, HIGH);
    digitalWrite(ledVermelho, HIGH);
  } else {
    digitalWrite(buzzer, LOW);
    digitalWrite(ledVermelho, LOW);
  }

  if (temperatureC > 50.0) {
    digitalWrite(buzzer, HIGH);
    digitalWrite(ledVermelho, HIGH);
  }

  Serial.print("Presenca: ");
  Serial.print(pirValue);
  Serial.print(" | Luminosidade: ");
  Serial.print(ldrValue);
  Serial.print(" | Temperatura: ");
  Serial.print(temperatureC);
  Serial.print("C ");
  Serial.print(temperatureF);
  Serial.println("F");

  delay(1000);
}