    //Bottone Fisso con chiamata barra di ricerca - Da togliere?
    var search_open = 0;
	window.onscroll = function() {scroll()};
	function scroll(){
		if (search_open == 0) {
			if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
				document.getElementById("fixedBtn").style.visibility = "hidden";
			document.getElementById("fixedBtn").style.transform = "translate(50px, 100px)";
			} else {
				document.getElementById("fixedBtn").style.visibility = "visible";
			document.getElementById("fixedBtn").style.transform = "translate(0px, 0px)";
			}
		}
	}
	function searchCall() {
		document.getElementById("fixedBtn").style.transform = "translate(0px, -100px)";
		document.getElementById("fixedBtn").style.width = "0px";
		document.getElementById("fixedBtn").style.height = "0px";
		document.getElementById("fixedBtn").style.visibility = "hidden";
		document.getElementById("fixedBtn").querySelector("i").style.display = "none";
		document.getElementById("search").style.display = "block";
		search_open = 1;
	}
	var search = document.getElementById('search');
	window.onclick = function(event) {
		if (event.target == search) {
			search.style.display = "none";
			document.getElementById("fixedBtn").style.transform = "translate(0px, 0px)";
			document.getElementById("fixedBtn").style.width = null;
			document.getElementById("fixedBtn").style.height = null;
			document.getElementById("fixedBtn").style.visibility = "visible";
			document.getElementById("fixedBtn").querySelector("i").style.display = null;
			search_open = 0;
		}
	}

    //Funzione per filtrare contenuti in base alla classe
	var cards = document.querySelectorAll('.card');
	var selectOptions;
	function filtro(x) {
	    selectOptions = document.getElementsByClassName(x);
	    var i;
	    for (var i = 0; i < cards.length; i ++) {
	        cards[i].style.display = 'none';
        }
        delay = setTimeout(loadView, 100);
	}
	function loadView() {
	    var i;
	    for (var i = 0; i < selectOptions.length; i ++) {
			selectOptions[i].style.display = null;
		}
	}

	//filtra tramite barra di ricerca
	function searchFilerElements() {
	  var input, filter, table, tr, name, i;
	  input = document.getElementById("myInput");
	  filter = input.value.toUpperCase();
	  table = document.getElementById("list");
	  tr = table.getElementsByClassName("card");
	  for (i = 0; i < tr.length; i++) {
		name = tr[i].getElementsByTagName("h3")[0];
		if (name) {
		  if (name.innerHTML.toUpperCase().indexOf(filter) > -1) {
			tr[i].style.display = "";
		  } else {
			tr[i].style.display = "none";
		  }
		}
	  }
	}

    //mostra menu in modalità responsiva
	function displayMenu() {
	  var elem = document.getElementById('responsiveMenu');
	  if (elem.style.display === 'block') {
		elem.style.display = 'none';
	  }
	  else {
		elem.style.display = 'block';
	  }
	}


	var delay;
	var idVar;
	var card = document.getElementsByClassName('card');
	function displayWindow(x) {
	  idVar = document.getElementById(x);
	  var i;
	  for (var i = 0; i < card.length; i ++) {
		  if (idVar.style.display = "block") {
			card[i].style.transform = "translate(2000px, 0px)";
			delay = setTimeout(dissolve, 900);
		  }
		  else {
		  //non fa niente
		  }
	  }
	}

	function dissolve() {
		delay = setTimeout(openWin, 250);
		for (var i = 0; i < card.length; i ++) {
		card[i].style.display = "none";
		}
		idVar.style.display = "block";
	}

	function hideIdVar() {
		idVar.style.display = "none";
		idVar.style.width = null;
		idVar.style.height = null;
		idVar.querySelector(".contentList").style.display = "none";
		idVar.querySelector(".close").style.display = "none";
		idVar.querySelector(".nuBtnYellow").style.display = null;
		//delay = setTimeout(displayWindow, 100);
		var i;
		for (var i = 0; i < card.length; i ++) {
			card[i].style.display = "block";
			card[i].style.transform = "translate(0px, 0px)";
		}
	}

	var filtri = document.getElementsByClassName("filtri")
	function openWin() {
		idVar.style.transform = "translate(0px, 0px)";
		idVar.style.width = "90%";
		idVar.style.height = "100%";
		idVar.querySelector(".contentList").style.display = "block";
		idVar.querySelector(".close").style.display = "block";
		idVar.querySelector(".nuBtnYellow").style.display = "none";
		var i;
		for (i=0; i < filtri.length; i++) {
			filtri[i].style.pointerEvents = "none";
			filtri[i].style.background = "rgb(55,55,55)";
		}
	}
	function closeWin() {
		idVar.style.transform = "translate(0px, 2000px)";
		delay = setTimeout(hideIdVar, 900);
		var i;
		for (i=0; i < filtri.length; i++) {
			filtri[i].style.pointerEvents = null;
			filtri[i].style.background = null;
		}
	}


