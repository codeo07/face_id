import RPi.GPIO as GPIO
import time

# Set GPIO mode and pin for the warning buzzer
GPIO.setmode(GPIO.BCM)
buzzer_pin = 18
GPIO.setup(buzzer_pin, GPIO.OUT)

# Define battery voltage thresholds (adjust these values as needed)
low_voltage_threshold = 10.5  # Example: Consider battery low below 10.5V
critical_voltage_threshold = 10.0  # Example: Critical low battery below 10.0V

# Function to read battery voltage (you may need to calibrate this)
def read_battery_voltage():
    # Replace this with code to read the actual battery voltage
    # For example, you can use an ADC (Analog-to-Digital Converter) to read voltage
    # The following line is a placeholder:
    return 11.0  # Example voltage reading

try:
    while True:
        # Read battery voltage
        battery_voltage = read_battery_voltage()
        
        # Print battery voltage for debugging
        print(f"Battery Voltage: {battery_voltage} V")
        
        # Check battery health and trigger warnings
        if battery_voltage < low_voltage_threshold:
            # Battery is low, trigger a warning
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Turn on the buzzer
            time.sleep(1)  # Sound the buzzer for 1 second
            GPIO.output(buzzer_pin, GPIO.LOW)  # Turn off the buzzer
            time.sleep(1)  # Delay for 1 second
        elif battery_voltage < critical_voltage_threshold:
            # Battery is critically low, trigger a more urgent warning
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(0.5)  # Sound the buzzer for 0.5 seconds
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(0.5)  # Delay for 0.5 seconds
        
        # Add more health checks and warnings as needed

        time.sleep(5)  # Delay for 5 seconds between checks (adjust as needed)

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO pins on Ctrl+C exit
