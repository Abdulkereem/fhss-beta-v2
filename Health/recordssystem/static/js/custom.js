var main = document.getElementById('main_navbar');
var sidenav = document.getElementById('side_navbar');
var list = {"status":'open'}
function otp(){
  document.getElementById('log_form').style.display = 'none';
  document.getElementById('otp_form').style.display = 'block';
}
function fields (caller) {
  
  document.getElementById('mode-indicator').innerHTML = `<p><strong>Registration mode: ${caller}</strong></p>`;
  if (caller == "Public"){
    document.getElementsByClassName('input-fields')[0].innerHTML = "";
  }
  else {
    document.getElementsByClassName('input-fields')[0].innerHTML =
    '<input list="sector" name="sector" placeholder="Choose a sector" required>'
    +'<datalist id="sector">'
    +'  <option value="Informal"></option>'
    +'  <option value="Formal"></option>'
    +'</datalist>';
  }
  document.getElementById('forms').style.display = "block";
  document.getElementById('sector_mode').value = caller;
}
function field_out (){
  document.getElementById('forms').style.display = "none";
}
function sidebar(){
  if (list.status == 'open'){
    sidenav.classList.add('side-nav');
    main.classList.add('main-body');
    list.status = 'close';
  }
  else {
    sidenav.classList.remove('side-nav');
    main.classList.remove('main-body');
    list.status = 'open';
  }
}
function clicks(caller){
  document.getElementById(caller).click();
}
function file_passer(change,pusher){
    val = document.getElementById(pusher).value;
    New_val = val.substr(12, (val.length - 1));
    document.getElementById(change).innerHTML = New_val;
}
function submitform(){
  cpasswd = document.getElementById('Cpasswd');
  passwd = document.getElementById('Passwd');
  if(cpasswd.value !== passwd.value){
    cpasswd.value = "";
    passwd.value = "";
    var k = document.getElementById("snackbar");
    k.className = "show";
    setTimeout(function(){ k.className = k.className.replace("show", ""); }, 3000);
  }
  else{
    document.getElementById('form_data').action = '/signup';
  }
}