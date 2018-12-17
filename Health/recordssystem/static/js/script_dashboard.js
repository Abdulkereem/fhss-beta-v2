var file_handler = document.getElementById("file_handler");
file_handler.addEventListener("change", function(){
		val = file_handler.value;
	    New_val = val.substr(12, (val.length - 1));
	    document.getElementById("file_label").innerHTML = New_val;
	},
	false
);



var date_place = document.getElementById("date_place");
var date_land = document.getElementById("date_land");

var gender_place = document.getElementById("gender_place");
var gender_land = document.getElementById("gender_land");

var blood_place = document.getElementById("blood_place");
var blood_land = document.getElementById("blood_land");





date_place.addEventListener("focus", function(event){
	  event.target.style.display = "none";
	  date_land.style.display = "block";
	},
	true
);

date_land.addEventListener("blur", function(event){
	  date_place.style.display = "block";
	  event.target.style.display = "none";
	  date_place.value = event.target.value
	},
	true
);

gender_place.addEventListener("focus", function(event){
	  event.target.style.display = "none";
	  gender_land.style.display = "block";
	},
	true
);

gender_land.addEventListener("blur", function(event){
	  gender_place.style.display = "block";
	  event.target.style.display = "none";
	  gender_place.value = event.target.value
	},
	true
);

blood_place.addEventListener("focus", function(event){
	  event.target.style.display = "none";
	  blood_land.style.display = "block";
	},
	true
);

blood_land.addEventListener("blur", function(event){
	  blood_place.style.display = "block";
	  event.target.style.display = "none";
	  blood_place.value = event.target.value
	},
	true
);
