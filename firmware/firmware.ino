#include <Servo.h>
#define pin_base 3
#define pin_L1 5
#define pin_L2 6
#define pin_eff 9       // manage gripper
#define pin_grip 7      // manage relay
#define pin_belt 8      // manage belt status
#define pin_belt_turn 4 // manage belt forward-backward

Servo base;
Servo L1;
Servo L2;
Servo eff;

int poser = 0; // initial position of server
int val;       // initial value of input

String inputString = "";
bool stringComplete = false;
// Homing
void axis_home()
{
  base.write(90);
  L1.write(90);
  L2.write(90);
  eff.write(90);
}

void setup()
{
  // Attach servos
  Serial.begin(115200);
  base.attach(pin_base);
  L1.attach(pin_L1);
  L2.attach(pin_L2);
  eff.attach(pin_eff);
  pinMode(pin_grip, OUTPUT);
  pinMode(pin_belt, OUTPUT);
  digitalWrite(pin_grip, HIGH); // relay init off inverse logic
  digitalWrite(pin_belt, LOW);  // belt init off

  // Homing inicial
  axis_home();
}

void serialEvent()
{
  while (Serial.available())
  {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n')
    {
      stringComplete = true;
    }
  }
}
void move_axis(int servoId, int position)
{
  if (servoId == 1)
  {
    base.write(position);
    delay(10);
  }

  if (servoId == 2)
  {
    L1.write(position);
    delay(10);
  }

  if (servoId == 3)
  {
    L2.write(position);
    delay(10);
  }


}
void loop()
{
   if (stringComplete)
  {
    // take the 6 first characters of the string
    // and compare it with "CMDVEL"
    if (inputString.substring(0, 6) == "MOVEAX")
    {
      // take and split the next 6 characters of the string
      int q0 = inputString.substring(6, 9).toInt();
      int q1 = inputString.substring(9, 12).toInt();
      int q2 = inputString.substring(12, 15).toInt();
      move_axis(1, q0);
      move_axis(2, q1);
      move_axis(3, q2);

    inputString = "";
    stringComplete = false;
  }
}
// move_axis function

}
