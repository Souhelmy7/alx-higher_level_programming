$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const language = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + language,
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
