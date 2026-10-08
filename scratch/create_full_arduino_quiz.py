#!/usr/bin/env python3
import os

md_file = 'Arduino_Assessment_.md'

content = []

# Header
content.append("""# Knowledge Assessment Quiz: Arduino Embedded Systems & Programming (Arduino Learning)

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
""")

# MCQ Data (1 to 60)
mcq_data = [
    # 1-15: Architecture, IDE, Setup, Pinout
    (1, "Arduino Architecture", "LO-ARD1", "Easy",
     "Which main microcontroller chip powers the standard Arduino Uno R3 board?",
     "ATmega328P", "ARM Cortex-M4", "ESP8266", "PIC16F877A",
     "ก", "The Arduino Uno R3 is powered by the 8-bit Microchip/Atmel ATmega328P microcontroller running at 16 MHz."),

    (2, "Sketch Structure", "LO-ARD1", "Easy",
     "What are the two mandatory functions that every Arduino sketch (.ino) must contain?",
     "start() and stop()", "setup() and loop()", "init() and main()", "begin() and run()",
     "ข", "Every Arduino program requires setup() (runs once at boot) and loop() (executes repeatedly indefinitely)."),

    (3, "Execution Flow", "LO-ARD1", "Easy",
     "When an Arduino board is powered on, how many times does the setup() function execute?",
     "Only once", "Repeatedly in an infinite loop", "Exactly 10 times", "Only when a button is pressed",
     "ก", "The setup() function executes exactly once upon power-up or whenever the reset button is pressed."),

    (4, "Operating Voltage", "LO-ARD1", "Easy",
     "What is the standard operating logic voltage of the digital pins on an Arduino Uno R3?",
     "1.8V", "3.3V", "5V", "12V",
     "ค", "The Arduino Uno R3 operates at 5V logic level, meaning HIGH is ~5V and LOW is 0V (GND)."),

    (5, "Hardware Pinout", "LO-ARD1", "Easy",
     "How many total Digital I/O pins are available on an Arduino Uno board (excluding dedicated analog-only pins)?",
     "8 pins", "14 pins (Pins 0 to 13)", "20 pins", "32 pins",
     "ข", "Arduino Uno features 14 digital I/O pins numbered from 0 to 13 (six of which support PWM output)."),

    (6, "Analog Inputs", "LO-ARD1", "Easy",
     "How many dedicated Analog Input pins (A0 to A5) are provided on an Arduino Uno?",
     "4 pins", "6 pins", "8 pins", "12 pins",
     "ข", "Arduino Uno provides 6 analog input pins labeled A0, A1, A2, A3, A4, and A5."),

    (7, "ADC Resolution", "LO-ARD1", "Medium",
     "What is the resolution of the Analog-to-Digital Converter (ADC) in the Arduino Uno?",
     "8-bit (0 to 255)", "10-bit (0 to 1023)", "12-bit (0 to 4095)", "16-bit (0 to 65535)",
     "ข", "The ATmega328P contains a 10-bit ADC, mapping 0 to 5V input into an integer range from 0 to 1023."),

    (8, "Clock Speed", "LO-ARD1", "Easy",
     "What is the crystal oscillator clock frequency of the Arduino Uno R3?",
     "8 MHz", "16 MHz", "48 MHz", "100 MHz",
     "ข", "The Arduino Uno operates with a 16 MHz external ceramic resonator / quartz crystal."),

    (9, "Built-in LED Pin", "LO-ARD1", "Easy",
     "Which digital pin on the Arduino Uno is connected to the on-board surface-mount LED (LED_BUILTIN)?",
     "Pin 0", "Pin 2", "Pin 9", "Pin 13",
     "ง", "Pin 13 is internally wired to the on-board LED through an active driver circuit on Arduino Uno."),

    (10, "Hardware Serial Pins", "LO-ARD1", "Medium",
     "Which two digital pins on the Arduino Uno serve as the primary hardware UART Serial pins (RX and TX)?",
     "Pin 0 (RX) and Pin 1 (TX)", "Pin 2 (RX) and Pin 3 (TX)", "Pin 10 (RX) and Pin 11 (TX)", "Pin A4 (RX) and Pin A5 (TX)",
     "ก", "Digital Pin 0 is Receive (RX) and Digital Pin 1 is Transmit (TX), shared with the on-board USB-to-Serial converter."),

    (11, "Power Pins", "LO-ARD1", "Easy",
     "What is the recommended DC input voltage range for the barrel jack or Vin pin of an Arduino Uno?",
     "3V to 5V", "7V to 12V", "24V to 48V", "110V to 220V AC",
     "ข", "The on-board linear voltage regulator operates reliably with an external DC supply of 7V to 12V."),

    (12, "IDE Compilation", "LO-ARD1", "Easy",
     "In the Arduino IDE, what does clicking the 'Verify / Compile' (Checkmark icon) button do?",
     "Uploads the program to the board", "Checks code syntax and compiles it into binary machine code", "Deletes the sketch", "Clears the EEPROM",
     "ข", "The Verify button checks syntax and compiles the C/C++ sketch into machine hex code without uploading."),

    (13, "IDE Upload Error", "LO-ARD1", "Medium",
     "If the Arduino IDE returns 'avrdude: ser_open(): can't open device', what is the most likely cause?",
     "Incorrect COM port selected or USB cable disconnected", "Syntax error inside setup()", "Using too many comments", "RAM memory is 100% full",
     "ก", "This avrdude communication error indicates the selected COM port is wrong, busy, or the USB cable is unplugged."),

    (14, "File Extension", "LO-ARD1", "Easy",
     "What is the standard file extension used for Arduino source code files?",
     ".c", ".cpp", ".ino", ".hex",
     "ค", "Arduino sketch files use the .ino extension (formerly .pde prior to Arduino 1.0)."),

    (15, "Current Limit per Pin", "LO-ARD1", "Medium",
     "What is the maximum absolute safe DC current that a single digital I/O pin of the ATmega328P can source/sink?",
     "5 mA", "20 mA (recommended) / 40 mA (absolute maximum)", "500 mA", "2 A",
     "ข", "Each I/O pin can safely source/sink up to 20 mA continuously (with 40 mA absolute maximum before hardware damage)."),

    # 16-30: Digital/Analog I/O, PWM & Actuators
    (16, "Pin Mode Configuration", "LO-ARD2", "Easy",
     "Which function must be called in setup() to configure a pin as an output?",
     "setPin(13, OUT);", "pinMode(13, OUTPUT);", "digitalWrite(13, HIGH);", "outputPin(13);",
     "ข", "pinMode(pin, mode) configures a specific digital pin as INPUT, OUTPUT, or INPUT_PULLUP."),

    (17, "Internal Pullup Resistor", "LO-ARD2", "Medium",
     "When configuring a pin with pinMode(2, INPUT_PULLUP), what voltage state is read when a pushbutton connected to GND is unpressed?",
     "0V (LOW)", "5V (HIGH)", "2.5V (FLOATING)", "-5V",
     "ข", "INPUT_PULLUP activates the internal 20k-50k ohm pullup resistor to 5V, reading HIGH when unpressed and LOW when pressed to GND."),

    (18, "Digital Output Control", "LO-ARD2", "Easy",
     "Which command sets Digital Pin 8 to 5V output to turn on an external LED?",
     "digitalWrite(8, HIGH);", "digitalRead(8, 5V);", "pinWrite(8, ON);", "analogWrite(8, 255);",
     "ก", "digitalWrite(pin, HIGH) sends 5V to the specified output pin."),

    (19, "Digital Input Reading", "LO-ARD2", "Easy",
     "What function reads the logic level (HIGH or LOW) of a digital input pin?",
     "analogRead()", "digitalRead()", "pinRead()", "digitalVal()",
     "ข", "digitalRead(pin) returns either HIGH (1) or LOW (0) from the specified digital pin."),

    (20, "Analog Value Calculation", "LO-ARD2", "Medium",
     "If analogRead(A0) returns a value of 512 with a 5V reference, what is the measured input voltage?",
     "1.25V", "2.5V", "3.75V", "5.0V",
     "ข", "Voltage = (512 / 1023.0) * 5.0V = approximately 2.50V (half of full scale)."),

    (21, "PWM Function", "LO-ARD2", "Easy",
     "Which Arduino function is used to output a Pulse Width Modulation (PWM) signal?",
     "pwmWrite()", "digitalWrite()", "analogWrite()", "setPWM()",
     "ค", "analogWrite(pin, value) generates a PWM square wave on designated PWM pins."),

    (22, "PWM Resolution & Range", "LO-ARD2", "Medium",
     "What is the valid parameter value range passed to analogWrite(pin, value)?",
     "0 to 1", "0 to 100", "0 to 255 (8-bit)", "0 to 1023 (10-bit)",
     "ค", "analogWrite() takes an 8-bit duty cycle value from 0 (0% duty cycle / always OFF) to 255 (100% duty cycle / always ON)."),

    (23, "PWM Pin Identification", "LO-ARD2", "Medium",
     "Which pins on the Arduino Uno support hardware PWM output via analogWrite()?",
     "Pins 0, 1, 2, 3, 4, 5", "Pins 3, 5, 6, 9, 10, 11 (marked with ~)", "Pins 2, 4, 6, 8, 10, 12", "All pins from 0 to 13",
     "ข", "On the Uno, digital pins 3, 5, 6, 9, 10, and 11 feature hardware PWM timers (marked with a tilde ~ symbol)."),

    (24, "Servo Motor Library", "LO-ARD2", "Easy",
     "Which header file must be included in an Arduino sketch to control a standard hobby servo motor?",
     "#include <Motor.h>", "#include <Servo.h>", "#include <PWM.h>", "#include <Actuator.h>",
     "ข", "The standard Arduino Servo library is included using #include <Servo.h>."),

    (25, "Servo Angle Command", "LO-ARD2", "Easy",
     "Given Servo myServo;, which command rotates the servo shaft to a 90-degree position?",
     "myServo.set(90);", "myServo.write(90);", "myServo.rotate(90);", "myServo.position(90);",
     "ข", "The write(angle) method of the Servo class commands the servo to a specific angular position (0 to 180 degrees)."),

    (26, "Piezo Buzzer Tone", "LO-ARD2", "Medium",
     "Which function generates a 440 Hz audio square wave tone on Digital Pin 8?",
     "tone(8, 440);", "sound(8, 440);", "audioWrite(8, 440);", "buzzer(8, 440);",
     "ก", "tone(pin, frequency) generates a 50% duty cycle square wave at the specified frequency in Hertz on the chosen pin."),

    (27, "Stopping Buzzer Tone", "LO-ARD2", "Easy",
     "Which function silences a tone generated by the tone() function on Pin 8?",
     "stopTone(8);", "noTone(8);", "silence(8);", "toneOff(8);",
     "ข", "noTone(pin) stops the square wave generation triggered by tone()."),

    (28, "LiquidCrystal Library", "LO-ARD2", "Medium",
     "When using a standard 16x2 character LCD with LiquidCrystal lcd(RS, E, D4, D5, D6, D7);, what must be called in setup()?",
     "lcd.init();", "lcd.begin(16, 2);", "lcd.start(16, 2);", "lcd.open();",
     "ข", "lcd.begin(cols, rows) initializes the display interface and specifies the dimensions (16 columns, 2 rows)."),

    (29, "Map Function", "LO-ARD2", "Medium",
     "What is the result of map(512, 0, 1023, 0, 255); in an Arduino sketch?",
     "0", "127 or 128", "255", "512",
     "ข", "map(val, fromLow, fromHigh, toLow, toHigh) proportionally scales 512 (50% of 1023) to approximately 127-128 (50% of 255)."),

    (30, "Constrain Function", "LO-ARD2", "Medium",
     "What does constrain(x, 10, 100); return if x has a value of 150?",
     "10", "100", "150", "0",
     "ข", "constrain(amt, low, high) clamps a number within the range, returning 100 when the value exceeds the upper bound."),

    # 31-45: Serial Communication, Protocols & Data Storage
    (31, "Serial Initialization", "LO-ARD3", "Easy",
     "Which command initializes serial communication at 9600 bits per second (baud)?",
     "Serial.start(9600);", "Serial.begin(9600);", "Serial.open(9600);", "Serial.connect(9600);",
     "ข", "Serial.begin(speed) sets the data rate in bits per second (baud rate) for serial data transmission."),

    (32, "Serial Available Check", "LO-ARD3", "Easy",
     "What does Serial.available() return?",
     "The current baud rate", "The number of bytes received and waiting in the serial buffer to be read", "True if the serial cable is plugged in", "The last character typed",
     "ข", "Serial.available() returns the count of bytes already received and stored in the 64-byte serial receive buffer."),

    (33, "Serial Read Character", "LO-ARD3", "Easy",
     "Which function reads one incoming byte from the serial buffer?",
     "Serial.get()", "Serial.read()", "Serial.input()", "Serial.fetch()",
     "ข", "Serial.read() reads and removes the next available byte from the serial receive buffer (or returns -1 if empty)."),

    (34, "Serial Print with Newline", "LO-ARD3", "Easy",
     "What is the difference between Serial.print(\"Hello\"); and Serial.println(\"Hello\");?",
     "Serial.println() appends a carriage return ('\\r') and newline ('\\n') at the end",
     "Serial.print() only works with numbers",
     "Serial.println() sends data in binary format",
     "There is no difference between them",
     "ก", "Serial.println() prints the data followed by carriage return (CR, ASCII 13) and newline (LF, ASCII 10)."),

    (35, "Python Serial Library", "LO-ARD3", "Medium",
     "Which Python package is commonly used to establish bidirectional serial communication with an Arduino board?",
     "pyarduino", "pyserial (import serial)", "python-usb", "serialnet",
     "ข", "PySerial (import serial) is the standard cross-platform Python module for reading/writing to serial ports."),

    (36, "I2C Protocol Pins", "LO-ARD3", "Medium",
     "Which pins on the Arduino Uno carry the I2C bus signals SDA (Serial Data) and SCL (Serial Clock)?",
     "Pins 0 (SDA) and 1 (SCL)", "Pins A4 (SDA) and A5 (SCL)", "Pins 10 (SDA) and 11 (SCL)", "Pins 2 (SDA) and 3 (SCL)",
     "ข", "On the Uno, Analog Pin A4 functions as SDA (Data) and Analog Pin A5 functions as SCL (Clock), also duplicated near AREF."),

    (37, "I2C Library", "LO-ARD3", "Easy",
     "Which built-in Arduino library handles I2C (Two-Wire Interface) communication?",
     "#include <SPI.h>", "#include <Wire.h>", "#include <I2C.h>", "#include <TwoWire.h>",
     "ข", "The Wire library (#include <Wire.h>) implements the I2C master and slave protocol."),

    (38, "SPI Protocol Signals", "LO-ARD3", "Medium",
     "What does the MOSI line represent in the SPI (Serial Peripheral Interface) communication protocol?",
     "Master In Slave Out", "Master Out Slave In", "Master Oscillator Signal Input", "Multiple Output Serial Interface",
     "ข", "MOSI stands for Master Out, Slave In — the data line carrying data from the Master to the Slave device."),

    (39, "SPI Hardware Pins on Uno", "LO-ARD3", "Medium",
     "Which digital pins on the Arduino Uno are assigned to hardware SPI (MOSI, MISO, SCK, SS)?",
     "Pins 11 (MOSI), 12 (MISO), 13 (SCK), 10 (SS)", "Pins 0 (MOSI), 1 (MISO), 2 (SCK), 3 (SS)", "Pins A0, A1, A2, A3", "Pins 4, 5, 6, 7",
     "ก", "On the Arduino Uno: Pin 11 = MOSI, Pin 12 = MISO, Pin 13 = SCK, Pin 10 = default SS (Slave Select)."),

    (40, "EEPROM Memory", "LO-ARD3", "Medium",
     "What is a primary characteristic of the ATmega328P's internal EEPROM memory?",
     "Data is wiped every time the power is disconnected", "Data is non-volatile and persists across power cycles and resets", "It holds 16 Gigabytes of data", "It executes code faster than Flash memory",
     "ข", "EEPROM (Electrically Erasable Programmable Read-Only Memory) provides 1 KB of non-volatile storage that persists when power is cut."),

    (41, "EEPROM Write vs Update", "LO-ARD3", "Medium",
     "Why is EEPROM.update(address, value) preferred over EEPROM.write(address, value)?",
     "EEPROM.update() only writes to memory if the new value is different, saving write endurance cycles",
     "EEPROM.update() encrypts the stored data with a password",
     "EEPROM.update() can write unlimited megabytes of data",
     "EEPROM.write() was deleted in newer Arduino versions",
     "ก", "EEPROM cells have a lifespan of ~100,000 write cycles; EEPROM.update() prevents unnecessary wear by checking if the value changed."),

    (42, "SD Card Communication", "LO-ARD3", "Medium",
     "Which communication protocol does the standard Arduino SD Card library (#include <SD.h>) use to communicate with SD card modules?",
     "UART Serial", "I2C", "SPI", "OneWire",
     "ค", "SD and MicroSD card breakout modules interface with the Arduino via high-speed SPI bus (Pins 11, 12, 13 + CS)."),

    (43, "Bluetooth Module Interface", "LO-ARD3", "Medium",
     "Which module is commonly used to provide classic Bluetooth serial communication to an Arduino Uno?",
     "HC-05 / HC-06", "ESP32", "NRF24L01", "SIM800L",
     "ก", "HC-05 (Master/Slave) and HC-06 (Slave-only) are popular UART serial Bluetooth bridge modules for Arduino."),

    (44, "SoftwareSerial Library", "LO-ARD3", "Medium",
     "Why do developers use the SoftwareSerial library on an Arduino Uno?",
     "To simulate digital pins on analog ports", "To create a software-emulated UART serial port on arbitrary digital pins without interfering with USB pins 0 and 1", "To speed up the microcontroller clock to 32 MHz", "To write Python code directly inside Arduino IDE",
     "ข", "SoftwareSerial allows using other digital pins (e.g. Pins 2 & 3) for serial sensors or Bluetooth while keeping Pins 0 & 1 free for USB debugging."),

    (45, "I2C Addressing", "LO-ARD3", "Medium",
     "In I2C communication, how does a Master device select which Slave device it wants to communicate with on shared SDA/SCL lines?",
     "By sending the unique 7-bit hardware address of the slave device", "By pulling all pins LOW simultaneously", "By switching the baud rate to 115200", "By cutting power to all other devices",
     "ก", "Each slave device on an I2C bus has a unique 7-bit (or 10-bit) address; the master broadcasts this address in the start frame."),

    # 46-60: Programming, Timing, Interrupts & Best Practices
    (46, "Data Types - Byte", "LO-ARD1", "Easy",
     "What is the value range that an 8-bit unsigned byte variable can hold in Arduino C++?",
     "-128 to 127", "0 to 255", "0 to 65535", "-32768 to 32767",
     "ข", "A byte is an unsigned 8-bit integer holding values from 0 to 255 (0x00 to 0xFF)."),

    (47, "Data Types - Int on Uno", "LO-ARD1", "Easy",
     "How many bits and what range does a standard signed int have on an 8-bit AVR Arduino Uno?",
     "8-bit (0 to 255)", "16-bit (-32,768 to 32,767)", "32-bit (-2,147,483,648 to 2,147,483,647)", "64-bit",
     "ข", "On 8-bit AVR microcontrollers (Uno, Nano, Mega), an int is 16-bit signed with range -32,768 to +32,767."),

    (48, "Data Types - Unsigned Long", "LO-ARD1", "Medium",
     "Which data type must be used to store the return value of millis() to prevent overflow bugs?",
     "byte", "int", "float", "unsigned long",
     "ง", "millis() returns a 32-bit unsigned integer (unsigned long) that counts milliseconds up to ~49.7 days before rolling over to 0."),

    (49, "Millis Function", "LO-ARD2", "Easy",
     "What does the millis() function return?",
     "The current real-world clock time in GMT", "The number of milliseconds passed since the Arduino board began running the current program", "The temperature of the ATmega328P chip", "The remaining battery voltage",
     "ข", "millis() returns the elapsed time in milliseconds since program execution started."),

    (50, "Delay Disadvantage", "LO-ARD2", "Medium",
     "Why is using delay(1000) considered bad practice in complex, responsive embedded systems?",
     "It consumes too much EEPROM flash space", "It is a blocking call that freezes the CPU, preventing it from reading buttons or sensors during the pause", "It damages the crystal oscillator over time", "It reverses the polarity of power pins",
     "ข", "delay() halts all execution (except background hardware interrupts), making the board unresponsive to inputs during the wait time."),

    (51, "External Interrupt Pins on Uno", "LO-ARD4", "Medium",
     "Which digital pins on an Arduino Uno support external hardware interrupts via attachInterrupt()?",
     "Pins 0 and 1", "Pins 2 (Interrupt 0) and 3 (Interrupt 1)", "Pins 9 and 10", "Pins A0 and A1",
     "ข", "Arduino Uno provides two external hardware interrupt pins: Digital Pin 2 (INT0) and Digital Pin 3 (INT1)."),

    (52, "Interrupt Mode Types", "LO-ARD4", "Medium",
     "Which interrupt trigger mode fires an ISR when a digital pin transitions from LOW (0V) to HIGH (5V)?",
     "LOW", "CHANGE", "FALLING", "RISING",
     "ง", "RISING triggers the interrupt when the pin changes state from LOW to HIGH. FALLING triggers from HIGH to LOW."),

    (53, "Volatile Keyword", "LO-ARD4", "Hard",
     "Why must global variables shared between an Interrupt Service Routine (ISR) and the main loop() be declared with volatile?",
     "To tell the compiler not to cache the variable in a CPU register, ensuring fresh reads from RAM",
     "To make the variable permanent in EEPROM",
     "To protect the variable from unauthorized WiFi access",
     "To convert the variable into floating-point format automatically",
     "ก", "The volatile qualifier prevents compiler optimization from caching the variable, ensuring the main loop always sees changes made inside the ISR."),

    (54, "ISR Best Practices", "LO-ARD4", "Medium",
     "What is a critical rule to follow when writing an Interrupt Service Routine (ISR) function in Arduino?",
     "Keep the ISR as short and fast as possible; avoid calling delay() or lengthy Serial.print() inside it",
     "Always insert delay(500) inside the ISR to debounce switches",
     "Perform complex floating-point calculations and file writes inside the ISR",
     "Call attachInterrupt() repeatedly inside the ISR",
     "ก", "ISRs must execute swiftly. Since interrupts are disabled inside an ISR, delay() will not tick and Serial buffers can overflow."),

    (55, "Array Syntax", "LO-ARD1", "Easy",
     "How do you declare and initialize an array of 4 integer pin numbers in Arduino C++?",
     "int pins = [2, 4, 6, 8];", "int pins[4] = {2, 4, 6, 8};", "array int pins(2, 4, 6, 8);", "pins[] = {2, 4, 6, 8};",
     "ข", "In C/C++, array declaration uses int pins[4] = {2, 4, 6, 8}; with curly braces for initialization."),

    (56, "Modulo Operator", "LO-ARD1", "Medium",
     "What is the result of the expression 17 % 5 in Arduino C++?",
     "3.4", "3", "2", "0",
     "ค", "The modulo operator (%) computes the integer remainder after division: 17 divided by 5 is 3 with a remainder of 2."),

    (57, "Blink Without Delay Pattern", "LO-ARD2", "Medium",
     "In the 'Blink Without Delay' paradigm, what condition triggers the LED state toggle?",
     "if (millis() - previousMillis >= interval)", "if (delay() == 1000)", "if (digitalRead(13) == true)", "if (Serial.available() > 0)",
     "ก", "The non-blocking timer calculates elapsed time by subtracting the saved timestamp from current millis(): (currentMillis - previousMillis >= interval)."),

    (58, "Random Number Generation", "LO-ARD2", "Medium",
     "Why is randomSeed(analogRead(A0)) frequently placed in setup() when an unconnected analog pin is used?",
     "To initialize the pseudo-random number generator with unpredictable atmospheric electrical noise",
     "To calibrate the analog pin for temperature measurement",
     "To increase the RAM memory capacity",
     "To reset the microcontroller every 10 seconds",
     "ก", "A floating analog pin picks up ambient electromagnetic noise, providing an unpredictable seed for random()."),

    (59, "Bitwise Operations", "LO-ARD1", "Medium",
     "What does the bitwise left-shift operation (1 << 3) evaluate to in binary and decimal?",
     "B00000001 (1)", "B00000100 (4)", "B00001000 (8)", "B00010000 (16)",
     "ค", "Left-shifting binary 1 by 3 positions yields 00001000 in binary, which is decimal 8 (2^3)."),

    (60, "Firmware Reset via Code", "LO-ARD4", "Hard",
     "What is the safest hardware-supported method to reset an Arduino via software if a program hangs?",
     "Configuring and using the internal AVR Watchdog Timer (WDT) via #include <avr/wdt.h>",
     "Connecting Digital Pin 13 directly to 5V",
     "Calling setup() inside loop() continuously",
     "Writing 255 to all EEPROM addresses",
     "ก", "The AVR Watchdog Timer (wdt_enable, wdt_reset) resets the processor automatically if the firmware hangs and fails to kick the dog.")
]

