function goBack() {
  window.history.back();
}

$(document).ready(function() {
  let year = new Date();
  year = year.getFullYear();
  $("#year").html(year);
});
