# Knowledge Assessment Quiz: Arduino Embedded Systems & Programming (Arduino Learning)

╔══════════════════════════════════════════════════════════════════════╗
║  QUIZ DATA — SciMaster Platform (Arduino Embedded Systems)          ║
╚══════════════════════════════════════════════════════════════════════╝

---

## Document Summary (สรุปเนื้อหาเอกสารและหลักสูตร Arduino Embedded Systems)

เอกสารฉบับนี้รวบรวมเนื้อหาและโจทย์ประเมินผลการเรียนรู้การเขียนโปรแกรมและการพัฒนาโครงงานระบบสมองกลฝังตัวด้วยบอร์ด Arduino (อ้างอิงจาก Arduino Learning Guide) ครอบคลุมสาระสำคัญ 4 หน่วยการเรียนรู้หลัก ได้แก่:

### 1. หน่วยการเรียนรู้ที่ 1: สถาปัตยกรรมฮาร์ดแวร์และโครงสร้างพื้นฐาน (Hardware Architecture & IDE Basics)
* **บอร์ด Arduino Uno R3**: ไมโครคอนโทรลเลอร์ ATmega328P, ขา Digital I/O (0–13), ขา Analog Input (A0–A5), ขาจ่ายไฟ (5V, 3.3V, GND, Vin), Clock Speed 16 MHz, และปุ่ม Reset
* **โปรแกรม Arduino IDE**: โครงสร้างสเก็ตช์พื้นฐานฟังก์ชัน `setup()` และ `loop()`, กระบวนการ Compile (Verify), Upload, การเลือก Board และ Serial Port (COM Port)

### 2. หน่วยการเรียนรู้ที่ 2: สัญญาณดิจิทัล แอนะล็อก และตัวขับเคลื่อน (Digital/Analog I/O, PWM & Actuators)
* **Digital I/O**: คำสั่ง `pinMode()`, `digitalWrite()`, `digitalRead()`, ตัวต้านทานภายในบอร์ด `INPUT_PULLUP`
* **Analog Input**: วงจร ADC ขนาด 10-bit (0–1023) ผ่านคำสั่ง `analogRead()`, การคำนวณแปลงค่าเป็นแรงดันไฟฟ้าจริง (0–5V)
* **PWM (Pulse Width Modulation)**: สัญญาณความกว้างพัลส์ขนาด 8-bit (0–255) ผ่านคำสั่ง `analogWrite()` บนขาที่มีสัญลักษณ์ `~` (ขา 3, 5, 6, 9, 10, 11) สำหรับหรี่ไฟ LED และควบคุมความเร็วมอเตอร์
* **Actuators & Displays**: การควบคุมเซอร์โวมอเตอร์ด้วยไลบรารี `Servo.h`, การสร้างสัญญาณเสียงด้วย `tone()` / `noTone()`, และการแสดงผลบนจอ LCD ด้วยไลบรารี `LiquidCrystal.h`

### 3. หน่วยการเรียนรู้ที่ 3: การสื่อสารข้อมูลและการจัดเก็บข้อมูล (Serial, Protocols & Data Storage)
* **Serial Communication (UART)**: คำสั่ง `Serial.begin()`, Baud Rate (เช่น 9600, 115200), `Serial.print()`, `Serial.println()`, `Serial.read()`, `Serial.available()`, และการเชื่อมต่อสื่อสารกับ Python ผ่านไลบรารี `pyserial`
* **Communication Protocols**: การสื่อสารแบบ I2C (`Wire.h`, ขา SDA/SCL บนขา A4/A5 ของ Uno, การระบุ Address), การสื่อสารแบบ SPI (`SPI.h`, ขา MOSI/MISO/SCK/SS), และโมดูลบลูทูธ (HC-05/HC-06 ผ่าน `SoftwareSerial`)
* **Data Storage**: หน่วยความจำถาวร EEPROM (`EEPROM.h`, `read()`, `write()`, `update()`) และการบันทึกข้อมูลลง MicroSD Card (`SD.h`)

### 4. หน่วยการเรียนรู้ที่ 4: การจัดการเวลา อินเทอร์รัปต์ และการเขียนโปรแกรมขั้นสูง (Timing, Interrupts & Best Practices)
* **Time Management**: การทำงานแบบ Blocking ด้วย `delay()` vs การทำงานแบบ Non-blocking ด้วยฟังก์ชัน `millis()` / `micros()` เพื่อทำงานหลายงานพร้อมกัน (Multitasking)
* **External Hardware Interrupts**: คำสั่ง `attachInterrupt()`, `digitalPinToInterrupt()`, โหมดตรวจจับ (`RISING`, `FALLING`, `CHANGE`, `LOW`), การสร้างฟังก์ชัน ISR (Interrupt Service Routine) และการใช้คีย์เวิร์ด `volatile`
* **Programming Concepts**: ชนิดข้อมูล (Data Types: `int`, `byte`, `float`, `boolean`, `char`, `unsigned long`), ตัวแปรอาร์เรย์ (Arrays), โครงสร้างควบคุม (`if-else`, `switch-case`, `for`, `while`, `do-while`), และการสร้างฟังก์ชันย่อย

---

## Learning Objectives Mapping (แผนผังจุดประสงค์การเรียนรู้)

* **LO-ARD1**: Knowledge & Understanding of Arduino hardware pinout, Uno architecture, IDE workflow, and C/C++ syntax.
* **LO-ARD2**: Application of Digital/Analog I/O, PWM modulation, sensor data reading, actuators, and non-blocking timers.
* **LO-ARD3**: Analysis of Communication protocols (UART Serial, I2C, SPI, Bluetooth) and non-volatile storage (EEPROM, SD).
* **LO-ARD4**: Evaluation, Debugging & Synthesis of Embedded systems, Interrupt Service Routines (ISRs), and Python integration.

---

## สรุปคะแนนรวม

| ส่วน | จำนวนข้อ | คะแนน/ข้อ | คะแนนรวม |
|------|----------|-----------|----------|
| A: ปรนัย (MCQ) | 60 | 1 | 60 |
| B: ถูก/ผิด (TF) | 30 | 1 | 30 |
| C: สถานการณ์ (Scenario) | 15 | 2 | 30 |
| D: อัตนัย (ShortAnswer) | 10 | 3 | 30 |
| **รวม** | **115** | — | **150** |
| **เกณฑ์ผ่าน (80%)** | — | — | **120** |

---

