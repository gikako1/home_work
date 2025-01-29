// შექმენით ფუნქცია რომელიც აბრუნებს 2დ მასივს (ზრდადი რიცხვების) სვეტების დს რიგების მიხედვით, მაგ: func(2,2) --> [ [1,2], [3,4] ]
function get2darray(row, column) {
  let res = [];
  let currentNum = 1;
  for (let i = 0; i < row; i++) {
    let row1 = [];
    for (let j = 0; j < column; j++) {
      row1.push(currentNum);
      currentNum++;
    }
    res.push(row1);
  }
}
