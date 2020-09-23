async function loadMessages()
{
	while (true)
	{
		let r = new XMLHttpRequest();
		r.open( "GET", "http://192.168.1.25:666/api/messages.txt", false );
		r.send( null );
		let response = r.responseText;
		let txtbox=document.getElementById("textField");
		txtbox.innerHTML=response;
		await new Promise(r => setTimeout(r, 500));
	}
}

function postMessage()
{
	let r = new XMLHttpRequest();
	r.open( "POST", "http://192.168.1.25:666/api/messages.txt", true );
	let message=document.getElementById("apiField");
	r.setRequestHeader("Content-type", "text/raw");
	r.send( message.value );
	message.value="";
}