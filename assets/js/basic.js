document.getElementById("textboxId").style.display = "none";

function showDivText() {
  var my_disply = document.getElementById("textboxId").style.display;
  if (my_disply == "block")
    document.getElementById("textboxId").style.display = "none";
  else document.getElementById("textboxId").style.display = "block";
}

$("input[type='text']").keypress(function(event) {
  if (event.which === 13) {
    //grab the newTodo text from input
    var todoText = $(this).val();
    $(this).val("");
    $("ul").append("<li>" + todoText + "</li>");
  }
});

