var formal_tab = document.getElementById('formal_tab');
var informal_tab = document.getElementById('informal_tab');
var file_handler = document.getElementById("file_handler");
var form_index = document.getElementById("form_index");
var form_hcp = document.getElementById("form_hcp");
var form_hmo = document.getElementById("form_hmo");
pf = document.getElementById("pf_number");




formal_tab.addEventListener("click", select_sector, false);
informal_tab.addEventListener("click", select_sector, false);
file_handler.addEventListener("change", file_passer, false);

function select_sector(){
	mode = this.id.substr(0, (this.id.length - 4));
	document.getElementById(mode).checked = "checked";
	document.getElementById('secr').style.display = "block";
	if (mode == 'formal'){
		formal_tab.style.backgroundColor = "#007bff";
		informal_tab.style.backgroundColor = 'gray';
		document.getElementById('formal_sector').innerHTML = '<h5 class="modal-title col-sm-12 col-md-12"><span>please select a tab:</span></h5>' +
															'<div class="col-md-5 col-sm-5 centralise custom-button white-text mrc-4 btn-c" id="private_tab" onclick="select_mode(`private_tab`)">' +
																'<label>Private</label>' +
																'<input type="radio" class="custom-radio center-v cloak" required="yes" value="Private" name="mode" id="private">' +
															'</div>' +
															'<div class="col-md-5 col-sm-5 centralise custom-button white-text mlc-4 btn-c" id="public_tab" onclick="select_mode(`public_tab`)">' +
																'<label>Public</label>' +
																'<input type="radio" class="custom-radio center-v cloak" required="yes" value="Public" name="mode" id="public">' +
															'</div>';
	}
	else {
		formal_tab.style.backgroundColor = 'gray';
		informal_tab.style.backgroundColor = "#007bff";
		document.getElementById('secr').style.display = "none";
		document.getElementById('formal_sector').innerHTML = "";
		document.getElementById('form_block').innerHTML = "";
		document.getElementById('hr_show').style.display = "none";
	}
}

function select_mode(mode){
	selector = mode;
	mode = mode.substr(0, (mode.length - 4));
	document.getElementById(mode).checked = "checked";
	document.getElementById('hr_show').style.display = "block";
	if (mode == 'private'){
		document.getElementById('private_tab').style.backgroundColor = "#007bff";
		document.getElementById('public_tab').style.backgroundColor = "gray";
		document.getElementById('form_block').innerHTML = '<h5 class="modal-title col-sm-12 col-md-12"><span>please select a tab:</span></h5>' +
														  '<div class="col-md-5 col-sm-5 centralise custom-button mrc-4" id="choice_1_tab" onclick="select_submode1(`choice_1_tab`)">' +
															'<label>Organization</label> ' +
															'<input type="radio" class="custom-radio center-v cloak" value="Organization" required="yes" name="sector_private" id="choice_1">' +
														  '</div>' +
														  '<div class="col-md-5 col-sm-5 mlc-4 centralise custom-button" id="choice_2_tab" onclick="select_submode1(`choice_2_tab`)">' +
														  	'<label>Private Sector</label>' +
														  	'<input type="radio" class="custom-radio center-v cloak"  value="Private Sector" required="yes" name="sector_private" id="choice_2">' +
														  '</div>';
		pf.style.display = "none";
		pf.innerHTML = "";
	}
	else {
		document.getElementById('private_tab').style.backgroundColor = "gray";
		document.getElementById('public_tab').style.backgroundColor = "#007bff";
		document.getElementById('form_block').innerHTML = '<h5 class="modal-title col-sm-12 col-md-12"><span>please select a tab:</span></h5>' +
														  '<div class="col-md-3 col-sm-5 centralise custom-button" id="choice_1s_tab" onclick="select_submode2(`choice_1s_tab`)">' +
															'<label>Sectariat</label> ' +
															'<input type="radio" class="custom-radio center-v cloak" id="choice_1s" value="Sectariat" required="yes" name="sector_public">' +
														  '</div>' +
														  '<div class="col-md-3 col-sm-5 mrc-5 mlc-5 centralise custom-button" id="choice_2s_tab" onclick="select_submode2(`choice_2s_tab`)">' +
														  	'<label>Department</label>' +
														  	'<input type="radio" class="custom-radio center-v cloak" id="choice_2s" value="Department" required="yes" name="sector_public">' +
														  '</div>' +
														  '<div class="col-md-3 centralise custom-button cmt-1" id="choice_3s_tab" onclick="select_submode2(`choice_3s_tab`)">' +
														  	'<label>Agencies</label>' +
														  	'<input type="radio" class="custom-radio center-v cloak" id="choice_3s" value="Agencies" required="yes" name="sector_public">' +
														  '</div>';
		pf.style.display = "block";
		pf.innerHTML = '<label title="Personal File Number">PF Number</label>' +
                	   '<input type="text" class="form-control" placeholder="Personal File Number" required="yes" title="Personal File Number">';
	}
}

