int num1=0;
int num2=0;
int soma=0;
bool recebeuNum1 = false;
bool recebeuNum2 = false;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.print("Digite o primeiro número: ");

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    String entrada= Sereal.readStringUntil('\n');
    entrad.trim();
  }

  if(!recebeuNum1){
    num1 = entrada.toInt();
    recebeuNum1= true;
    Serial.println("Digite o segundo numero: ");
  }else if(!recebeuNum2){
    num2 = entrada.toInt();
    recebeuNum2= true;

    soma= num1+num2;
    Serial.println("A soma dos numeros é: ",soma);
    Serial.println(soma);
  }
}