for item in mcq_data:
    q_num, topic, lo, diff, prompt, opt_a, opt_b, opt_c, opt_d, ans, exp = item
    content.append(f"""#### ข้อ {q_num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Prompt**: {prompt}
* ก. {opt_a}
* ข. {opt_b}
* ค. {opt_c}
* ง. {opt_d}
* **Correct Answer**: {ans}
* **Explanation**: {exp}
""")

content.append("""
# Section B: True / False Questions (ถูก / ผิด 30 ข้อ)

<!--
RULES Section B:
- ข้อ 61–90 (30 ข้อ, 1 คะแนน/ข้อ)
- **Correct Answer**: True | False
-->
""")

# TF Data (61 to 90)
tf_data = [
    (61, "Arduino Hardware", "LO-ARD1", "Easy",
     "The Arduino Uno R3 digital pins can directly supply 10 Amperes of current to drive heavy industrial motors.",
     "False", "Arduino pins have a safe limit of ~20 mA (40 mA absolute max). External transistors, relays, or motor drivers (e.g. L298N) are required for motors."),

    (62, "Sketch Execution", "LO-ARD1", "Easy",
     "Code written inside the loop() function runs repeatedly until the Arduino board is powered off or reset.",
     "True", "The loop() function executes endlessly in a continuous cycle after setup() finishes."),

    (63, "ADC Reading", "LO-ARD2", "Easy",
     "analogRead() on an Arduino Uno returns an integer value ranging from 0 to 1023.",
     "True", "The built-in 10-bit ADC converts 0V-5V input voltages into values from 0 to 1023."),

    (64, "PWM Output", "LO-ARD2", "Easy",
     "analogWrite(pin, 0) outputs a continuous 0V (0% duty cycle), while analogWrite(pin, 255) outputs continuous 5V (100% duty cycle).",
     "True", "analogWrite() uses an 8-bit parameter (0-255) to control the duty cycle of the PWM square wave."),

    (65, "PWM Hardware", "LO-ARD2", "Medium",
     "On the Arduino Uno, analogWrite() can be called on any digital pin from 0 through 13 with equal hardware timer support.",
     "False", "Only digital pins 3, 5, 6, 9, 10, and 11 on the Uno have built-in PWM timer support (marked with ~)."),

    (66, "Internal Pullup", "LO-ARD2", "Easy",
     "When pinMode(pin, INPUT_PULLUP) is configured, connecting a pushbutton between the pin and GND will read LOW when pressed.",
     "True", "The internal resistor pulls the line to HIGH (5V) when unpressed, and pressing the button connects the pin to GND (LOW)."),

    (67, "Serial Baud Rate", "LO-ARD3", "Easy",
     "Both the Arduino sketch (Serial.begin) and the Serial Monitor dropdown must be set to the same baud rate to display readable text.",
     "True", "Mismatched baud rates result in corrupted gibberish characters on the Serial Monitor."),

    (68, "Serial Communication Buffer", "LO-ARD3", "Medium",
     "Serial.read() reads all available bytes in the serial buffer simultaneously and returns them as a single String.",
     "False", "Serial.read() reads only a single byte (character) at a time from the incoming buffer."),

    (69, "I2C Wire Connection", "LO-ARD3", "Medium",
     "The I2C communication protocol requires only two signal lines: SDA (Data) and SCL (Clock), plus a common ground.",
     "True", "I2C is a 2-wire synchronous serial protocol sharing SDA and SCL across multiple addressed devices."),

    (70, "I2C Pins on Uno", "LO-ARD3", "Medium",
     "On the Arduino Uno, Analog Pin A4 is SCL and Analog Pin A5 is SDA.",
     "False", "On the Uno, Analog Pin A4 is SDA (Data) and Analog Pin A5 is SCL (Clock)."),

    (71, "SPI Bus Speed", "LO-ARD3", "Medium",
     "SPI (Serial Peripheral Interface) communication is generally much faster than I2C and UART serial communication.",
     "True", "SPI uses dedicated clock and separate input/output lines (MOSI/MISO), achieving speeds of several megahertz."),

    (72, "SPI Slave Select", "LO-ARD3", "Medium",
     "In SPI communication, multiple slave devices can share the same MOSI, MISO, and SCK lines if each slave has a dedicated Chip Select (CS/SS) pin.",
     "True", "Each slave device is activated individually by pulling its dedicated Slave Select (SS) pin LOW."),

    (73, "EEPROM Endurance", "LO-ARD3", "Medium",
     "Writing to the EEPROM in a fast loop() without conditions can wear out the flash memory cells in a matter of minutes.",
     "True", "EEPROM cells are rated for ~100,000 write cycles; an unconditional write in a tight loop exhausts this lifespan rapidly."),

    (74, "EEPROM Retention", "LO-ARD3", "Easy",
     "Data stored in EEPROM using EEPROM.write() is retained even after the Arduino is powered off.",
     "True", "EEPROM is non-volatile memory designed specifically for permanent data retention across power cycles."),

    (75, "Blocking Delay", "LO-ARD2", "Easy",
     "Calling delay(5000) allows the Arduino to continue checking if a user presses a button during those 5 seconds.",
     "False", "delay() is blocking; the microcontroller stops executing normal code and cannot poll button states during the delay."),

    (76, "Millis Timer", "LO-ARD2", "Medium",
     "The millis() timer stops counting whenever a digitalRead() function is called.",
     "False", "millis() relies on Hardware Timer 0 overflow interrupts and continues incrementing in the background continuously."),

    (77, "External Interrupts Pins", "LO-ARD4", "Medium",
     "Digital Pin 2 and Digital Pin 3 are the only two external hardware interrupt pins available on the standard Arduino Uno.",
     "True", "The ATmega328P on the Uno maps INT0 to Digital Pin 2 and INT1 to Digital Pin 3."),

    (78, "Interrupt Service Routine", "LO-ARD4", "Medium",
     "Calling delay(1000) inside an Interrupt Service Routine (ISR) is a recommended technique for debouncing switches.",
     "False", "delay() relies on interrupts, which are disabled inside an ISR. Calling delay() inside an ISR causes the code to hang."),

    (79, "Volatile Keyword in ISR", "LO-ARD4", "Hard",
     "Variables modified inside an ISR and checked in the loop() should be declared with the volatile keyword.",
     "True", "volatile forces the compiler to load the variable from RAM each time, ensuring the loop() sees updates from the ISR."),

    (80, "Servo Power Supply", "LO-ARD2", "Medium",
     "High-torque hobby servos should ideally be powered from an external 5V power supply rather than directly from the Arduino's 5V pin.",
     "True", "Servos draw high peak stall currents (up to 1A+) which can overload the Arduino regulator and cause brownout resets."),

    (81, "Tone Function Limitation", "LO-ARD2", "Medium",
     "The tone() function can play polyphonic 5-note musical chords simultaneously on a single digital pin.",
     "False", "tone() produces only a single square wave frequency (monophonic) at any given moment on a pin."),

    (82, "LiquidCrystal Pin Requirement", "LO-ARD2", "Medium",
     "In 4-bit mode, an HD44780 LCD display requires 6 Arduino digital pins (RS, Enable, D4, D5, D6, D7).",
     "True", "4-bit mode utilizes 6 I/O lines, saving pins compared to 8-bit mode (which requires 10 pins)."),

    (83, "Python PySerial Communication", "LO-ARD4", "Medium",
     "When Python opens a serial connection to an Arduino Uno, the DTR line automatically triggers an Arduino hardware reboot by default.",
     "True", "Opening the serial port pulses DTR, resetting the ATmega328P to initiate the bootloader."),

    (84, "Analog Reference Voltage", "LO-ARD2", "Medium",
     "Calling analogReference(INTERNAL) on an Arduino Uno changes the ADC reference voltage to 1.1 Volts.",
     "True", "On ATmega328P, the internal reference is a precise ~1.1V bandgap voltage."),

    (85, "Array Indexing", "LO-ARD1", "Easy",
     "In Arduino C++, the first element of an array myValues[5] is accessed at index 0 (myValues[0]).",
     "True", "C/C++ arrays are zero-indexed, meaning elements range from index 0 to size-1."),

    (86, "Data Types - Boolean", "LO-ARD1", "Easy",
     "A boolean data type in Arduino can only hold one of two values: true or false.",
     "True", "boolean (or bool) represents logical truth values true (1) or false (0)."),

    (87, "Digital Pin as Analog Output", "LO-ARD2", "Medium",
     "The analogWrite() function outputs a true, smooth, continuous analog DC voltage like a variable DAC battery.",
     "False", "analogWrite() outputs a Pulse Width Modulated (PWM) high-frequency digital square wave, not a true continuous analog voltage."),

    (88, "Const Keyword", "LO-ARD1", "Easy",
     "Declaring const int ledPin = 13; prevents the value of ledPin from being accidentally modified later in the code.",
     "True", "The const qualifier marks a variable as read-only, causing a compiler error if modified."),

    (89, "Hardware Reset Pin", "LO-ARD1", "Easy",
     "Pulling the RESET pin on the Arduino Uno to GND momentarily resets the microcontroller.",
     "True", "The active-low RESET pin restarts the ATmega328P when pulled to 0V (GND)."),

    (90, "SD Card Library", "LO-ARD3", "Medium",
     "The Arduino SD library supports opening multiple files simultaneously for writing on an ATmega328P without RAM constraints.",
     "False", "Each open file buffer requires 512 bytes of SRAM. On a 2KB RAM Uno, opening multiple files risks running out of memory.")
]

