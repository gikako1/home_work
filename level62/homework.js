function homework() {
  let userInput = prompt("enter text:");
  let conditions = /[\d\W]/;

  if (conditions.test(userInput)) {
    console.log("error");
  } else {
    console.log("opperation succesful!");
  }
}

homework();
