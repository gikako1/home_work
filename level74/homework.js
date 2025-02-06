function carconstructor(brand, model, year, engine) {
  this.brand = brand;
  this.model = model;
  this.year = year;
  this.engine = engine + "L";
}
let mercedes = new carconstructor("mercedes", "baymach", "2022", "3.0");

function animalconstructor(name, type, food) {
  this.name = name;
  this.type = type;
  this.food = food;
}
let mammoth = new animalconstructor("mammoth", "mammal", "vegan?");

function studentconstructor(name, age, grades) {
  this.name = name;
  this.age = age;
  this.grades = grades;
}
let stickler = new studentconstructor("stickler", "17", "A++");
