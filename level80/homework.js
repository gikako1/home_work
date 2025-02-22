//! unshift
// ამატებს ახალ ელემენტებს array-ს დასაწყისში
const names1 = ["miranduxti", "tarieli", "solomon"];
names1.unshift("gela", "sigma");

//! shift
// აშორებს array-ს პირველ ელემენტს
names1.shift();
/// მივიღებთ [sigma, miranduxti, tarieli, solomon]

//! slice
// აბრუნებს დასაწყისის და დასასრულის ინდექსის მიხედვით ახალ array-ს
let names_new = names1.slice(1, 3);
/// მივიღებთ [miranduxt,tarieli]
// *names1.slice(1,3) ნიშნავს 1 ინდექსის ჩათვლით 3 ინდექსამდე, ამიტომაც დაბრუნდება მხოლოდ ორი ელემენტი.

//! splice
// array-ს მონიშნულ ინდექსში ამატებს ელემენტს
// splice-ს გააჩნია 3 არგუმენტი( ინდექსი | რამდენი ელემენტი ამოშალოს | რა ელემენტი ჩაამატოს )
names1.splice(1, 0, "gela");
//* ეს ეხლა პირველ ინდექსში არაფერს ამოშლის და მანდვე ჩაამატებს "gela"-ს

//! concat
// ამატებს ორ ან მეტ array-ს და ვიღებთ ახალ array-ს
const names2 = [nika, mika, tika];
let names_pro_max = names1.concat(names_new, names2);
/// მივიღებთ [sigma,miranduxt,tarieli,solomon,miranduxt,tarieli,nika,mika,tika]
//* names1-ს დაემატა names_new და names2 და მივიღეთ ზემოთ რაც წერია

//! join
// ამატებს array-ში string-ს ელემენტებს შორის
let name_list = names_pro_max.join("and");
/// აქ ყოველი სახელის შემდეგ იქნება "and". (sigma and miranduxt and tarieli and...)

//! reverse
// array-ს ატრიალებს
let names_rev = names1.reverse();
/// მივიღებთ [solomon,tarieli,miranduxti,sigma]

//! sort
// ალაგებს array-ს ალფაბეტურად
let names_sort = names1.sort();
/// მივიღებთ [miranduxti,sigma,solomon,tarieli]
//// ეს ფუნქცია ციფრებზეც (10-ის მერე რიცხვებზე არა) მუშაობს 0 დან 10მდე.
