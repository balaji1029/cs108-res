function makeChanges() {


    images = document.getElementsByTagName("img");
    for(let i=0;i<images.length;i++){
        images[i].src="timepass.png";
    }

    h1s = document.getElementsByTagName("h1");
    for(let i=0;i<h1s.length;i++){
        h1s[i].remove();
    }

    paras = document.getElementsByTagName("p");
    for(let i=0;i<paras.length;i++){
        paras[i].innerHTML="Enough of JavaScript, let's stop";
    }

    h2s = document.getElementsByTagName("h2");
    for(let i=0;i<h2s.length;i++){
        let temp = h2s[i].innerHTML;
        let temp2 = temp.toUpperCase();
        h2s[i].innerHTML = temp2;

    }

    div1s = document.getElementById("div1");
        var umm=document.createElement('h3');
        div1s.appendChild(umm);

}

