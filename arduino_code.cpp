short ledPin = 5;
short buttonPin = 7;

void setup() {
 	Serial.begin(115200);
 	pinMode(ledPin, OUTPUT);
	pinMode(buttonPin, INPUT);
}

void loop() {
	//wait for user to press button
  	int button_state = 0;
  	digitalWrite(ledPin, LOW);
  	while(button_state == LOW){
    	button_state = digitalRead(buttonPin);
    	delay(10);
  	}
  	delay(5);
  	
  	//when button is pressed, signal it by activating LED
  	digitalWrite(ledPin, HIGH);
  
  	int user_input = 0;
  	int reference_input = 0;
  	int n_reads = 5000; //number of measurements to be done
 	while(n_reads > 0){
 		// analog-to-digital of reference sine wave
    	reference_input = analogRead(A1);
    	float ref_ADC = reference_input * 5.0 / 1023.0;
    	Serial.println(ref_ADC);

    	// analog-to-digital of user hand generated sine wave
	    user_input = analogRead(A0);
    	float user_ADC = user_input * 5.0 / 1023.0;
    	Serial.println(user_ADC);
    	n_reads--;

    	delay(3); // small delay for stability
  	}

}
