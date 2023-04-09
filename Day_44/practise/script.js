colors = [
  "blue",
  "grey",
  "orange",
  "yellow",
  "red",
  "black",
  "cyan",
  "green",
  "pink",
  "brown",
  "powdered-blue",
  "violet",
  "purple",
];

//elements
first = document.querySelector(".first");
second = document.querySelector(".second");
third = document.querySelector(".third");
forth = document.querySelector(".forth");
fifth = document.querySelector(".fifth");

arr = [first, second, third, forth, fifth];
btn = document.querySelector(".button");

const changeColor = () => {
  arr.forEach(
    (box) =>
      (box.style.backgroundColor =
        colors[Math.floor(Math.random() * colors.length)])
  );
};

btn.addEventListener("click", function () {
  setInterval(changeColor, 1000);
});
