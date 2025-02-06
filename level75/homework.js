function carconstructor(brand, model, year, engine) {
  this.brand = brand;
  this.model = model;
  this.year = year;
  this.engine = engine + "L";
  console.log(
    "this is a",
    brand,
    model + ",",
    "released in",
    year,
    "with a",
    engine,
    "L engine"
  );
}
let mercedes = new carconstructor("mercedes", "baymach", "2022", "3.0");

function bookconstructor(title, author, year, pages) {
  this.title = title;
  this.author = author;
  this.year = year;
  this.pages = pages;
  console.log(
    "the book is called",
    '"' + title + '",',
    "by",
    author + ",",
    "released in",
    year + ",",
    "which has a length of",
    pages,
    "pages."
  );
  time = pages / 7;
  console.log(
    "if you want to finish the book in a week, you have to read",
    time,
    "pages a day."
  );
}
let book = new bookconstructor(
  "the knight in the tigers leather",
  "shota rustaveli",
  "????",
  238
);
