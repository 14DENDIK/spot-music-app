function likeSong(id) {
  $.ajax({
    url: '{% url "music:like-song" %}',
    data: {
      'songId': id,
    },
    dataType: 'json',
    success: function(data) {
      let fav_button = document.getElementById("song"+id);
      if (data.is_liked) {
        element.class = "btn btn-warning fa fa-star";
      } else {
        element.class = "btn btn-outline-warning fa fa-star";
      }
    }
  });
}

// $('.like-song').click(function() {
//     alert("I am an alert box!");
//     $.ajax({
//       url: '{% url "music:like-song" %}',
//       data: {
//         'songId': id,
//       },
//       dataType: 'json',
//       success: function(data) {
//         if (data.is_liked) {
//           alert('Hey submitted');
//         } else {
//           alert('Hey not submitted');
//         }
//     });
// });
