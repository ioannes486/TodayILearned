const title = document.querySelector("div.title:first-child h1");
let originalInnerText = title.innerText;

function handleTitleClick() {
  const clickedClass = "active";
  // if (title.classList.contains(clickedClass)) {
  //   title.classList.remove(clickedClass);
  // } else {
  //   title.classList.add(clickedClass);
  // }
  title.classList.toggle("active");
}

title.addEventListener("click", handleTitleClick);
// title.addEventListener("mouseenter", handleMouseEnter);
// title.addEventListener("mouseleave", handleMouseLeave);

// window.addEventListener("resize", handleResize);
// window.addEventListener("copy", handleCopy);
// window.addEventListener("offline", handleConnection);
