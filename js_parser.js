var audioCollection = document.getElementsByClassName('audio');
var text = '';
for (var i = 0; i < 30; i++) {
	var audio = audioCollection[i];
	var src = audio.children[1].children[0].children[1].value;
	var name = audio.children[1].children[1].children[0].innerText;
	text += name + ' src=' + src + '<br>';
}
document.write(text);