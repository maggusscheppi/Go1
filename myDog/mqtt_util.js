/*
   mqtt_util.js
   2022-12-18 Markus Schepp
   function for sending commands via mqtt to the Go1
*/

const DEBUG_SOCKETCLIENT = true;

/**
 * This adds an Text in the message-div if available or to the browser console 
 */
function addMessage(aText)
{
	if (DEBUG_SOCKETCLIENT == false)
		return;

	var myTextArea = document.getElementById("message_text");
	if (myTextArea)
	{
		myTextArea.value = aText+"\n"+myTextArea.value;
	}
	else
	{
		console.log(aText);
	}
}

var connection = null;
var connected = false;
var client_connected = false;
var dataTimeOut;
var host=window.location.host;
var port=80;


/*
 * callback function if connection succeeds. We just inform the user via console.
*/
function onConnect() {
	if (connection) {
		addMessage('oo Go1 mqtt connected');
		connected = true;
		client_connected = true;
	}
}

function onClose() {
	addMessage('oo socket closed');

	connected = false;	
	sending = false;
	// try reconnect
	setTimeout(connectionStatus, 2000);
}

function onMessage(e) {
	addMessage('oo message:' + e.payloadString)
}

function onError(e) {
	addMessage('oo error:' + e.data)
}


// lets do a reconnect, if not connected after 2 seconds
function connectionStatus()
{
	if (connected === false)
	{
		connect();
	}
}


/*
 * Connects the mqtt client to the Go1 mqtt server on the raspberry pi
*/
function connect() {
	addMessage('oo trying to connect');

	// just in case, an object exists
	delete connection;
	connection = null;

	if (window.location.protocol == 'http:') { 
		addMessage('oo connecting mqtt client');
		try {
			connection = new Paho.MQTT.Client(host,port,"/mqtt", "myDog");
			var options = {
				timeout: 3,
				onSuccess: onConnect,
				onFailure: onError
			};
			
			connection.connect(options);

			connection.onConnectionLost = onClose;
			connection.onMessageArrive = onMessage;
		
		} catch (e) {
			console.log(e);
		};

	}

}

// this function is called by clicking the command button 
function sendData(destination, message)
{
	addMessage("sendData: "+ destination + ";" + message);
	aMessage = new Paho.MQTT.Message(message);
	aMessage.destinationName = destination;
	connection.send(aMessage);
}

