$(function() {
  $.scrollUp({
    animation: 'fade'
  });

  $('#logo').click(function() {
    $(this).rotate(360, {
      complete: function() {
        location.reload();
      }
    });
  });
});

