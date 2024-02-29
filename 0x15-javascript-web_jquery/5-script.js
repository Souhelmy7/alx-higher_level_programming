$(document).ready(function () {
  $('#add_item').on('click', function () {
    const item = '<li>Item</li>';
    $('.my_list').append(item);
  });
});
