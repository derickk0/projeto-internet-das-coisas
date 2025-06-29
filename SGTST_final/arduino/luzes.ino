/*
Nome do arquivo: luzes.ino
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
*/

/*
Cada LED representa as luzes de um setor:
	Laranja - Oficina
    Azul - Galpão
    Amarelo - Escritório
    Branco - Corredor
    Verde - Área de serviço
    Vermelho - Área externa
*/


int ledLaranja = 2;
int ledAzul1 = 3;
int ledAzul2 = 4;
int ledAzul3 = 5;
int ledAmarelo = 6;
int ledBranco = 7;
int ledVerde = 8;
int ledVermelho = 9;

void setup() {
  pinMode(ledLaranja, OUTPUT);
  pinMode(ledAzul1, OUTPUT);
  pinMode(ledAzul2, OUTPUT);
  pinMode(ledAzul3, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledBranco, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  char letra = Serial.read();
  
  if (letra == 'a') {
  	digitalWrite(ledLaranja, HIGH);
  } else if (letra == 'b'){
  	digitalWrite(ledLaranja, LOW);
  } else if (letra == 'c') {
  	digitalWrite(ledAmarelo, HIGH);
  } else if (letra == 'd'){
  	digitalWrite(ledAmarelo, LOW);
  } else if (letra == 'e') {
  	digitalWrite(ledBranco, HIGH);
  } else if (letra == 'f') {
  	digitalWrite(ledBranco,  LOW);
  } else if (letra == 'g') {
  	digitalWrite(ledVerde, HIGH);
  } else if (letra == 'h') {
  	digitalWrite(ledVerde, LOW);
  } else if (letra == 'i') {
  	digitalWrite(ledVermelho, HIGH);
  } else if (letra == 'j') {
  	digitalWrite(ledVermelho, LOW);
  }
  
  if (letra == 'k') {
  	digitalWrite(ledAzul1, HIGH);
    digitalWrite(ledAzul2, HIGH);
    digitalWrite(ledAzul3, HIGH);
  } else if (letra == 'l') {
  	digitalWrite(ledAzul1, HIGH);
    digitalWrite(ledAzul2, LOW);
    digitalWrite(ledAzul3, LOW);
  } else if (letra == 'm') {
  	digitalWrite(ledAzul1, LOW);
    digitalWrite(ledAzul2, HIGH);
    digitalWrite(ledAzul3, LOW);
  } else if (letra == 'n'){
  	digitalWrite(ledAzul1, LOW);
    digitalWrite(ledAzul2, LOW);
    digitalWrite(ledAzul3, HIGH);
  } else if (letra == 'o'){
  	digitalWrite(ledAzul1, LOW);
    digitalWrite(ledAzul2, LOW);
    digitalWrite(ledAzul3, LOW);
  }
  delay(100);
}