for item in tf_data:
    q_num, topic, lo, diff, stmt, ans, exp = item
    content.append(f"""#### ข้อ {q_num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Statement**: {stmt}
* **Correct Answer**: {ans}
* **Explanation**: {exp}
""")

content.append("""
# Section C: Scenario-Based Questions (สถานการณ์จำลอง 15 ข้อ)

<!--
RULES Section C:
- ข้อ 91–105 (15 ข้อ, 2 คะแนน/ข้อ)
-->
""")

# Scenario Data (91 to 105)
scenario_data = [
    (91, "Non-blocking Timer Design", "LO-ARD2", "Hard",
     "Developer Alex wants an Arduino Uno to blink an LED on Pin 13 every 500 ms while continuously monitoring a pushbutton on Pin 2. When using delay(500), button presses during the delay are missed.",
     "How should Alex redesign the code using millis() to achieve responsive non-blocking operation?",
     "Alex should store the current timestamp in an unsigned long currentMillis = millis();. He should check if (currentMillis - previousMillis >= 500). When true, update previousMillis = currentMillis; and toggle the LED state. Outside this condition in loop(), the pushbutton on Pin 2 can be read with digitalRead(2) on every iteration without delay, ensuring instant response.",
     "The millis() pattern allows multitasking by checking elapsed time on each cycle without blocking CPU execution."),

    (92, "Analog Voltage Measurement & Calibration", "LO-ARD2", "Hard",
     "A student connects a 10k potentiometer to Analog Pin A0. The analogRead(A0) function returns a raw integer value of 768. The reference voltage is 5.00V.",
     "Calculate the exact measured voltage on Pin A0 and write the Arduino C++ formula to compute it.",
     "Formula: float voltage = (rawADC * 5.0) / 1023.0; Calculation: (768 * 5.0) / 1023.0 = 3840.0 / 1023.0 = approximately 3.75 Volts (or 3.753V).",
     "ADC mapping divides the 10-bit reading (0-1023) by 1023.0 and multiplies by the 5.0V reference."),

    (93, "Pushbutton Active-Low Circuit with Internal Pullup", "LO-ARD2", "Hard",
     "A circuit connects a momentary tactile button between Digital Pin 4 and GND with no external resistors. The designer writes pinMode(4, INPUT_PULLUP);.",
     "Explain the logic states read by digitalRead(4) when the button is open (unpressed) vs closed (pressed), and describe how to light an LED when pressed.",
     "When unpressed, the internal pullup resistor pulls Pin 4 to 5V (HIGH / 1). When pressed, the button grounds Pin 4 to 0V (LOW / 0). To turn ON an LED when pressed, the code should check: if (digitalRead(4) == LOW) { digitalWrite(ledPin, HIGH); } else { digitalWrite(ledPin, LOW); }.",
     "INPUT_PULLUP creates an active-low input circuit, reading LOW when the button connects the pin to ground."),

    (94, "PWM Motor Speed Control with Serial Commands", "LO-ARD3", "Hard",
     "A robotics engineer controls a DC motor speed on PWM Pin 9 via the Serial Monitor. The user sends single-byte characters from '0' (stop) to '9' (full speed).",
     "Write the Arduino code snippet to read the serial character and map '0'-'9' to the appropriate PWM duty cycle on Pin 9.",
     "In loop(): if (Serial.available() > 0) { char c = Serial.read(); if (c >= '0' && c <= '9') { int speed = map(c - '0', 0, 9, 0, 255); analogWrite(9, speed); Serial.print(\"Motor speed set to: \"); Serial.println(speed); } }.",
     "Characters '0'-'9' are converted to integer 0-9 by subtracting '0' (ASCII 48), then mapped to PWM range 0-255."),

    (95, "External Hardware Interrupt with Button Debouncing", "LO-ARD4", "Hard",
     "An optical tachometer sensor generates a pulse every time a motor wheel completes one rotation, connected to Digital Pin 2. The engineer needs to count total rotations accurately without missing pulses during LCD screen updates.",
     "How should the engineer configure attachInterrupt() on Pin 2 and declare the counter variable?",
     "1. Declare a global variable: volatile unsigned long revCount = 0;. 2. In setup(): pinMode(2, INPUT_PULLUP); attachInterrupt(digitalPinToInterrupt(2), countRev, FALLING);. 3. Define the ISR: void countRev() { revCount++; }. The volatile keyword ensures revCount updates safely across interrupt boundaries without compiler register caching.",
     "Hardware interrupts trigger immediately on edge transitions (FALLING), ensuring pulses are never lost during slow LCD routines."),

    (96, "Python to Arduino Serial Protocol", "LO-ARD4", "Hard",
     "A Python application sends the string 'LED_ON\\n' or 'LED_OFF\\n' over USB serial COM port at 9600 baud to an Arduino Uno.",
     "Describe how the Arduino sketch should buffer and parse the incoming serial string to turn Pin 13 ON or OFF.",
     "In loop(): if (Serial.available() > 0) { String command = Serial.readStringUntil('\\n'); command.trim(); if (command == \"LED_ON\") { digitalWrite(13, HIGH); Serial.println(\"ACK: ON\"); } else if (command == \"LED_OFF\") { digitalWrite(13, LOW); Serial.println(\"ACK: OFF\"); } }.",
     "Serial.readStringUntil('\\n') captures text until newline, and trim() removes whitespace for accurate string comparison."),

    (97, "EEPROM Configuration Persistence", "LO-ARD3", "Hard",
     "A smart thermostat allows users to set a desired target temperature (e.g. 24 degrees Celsius) via buttons. If power goes out, the user setting must not be lost.",
     "Explain how to use EEPROM.h to load the setting on startup and save the setting only when changed.",
     "1. In setup(): byte targetTemp = EEPROM.read(0); if (targetTemp == 255 || targetTemp < 10 || targetTemp > 40) targetTemp = 24; (default sanity check). 2. When the user changes temperature with buttons, save with: EEPROM.update(0, targetTemp);. EEPROM.update() avoids unnecessary flash wear by only writing when targetTemp has altered.",
     "EEPROM retains settings across power cuts. EEPROM.update() preserves write endurance."),

    (98, "I2C Multi-Sensor Bus Architecture", "LO-ARD3", "Hard",
     "An IoT weather station connects an I2C OLED display (address 0x3C), an I2C BMP280 pressure sensor (address 0x76), and an I2C RTC clock (address 0x68) to an Arduino Uno.",
     "Explain how the hardware wiring is arranged for all 3 devices and how the Arduino communicates with each device independently.",
     "Hardware Wiring: All 3 devices share the same two bus wires: SDA connects to A4 and SCL connects to A5, with pullup resistors (4.7k) to 5V/3.3V and common GND. Communication: Because each peripheral has a distinct 7-bit I2C address (0x3C, 0x76, 0x68), the Arduino Master addresses each device individually using Wire.beginTransmission(address) without physical signal conflicts.",
     "I2C is an addressable multi-drop bus where devices share common SDA/SCL lines and respond only to their unique address."),

    (99, "SPI Communication with Multiple Slaves", "LO-ARD3", "Hard",
     "An embedded system interfaces two SPI devices: a high-speed MicroSD Card module and an SPI digital potentiometer (MCP41010) on an Arduino Uno.",
     "How are the SPI pins connected between the Uno and the two SPI modules, and how does the code select which device to talk to?",
     "Shared Pins: Both modules share Digital Pin 11 (MOSI), Pin 12 (MISO), and Pin 13 (SCK). Separate Pins: The SD card CS connects to Pin 4, and the MCP41010 CS connects to Pin 10. To talk to the MCP41010: digitalWrite(10, LOW); SPI.transfer(data); digitalWrite(10, HIGH);. Pin 4 remains HIGH (inactive) during this transfer.",
     "SPI peripherals share MOSI, MISO, and SCK lines while being selected individually by driving their specific Chip Select (CS) pin LOW."),

    (100, "Servo Sweeping with Non-blocking Timing", "LO-ARD2", "Hard",
     "A surveillance camera pan mechanism uses a Servo on Pin 9. It must sweep back and forth between 0 and 180 degrees, incrementing 1 degree every 20 ms without using delay(20).",
     "Outline the non-blocking state machine algorithm to implement this sweep.",
     "Declare global variables: int pos = 0; int step = 1; unsigned long lastMove = 0;. In loop(): unsigned long now = millis(); if (now - lastMove >= 20) { lastMove = now; pos += step; myServo.write(pos); if (pos >= 180 || pos <= 0) { step = -step; } }.",
     "Using an interval timer with a directional step variable (+1/-1) creates smooth sweeping without blocking CPU time."),

    (101, "Preventing Variable Overflow in Millis", "LO-ARD4", "Hard",
     "A beginner programmer writes: int lastTime = 0; if (millis() - lastTime > 1000) { lastTime = millis(); toggleLED(); }. After approximately 32.7 seconds, the LED stops blinking properly.",
     "Diagnose the bug and provide the proper fix.",
     "Diagnosis: On Arduino Uno, an int is a 16-bit signed integer (maximum +32,767). After 32,767 ms (~32.7 seconds), lastTime overflows into negative values (-32,768), breaking the arithmetic comparison. Fix: Change lastTime declaration to unsigned long lastTime = 0;, which can hold values up to ~4,294,967,295 ms (~49.7 days) and handles rollover subtraction safely.",
     "Timer variables tracking millis() must always use the unsigned long data type to avoid 16-bit signed integer overflow."),

    (102, "HC-05 Bluetooth Control Circuit", "LO-ARD3", "Hard",
     "An HC-05 Bluetooth module has its TX pin connected to Arduino Pin 2 (RX) and RX pin connected to Arduino Pin 3 (TX) through a voltage divider (2k/1k resistors).",
     "Why is a voltage divider required on the HC-05 RX line, and how is SoftwareSerial initialized in code?",
     "1. Voltage Divider: The HC-05 RX pin operates at 3.3V logic level. Connecting Arduino's 5V TX pin directly can damage the Bluetooth module; the voltage divider steps 5V down to ~3.3V. 2. SoftwareSerial: #include <SoftwareSerial.h> SoftwareSerial btSerial(2, 3); // RX=2, TX=3. In setup(): btSerial.begin(9600);.",
     "Level shifting protects 3.3V Bluetooth inputs from 5V Arduino outputs. SoftwareSerial enables communication on Pins 2 and 3."),

    (103, "SD Card Data Logger Failure Modes", "LO-ARD3", "Hard",
     "An environmental data logger writes sensor readings to an SD card file every 10 seconds. After 2 hours, the file on the SD card is corrupted or 0 bytes.",
     "Identify two common causes for this issue and explain the correct file handling practice in Arduino.",
     "Causes: 1. Failure to call myFile.close() or myFile.flush() after writing, leaving data in the RAM buffer without flushing to physical SD flash. 2. Loss of power during write operations without file closing. Practice: Open file -> write data -> immediately close file: File dataFile = SD.open(\"log.txt\", FILE_WRITE); if (dataFile) { dataFile.println(dataString); dataFile.close(); }.",
     "Calling myFile.close() or myFile.flush() writes the buffer and updates FAT directory tables, preventing data corruption."),

    (104, "Debouncing a Mechanical Switch in Software", "LO-ARD2", "Hard",
     "When pressing a mechanical tactile button, the metal contacts bounce rapidly for 5-10 ms, causing a counter to increment by 3 or 4 instead of 1.",
     "Explain how software debouncing solves this problem without adding physical capacitors.",
     "Software debouncing reads the button state and checks if it remains stable for a debounce interval (e.g. 50 ms) before registering a valid press. When a state transition is detected, the current millis() is saved. Only if the state stays constant for >50 ms is the state change accepted and the counter incremented by exactly 1.",
     "Software debouncing ignores rapid contact bounce transitions by waiting for signal stabilization."),

    (105, "LiquidCrystal Custom Character Creation", "LO-ARD2", "Hard",
     "A developer wants to create a custom battery indicator icon on a 16x2 HD44780 LCD display using the LiquidCrystal library.",
     "Describe the process of defining the 5x8 pixel binary array and registering it with lcd.createChar().",
     "1. Define byte array of 8 rows: byte batteryIcon[8] = { B01110, B11111, B10001, B10001, B11111, B11111, B11111, B11111 };. 2. In setup(), register custom character to CGRAM slot 0: lcd.createChar(0, batteryIcon);. 3. To print: lcd.setCursor(0, 0); lcd.write(byte(0));.",
     "HD44780 controllers support up to 8 custom 5x8 pixel characters (slots 0-7) created via createChar().")
]

