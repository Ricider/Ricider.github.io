var currentIndex=0;

const urls =
[
"https://www.youtube.com/embed/fC7oUOUEEi4",
"https://www.youtube.com/embed/TVoGKvVBC6Q"
]

function nextVideo()
{
	currentIndex=(currentIndex+1) % urls.length;
	let frame = document.getElementById("leftDiv").querySelector("iframe");
	frame.setAttribute("src",urls[currentIndex]);
}