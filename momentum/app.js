const loginInput = document.querySelector(".login-form input");
const loginBtn = document.querySelector(".login-form button");

function clickLoginBtn() {
  // console.log("clicked");
  console.log(loginInput.value);
}

loginBtn.addEventListener("click", clickLoginBtn);
