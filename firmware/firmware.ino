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

void loop()
{
  if (stringComplete)
  {
    inputString.substring(0, 3);
    Serial.println(inputString);
    int num = inputString.toInt();
    if (num < 1999)
    {
      int val0 = num - 1000;
      move_axis(1, val0);
    }
    if (num > 2000 and num < 2999)
    {
      int val1 = num - 2000;
      move_axis(2, val1);
    }
    if (num > 3000 and num < 3999)
    {
      int val2 = num - 3000;
      move_axis(3, val2);
    }
    if (num > 4000 and num < 4999)
    {
      int val3 = num - 4000;
      move_axis(4, val3);
    }
    if (num == 5001)
    {
      move_axis(5, 1);
    }
    if (num == 5000)
    {
      move_axis(5, 0);
    }

    inputString = "";
    stringComplete = false;
  }
}
// move_axis function
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

  if (servoId == 4)
  {
    eff.write(position);
    delay(10);
  }
  if (servoId == 5)
  {
    if (position == 1)
    {
      // inverse logic for relay
      digitalWrite(pin_grip, LOW);
    }
    if (position == 0)
    {
      // inverse logic for relay
      digitalWrite(pin_grip, HIGH);
    }
  }
  if (servoId == 6)
  {
    if (position == 1)
    {
      digitalWrite(pin_belt, HIGH);
    }
    if (position == 0)
    {
      digitalWrite(pin_belt, LOW);
    }
  }
  if (servoId == 7)
  {
    if (position == 1)
    {
      digitalWrite(pin_belt_turn, HIGH); // forward
    }
    if (position == 0)
    {
      digitalWrite(pin_belt_turn, LOW); // backward
    }
  }
}