function select_submode1(mode){
	mode = mode.substr(0, (mode.length - 4));
	document.getElementById(mode).checked = "checked";
	if (mode == 'choice_1'){
		document.getElementById('choice_1_tab').style.backgroundColor = "#007bff";
		document.getElementById('choice_2_tab').style.backgroundColor = "gray";
	}
	else {
		document.getElementById('choice_1_tab').style.backgroundColor = "gray";
		document.getElementById('choice_2_tab').style.backgroundColor = "#007bff";
	}
}

function select_submode2(mode){
	mode = mode.substr(0, (mode.length - 4));
	document.getElementById(mode).checked = "checked";
	if (mode == 'choice_1s'){
		document.getElementById('choice_1s_tab').style.backgroundColor = "#007bff";
		document.getElementById('choice_2s_tab').style.backgroundColor = "gray";
		document.getElementById('choice_3s_tab').style.backgroundColor = "gray";
	}
	else if (mode == 'choice_2s'){
		document.getElementById('choice_1s_tab').style.backgroundColor = "gray";
		document.getElementById('choice_2s_tab').style.backgroundColor = "#007bff";
		document.getElementById('choice_3s_tab').style.backgroundColor = "gray";
	}
	else {
		document.getElementById('choice_1s_tab').style.backgroundColor = "gray";
		document.getElementById('choice_2s_tab').style.backgroundColor = "gray";
		document.getElementById('choice_3s_tab').style.backgroundColor = "#007bff";
	}
}

form_index.addEventListener("submit", function(){
		password = document.getElementById("pass_index");
		cpassword = document.getElementById("cpass_index");
		phone = document.getElementById("phone_num");
		isPhoneNum = Number.isInteger(parseInt(phone.value));

		if (cpassword.value == password.value){
			if (phone.value.length >= 9 && isPhoneNum == true){
				form_index.action = "/signup";
			}
			else {
				alert("phone number entered is invalid");
			}
		}
		else{
			alert("Password does not match");
		}
	},
);

form_hcp.addEventListener("submit", function(){
		password = document.getElementById("pass_hcp");
		cpassword = document.getElementById("cpass_hcp");

		if (cpassword.value == password.value){
			form_hcp.action = "/hcp/join"
		}
		else{
			alert("Password does not match");
		}
	},
);

form_hmo.addEventListener("submit", function(){
		password = document.getElementById("pass_hmo");
		cpassword = document.getElementById("cpass_hmo");

		if (cpassword.value == password.value){
			form_hmo.action = "/hmo/signup"
		}
		else{
			alert("Password does not match");
		}
	},
);

function clicker_func(val){
	document.getElementById(val).click()
}


function file_passer(){
    val = file_handler.value;
    New_val = val.substr(12, (val.length - 1));
    document.getElementById("file_label").innerHTML = New_val;
}