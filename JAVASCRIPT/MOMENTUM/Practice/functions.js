// js로 html변화시키기
// js는 html을 변경헤서 웹페이지의 스타일을 변경할 수 있다.
// 이는 css보다 우선순위로 적용된다.
// 하지만 스타일은 css에서 편집하는 것이 바람직하기 때문에 js로 인라인 스타일을 변경하는 것보단 클래스를 변경해서 다른 클래스의 스타일을 적용할 수 있도록 하는 것이 바람직하다

function handleTitleClick() {
  const currentColor = title.style.color; //이렇게 변수에다 넣으면 왜 실행이 안될까??
  let newColor;
  if (currentColor === "blue") {
    newColor = "tomato";
  } else {
    newColor = "blue";
  }
  title.style.color = newColor;
}
function handleMouseEnter() {
  title.innerText = "you've entered me indeed!";
}

function handleMouseLeave() {
  title.innerText = "Don't leave me alone you fucking idiot!!";
  setTimeout(function () {
    title.innerText = originalInnerText;
  }, 2000);
}

function handleResize() {
  document.body.style.backgroundColor = "tomato";
}

function handleCopy() {
  alert("copier");
}

function handleConnection() {
  alert("Network Has Been disconnected");
}