# Section A: Multiple Choice Questions (ปรนัย 4 ตัวเลือก)
#### ข้อ 1
* **Topic**: Arduino Architecture
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: Which main microcontroller chip powers the standard Arduino Uno R3 board?
* ก. ATmega328P
* ข. ARM Cortex-M4
* ค. ESP8266
* ง. PIC16F877A
* **Correct Answer**: ก
* **Explanation**: The Arduino Uno R3 is powered by the 8-bit Microchip/Atmel ATmega328P microcontroller running at 16 MHz.
#### ข้อ 2
* **Topic**: Sketch Structure
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: What are the two mandatory functions that every Arduino sketch (.ino) must contain?
* ก. start() and stop()
* ข. setup() and loop()
* ค. init() and main()
* ง. begin() and run()
* **Correct Answer**: ข
* **Explanation**: Every Arduino program requires setup() (runs once at boot) and loop() (executes repeatedly indefinitely).
#### ข้อ 3
* **Topic**: Execution Flow
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: When an Arduino board is powered on, how many times does the setup() function execute?
* ก. Only once
* ข. Repeatedly in an infinite loop
* ค. Exactly 10 times
* ง. Only when a button is pressed
* **Correct Answer**: ก
* **Explanation**: The setup() function executes exactly once upon power-up or whenever the reset button is pressed.
#### ข้อ 4
* **Topic**: Operating Voltage
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: What is the standard operating logic voltage of the digital pins on an Arduino Uno R3?
* ก. 1.8V
* ข. 3.3V
* ค. 5V
* ง. 12V
* **Correct Answer**: ค
* **Explanation**: The Arduino Uno R3 operates at 5V logic level, meaning HIGH is ~5V and LOW is 0V (GND).
#### ข้อ 5
* **Topic**: Hardware Pinout
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: How many total Digital I/O pins are available on an Arduino Uno board (excluding dedicated analog-only pins)?
* ก. 8 pins
* ข. 14 pins (Pins 0 to 13)
* ค. 20 pins
* ง. 32 pins
* **Correct Answer**: ข
* **Explanation**: Arduino Uno features 14 digital I/O pins numbered from 0 to 13 (six of which support PWM output).
#### ข้อ 6
* **Topic**: Analog Inputs
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: How many dedicated Analog Input pins (A0 to A5) are provided on an Arduino Uno?
* ก. 4 pins
* ข. 6 pins
* ค. 8 pins
* ง. 12 pins
* **Correct Answer**: ข
* **Explanation**: Arduino Uno provides 6 analog input pins labeled A0, A1, A2, A3, A4, and A5.
#### ข้อ 7
* **Topic**: ADC Resolution
* **Learning Objective**: LO-ARD1
* **Difficulty**: Medium
* **Prompt**: What is the resolution of the Analog-to-Digital Converter (ADC) in the Arduino Uno?
* ก. 8-bit (0 to 255)
* ข. 10-bit (0 to 1023)
* ค. 12-bit (0 to 4095)
* ง. 16-bit (0 to 65535)
* **Correct Answer**: ข
* **Explanation**: The ATmega328P contains a 10-bit ADC, mapping 0 to 5V input into an integer range from 0 to 1023.
#### ข้อ 8
* **Topic**: Clock Speed
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: What is the crystal oscillator clock frequency of the Arduino Uno R3?
* ก. 8 MHz
* ข. 16 MHz
* ค. 48 MHz
* ง. 100 MHz
* **Correct Answer**: ข
* **Explanation**: The Arduino Uno operates with a 16 MHz external ceramic resonator / quartz crystal.
#### ข้อ 9
* **Topic**: Built-in LED Pin
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: Which digital pin on the Arduino Uno is connected to the on-board surface-mount LED (LED_BUILTIN)?
* ก. Pin 0
* ข. Pin 2
* ค. Pin 9
* ง. Pin 13
* **Correct Answer**: ง
* **Explanation**: Pin 13 is internally wired to the on-board LED through an active driver circuit on Arduino Uno.
#### ข้อ 10
* **Topic**: Hardware Serial Pins
* **Learning Objective**: LO-ARD1
* **Difficulty**: Medium
* **Prompt**: Which two digital pins on the Arduino Uno serve as the primary hardware UART Serial pins (RX and TX)?
* ก. Pin 0 (RX) and Pin 1 (TX)
* ข. Pin 2 (RX) and Pin 3 (TX)
* ค. Pin 10 (RX) and Pin 11 (TX)
* ง. Pin A4 (RX) and Pin A5 (TX)
* **Correct Answer**: ก
* **Explanation**: Digital Pin 0 is Receive (RX) and Digital Pin 1 is Transmit (TX), shared with the on-board USB-to-Serial converter.
#### ข้อ 11
* **Topic**: Power Pins
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: What is the recommended DC input voltage range for the barrel jack or Vin pin of an Arduino Uno?
* ก. 3V to 5V
* ข. 7V to 12V
* ค. 24V to 48V
* ง. 110V to 220V AC
* **Correct Answer**: ข
* **Explanation**: The on-board linear voltage regulator operates reliably with an external DC supply of 7V to 12V.
#### ข้อ 12
* **Topic**: IDE Compilation
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: In the Arduino IDE, what does clicking the 'Verify / Compile' (Checkmark icon) button do?
* ก. Uploads the program to the board
* ข. Checks code syntax and compiles it into binary machine code
* ค. Deletes the sketch
* ง. Clears the EEPROM
* **Correct Answer**: ข
* **Explanation**: The Verify button checks syntax and compiles the C/C++ sketch into machine hex code without uploading.
#### ข้อ 13
* **Topic**: IDE Upload Error
* **Learning Objective**: LO-ARD1
* **Difficulty**: Medium
* **Prompt**: If the Arduino IDE returns 'avrdude: ser_open(): can't open device', what is the most likely cause?
* ก. Incorrect COM port selected or USB cable disconnected
* ข. Syntax error inside setup()
* ค. Using too many comments
* ง. RAM memory is 100% full
* **Correct Answer**: ก
* **Explanation**: This avrdude communication error indicates the selected COM port is wrong, busy, or the USB cable is unplugged.
#### ข้อ 14
* **Topic**: File Extension
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: What is the standard file extension used for Arduino source code files?
* ก. .c
* ข. .cpp
* ค. .ino
* ง. .hex
* **Correct Answer**: ค
* **Explanation**: Arduino sketch files use the .ino extension (formerly .pde prior to Arduino 1.0).
#### ข้อ 15
* **Topic**: Current Limit per Pin
* **Learning Objective**: LO-ARD1
* **Difficulty**: Medium
* **Prompt**: What is the maximum absolute safe DC current that a single digital I/O pin of the ATmega328P can source/sink?
* ก. 5 mA
* ข. 20 mA (recommended) / 40 mA (absolute maximum)
* ค. 500 mA
* ง. 2 A
* **Correct Answer**: ข
* **Explanation**: Each I/O pin can safely source/sink up to 20 mA continuously (with 40 mA absolute maximum before hardware damage).
#### ข้อ 16
* **Topic**: Pin Mode Configuration
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: Which function must be called in setup() to configure a pin as an output?
* ก. setPin(13, OUT);
* ข. pinMode(13, OUTPUT);
* ค. digitalWrite(13, HIGH);
* ง. outputPin(13);
* **Correct Answer**: ข
* **Explanation**: pinMode(pin, mode) configures a specific digital pin as INPUT, OUTPUT, or INPUT_PULLUP.
#### ข้อ 17
* **Topic**: Internal Pullup Resistor
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: When configuring a pin with pinMode(2, INPUT_PULLUP), what voltage state is read when a pushbutton connected to GND is unpressed?
* ก. 0V (LOW)
* ข. 5V (HIGH)
* ค. 2.5V (FLOATING)
* ง. -5V
* **Correct Answer**: ข
* **Explanation**: INPUT_PULLUP activates the internal 20k-50k ohm pullup resistor to 5V, reading HIGH when unpressed and LOW when pressed to GND.
#### ข้อ 18
* **Topic**: Digital Output Control
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: Which command sets Digital Pin 8 to 5V output to turn on an external LED?
* ก. digitalWrite(8, HIGH);
* ข. digitalRead(8, 5V);
* ค. pinWrite(8, ON);
* ง. analogWrite(8, 255);
* **Correct Answer**: ก
* **Explanation**: digitalWrite(pin, HIGH) sends 5V to the specified output pin.
#### ข้อ 19
* **Topic**: Digital Input Reading
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: What function reads the logic level (HIGH or LOW) of a digital input pin?
* ก. analogRead()
* ข. digitalRead()
* ค. pinRead()
* ง. digitalVal()
* **Correct Answer**: ข
* **Explanation**: digitalRead(pin) returns either HIGH (1) or LOW (0) from the specified digital pin.
#### ข้อ 20
* **Topic**: Analog Value Calculation
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: If analogRead(A0) returns a value of 512 with a 5V reference, what is the measured input voltage?
* ก. 1.25V
* ข. 2.5V
* ค. 3.75V
* ง. 5.0V
* **Correct Answer**: ข
* **Explanation**: Voltage = (512 / 1023.0) * 5.0V = approximately 2.50V (half of full scale).
#### ข้อ 21
* **Topic**: PWM Function
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: Which Arduino function is used to output a Pulse Width Modulation (PWM) signal?
* ก. pwmWrite()
* ข. digitalWrite()
* ค. analogWrite()
* ง. setPWM()
* **Correct Answer**: ค
* **Explanation**: analogWrite(pin, value) generates a PWM square wave on designated PWM pins.
#### ข้อ 22
* **Topic**: PWM Resolution & Range
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: What is the valid parameter value range passed to analogWrite(pin, value)?
* ก. 0 to 1
* ข. 0 to 100
* ค. 0 to 255 (8-bit)
* ง. 0 to 1023 (10-bit)
* **Correct Answer**: ค
* **Explanation**: analogWrite() takes an 8-bit duty cycle value from 0 (0% duty cycle / always OFF) to 255 (100% duty cycle / always ON).
#### ข้อ 23
* **Topic**: PWM Pin Identification
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: Which pins on the Arduino Uno support hardware PWM output via analogWrite()?
* ก. Pins 0, 1, 2, 3, 4, 5
* ข. Pins 3, 5, 6, 9, 10, 11 (marked with ~)
* ค. Pins 2, 4, 6, 8, 10, 12
* ง. All pins from 0 to 13
* **Correct Answer**: ข
* **Explanation**: On the Uno, digital pins 3, 5, 6, 9, 10, and 11 feature hardware PWM timers (marked with a tilde ~ symbol).
#### ข้อ 24
* **Topic**: Servo Motor Library
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: Which header file must be included in an Arduino sketch to control a standard hobby servo motor?
* ก. #include <Motor.h>
* ข. #include <Servo.h>
* ค. #include <PWM.h>
* ง. #include <Actuator.h>
* **Correct Answer**: ข
* **Explanation**: The standard Arduino Servo library is included using #include <Servo.h>.
#### ข้อ 25
* **Topic**: Servo Angle Command
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: Given Servo myServo;, which command rotates the servo shaft to a 90-degree position?
* ก. myServo.set(90);
* ข. myServo.write(90);
* ค. myServo.rotate(90);
* ง. myServo.position(90);
* **Correct Answer**: ข
* **Explanation**: The write(angle) method of the Servo class commands the servo to a specific angular position (0 to 180 degrees).
#### ข้อ 26
* **Topic**: Piezo Buzzer Tone
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: Which function generates a 440 Hz audio square wave tone on Digital Pin 8?
* ก. tone(8, 440);
* ข. sound(8, 440);
* ค. audioWrite(8, 440);
* ง. buzzer(8, 440);
* **Correct Answer**: ก
* **Explanation**: tone(pin, frequency) generates a 50% duty cycle square wave at the specified frequency in Hertz on the chosen pin.
#### ข้อ 27
* **Topic**: Stopping Buzzer Tone
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: Which function silences a tone generated by the tone() function on Pin 8?
* ก. stopTone(8);
* ข. noTone(8);
* ค. silence(8);
* ง. toneOff(8);
* **Correct Answer**: ข
* **Explanation**: noTone(pin) stops the square wave generation triggered by tone().
#### ข้อ 28
* **Topic**: LiquidCrystal Library
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: When using a standard 16x2 character LCD with LiquidCrystal lcd(RS, E, D4, D5, D6, D7);, what must be called in setup()?
* ก. lcd.init();
* ข. lcd.begin(16, 2);
* ค. lcd.start(16, 2);
* ง. lcd.open();
* **Correct Answer**: ข
* **Explanation**: lcd.begin(cols, rows) initializes the display interface and specifies the dimensions (16 columns, 2 rows).
#### ข้อ 29
* **Topic**: Map Function
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: What is the result of map(512, 0, 1023, 0, 255); in an Arduino sketch?
* ก. 0
* ข. 127 or 128
* ค. 255
* ง. 512
* **Correct Answer**: ข
* **Explanation**: map(val, fromLow, fromHigh, toLow, toHigh) proportionally scales 512 (50% of 1023) to approximately 127-128 (50% of 255).
#### ข้อ 30
* **Topic**: Constrain Function
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: What does constrain(x, 10, 100); return if x has a value of 150?
* ก. 10
* ข. 100
* ค. 150
* ง. 0
* **Correct Answer**: ข
* **Explanation**: constrain(amt, low, high) clamps a number within the range, returning 100 when the value exceeds the upper bound.
#### ข้อ 31
* **Topic**: Serial Initialization
* **Learning Objective**: LO-ARD3
* **Difficulty**: Easy
* **Prompt**: Which command initializes serial communication at 9600 bits per second (baud)?
* ก. Serial.start(9600);
* ข. Serial.begin(9600);
* ค. Serial.open(9600);
* ง. Serial.connect(9600);
* **Correct Answer**: ข
* **Explanation**: Serial.begin(speed) sets the data rate in bits per second (baud rate) for serial data transmission.
#### ข้อ 32
* **Topic**: Serial Available Check
* **Learning Objective**: LO-ARD3
* **Difficulty**: Easy
* **Prompt**: What does Serial.available() return?
* ก. The current baud rate
* ข. The number of bytes received and waiting in the serial buffer to be read
* ค. True if the serial cable is plugged in
* ง. The last character typed
* **Correct Answer**: ข
* **Explanation**: Serial.available() returns the count of bytes already received and stored in the 64-byte serial receive buffer.
#### ข้อ 33
* **Topic**: Serial Read Character
* **Learning Objective**: LO-ARD3
* **Difficulty**: Easy
* **Prompt**: Which function reads one incoming byte from the serial buffer?
* ก. Serial.get()
* ข. Serial.read()
* ค. Serial.input()
* ง. Serial.fetch()
* **Correct Answer**: ข
* **Explanation**: Serial.read() reads and removes the next available byte from the serial receive buffer (or returns -1 if empty).
#### ข้อ 34
* **Topic**: Serial Print with Newline
* **Learning Objective**: LO-ARD3
* **Difficulty**: Easy
* **Prompt**: What is the difference between Serial.print("Hello"); and Serial.println("Hello");?
* ก. Serial.println() appends a carriage return ('\r') and newline ('\n') at the end
* ข. Serial.print() only works with numbers
* ค. Serial.println() sends data in binary format
* ง. There is no difference between them
* **Correct Answer**: ก
* **Explanation**: Serial.println() prints the data followed by carriage return (CR, ASCII 13) and newline (LF, ASCII 10).
#### ข้อ 35
* **Topic**: Python Serial Library
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: Which Python package is commonly used to establish bidirectional serial communication with an Arduino board?
* ก. pyarduino
* ข. pyserial (import serial)
* ค. python-usb
* ง. serialnet
* **Correct Answer**: ข
* **Explanation**: PySerial (import serial) is the standard cross-platform Python module for reading/writing to serial ports.
#### ข้อ 36
* **Topic**: I2C Protocol Pins
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: Which pins on the Arduino Uno carry the I2C bus signals SDA (Serial Data) and SCL (Serial Clock)?
* ก. Pins 0 (SDA) and 1 (SCL)
* ข. Pins A4 (SDA) and A5 (SCL)
* ค. Pins 10 (SDA) and 11 (SCL)
* ง. Pins 2 (SDA) and 3 (SCL)
* **Correct Answer**: ข
* **Explanation**: On the Uno, Analog Pin A4 functions as SDA (Data) and Analog Pin A5 functions as SCL (Clock), also duplicated near AREF.
#### ข้อ 37
* **Topic**: I2C Library
* **Learning Objective**: LO-ARD3
* **Difficulty**: Easy
* **Prompt**: Which built-in Arduino library handles I2C (Two-Wire Interface) communication?
* ก. #include <SPI.h>
* ข. #include <Wire.h>
* ค. #include <I2C.h>
* ง. #include <TwoWire.h>
* **Correct Answer**: ข
* **Explanation**: The Wire library (#include <Wire.h>) implements the I2C master and slave protocol.
#### ข้อ 38
* **Topic**: SPI Protocol Signals
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: What does the MOSI line represent in the SPI (Serial Peripheral Interface) communication protocol?
* ก. Master In Slave Out
* ข. Master Out Slave In
* ค. Master Oscillator Signal Input
* ง. Multiple Output Serial Interface
* **Correct Answer**: ข
* **Explanation**: MOSI stands for Master Out, Slave In — the data line carrying data from the Master to the Slave device.
#### ข้อ 39
* **Topic**: SPI Hardware Pins on Uno
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: Which digital pins on the Arduino Uno are assigned to hardware SPI (MOSI, MISO, SCK, SS)?
* ก. Pins 11 (MOSI), 12 (MISO), 13 (SCK), 10 (SS)
* ข. Pins 0 (MOSI), 1 (MISO), 2 (SCK), 3 (SS)
* ค. Pins A0, A1, A2, A3
* ง. Pins 4, 5, 6, 7
* **Correct Answer**: ก
* **Explanation**: On the Arduino Uno: Pin 11 = MOSI, Pin 12 = MISO, Pin 13 = SCK, Pin 10 = default SS (Slave Select).
#### ข้อ 40
* **Topic**: EEPROM Memory
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: What is a primary characteristic of the ATmega328P's internal EEPROM memory?
* ก. Data is wiped every time the power is disconnected
* ข. Data is non-volatile and persists across power cycles and resets
* ค. It holds 16 Gigabytes of data
* ง. It executes code faster than Flash memory
* **Correct Answer**: ข
* **Explanation**: EEPROM (Electrically Erasable Programmable Read-Only Memory) provides 1 KB of non-volatile storage that persists when power is cut.
#### ข้อ 41
* **Topic**: EEPROM Write vs Update
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: Why is EEPROM.update(address, value) preferred over EEPROM.write(address, value)?
* ก. EEPROM.update() only writes to memory if the new value is different, saving write endurance cycles
* ข. EEPROM.update() encrypts the stored data with a password
* ค. EEPROM.update() can write unlimited megabytes of data
* ง. EEPROM.write() was deleted in newer Arduino versions
* **Correct Answer**: ก
* **Explanation**: EEPROM cells have a lifespan of ~100,000 write cycles; EEPROM.update() prevents unnecessary wear by checking if the value changed.
#### ข้อ 42
* **Topic**: SD Card Communication
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: Which communication protocol does the standard Arduino SD Card library (#include <SD.h>) use to communicate with SD card modules?
* ก. UART Serial
* ข. I2C
* ค. SPI
* ง. OneWire
* **Correct Answer**: ค
* **Explanation**: SD and MicroSD card breakout modules interface with the Arduino via high-speed SPI bus (Pins 11, 12, 13 + CS).
#### ข้อ 43
* **Topic**: Bluetooth Module Interface
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: Which module is commonly used to provide classic Bluetooth serial communication to an Arduino Uno?
* ก. HC-05 / HC-06
* ข. ESP32
* ค. NRF24L01
* ง. SIM800L
* **Correct Answer**: ก
* **Explanation**: HC-05 (Master/Slave) and HC-06 (Slave-only) are popular UART serial Bluetooth bridge modules for Arduino.
#### ข้อ 44
* **Topic**: SoftwareSerial Library
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: Why do developers use the SoftwareSerial library on an Arduino Uno?
* ก. To simulate digital pins on analog ports
* ข. To create a software-emulated UART serial port on arbitrary digital pins without interfering with USB pins 0 and 1
* ค. To speed up the microcontroller clock to 32 MHz
* ง. To write Python code directly inside Arduino IDE
* **Correct Answer**: ข
* **Explanation**: SoftwareSerial allows using other digital pins (e.g. Pins 2 & 3) for serial sensors or Bluetooth while keeping Pins 0 & 1 free for USB debugging.
#### ข้อ 45
* **Topic**: I2C Addressing
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Prompt**: In I2C communication, how does a Master device select which Slave device it wants to communicate with on shared SDA/SCL lines?
* ก. By sending the unique 7-bit hardware address of the slave device
* ข. By pulling all pins LOW simultaneously
* ค. By switching the baud rate to 115200
* ง. By cutting power to all other devices
* **Correct Answer**: ก
* **Explanation**: Each slave device on an I2C bus has a unique 7-bit (or 10-bit) address; the master broadcasts this address in the start frame.
#### ข้อ 46
* **Topic**: Data Types - Byte
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: What is the value range that an 8-bit unsigned byte variable can hold in Arduino C++?
* ก. -128 to 127
* ข. 0 to 255
* ค. 0 to 65535
* ง. -32768 to 32767
* **Correct Answer**: ข
* **Explanation**: A byte is an unsigned 8-bit integer holding values from 0 to 255 (0x00 to 0xFF).
#### ข้อ 47
* **Topic**: Data Types - Int on Uno
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: How many bits and what range does a standard signed int have on an 8-bit AVR Arduino Uno?
* ก. 8-bit (0 to 255)
* ข. 16-bit (-32,768 to 32,767)
* ค. 32-bit (-2,147,483,648 to 2,147,483,647)
* ง. 64-bit
* **Correct Answer**: ข
* **Explanation**: On 8-bit AVR microcontrollers (Uno, Nano, Mega), an int is 16-bit signed with range -32,768 to +32,767.
#### ข้อ 48
* **Topic**: Data Types - Unsigned Long
* **Learning Objective**: LO-ARD1
* **Difficulty**: Medium
* **Prompt**: Which data type must be used to store the return value of millis() to prevent overflow bugs?
* ก. byte
* ข. int
* ค. float
* ง. unsigned long
* **Correct Answer**: ง
* **Explanation**: millis() returns a 32-bit unsigned integer (unsigned long) that counts milliseconds up to ~49.7 days before rolling over to 0.
#### ข้อ 49
* **Topic**: Millis Function
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Prompt**: What does the millis() function return?
* ก. The current real-world clock time in GMT
* ข. The number of milliseconds passed since the Arduino board began running the current program
* ค. The temperature of the ATmega328P chip
* ง. The remaining battery voltage
* **Correct Answer**: ข
* **Explanation**: millis() returns the elapsed time in milliseconds since program execution started.
#### ข้อ 50
* **Topic**: Delay Disadvantage
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: Why is using delay(1000) considered bad practice in complex, responsive embedded systems?
* ก. It consumes too much EEPROM flash space
* ข. It is a blocking call that freezes the CPU, preventing it from reading buttons or sensors during the pause
* ค. It damages the crystal oscillator over time
* ง. It reverses the polarity of power pins
* **Correct Answer**: ข
* **Explanation**: delay() halts all execution (except background hardware interrupts), making the board unresponsive to inputs during the wait time.
#### ข้อ 51
* **Topic**: External Interrupt Pins on Uno
* **Learning Objective**: LO-ARD4
* **Difficulty**: Medium
* **Prompt**: Which digital pins on an Arduino Uno support external hardware interrupts via attachInterrupt()?
* ก. Pins 0 and 1
* ข. Pins 2 (Interrupt 0) and 3 (Interrupt 1)
* ค. Pins 9 and 10
* ง. Pins A0 and A1
* **Correct Answer**: ข
* **Explanation**: Arduino Uno provides two external hardware interrupt pins: Digital Pin 2 (INT0) and Digital Pin 3 (INT1).
#### ข้อ 52
* **Topic**: Interrupt Mode Types
* **Learning Objective**: LO-ARD4
* **Difficulty**: Medium
* **Prompt**: Which interrupt trigger mode fires an ISR when a digital pin transitions from LOW (0V) to HIGH (5V)?
* ก. LOW
* ข. CHANGE
* ค. FALLING
* ง. RISING
* **Correct Answer**: ง
* **Explanation**: RISING triggers the interrupt when the pin changes state from LOW to HIGH. FALLING triggers from HIGH to LOW.
#### ข้อ 53
* **Topic**: Volatile Keyword
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Prompt**: Why must global variables shared between an Interrupt Service Routine (ISR) and the main loop() be declared with volatile?
* ก. To tell the compiler not to cache the variable in a CPU register, ensuring fresh reads from RAM
* ข. To make the variable permanent in EEPROM
* ค. To protect the variable from unauthorized WiFi access
* ง. To convert the variable into floating-point format automatically
* **Correct Answer**: ก
* **Explanation**: The volatile qualifier prevents compiler optimization from caching the variable, ensuring the main loop always sees changes made inside the ISR.
#### ข้อ 54
* **Topic**: ISR Best Practices
* **Learning Objective**: LO-ARD4
* **Difficulty**: Medium
* **Prompt**: What is a critical rule to follow when writing an Interrupt Service Routine (ISR) function in Arduino?
* ก. Keep the ISR as short and fast as possible; avoid calling delay() or lengthy Serial.print() inside it
* ข. Always insert delay(500) inside the ISR to debounce switches
* ค. Perform complex floating-point calculations and file writes inside the ISR
* ง. Call attachInterrupt() repeatedly inside the ISR
* **Correct Answer**: ก
* **Explanation**: ISRs must execute swiftly. Since interrupts are disabled inside an ISR, delay() will not tick and Serial buffers can overflow.
#### ข้อ 55
* **Topic**: Array Syntax
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Prompt**: How do you declare and initialize an array of 4 integer pin numbers in Arduino C++?
* ก. int pins = [2, 4, 6, 8];
* ข. int pins[4] = {2, 4, 6, 8};
* ค. array int pins(2, 4, 6, 8);
* ง. pins[] = {2, 4, 6, 8};
* **Correct Answer**: ข
* **Explanation**: In C/C++, array declaration uses int pins[4] = {2, 4, 6, 8}; with curly braces for initialization.
#### ข้อ 56
* **Topic**: Modulo Operator
* **Learning Objective**: LO-ARD1
* **Difficulty**: Medium
* **Prompt**: What is the result of the expression 17 % 5 in Arduino C++?
* ก. 3.4
* ข. 3
* ค. 2
* ง. 0
* **Correct Answer**: ค
* **Explanation**: The modulo operator (%) computes the integer remainder after division: 17 divided by 5 is 3 with a remainder of 2.
#### ข้อ 57
* **Topic**: Blink Without Delay Pattern
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: In the 'Blink Without Delay' paradigm, what condition triggers the LED state toggle?
* ก. if (millis() - previousMillis >= interval)
* ข. if (delay() == 1000)
* ค. if (digitalRead(13) == true)
* ง. if (Serial.available() > 0)
* **Correct Answer**: ก
* **Explanation**: The non-blocking timer calculates elapsed time by subtracting the saved timestamp from current millis(): (currentMillis - previousMillis >= interval).
#### ข้อ 58
* **Topic**: Random Number Generation
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Prompt**: Why is randomSeed(analogRead(A0)) frequently placed in setup() when an unconnected analog pin is used?
* ก. To initialize the pseudo-random number generator with unpredictable atmospheric electrical noise
* ข. To calibrate the analog pin for temperature measurement
* ค. To increase the RAM memory capacity
* ง. To reset the microcontroller every 10 seconds
* **Correct Answer**: ก
* **Explanation**: A floating analog pin picks up ambient electromagnetic noise, providing an unpredictable seed for random().
#### ข้อ 59
* **Topic**: Bitwise Operations
* **Learning Objective**: LO-ARD1
* **Difficulty**: Medium
* **Prompt**: What does the bitwise left-shift operation (1 << 3) evaluate to in binary and decimal?
* ก. B00000001 (1)
* ข. B00000100 (4)
* ค. B00001000 (8)
* ง. B00010000 (16)
* **Correct Answer**: ค
* **Explanation**: Left-shifting binary 1 by 3 positions yields 00001000 in binary, which is decimal 8 (2^3).
#### ข้อ 60
* **Topic**: Firmware Reset via Code
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Prompt**: What is the safest hardware-supported method to reset an Arduino via software if a program hangs?
* ก. Configuring and using the internal AVR Watchdog Timer (WDT) via #include <avr/wdt.h>
* ข. Connecting Digital Pin 13 directly to 5V
* ค. Calling setup() inside loop() continuously
* ง. Writing 255 to all EEPROM addresses
* **Correct Answer**: ก
* **Explanation**: The AVR Watchdog Timer (wdt_enable, wdt_reset) resets the processor automatically if the firmware hangs and fails to kick the dog.

# Section B: True / False Questions (ถูก / ผิด 30 ข้อ)

<!--
RULES Section B:
- ข้อ 61–90 (30 ข้อ, 1 คะแนน/ข้อ)
- **Correct Answer**: True | False
-->
#### ข้อ 61
* **Topic**: Arduino Hardware
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Statement**: The Arduino Uno R3 digital pins can directly supply 10 Amperes of current to drive heavy industrial motors.
* **Correct Answer**: False
* **Explanation**: Arduino pins have a safe limit of ~20 mA (40 mA absolute max). External transistors, relays, or motor drivers (e.g. L298N) are required for motors.
#### ข้อ 62
* **Topic**: Sketch Execution
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Statement**: Code written inside the loop() function runs repeatedly until the Arduino board is powered off or reset.
* **Correct Answer**: True
* **Explanation**: The loop() function executes endlessly in a continuous cycle after setup() finishes.
#### ข้อ 63
* **Topic**: ADC Reading
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Statement**: analogRead() on an Arduino Uno returns an integer value ranging from 0 to 1023.
* **Correct Answer**: True
* **Explanation**: The built-in 10-bit ADC converts 0V-5V input voltages into values from 0 to 1023.
#### ข้อ 64
* **Topic**: PWM Output
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Statement**: analogWrite(pin, 0) outputs a continuous 0V (0% duty cycle), while analogWrite(pin, 255) outputs continuous 5V (100% duty cycle).
* **Correct Answer**: True
* **Explanation**: analogWrite() uses an 8-bit parameter (0-255) to control the duty cycle of the PWM square wave.
#### ข้อ 65
* **Topic**: PWM Hardware
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Statement**: On the Arduino Uno, analogWrite() can be called on any digital pin from 0 through 13 with equal hardware timer support.
* **Correct Answer**: False
* **Explanation**: Only digital pins 3, 5, 6, 9, 10, and 11 on the Uno have built-in PWM timer support (marked with ~).
#### ข้อ 66
* **Topic**: Internal Pullup
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Statement**: When pinMode(pin, INPUT_PULLUP) is configured, connecting a pushbutton between the pin and GND will read LOW when pressed.
* **Correct Answer**: True
* **Explanation**: The internal resistor pulls the line to HIGH (5V) when unpressed, and pressing the button connects the pin to GND (LOW).
#### ข้อ 67
* **Topic**: Serial Baud Rate
* **Learning Objective**: LO-ARD3
* **Difficulty**: Easy
* **Statement**: Both the Arduino sketch (Serial.begin) and the Serial Monitor dropdown must be set to the same baud rate to display readable text.
* **Correct Answer**: True
* **Explanation**: Mismatched baud rates result in corrupted gibberish characters on the Serial Monitor.
#### ข้อ 68
* **Topic**: Serial Communication Buffer
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Statement**: Serial.read() reads all available bytes in the serial buffer simultaneously and returns them as a single String.
* **Correct Answer**: False
* **Explanation**: Serial.read() reads only a single byte (character) at a time from the incoming buffer.
#### ข้อ 69
* **Topic**: I2C Wire Connection
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Statement**: The I2C communication protocol requires only two signal lines: SDA (Data) and SCL (Clock), plus a common ground.
* **Correct Answer**: True
* **Explanation**: I2C is a 2-wire synchronous serial protocol sharing SDA and SCL across multiple addressed devices.
#### ข้อ 70
* **Topic**: I2C Pins on Uno
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Statement**: On the Arduino Uno, Analog Pin A4 is SCL and Analog Pin A5 is SDA.
* **Correct Answer**: False
* **Explanation**: On the Uno, Analog Pin A4 is SDA (Data) and Analog Pin A5 is SCL (Clock).
#### ข้อ 71
* **Topic**: SPI Bus Speed
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Statement**: SPI (Serial Peripheral Interface) communication is generally much faster than I2C and UART serial communication.
* **Correct Answer**: True
* **Explanation**: SPI uses dedicated clock and separate input/output lines (MOSI/MISO), achieving speeds of several megahertz.
#### ข้อ 72
* **Topic**: SPI Slave Select
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Statement**: In SPI communication, multiple slave devices can share the same MOSI, MISO, and SCK lines if each slave has a dedicated Chip Select (CS/SS) pin.
* **Correct Answer**: True
* **Explanation**: Each slave device is activated individually by pulling its dedicated Slave Select (SS) pin LOW.
#### ข้อ 73
* **Topic**: EEPROM Endurance
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Statement**: Writing to the EEPROM in a fast loop() without conditions can wear out the flash memory cells in a matter of minutes.
* **Correct Answer**: True
* **Explanation**: EEPROM cells are rated for ~100,000 write cycles; an unconditional write in a tight loop exhausts this lifespan rapidly.
#### ข้อ 74
* **Topic**: EEPROM Retention
* **Learning Objective**: LO-ARD3
* **Difficulty**: Easy
* **Statement**: Data stored in EEPROM using EEPROM.write() is retained even after the Arduino is powered off.
* **Correct Answer**: True
* **Explanation**: EEPROM is non-volatile memory designed specifically for permanent data retention across power cycles.
#### ข้อ 75
* **Topic**: Blocking Delay
* **Learning Objective**: LO-ARD2
* **Difficulty**: Easy
* **Statement**: Calling delay(5000) allows the Arduino to continue checking if a user presses a button during those 5 seconds.
* **Correct Answer**: False
* **Explanation**: delay() is blocking; the microcontroller stops executing normal code and cannot poll button states during the delay.
#### ข้อ 76
* **Topic**: Millis Timer
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Statement**: The millis() timer stops counting whenever a digitalRead() function is called.
* **Correct Answer**: False
* **Explanation**: millis() relies on Hardware Timer 0 overflow interrupts and continues incrementing in the background continuously.
#### ข้อ 77
* **Topic**: External Interrupts Pins
* **Learning Objective**: LO-ARD4
* **Difficulty**: Medium
* **Statement**: Digital Pin 2 and Digital Pin 3 are the only two external hardware interrupt pins available on the standard Arduino Uno.
* **Correct Answer**: True
* **Explanation**: The ATmega328P on the Uno maps INT0 to Digital Pin 2 and INT1 to Digital Pin 3.
#### ข้อ 78
* **Topic**: Interrupt Service Routine
* **Learning Objective**: LO-ARD4
* **Difficulty**: Medium
* **Statement**: Calling delay(1000) inside an Interrupt Service Routine (ISR) is a recommended technique for debouncing switches.
* **Correct Answer**: False
* **Explanation**: delay() relies on interrupts, which are disabled inside an ISR. Calling delay() inside an ISR causes the code to hang.
#### ข้อ 79
* **Topic**: Volatile Keyword in ISR
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Statement**: Variables modified inside an ISR and checked in the loop() should be declared with the volatile keyword.
* **Correct Answer**: True
* **Explanation**: volatile forces the compiler to load the variable from RAM each time, ensuring the loop() sees updates from the ISR.
#### ข้อ 80
* **Topic**: Servo Power Supply
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Statement**: High-torque hobby servos should ideally be powered from an external 5V power supply rather than directly from the Arduino's 5V pin.
* **Correct Answer**: True
* **Explanation**: Servos draw high peak stall currents (up to 1A+) which can overload the Arduino regulator and cause brownout resets.
#### ข้อ 81
* **Topic**: Tone Function Limitation
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Statement**: The tone() function can play polyphonic 5-note musical chords simultaneously on a single digital pin.
* **Correct Answer**: False
* **Explanation**: tone() produces only a single square wave frequency (monophonic) at any given moment on a pin.
#### ข้อ 82
* **Topic**: LiquidCrystal Pin Requirement
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Statement**: In 4-bit mode, an HD44780 LCD display requires 6 Arduino digital pins (RS, Enable, D4, D5, D6, D7).
* **Correct Answer**: True
* **Explanation**: 4-bit mode utilizes 6 I/O lines, saving pins compared to 8-bit mode (which requires 10 pins).
#### ข้อ 83
* **Topic**: Python PySerial Communication
* **Learning Objective**: LO-ARD4
* **Difficulty**: Medium
* **Statement**: When Python opens a serial connection to an Arduino Uno, the DTR line automatically triggers an Arduino hardware reboot by default.
* **Correct Answer**: True
* **Explanation**: Opening the serial port pulses DTR, resetting the ATmega328P to initiate the bootloader.
#### ข้อ 84
* **Topic**: Analog Reference Voltage
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Statement**: Calling analogReference(INTERNAL) on an Arduino Uno changes the ADC reference voltage to 1.1 Volts.
* **Correct Answer**: True
* **Explanation**: On ATmega328P, the internal reference is a precise ~1.1V bandgap voltage.
#### ข้อ 85
* **Topic**: Array Indexing
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Statement**: In Arduino C++, the first element of an array myValues[5] is accessed at index 0 (myValues[0]).
* **Correct Answer**: True
* **Explanation**: C/C++ arrays are zero-indexed, meaning elements range from index 0 to size-1.
#### ข้อ 86
* **Topic**: Data Types - Boolean
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Statement**: A boolean data type in Arduino can only hold one of two values: true or false.
* **Correct Answer**: True
* **Explanation**: boolean (or bool) represents logical truth values true (1) or false (0).
#### ข้อ 87
* **Topic**: Digital Pin as Analog Output
* **Learning Objective**: LO-ARD2
* **Difficulty**: Medium
* **Statement**: The analogWrite() function outputs a true, smooth, continuous analog DC voltage like a variable DAC battery.
* **Correct Answer**: False
* **Explanation**: analogWrite() outputs a Pulse Width Modulated (PWM) high-frequency digital square wave, not a true continuous analog voltage.
#### ข้อ 88
* **Topic**: Const Keyword
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Statement**: Declaring const int ledPin = 13; prevents the value of ledPin from being accidentally modified later in the code.
* **Correct Answer**: True
* **Explanation**: The const qualifier marks a variable as read-only, causing a compiler error if modified.
#### ข้อ 89
* **Topic**: Hardware Reset Pin
* **Learning Objective**: LO-ARD1
* **Difficulty**: Easy
* **Statement**: Pulling the RESET pin on the Arduino Uno to GND momentarily resets the microcontroller.
* **Correct Answer**: True
* **Explanation**: The active-low RESET pin restarts the ATmega328P when pulled to 0V (GND).
#### ข้อ 90
* **Topic**: SD Card Library
* **Learning Objective**: LO-ARD3
* **Difficulty**: Medium
* **Statement**: The Arduino SD library supports opening multiple files simultaneously for writing on an ATmega328P without RAM constraints.
* **Correct Answer**: False
* **Explanation**: Each open file buffer requires 512 bytes of SRAM. On a 2KB RAM Uno, opening multiple files risks running out of memory.

# Section C: Scenario-Based Questions (สถานการณ์จำลอง 15 ข้อ)

<!--
RULES Section C:
- ข้อ 91–105 (15 ข้อ, 2 คะแนน/ข้อ)
-->
#### ข้อ 91
* **Topic**: Non-blocking Timer Design
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Scenario**: Developer Alex wants an Arduino Uno to blink an LED on Pin 13 every 500 ms while continuously monitoring a pushbutton on Pin 2. When using delay(500), button presses during the delay are missed.
* **Question**: How should Alex redesign the code using millis() to achieve responsive non-blocking operation?
* **Answer**: Alex should store the current timestamp in an unsigned long currentMillis = millis();. He should check if (currentMillis - previousMillis >= 500). When true, update previousMillis = currentMillis; and toggle the LED state. Outside this condition in loop(), the pushbutton on Pin 2 can be read with digitalRead(2) on every iteration without delay, ensuring instant response.
* **Explanation**: The millis() pattern allows multitasking by checking elapsed time on each cycle without blocking CPU execution.
#### ข้อ 92
* **Topic**: Analog Voltage Measurement & Calibration
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Scenario**: A student connects a 10k potentiometer to Analog Pin A0. The analogRead(A0) function returns a raw integer value of 768. The reference voltage is 5.00V.
* **Question**: Calculate the exact measured voltage on Pin A0 and write the Arduino C++ formula to compute it.
* **Answer**: Formula: float voltage = (rawADC * 5.0) / 1023.0; Calculation: (768 * 5.0) / 1023.0 = 3840.0 / 1023.0 = approximately 3.75 Volts (or 3.753V).
* **Explanation**: ADC mapping divides the 10-bit reading (0-1023) by 1023.0 and multiplies by the 5.0V reference.
#### ข้อ 93
* **Topic**: Pushbutton Active-Low Circuit with Internal Pullup
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Scenario**: A circuit connects a momentary tactile button between Digital Pin 4 and GND with no external resistors. The designer writes pinMode(4, INPUT_PULLUP);.
* **Question**: Explain the logic states read by digitalRead(4) when the button is open (unpressed) vs closed (pressed), and describe how to light an LED when pressed.
* **Answer**: When unpressed, the internal pullup resistor pulls Pin 4 to 5V (HIGH / 1). When pressed, the button grounds Pin 4 to 0V (LOW / 0). To turn ON an LED when pressed, the code should check: if (digitalRead(4) == LOW) { digitalWrite(ledPin, HIGH); } else { digitalWrite(ledPin, LOW); }.
* **Explanation**: INPUT_PULLUP creates an active-low input circuit, reading LOW when the button connects the pin to ground.
#### ข้อ 94
* **Topic**: PWM Motor Speed Control with Serial Commands
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Scenario**: A robotics engineer controls a DC motor speed on PWM Pin 9 via the Serial Monitor. The user sends single-byte characters from '0' (stop) to '9' (full speed).
* **Question**: Write the Arduino code snippet to read the serial character and map '0'-'9' to the appropriate PWM duty cycle on Pin 9.
* **Answer**: In loop(): if (Serial.available() > 0) { char c = Serial.read(); if (c >= '0' && c <= '9') { int speed = map(c - '0', 0, 9, 0, 255); analogWrite(9, speed); Serial.print("Motor speed set to: "); Serial.println(speed); } }.
* **Explanation**: Characters '0'-'9' are converted to integer 0-9 by subtracting '0' (ASCII 48), then mapped to PWM range 0-255.
#### ข้อ 95
* **Topic**: External Hardware Interrupt with Button Debouncing
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Scenario**: An optical tachometer sensor generates a pulse every time a motor wheel completes one rotation, connected to Digital Pin 2. The engineer needs to count total rotations accurately without missing pulses during LCD screen updates.
* **Question**: How should the engineer configure attachInterrupt() on Pin 2 and declare the counter variable?
* **Answer**: 1. Declare a global variable: volatile unsigned long revCount = 0;. 2. In setup(): pinMode(2, INPUT_PULLUP); attachInterrupt(digitalPinToInterrupt(2), countRev, FALLING);. 3. Define the ISR: void countRev() { revCount++; }. The volatile keyword ensures revCount updates safely across interrupt boundaries without compiler register caching.
* **Explanation**: Hardware interrupts trigger immediately on edge transitions (FALLING), ensuring pulses are never lost during slow LCD routines.
#### ข้อ 96
* **Topic**: Python to Arduino Serial Protocol
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Scenario**: A Python application sends the string 'LED_ON\n' or 'LED_OFF\n' over USB serial COM port at 9600 baud to an Arduino Uno.
* **Question**: Describe how the Arduino sketch should buffer and parse the incoming serial string to turn Pin 13 ON or OFF.
* **Answer**: In loop(): if (Serial.available() > 0) { String command = Serial.readStringUntil('\n'); command.trim(); if (command == "LED_ON") { digitalWrite(13, HIGH); Serial.println("ACK: ON"); } else if (command == "LED_OFF") { digitalWrite(13, LOW); Serial.println("ACK: OFF"); } }.
* **Explanation**: Serial.readStringUntil('\n') captures text until newline, and trim() removes whitespace for accurate string comparison.
#### ข้อ 97
* **Topic**: EEPROM Configuration Persistence
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Scenario**: A smart thermostat allows users to set a desired target temperature (e.g. 24 degrees Celsius) via buttons. If power goes out, the user setting must not be lost.
* **Question**: Explain how to use EEPROM.h to load the setting on startup and save the setting only when changed.
* **Answer**: 1. In setup(): byte targetTemp = EEPROM.read(0); if (targetTemp == 255 || targetTemp < 10 || targetTemp > 40) targetTemp = 24; (default sanity check). 2. When the user changes temperature with buttons, save with: EEPROM.update(0, targetTemp);. EEPROM.update() avoids unnecessary flash wear by only writing when targetTemp has altered.
* **Explanation**: EEPROM retains settings across power cuts. EEPROM.update() preserves write endurance.
#### ข้อ 98
* **Topic**: I2C Multi-Sensor Bus Architecture
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Scenario**: An IoT weather station connects an I2C OLED display (address 0x3C), an I2C BMP280 pressure sensor (address 0x76), and an I2C RTC clock (address 0x68) to an Arduino Uno.
* **Question**: Explain how the hardware wiring is arranged for all 3 devices and how the Arduino communicates with each device independently.
* **Answer**: Hardware Wiring: All 3 devices share the same two bus wires: SDA connects to A4 and SCL connects to A5, with pullup resistors (4.7k) to 5V/3.3V and common GND. Communication: Because each peripheral has a distinct 7-bit I2C address (0x3C, 0x76, 0x68), the Arduino Master addresses each device individually using Wire.beginTransmission(address) without physical signal conflicts.
* **Explanation**: I2C is an addressable multi-drop bus where devices share common SDA/SCL lines and respond only to their unique address.
#### ข้อ 99
* **Topic**: SPI Communication with Multiple Slaves
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Scenario**: An embedded system interfaces two SPI devices: a high-speed MicroSD Card module and an SPI digital potentiometer (MCP41010) on an Arduino Uno.
* **Question**: How are the SPI pins connected between the Uno and the two SPI modules, and how does the code select which device to talk to?
* **Answer**: Shared Pins: Both modules share Digital Pin 11 (MOSI), Pin 12 (MISO), and Pin 13 (SCK). Separate Pins: The SD card CS connects to Pin 4, and the MCP41010 CS connects to Pin 10. To talk to the MCP41010: digitalWrite(10, LOW); SPI.transfer(data); digitalWrite(10, HIGH);. Pin 4 remains HIGH (inactive) during this transfer.
* **Explanation**: SPI peripherals share MOSI, MISO, and SCK lines while being selected individually by driving their specific Chip Select (CS) pin LOW.
#### ข้อ 100
* **Topic**: Servo Sweeping with Non-blocking Timing
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Scenario**: A surveillance camera pan mechanism uses a Servo on Pin 9. It must sweep back and forth between 0 and 180 degrees, incrementing 1 degree every 20 ms without using delay(20).
* **Question**: Outline the non-blocking state machine algorithm to implement this sweep.
* **Answer**: Declare global variables: int pos = 0; int step = 1; unsigned long lastMove = 0;. In loop(): unsigned long now = millis(); if (now - lastMove >= 20) { lastMove = now; pos += step; myServo.write(pos); if (pos >= 180 || pos <= 0) { step = -step; } }.
* **Explanation**: Using an interval timer with a directional step variable (+1/-1) creates smooth sweeping without blocking CPU time.
#### ข้อ 101
* **Topic**: Preventing Variable Overflow in Millis
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Scenario**: A beginner programmer writes: int lastTime = 0; if (millis() - lastTime > 1000) { lastTime = millis(); toggleLED(); }. After approximately 32.7 seconds, the LED stops blinking properly.
* **Question**: Diagnose the bug and provide the proper fix.
* **Answer**: Diagnosis: On Arduino Uno, an int is a 16-bit signed integer (maximum +32,767). After 32,767 ms (~32.7 seconds), lastTime overflows into negative values (-32,768), breaking the arithmetic comparison. Fix: Change lastTime declaration to unsigned long lastTime = 0;, which can hold values up to ~4,294,967,295 ms (~49.7 days) and handles rollover subtraction safely.
* **Explanation**: Timer variables tracking millis() must always use the unsigned long data type to avoid 16-bit signed integer overflow.
#### ข้อ 102
* **Topic**: HC-05 Bluetooth Control Circuit
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Scenario**: An HC-05 Bluetooth module has its TX pin connected to Arduino Pin 2 (RX) and RX pin connected to Arduino Pin 3 (TX) through a voltage divider (2k/1k resistors).
* **Question**: Why is a voltage divider required on the HC-05 RX line, and how is SoftwareSerial initialized in code?
* **Answer**: 1. Voltage Divider: The HC-05 RX pin operates at 3.3V logic level. Connecting Arduino's 5V TX pin directly can damage the Bluetooth module; the voltage divider steps 5V down to ~3.3V. 2. SoftwareSerial: #include <SoftwareSerial.h> SoftwareSerial btSerial(2, 3); // RX=2, TX=3. In setup(): btSerial.begin(9600);.
* **Explanation**: Level shifting protects 3.3V Bluetooth inputs from 5V Arduino outputs. SoftwareSerial enables communication on Pins 2 and 3.
#### ข้อ 103
* **Topic**: SD Card Data Logger Failure Modes
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Scenario**: An environmental data logger writes sensor readings to an SD card file every 10 seconds. After 2 hours, the file on the SD card is corrupted or 0 bytes.
* **Question**: Identify two common causes for this issue and explain the correct file handling practice in Arduino.
* **Answer**: Causes: 1. Failure to call myFile.close() or myFile.flush() after writing, leaving data in the RAM buffer without flushing to physical SD flash. 2. Loss of power during write operations without file closing. Practice: Open file -> write data -> immediately close file: File dataFile = SD.open("log.txt", FILE_WRITE); if (dataFile) { dataFile.println(dataString); dataFile.close(); }.
* **Explanation**: Calling myFile.close() or myFile.flush() writes the buffer and updates FAT directory tables, preventing data corruption.
#### ข้อ 104
* **Topic**: Debouncing a Mechanical Switch in Software
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Scenario**: When pressing a mechanical tactile button, the metal contacts bounce rapidly for 5-10 ms, causing a counter to increment by 3 or 4 instead of 1.
* **Question**: Explain how software debouncing solves this problem without adding physical capacitors.
* **Answer**: Software debouncing reads the button state and checks if it remains stable for a debounce interval (e.g. 50 ms) before registering a valid press. When a state transition is detected, the current millis() is saved. Only if the state stays constant for >50 ms is the state change accepted and the counter incremented by exactly 1.
* **Explanation**: Software debouncing ignores rapid contact bounce transitions by waiting for signal stabilization.
#### ข้อ 105
* **Topic**: LiquidCrystal Custom Character Creation
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Scenario**: A developer wants to create a custom battery indicator icon on a 16x2 HD44780 LCD display using the LiquidCrystal library.
* **Question**: Describe the process of defining the 5x8 pixel binary array and registering it with lcd.createChar().
* **Answer**: 1. Define byte array of 8 rows: byte batteryIcon[8] = { B01110, B11111, B10001, B10001, B11111, B11111, B11111, B11111 };. 2. In setup(), register custom character to CGRAM slot 0: lcd.createChar(0, batteryIcon);. 3. To print: lcd.setCursor(0, 0); lcd.write(byte(0));.
* **Explanation**: HD44780 controllers support up to 8 custom 5x8 pixel characters (slots 0-7) created via createChar().

# Section D: Short Answer Questions (อัตนัย / อธิบายความรู้ 10 ข้อ)

<!--
RULES Section D:
- ข้อ 106–115 (10 ข้อ, 3 คะแนน/ข้อ)
-->
#### ข้อ 106
* **Topic**: Arduino Uno Hardware Architecture
* **Learning Objective**: LO-ARD1
* **Difficulty**: Hard
* **Prompt**: Describe the core hardware specifications of the Arduino Uno R3, including microcontroller model, operating voltage, clock speed, digital I/O count, analog input count, and flash memory size.
* **Expected Answer**: 1. Microcontroller: Microchip/Atmel ATmega328P (8-bit AVR architecture). 2. Operating Voltage: 5V DC (recommended input 7-12V on Vin/barrel jack). 3. Clock Speed: 16 MHz quartz crystal oscillator. 4. Digital I/O Pins: 14 pins (Pins 0-13, with 6 PWM outputs on pins 3, 5, 6, 9, 10, 11). 5. Analog Inputs: 6 pins (A0-A5 with 10-bit ADC). 6. Memory: 32 KB Flash memory (0.5 KB used by bootloader), 2 KB SRAM, 1 KB EEPROM.
#### ข้อ 107
* **Topic**: C++ Sketch Lifecycle and Flow
* **Learning Objective**: LO-ARD1
* **Difficulty**: Hard
* **Prompt**: Explain the execution lifecycle of an Arduino sketch, detailing the role of setup(), loop(), and the hidden main() function generated by the Arduino core.
* **Expected Answer**: When compiled, the Arduino core provides a hidden main() function that: 1. Initializes hardware timers and ADC subsystems via init(). 2. Calls the user's setup() function exactly once to configure pin modes, initialize serial communications, and attach libraries. 3. Enters an infinite for (;;) or while (1) loop that repeatedly calls the user's loop() function and handles serial event checks until the microcontroller is powered down or reset.
#### ข้อ 108
* **Topic**: Digital vs. Analog Signals & ADC Conversion
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Prompt**: Explain how the Arduino Uno reads analog sensor voltages using its 10-bit ADC, including the mathematical conversion formula and the significance of analogReference().
* **Expected Answer**: The ATmega328P uses a Successive Approximation 10-bit ADC that converts an input voltage (0V to Vref) into an integer from 0 to 1023 (2^10 = 1024 levels). Formula: Measured_Voltage = (analogRead(pin) * Vref) / 1023.0. By default, Vref is 5.0V (DEFAULT), yielding ~4.88 mV per unit resolution. analogReference() can switch Vref to INTERNAL (1.1V for higher sensitivity on small signals) or EXTERNAL (using voltage applied to the AREF pin).
#### ข้อ 109
* **Topic**: Pulse Width Modulation (PWM) Principles
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Prompt**: Describe how Pulse Width Modulation (PWM) works in Arduino to simulate analog output for LED dimming or motor speed, including duty cycle calculation and analogWrite() parameters.
* **Expected Answer**: PWM simulates variable analog output by switching a digital pin between 5V (HIGH) and 0V (LOW) at a fixed high frequency (~490 Hz or ~980 Hz). The proportion of time the signal stays HIGH during one cycle is called the Duty Cycle. Formula: Duty_Cycle (%) = (Value / 255.0) * 100%. Passing 0 gives 0% duty cycle (0V average / OFF); 128 gives 50% duty cycle (2.5V average); 255 gives 100% duty cycle (5V continuous / full speed).
#### ข้อ 110
* **Topic**: Blocking vs. Non-Blocking Timing Architecture
* **Learning Objective**: LO-ARD2
* **Difficulty**: Hard
* **Prompt**: Compare delay() versus millis() in Arduino time management, explaining why millis() is essential for multitasking and responsive embedded applications.
* **Expected Answer**: delay() is a blocking function that halts CPU instruction execution for a specified number of milliseconds, making the microcontroller blind to button presses, sensor changes, or incoming serial data during that window. In contrast, millis() is non-blocking; it returns the elapsed time from an internal hardware timer without pausing the CPU. By comparing (currentMillis - previousMillis >= interval), the CPU can execute other tasks simultaneously, enabling true cooperative multitasking on a single core.
#### ข้อ 111
* **Topic**: UART Serial Communication Mechanism
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Prompt**: Explain how UART Serial communication works between an Arduino Uno and a computer, detailing baud rates, transmit/receive buffers, and the roles of Serial.available(), Serial.read(), and Serial.print().
* **Expected Answer**: UART is an asynchronous serial communication protocol transmitting data frame by frame (start bit, 8 data bits, stop bit) at a agreed-upon Baud Rate (e.g. 9600 bps). Hardware pins 0 (RX) and 1 (TX) connect through an on-board USB-Serial bridge chip to the computer. Incoming bytes are placed into a 64-byte circular FIFO ring buffer in RAM. Serial.available() returns the count of unread bytes in this buffer; Serial.read() extracts one byte at a time; and Serial.print() formats and transmits outgoing ASCII data.
#### ข้อ 112
* **Topic**: I2C vs. SPI Protocol Comparison
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Prompt**: Compare I2C and SPI communication protocols in Arduino systems, contrasting pin requirements, communication speed, bus topologies, and device addressing methods.
* **Expected Answer**: 1. Pin Requirements: I2C needs only 2 lines (SDA, SCL); SPI requires 4 lines (MOSI, MISO, SCK, plus one SS/CS line per slave device). 2. Speed: SPI is full-duplex and significantly faster (up to 8+ MHz); I2C is half-duplex and slower (standard 100 kHz or fast 400 kHz). 3. Addressing: I2C uses software 7-bit addresses sent in the data stream to select slaves on a shared 2-wire bus; SPI uses dedicated physical Chip Select (CS) hardware pins pulled LOW to activate specific slaves.
#### ข้อ 113
* **Topic**: External Hardware Interrupts and ISR Design
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Prompt**: Detail the configuration and execution of external hardware interrupts on an Arduino Uno, explaining attachInterrupt(), trigger modes, ISR guidelines, and the volatile qualifier.
* **Expected Answer**: On the Uno, external hardware interrupts are available on Pin 2 (INT0) and Pin 3 (INT1). attachInterrupt(digitalPinToInterrupt(pin), ISR_func, mode) binds an ISR function to triggers (RISING, FALLING, CHANGE, LOW). Guidelines: ISRs must execute extremely fast; delay() and heavy Serial calls must not be used inside an ISR because nested interrupts are disabled. Any global variable modified inside an ISR and accessed in loop() must be declared volatile so the compiler reads it directly from RAM rather than caching it in CPU registers.
#### ข้อ 114
* **Topic**: EEPROM Memory Storage Architecture
* **Learning Objective**: LO-ARD3
* **Difficulty**: Hard
* **Prompt**: Explain the role and characteristics of EEPROM memory in an ATmega328P Arduino, including capacity, endurance limits, and the difference between EEPROM.write() and EEPROM.update().
* **Expected Answer**: The ATmega328P contains 1024 bytes (1 KB) of non-volatile EEPROM (addresses 0 to 1023) that retains configuration parameters, calibration constants, and state data when power is lost. Each cell has an endurance limit of approximately 100,000 write cycles. EEPROM.write(addr, val) writes a byte directly every time called. EEPROM.update(addr, val) first reads the existing byte and only performs a write operation if the value has changed, dramatically reducing wear and extending memory lifespan.
#### ข้อ 115
* **Topic**: Python and Arduino Integration via PySerial
* **Learning Objective**: LO-ARD4
* **Difficulty**: Hard
* **Prompt**: Explain how to establish a robust bidirectional communication pipeline between a Python desktop application and an Arduino Uno using the PySerial library.
* **Expected Answer**: 1. Arduino Setup: Configure Serial.begin(115200); in setup() and send structured data (e.g. comma-separated sensor values followed by newline '\n'). 2. Python Setup: Import serial, time and instantiate ser = serial.Serial('COM3', 115200, timeout=1). 3. Handshake & DTR Delay: Opening serial causes an automatic DTR reset on Arduino Uno; Python must wait 2 seconds (time.sleep(2)) for Arduino bootloader initialization before sending commands. 4. Data Exchange: Python sends ser.write(b'COMMAND\n') and reads responses via line = ser.readline().decode('utf-8').strip().