for item in scenario_data:
    q_num, topic, lo, diff, scen, q, ans, exp = item
    content.append(f"""#### ข้อ {q_num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Scenario**: {scen}
* **Question**: {q}
* **Answer**: {ans}
* **Explanation**: {exp}
""")

content.append("""
# Section D: Short Answer Questions (อัตนัย / อธิบายความรู้ 10 ข้อ)

<!--
RULES Section D:
- ข้อ 106–115 (10 ข้อ, 3 คะแนน/ข้อ)
-->
""")

# Short Answer Data (106 to 115)
sa_data = [
    (106, "Arduino Uno Hardware Architecture", "LO-ARD1", "Hard",
     "Describe the core hardware specifications of the Arduino Uno R3, including microcontroller model, operating voltage, clock speed, digital I/O count, analog input count, and flash memory size.",
     "1. Microcontroller: Microchip/Atmel ATmega328P (8-bit AVR architecture). 2. Operating Voltage: 5V DC (recommended input 7-12V on Vin/barrel jack). 3. Clock Speed: 16 MHz quartz crystal oscillator. 4. Digital I/O Pins: 14 pins (Pins 0-13, with 6 PWM outputs on pins 3, 5, 6, 9, 10, 11). 5. Analog Inputs: 6 pins (A0-A5 with 10-bit ADC). 6. Memory: 32 KB Flash memory (0.5 KB used by bootloader), 2 KB SRAM, 1 KB EEPROM."),

    (107, "C++ Sketch Lifecycle and Flow", "LO-ARD1", "Hard",
     "Explain the execution lifecycle of an Arduino sketch, detailing the role of setup(), loop(), and the hidden main() function generated by the Arduino core.",
     "When compiled, the Arduino core provides a hidden main() function that: 1. Initializes hardware timers and ADC subsystems via init(). 2. Calls the user's setup() function exactly once to configure pin modes, initialize serial communications, and attach libraries. 3. Enters an infinite for (;;) or while (1) loop that repeatedly calls the user's loop() function and handles serial event checks until the microcontroller is powered down or reset."),

    (108, "Digital vs. Analog Signals & ADC Conversion", "LO-ARD2", "Hard",
     "Explain how the Arduino Uno reads analog sensor voltages using its 10-bit ADC, including the mathematical conversion formula and the significance of analogReference().",
     "The ATmega328P uses a Successive Approximation 10-bit ADC that converts an input voltage (0V to Vref) into an integer from 0 to 1023 (2^10 = 1024 levels). Formula: Measured_Voltage = (analogRead(pin) * Vref) / 1023.0. By default, Vref is 5.0V (DEFAULT), yielding ~4.88 mV per unit resolution. analogReference() can switch Vref to INTERNAL (1.1V for higher sensitivity on small signals) or EXTERNAL (using voltage applied to the AREF pin)."),

    (109, "Pulse Width Modulation (PWM) Principles", "LO-ARD2", "Hard",
     "Describe how Pulse Width Modulation (PWM) works in Arduino to simulate analog output for LED dimming or motor speed, including duty cycle calculation and analogWrite() parameters.",
     "PWM simulates variable analog output by switching a digital pin between 5V (HIGH) and 0V (LOW) at a fixed high frequency (~490 Hz or ~980 Hz). The proportion of time the signal stays HIGH during one cycle is called the Duty Cycle. Formula: Duty_Cycle (%) = (Value / 255.0) * 100%. Passing 0 gives 0% duty cycle (0V average / OFF); 128 gives 50% duty cycle (2.5V average); 255 gives 100% duty cycle (5V continuous / full speed)."),

    (110, "Blocking vs. Non-Blocking Timing Architecture", "LO-ARD2", "Hard",
     "Compare delay() versus millis() in Arduino time management, explaining why millis() is essential for multitasking and responsive embedded applications.",
     "delay() is a blocking function that halts CPU instruction execution for a specified number of milliseconds, making the microcontroller blind to button presses, sensor changes, or incoming serial data during that window. In contrast, millis() is non-blocking; it returns the elapsed time from an internal hardware timer without pausing the CPU. By comparing (currentMillis - previousMillis >= interval), the CPU can execute other tasks simultaneously, enabling true cooperative multitasking on a single core."),

    (111, "UART Serial Communication Mechanism", "LO-ARD3", "Hard",
     "Explain how UART Serial communication works between an Arduino Uno and a computer, detailing baud rates, transmit/receive buffers, and the roles of Serial.available(), Serial.read(), and Serial.print().",
     "UART is an asynchronous serial communication protocol transmitting data frame by frame (start bit, 8 data bits, stop bit) at a agreed-upon Baud Rate (e.g. 9600 bps). Hardware pins 0 (RX) and 1 (TX) connect through an on-board USB-Serial bridge chip to the computer. Incoming bytes are placed into a 64-byte circular FIFO ring buffer in RAM. Serial.available() returns the count of unread bytes in this buffer; Serial.read() extracts one byte at a time; and Serial.print() formats and transmits outgoing ASCII data."),

    (112, "I2C vs. SPI Protocol Comparison", "LO-ARD3", "Hard",
     "Compare I2C and SPI communication protocols in Arduino systems, contrasting pin requirements, communication speed, bus topologies, and device addressing methods.",
     "1. Pin Requirements: I2C needs only 2 lines (SDA, SCL); SPI requires 4 lines (MOSI, MISO, SCK, plus one SS/CS line per slave device). 2. Speed: SPI is full-duplex and significantly faster (up to 8+ MHz); I2C is half-duplex and slower (standard 100 kHz or fast 400 kHz). 3. Addressing: I2C uses software 7-bit addresses sent in the data stream to select slaves on a shared 2-wire bus; SPI uses dedicated physical Chip Select (CS) hardware pins pulled LOW to activate specific slaves."),

    (113, "External Hardware Interrupts and ISR Design", "LO-ARD4", "Hard",
     "Detail the configuration and execution of external hardware interrupts on an Arduino Uno, explaining attachInterrupt(), trigger modes, ISR guidelines, and the volatile qualifier.",
     "On the Uno, external hardware interrupts are available on Pin 2 (INT0) and Pin 3 (INT1). attachInterrupt(digitalPinToInterrupt(pin), ISR_func, mode) binds an ISR function to triggers (RISING, FALLING, CHANGE, LOW). Guidelines: ISRs must execute extremely fast; delay() and heavy Serial calls must not be used inside an ISR because nested interrupts are disabled. Any global variable modified inside an ISR and accessed in loop() must be declared volatile so the compiler reads it directly from RAM rather than caching it in CPU registers."),

    (114, "EEPROM Memory Storage Architecture", "LO-ARD3", "Hard",
     "Explain the role and characteristics of EEPROM memory in an ATmega328P Arduino, including capacity, endurance limits, and the difference between EEPROM.write() and EEPROM.update().",
     "The ATmega328P contains 1024 bytes (1 KB) of non-volatile EEPROM (addresses 0 to 1023) that retains configuration parameters, calibration constants, and state data when power is lost. Each cell has an endurance limit of approximately 100,000 write cycles. EEPROM.write(addr, val) writes a byte directly every time called. EEPROM.update(addr, val) first reads the existing byte and only performs a write operation if the value has changed, dramatically reducing wear and extending memory lifespan."),

    (115, "Python and Arduino Integration via PySerial", "LO-ARD4", "Hard",
     "Explain how to establish a robust bidirectional communication pipeline between a Python desktop application and an Arduino Uno using the PySerial library.",
     "1. Arduino Setup: Configure Serial.begin(115200); in setup() and send structured data (e.g. comma-separated sensor values followed by newline '\\n'). 2. Python Setup: Import serial, time and instantiate ser = serial.Serial('COM3', 115200, timeout=1). 3. Handshake & DTR Delay: Opening serial causes an automatic DTR reset on Arduino Uno; Python must wait 2 seconds (time.sleep(2)) for Arduino bootloader initialization before sending commands. 4. Data Exchange: Python sends ser.write(b'COMMAND\\n') and reads responses via line = ser.readline().decode('utf-8').strip().")
]

for item in sa_data:
    q_num, topic, lo, diff, prompt, exp_ans = item
    content.append(f"""#### ข้อ {q_num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Prompt**: {prompt}
* **Expected Answer**: {exp_ans}
""")

# Write out full file
with open(md_file, 'w', encoding='utf-8') as f:
    f.write(''.join(content))

print(f"Successfully generated {md_file} with all 115 Arduino questions!")
